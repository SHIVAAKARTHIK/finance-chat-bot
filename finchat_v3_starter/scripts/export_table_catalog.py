"""Export metadata for all tables in lakehouse_mvpai.silver and lakehouse_mvpai.gold to Excel.

READ-ONLY: every statement is checked before it runs; only SELECT / SHOW / DESCRIBE / WITH are allowed.

Usage (from the backend folder, where .env lives):
    pip install databricks-sql-connector openpyxl requests
    python scripts/export_table_catalog.py                    # reads ./.env
    python scripts/export_table_catalog.py --env path/to/.env --out output/table_catalog.xlsx

Auth (same settings as the app):
    DATABRICKS_SERVER_HOSTNAME, DATABRICKS_HTTP_PATH
    DATABRICKS_AUTH=azure_spn  -> AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET
    otherwise                  -> DATABRICKS_TOKEN
"""
from __future__ import annotations

import argparse
import csv
import os
import re
import sys
import time
from itertools import combinations
from pathlib import Path

import requests
from databricks import sql as dbsql
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

CATALOG = "lakehouse_mvpai"
SCHEMAS = ("silver", "gold")
MAX_DISTINCT_FOR_VALUES = 50
SKIP_TYPES = ("array", "map", "struct", "binary", "variant")
SAMPLE_ROWS = 5
DATABRICKS_RESOURCE = "2ff814a6-3304-4ab8-85cb-cd0e6f879c1d"  # Azure Databricks application id (public)
TOKEN_MAX_AGE_S = 45 * 60
KEY_LIKE = re.compile(r"(_KEY|_ID|_CODE|_CD|_NUMBER|_NUM|_NBR|_NO)$|^(ID|KEY)$|PERIOD|FISCAL_YEAR|^YEAR$|^MONTH$", re.I)
NOT_KEY_TYPES = ("decimal", "double", "float", "timestamp", "boolean")
MAX_KEY_CANDIDATES = 8          # up to 8 columns -> at most 8 + 28 + 56 combinations
KEY_SEARCH_MAX_ROWS = 5_000_000  # skip exact key search on very large tables
FILL_HEADER = ["schema", "table", "layer", "domain (ar/ap/gl/fa/cash/recon/subledger)", "purpose",
               "grain (one row = ?)", "primary_key", "entity_column", "period_columns", "pii_columns",
               "built_from", "known_issues"]

ALLOWED_START = re.compile(r"^\s*(SELECT|SHOW|DESCRIBE|WITH)\b", re.I)
FORBIDDEN = re.compile(r"\b(INSERT|UPDATE|DELETE|MERGE|ALTER|DROP|CREATE|TRUNCATE|GRANT|REVOKE|REPLACE|COPY|OPTIMIZE|VACUUM)\b", re.I)


def check_read_only(statement: str) -> None:
    """Raise if the statement is not a plain read."""
    code = re.sub(r"'[^']*'", "''", statement)  # ignore words inside string literals
    if not ALLOWED_START.match(code) or FORBIDDEN.search(code) or ";" in code.strip().rstrip(";"):
        raise ValueError(f"Blocked non read-only statement: {statement[:120]}")


def load_env(path: Path) -> None:
    if not path.exists():
        sys.exit(f".env not found at {path}")
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def need(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        sys.exit(f"Missing {name} in .env")
    return value


class Warehouse:
    """Databricks SQL connection that renews the Entra token before it expires."""

    def __init__(self) -> None:
        self.host = need("DATABRICKS_SERVER_HOSTNAME").replace("https://", "").rstrip("/")
        self.http_path = need("DATABRICKS_HTTP_PATH")
        self.use_spn = os.environ.get("DATABRICKS_AUTH", "").lower() == "azure_spn"
        self.conn = None
        self.opened = 0.0

    def _token(self) -> str:
        if not self.use_spn:
            return need("DATABRICKS_TOKEN")
        resp = requests.post(
            f"https://login.microsoftonline.com/{need('AZURE_TENANT_ID')}/oauth2/v2.0/token",
            data={"grant_type": "client_credentials", "client_id": need("AZURE_CLIENT_ID"),
                  "client_secret": need("AZURE_CLIENT_SECRET"), "scope": f"{DATABRICKS_RESOURCE}/.default"},
            timeout=30,
        )
        if resp.status_code != 200:
            sys.exit(f"Token request failed ({resp.status_code}): {resp.json().get('error_description', '')[:300]}")
        return resp.json()["access_token"]

    def _connect(self) -> None:
        if self.conn is not None:
            try:
                self.conn.close()
            except Exception:
                pass
        self.conn = dbsql.connect(server_hostname=self.host, http_path=self.http_path, access_token=self._token())
        self.opened = time.time()

    def query(self, statement: str) -> list[tuple]:
        check_read_only(statement)
        if self.conn is None or time.time() - self.opened > TOKEN_MAX_AGE_S:
            self._connect()
        with self.conn.cursor() as cur:
            cur.execute(statement)
            return [tuple(r) for r in cur.fetchall()]

    def close(self) -> None:
        if self.conn is not None:
            self.conn.close()


def q(identifier: str) -> str:
    return "`" + identifier.replace("`", "``") + "`"


def write_sheet(wb: Workbook, title: str, header: list[str], rows: list[list]) -> None:
    ws = wb.create_sheet(title)
    ws.append(header)
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="1F3864")
    for row in rows:
        ws.append(["" if v is None else (str(v) if not isinstance(v, (int, float)) else v) for v in row])
    ws.freeze_panes = "A2"
    for col in ws.columns:
        width = max(len(str(c.value or "")) for c in col[:200])
        ws.column_dimensions[col[0].column_letter].width = min(max(width + 2, 10), 60)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", default=".env")
    ap.add_argument("--out", default="output/table_catalog.xlsx")
    args = ap.parse_args()
    load_env(Path(args.env))

    wh = Warehouse()
    schema_list = ", ".join(f"'{s}'" for s in SCHEMAS)
    tables = wh.query(
        f"SELECT table_schema, table_name, table_type, comment FROM {CATALOG}.information_schema.tables "
        f"WHERE table_schema IN ({schema_list}) ORDER BY table_schema, table_name"
    )
    columns = wh.query(
        f"SELECT table_schema, table_name, ordinal_position, column_name, data_type, is_nullable, comment "
        f"FROM {CATALOG}.information_schema.columns WHERE table_schema IN ({schema_list}) "
        f"ORDER BY table_schema, table_name, ordinal_position"
    )
    cols_by_table: dict[tuple, list[tuple]] = {}
    for c in columns:
        cols_by_table.setdefault((c[0], c[1]), []).append(c)
    print(f"Found {len(tables)} tables, {len(columns)} columns")

    # Declared keys (PRIMARY KEY / FOREIGN KEY constraints are informational in Unity Catalog and often missing)
    key_rows: list[list] = []
    declared_pk: dict[tuple, list[str]] = {}
    try:
        kc = wh.query(
            f"SELECT tc.table_schema, tc.table_name, tc.constraint_name, tc.constraint_type, "
            f"kcu.column_name, kcu.ordinal_position "
            f"FROM {CATALOG}.information_schema.table_constraints tc "
            f"JOIN {CATALOG}.information_schema.key_column_usage kcu "
            f"  ON tc.constraint_catalog = kcu.constraint_catalog AND tc.constraint_schema = kcu.constraint_schema "
            f" AND tc.constraint_name = kcu.constraint_name "
            f"WHERE tc.table_schema IN ({schema_list}) AND tc.constraint_type IN ('PRIMARY KEY', 'FOREIGN KEY') "
            f"ORDER BY 1, 2, 3, 6"
        )
        fk_targets: dict[str, str] = {}
        try:
            for name, sch, tbl, col in wh.query(
                f"SELECT constraint_name, table_schema, table_name, column_name "
                f"FROM {CATALOG}.information_schema.constraint_column_usage WHERE constraint_schema IN ({schema_list})"
            ):
                fk_targets.setdefault(name, f"{sch}.{tbl}.{col}")
        except Exception as exc:
            print(f"   (could not read foreign key targets: {str(exc)[:150]})")
        for schema, table, cname, ctype, col, pos in kc:
            refs = fk_targets.get(cname, "") if ctype == "FOREIGN KEY" else ""
            key_rows.append([schema, table, ctype, cname, col, pos, refs, "declared"])
            if ctype == "PRIMARY KEY":
                declared_pk.setdefault((schema, table), []).append(col)
        print(f"Declared key columns found: {len(key_rows)}")
    except Exception as exc:
        print(f"   (could not read declared keys: {str(exc)[:200]})")

    table_rows, column_rows, value_rows, fill_rows, failed, summaries, sample_rows = [], [], [], [], [], [], []
    for i, (schema, table, ttype, comment) in enumerate(tables, 1):
        full = f"{CATALOG}.{q(schema)}.{q(table)}"
        cols = cols_by_table.get((schema, table), [])
        print(f"[{i}/{len(tables)}] {schema}.{table} ({len(cols)} columns)")
        row_count, distinct, stats = None, {}, {}
        profiled = [c for c in cols if not str(c[4]).lower().startswith(SKIP_TYPES)]
        try:
            exprs = ["COUNT(*)"]
            for c in cols:
                exprs.append(f"count_if({q(c[3])} IS NULL)")
                if c in profiled:
                    exprs += [f"approx_count_distinct({q(c[3])})", f"CAST(min({q(c[3])}) AS STRING)", f"CAST(max({q(c[3])}) AS STRING)"]
            result = wh.query(f"SELECT {', '.join(exprs)} FROM {full}")[0]
            row_count, k = result[0], 1
            for c in cols:
                nulls = result[k]; k += 1
                if c in profiled:
                    distinct[c[3]] = result[k]
                    stats[c[3]] = (result[k + 1], result[k + 2], nulls); k += 3
                else:
                    stats[c[3]] = (None, None, nulls)
        except Exception as exc:  # keep going; report at the end
            failed.append(f"{schema}.{table}: {str(exc)[:200]}")
            print(f"   failed profiling: {str(exc)[:200]}")

        for c in cols:
            mn, mx, nulls = stats.get(c[3], (None, None, None))
            column_rows.append([schema, table, c[2], c[3], c[4], c[5], c[6], distinct.get(c[3]), mn, mx, nulls])
            n = distinct.get(c[3])
            if n is not None and n <= MAX_DISTINCT_FOR_VALUES:
                try:
                    for value, count in wh.query(
                        f"SELECT {q(c[3])}, COUNT(*) FROM {full} GROUP BY 1 ORDER BY 2 DESC LIMIT {MAX_DISTINCT_FOR_VALUES}"
                    ):
                        value_rows.append([schema, table, c[3], value, count])
                except Exception as exc:
                    failed.append(f"{schema}.{table}.{c[3]} values: {str(exc)[:200]}")

        # ---- sample rows (all columns) ---------------------------------------------------
        samples: dict[str, list[str]] = {}
        if row_count:
            try:
                sel = ", ".join(f"to_json({q(c[3])})" if c not in profiled else f"CAST({q(c[3])} AS STRING)" for c in cols)
                for r_no, r in enumerate(wh.query(f"SELECT {sel} FROM {full} LIMIT {SAMPLE_ROWS}"), 1):
                    for c, v in zip(cols, r):
                        sample_rows.append([schema, table, r_no, c[3], v])
                        samples.setdefault(c[3], []).append("NULL" if v is None else str(v))
            except Exception as exc:
                failed.append(f"{schema}.{table} samples: {str(exc)[:200]}")

        # ---- keys and grain -------------------------------------------------------------
        pk = declared_pk.get((schema, table))
        key_like = [c[3] for c in profiled if KEY_LIKE.search(c[3]) and not str(c[4]).lower().startswith(NOT_KEY_TYPES)]
        key_like.sort(key=lambda n: (0 if re.search(r"(_KEY|_ID)$", n, re.I) else 1 if re.search(r"(PERIOD|YEAR|MONTH)", n, re.I) else 2))
        key_like = key_like[:MAX_KEY_CANDIDATES]
        found, dup_rows, key_note = [], None, ""
        if row_count and row_count <= KEY_SEARCH_MAX_ROWS:
            try:  # exact duplicate rows across all profiled columns
                distinct_rows = wh.query(f"SELECT COUNT(*) FROM (SELECT DISTINCT {', '.join(q(c[3]) for c in profiled)} FROM {full})")[0][0]
                dup_rows = row_count - distinct_rows
            except Exception as exc:
                failed.append(f"{schema}.{table} duplicate check: {str(exc)[:200]}")
            if not pk and key_like:
                for size in (1, 2, 3):
                    combos = list(combinations(key_like, size))
                    if not combos:
                        break
                    try:
                        exprs = [f"COUNT(DISTINCT struct({', '.join(q(x) for x in combo)}))" for combo in combos]
                        counts = wh.query(f"SELECT {', '.join(exprs)} FROM {full}")[0]
                    except Exception as exc:
                        failed.append(f"{schema}.{table} key search size {size}: {str(exc)[:200]}")
                        break
                    found = [list(combo) for combo, n in zip(combos, counts) if n == row_count]
                    if found:
                        break
                if not found:
                    key_note = "no unique combination of up to 3 key-like columns"
                    if dup_rows:
                        key_note += f"; {dup_rows} exact duplicate rows (possible double load)"
        elif row_count:
            key_note = f"key search skipped (more than {KEY_SEARCH_MAX_ROWS:,} rows)"
        for combo in found[:3]:
            key_rows.append([schema, table, "PROPOSED KEY (unique in current data)", "", " + ".join(combo), len(combo), "",
                             f"distinct = rows = {row_count}"])
        if pk:
            pk_text, grain = ", ".join(pk), "proposed: one row per " + " + ".join(pk)
        elif found:
            pk_text, grain = "proposed: " + ", ".join(found[0]), "proposed: one row per " + " + ".join(found[0])
        else:
            pk_text, grain = "", ""
        issues = f"proposed: {dup_rows} exact duplicate rows ({dup_rows * 100 / row_count:.1f}%)" if dup_rows else ""
        pk_hint = pk_text or key_note or "none found (please fill in)"
        table_rows.append([schema, table, ttype, comment, row_count, len(cols), pk_hint, dup_rows])
        fill_rows.append([schema, table, schema, "", "", grain, pk_text, "", "", "", "", issues])
        summaries.append((schema, table, comment, row_count, pk_hint, grain, dup_rows, cols, distinct, stats, samples))

    wh.close()
    values_by_col: dict[tuple, list[str]] = {}
    for sch, tbl, col, val, cnt in value_rows:
        values_by_col.setdefault((sch, tbl, col), []).append(str(val))
    wb = Workbook()
    wb.remove(wb.active)
    write_sheet(wb, "Tables", ["schema", "table", "type", "comment", "row_count", "column_count", "primary_key_hint",
                               "exact_duplicate_rows"], table_rows)
    write_sheet(wb, "Keys", ["schema", "table", "kind", "constraint", "column", "position", "references", "note"], key_rows)
    write_sheet(wb, "Columns", ["schema", "table", "position", "column", "type", "nullable", "comment", "approx_distinct",
                                "min", "max", "null_count"], column_rows)
    write_sheet(wb, "Values", ["schema", "table", "column", "value", "count"], value_rows)
    write_sheet(wb, "Samples", ["schema", "table", "row", "column", "value"], sample_rows)
    write_sheet(wb, "Fill_in", FILL_HEADER, fill_rows)
    if failed:
        write_sheet(wb, "Errors", ["problem"], [[f] for f in failed])
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)

    # Plain-text copies for Copilot / Claude Code (cheap to read and edit)
    with open(out.with_name("fill_in.csv"), "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(FILL_HEADER)
        writer.writerows(fill_rows)
    lines = ["# Table catalog summary", "", f"{len(tables)} tables in {CATALOG} ({', '.join(SCHEMAS)}).", ""]
    for sch, tbl, cmt, rows, hint, grain, dups, cols, dist, st, smp in summaries:
        lines.append(f"## {sch}.{tbl}")
        lines.append(f"rows: {rows} | key: {hint} | grain: {grain or '?'} | exact duplicate rows: {dups}")
        if cmt:
            lines.append(f"comment: {cmt}")
        parts = []
        for c in cols:
            vals = values_by_col.get((sch, tbl, c[3]))
            mn, mx, nulls = st.get(c[3], (None, None, None))
            if vals:
                v = f" values: {', '.join(vals[:MAX_DISTINCT_FOR_VALUES])}"
            else:
                ex = [x[:60] for x in smp.get(c[3], [])[:3]]
                v = f" examples: {' | '.join(ex)}" if ex else ""
            rng = f", min {mn}, max {mx}" if mn is not None or mx is not None else ""
            note = f" -- {c[6]}" if c[6] else ""
            parts.append(f"- {c[3]} ({c[4]}, distinct~{dist.get(c[3])}, nulls {nulls}{rng}){v}{note}")
        lines.extend(parts)
        lines.append("")
    out.with_name("catalog_summary.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\nDone: {len(tables)} tables, {len(failed)} problems. File: {out.resolve()}")


if __name__ == "__main__":
    main()
