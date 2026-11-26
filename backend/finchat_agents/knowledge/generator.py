"""Generate / update table pages from the catalog export (scripts/export_table_catalog.py).

Inputs: the catalog Excel (sheets Tables, Keys, Columns, Values, Samples, Fill_in, Errors; names are case-insensitive)
plus reviewed / draft fill-in rows, which win over Fill_in: sheets named `fill_in_draft_*` or `fill_in_reviewed_*` in the
workbook, and/or CSV files (`fill_in_reviewed_*.csv`). They carry `confidence` and `notes` columns.

Never overwrites what a person edited:
- front matter fields listed in `reviewed` (or all fields when `reviewed: true`) are kept;
- a section whose heading is followed by `<!-- reviewed -->` is kept as is;
- Columns and Values sections are merged: existing rows and cells are kept, only new columns / values are added.
Safety exception: new columns whose names look like personal data are always added to `pii_columns` (append only).
Generator-owned fields: status, broken_error, and the "Empty columns" section.
Pages hold only what the agents read: no row counts, per-value counts, data profile or sample rows (they are snapshots
that go out of date; answers always come from live queries). The export's Samples sheet is not used.

Data hygiene: values of entity and key columns are not written to pages (entity codes change and must be checked live
with get_column_values); values of personal-data columns are never listed, and email addresses are never written,
whatever the column (`scrub_personal`, applied to reviewed sections too).

Broken objects: tables named in the Errors sheet; when the workbook has no Errors sheet, tables without a row count
(the profiling query failed). They get `status: broken`; a later clean export re-enables them.

    python -m finchat_agents.knowledge.generator path/to/catalog.xlsx [--reviewed x.csv ...] [--review]
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

from .loader import KNOWLEDGE_DIR
from .page import PageDoc, parse_columns, parse_page, parse_values, render_columns, render_page, render_values

PROPOSED = "proposed:"
LIST_FIELDS = ("primary_key", "period_columns", "pii_columns", "built_from")
TEXT_FIELDS = ("domain", "purpose", "grain", "entity_column")
COLUMN_FIELDS = ("primary_key", "entity_column", "period_columns", "pii_columns")
FILL_FIELDS = TEXT_FIELDS + LIST_FIELDS + ("known_issues", "layer")
CONFIDENCE = {"high", "medium", "low"}
MAX_VALUES_PER_COLUMN = 50

PII_NAME = re.compile(
    r"(EMAIL|USERNAME|USER_NAME|USER_ID|PERSONNEL_NUMBER|(^|_)PERSON(_[A-Z]+)*_NAME(_PREFIX)?$"
    r"|(^|_)(PREPARER|APPROVER|REVIEWER|ASSIGNEE|ASSIGNED_TO|PREPARED_BY|APPROVED_BY|"
    r"REVIEWED_BY|REJECTED_BY|CREATED_BY|MODIFIED_BY|ADDED_BY|EMPLOYEE|OWNER|RESPONSIBLE|CONTACT|MANAGER|REPORTEE|"
    r"REQUESTER|BUYER|WORKER|PERSON|CERTIFIER)(_BY)?(_NAME|_ID|_USERNAME|_NUMBER)?$)",
    re.I,
)
CAMEL_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
MASKED = "<masked>"
ENTITY_LIKE = re.compile(r"(ENTITY|DATA_AREA|DATAAREA|COMPANY|_KEY$)", re.I)
PERIOD_LIKE = re.compile(r"(DATE|PERIOD|YEAR|MONTH|QUARTER|WEEK|ISSUED|COVERED)", re.I)


def looks_pii(column: str) -> bool:
    """Column names in both styles: APPROVED_BY_NAME and ApprovedByName."""
    return bool(PII_NAME.search(column) or PII_NAME.search(CAMEL_BOUNDARY.sub("_", column)))


def _cells(line: str) -> list[str]:
    return re.split(r"(?<!\\)\|", line)


def scrub_personal(text: str, pii: Iterable[str]) -> str:
    """Remove personal data from a page's text: for personal-data columns their listed values, min/max and sample cells;
    and every email address anywhere."""
    pii = set(pii)
    out: list[str] = []
    section, header, skipping = "", [], False
    for line in text.split("\n"):
        if line.startswith("## "):
            section, header, skipping = line[3:].strip().lower(), [], False
        if section == "values":
            head = re.match(r"^\*\*(.+?)\*\*\s*$", line.strip())
            if head:
                skipping = head.group(1) in pii
            if skipping:
                if not line.strip():
                    skipping = False
                continue
            if line.lstrip().startswith("- ") and EMAIL.search(line):
                continue
        elif section == "profile" and line.startswith("| `"):
            cells = _cells(line)
            if len(cells) >= 8 and cells[1].strip().strip("`") in pii:
                cells[5], cells[6] = "  ", "  "
                line = "|".join(cells)
        elif section == "sample rows" and line.startswith("|") and not line.startswith("|-"):
            cells = _cells(line)
            if not header:
                header = [c.strip() for c in cells]
            else:
                cells = [f" {MASKED} " if i < len(header) and header[i] in pii and c.strip() not in ("", "NULL") else c
                         for i, c in enumerate(cells)]
                line = "|".join(cells)
        out.append(EMAIL.sub(MASKED, line))
    return "\n".join(out)


@dataclass
class CatalogTable:
    schema: str
    table: str
    object_type: str = ""
    comment: str = ""
    row_count: int | None = None
    duplicate_rows: int | None = None
    columns: list[dict[str, Any]] = field(default_factory=list)
    values: dict[str, list[tuple[str, Any]]] = field(default_factory=dict)
    fill: dict[str, str] = field(default_factory=dict)
    keys: list[dict[str, Any]] = field(default_factory=list)  # Keys sheet rows (declared and proposed keys)
    confidence: str = ""
    notes: str = ""
    repaired: bool = False  # the draft row was misaligned and rebuilt from cell contents
    dropped: list[str] = field(default_factory=list)  # draft values that could not be used, with the reason
    excel_altered: set[str] = field(default_factory=set)  # STRING columns whose values came back as dates (Excel)
    error: str | None = None

    @property
    def id(self) -> str:
        return f"{self.schema}.{self.table}"

    @property
    def column_names(self) -> list[str]:
        return [str(c["column"]) for c in self.columns]

    def canonical(self, name: str) -> str | None:
        low = name.strip().strip("`").lower()
        return next((c for c in self.column_names if c.lower() == low), None)


@dataclass
class GenerateReport:
    created: list[str] = field(default_factory=list)
    updated: list[str] = field(default_factory=list)
    unchanged: list[str] = field(default_factory=list)
    broken: list[str] = field(default_factory=list)
    re_enabled: list[str] = field(default_factory=list)
    kept_reviewed: list[str] = field(default_factory=list)  # "table: field"
    missing_columns: list[str] = field(default_factory=list)  # in the page, not in the export: "table.column"
    auto_pii: list[str] = field(default_factory=list)  # "table.column" flagged as personal data by name
    catalog: dict[str, CatalogTable] = field(default_factory=dict)


# ---------------------------------------------------------------- reading the export

def _header_key(h: Any) -> str:
    """'domain (ar/ap/...)' -> 'domain'; 'grain (one row = ?)' -> 'grain'."""
    return str(h or "").split("(")[0].strip().lower().replace(" ", "_")


def _txt(v: Any) -> Any:
    """Excel numbers: 100.0 -> '100'; other values unchanged."""
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    return v


def _rows(ws: Any) -> list[dict[str, Any]]:
    it = ws.iter_rows(values_only=True)
    try:
        header = [_header_key(h) for h in next(it)]
    except StopIteration:
        return []
    out = []
    for r in it:
        if not any(v not in (None, "") for v in r):
            continue
        cells = [_txt(v) for v in r]
        row = dict(zip(header, cells))
        row["_cells"] = cells
        out.append(row)
    return out


def _excel_date(v: Any, sql_type: str) -> bool:
    return isinstance(v, (dt.date, dt.datetime)) and sql_type.startswith(("STRING", "VARCHAR", "CHAR"))


def _int(v: Any) -> int | None:
    try:
        return int(float(v)) if v not in (None, "") else None
    except (TypeError, ValueError):
        return None


def _list(value: str) -> list[str]:
    return [p.strip() for p in re.split(r"[,;+]", value) if p.strip()]


def _split_proposed(value: str) -> tuple[str, bool]:
    if value.lower().startswith(PROPOSED):
        return value[len(PROPOSED):].strip(), True
    return value, False


def repair_draft_cells(cells: list[Any], t: CatalogTable, table_names: set[str]) -> dict[str, str]:
    """Rebuild a misaligned draft row (values slid into the wrong columns) from what each cell contains.
    schema/table/layer/domain/purpose/grain (cells 0-5) are kept; the rest is classified by content."""
    out: dict[str, str] = {}
    for key, idx in (("layer", 2), ("domain", 3), ("purpose", 4), ("grain", 5)):
        if idx < len(cells) and cells[idx] not in (None, ""):
            out[key] = str(cells[idx]).strip()
    notes: list[str] = []
    pk: list[str] = []
    for v in cells[6:]:
        if v in (None, ""):
            continue
        s = str(v).strip()
        low = s.lower()
        if low in CONFIDENCE and "confidence" not in out:
            out["confidence"] = low
            continue
        tokens = _list(_split_proposed(s)[0])
        if tokens and all(tok.lower() in table_names for tok in tokens):
            out["built_from"] = s
            continue
        if "duplicate" in low or low.startswith("broken") or "on all rows" in low:
            out["known_issues"] = s
            continue
        if tokens and all(t.canonical(tok) for tok in tokens):
            # column lists appear in the order primary key, entity, period, pii
            if all(looks_pii(tok) for tok in tokens):
                out["pii_columns"] = s
            elif len(tokens) == 1 and ENTITY_LIKE.search(tokens[0]) and "entity_column" not in out:
                out["entity_column"] = s
            elif pk and "period_columns" not in out and all(PERIOD_LIKE.search(tok) for tok in tokens):
                out["period_columns"] = s
            else:
                pk.append(s)
            continue
        notes.append(s)
    if pk:
        joined = ", ".join(_split_proposed(p)[0] for p in pk)
        out["primary_key"] = (PROPOSED + " " + joined) if any(p.lower().startswith(PROPOSED) for p in pk) else joined
    out["notes"] = "; ".join(notes)
    out.setdefault("confidence", "low")
    return out


_BROKEN = re.compile(r"^(\w+)\.(\w+): (.*)$", re.S)


def read_catalog(xlsx: Path | str, reviewed_csvs: Iterable[Path | str] = ()) -> dict[str, CatalogTable]:
    from openpyxl import load_workbook

    wb = load_workbook(xlsx, read_only=True, data_only=True)
    sheets = {name.lower(): _rows(wb[name]) for name in wb.sheetnames}
    tables: dict[str, CatalogTable] = {}

    def get(schema: Any, table: Any) -> CatalogTable:
        key = f"{schema}.{table}"
        if key not in tables:
            tables[key] = CatalogTable(schema=str(schema), table=str(table))
        return tables[key]

    for r in sheets.get("tables", []):
        t = get(r["schema"], r["table"])
        t.object_type = str(r.get("type") or "")
        t.comment = str(r.get("comment") or "")
        t.row_count = _int(r.get("row_count"))
        t.duplicate_rows = _int(r.get("exact_duplicate_rows"))
    types: dict[tuple[str, str], str] = {}
    for r in sorted(sheets.get("columns", []), key=lambda r: _int(r.get("position")) or 0):
        t = get(r["schema"], r["table"])
        types[(t.id, str(r["column"]))] = str(r.get("type") or "").upper()
        for k in ("min", "max"):  # the export writes text: a date in a STRING column means Excel converted it
            if _excel_date(r.get(k), types[(t.id, str(r["column"]))]):
                r[k] = None
                t.excel_altered.add(str(r["column"]))
        t.columns.append(r)
    for r in sheets.get("values", []):
        t = get(r["schema"], r["table"])
        if _excel_date(r["value"], types.get((t.id, str(r["column"])), "")):
            t.excel_altered.add(str(r["column"]))
            continue
        t.values.setdefault(str(r["column"]), []).append((str(r["value"]), r.get("count")))
    for r in sheets.get("keys", []):
        get(r["schema"], r["table"]).keys.append(r)
    for r in sheets.get("fill_in", []):
        get(r["schema"], r["table"]).fill.update({k: str(v).strip() for k, v in r.items() if k in FILL_FIELDS and v not in (None, "")})

    table_names = {t.table.lower() for t in tables.values()} | {k.lower() for k in tables}

    def apply_reviewed(row: dict[str, Any], cells: list[Any] | None) -> None:
        if not row.get("schema") or not row.get("table"):
            return
        t = get(row["schema"], row["table"])
        conf = str(row.get("confidence") or "").strip().lower()
        if cells is not None and conf not in CONFIDENCE:  # misaligned row: rebuild from cell contents
            fixed = repair_draft_cells(cells, t, table_names)
            t.repaired = True
            t.confidence = fixed.pop("confidence")
            t.notes = fixed.pop("notes", "")
            t.fill.update({k: v for k, v in fixed.items() if v})
            return
        t.confidence = conf
        t.notes = str(row.get("notes") or "").strip()
        t.fill.update({k: str(v).strip() for k, v in row.items() if k in FILL_FIELDS and v not in (None, "") and str(v).strip()})

    for name, rows in sheets.items():
        if name.startswith(("fill_in_draft", "fill_in_reviewed")):
            for r in rows:
                apply_reviewed(r, r.get("_cells"))
    for path in reviewed_csvs:
        with open(path, newline="", encoding="utf-8-sig") as fh:
            for r in csv.DictReader(fh):
                apply_reviewed({_header_key(k): v for k, v in r.items()}, None)

    if "errors" in sheets:
        for r in sheets["errors"]:
            m = _BROKEN.match(str(r.get("problem") or ""))
            if m:  # "schema.table: error" = the profiling query failed; ".col values:" / " samples:" lines are not
                get(m.group(1), m.group(2)).error = m.group(3).strip()
    else:
        for t in tables.values():
            if t.row_count is None and t.columns:
                t.error = "the profiling query failed in the catalog export (no row count); the error text is not in the workbook"
    return tables


# ---------------------------------------------------------------- merging into a page

def _issues_from(t: CatalogTable) -> list[dict[str, str]]:
    out = []
    if t.duplicate_rows:
        pct = f" ({t.duplicate_rows * 100 / t.row_count:.1f}%)" if t.row_count else ""
        out.append({"code": "duplicates", "note": f"{t.duplicate_rows} exact duplicate rows in the latest export{pct}. "
                    "Check duplicates at the grain before counting or summing; warn the user."})
    text = t.fill.get("known_issues", "")
    if text:
        clean, _ = _split_proposed(text)
        low = clean.lower()
        if "duplicate" in low:
            if not t.duplicate_rows:
                out.append({"code": "duplicates", "note": clean})
        elif low.startswith("broken"):
            pass  # status: broken comes from the Errors sheet
        elif not all(tok.lower() in {c.lower() for c in t.column_names} for tok in _list(clean)):
            out.append({"code": "empty_column" if ("null" in low or "empty" in low) else "other", "note": clean})
    return out


def _new_front(t: CatalogTable) -> dict[str, Any]:
    return {
        "name": t.table,
        "schema": t.schema,
        "layer": t.schema if t.schema in ("bronze", "silver", "gold") else "silver",
        "domain": None,
        "type": "view" if "view" in t.object_type.lower() else "table",
        "status": "active",
        "purpose": t.comment or "",
        "grain": "",
        "primary_key": [],
        "entity_column": None,
        "period_columns": [],
        "pii_columns": [],
        "synonyms": [],
        "built_from": [],
        "known_issues": [],
        "proposed_fields": [],
        "reviewed": False,
    }


def _is_reviewed(front: dict[str, Any], name: str) -> bool:
    rev = front.get("reviewed")
    return rev is True or (isinstance(rev, list) and name in rev)


def _check_columns(t: CatalogTable, name: str, values: list[str]) -> list[str]:
    """Keep column references that exist in the export (fixing their case); report the rest."""
    if not t.columns:
        return values
    out = []
    for v in values:
        canon = t.canonical(v)
        if canon:
            out.append(canon)
        else:
            t.dropped.append(f"{name}: '{v}' is not a column of the table")
    return out


def _merge_front(front: dict[str, Any], t: CatalogTable, report: GenerateReport, domains: set[str] | None) -> None:
    proposed = set(front.get("proposed_fields") or [])
    for name in ("layer",) + TEXT_FIELDS + LIST_FIELDS:
        raw = t.fill.get(name)
        if not raw:
            continue
        if _is_reviewed(front, name):
            report.kept_reviewed.append(f"{t.id}: {name}")
            continue
        value, is_proposed = _split_proposed(raw)
        if name in LIST_FIELDS:
            items = _list(value)
            if name in COLUMN_FIELDS:
                items = _check_columns(t, name, items)
            front[name] = items
        elif name == "entity_column":
            cols = _check_columns(t, name, _list(value)[:1])
            front[name] = cols[0] if cols else None
        elif name == "domain":
            dom = value.strip().lower()
            if domains is not None and dom not in domains:
                t.dropped.append(f"domain: '{value}' is not a domain in the access file")
                continue
            front[name] = dom
        else:
            front[name] = value
        (proposed.add if is_proposed else proposed.discard)(name)
    if not front.get("purpose") and t.comment and not _is_reviewed(front, "purpose"):
        front["purpose"] = t.comment

    if _is_reviewed(front, "known_issues"):
        if _issues_from(t):
            report.kept_reviewed.append(f"{t.id}: known_issues")
    else:
        issues = list(front.get("known_issues") or [])
        codes = {i.get("code") for i in issues}
        for issue in _issues_from(t):
            if issue["code"] not in codes:
                issues.append(issue)
                codes.add(issue["code"])
        front["known_issues"] = issues

    front["proposed_fields"] = sorted(proposed)
    front.pop("row_count", None)  # a snapshot the agents do not use
    if t.error:
        front["status"] = "broken"
        front["broken_error"] = t.error
    else:
        front["status"] = "active"
        front.pop("broken_error", None)


def _merge_columns(doc: PageDoc, t: CatalogTable, report: GenerateReport) -> list[str]:
    """Returns the names of columns added in this run."""
    section = doc.section("Columns")
    if section is not None and section.reviewed:
        return []
    existing = parse_columns(section.content) if section else []
    by_name = {c["name"]: c for c in existing}
    export_names, added = set(), []
    for col in t.columns:
        name = str(col["column"])
        export_names.add(name)
        meaning = str(col.get("comment") or "")
        if name in by_name:
            c = by_name[name]
            if not c.get("meaning") and meaning:
                c["meaning"] = meaning
        else:
            new = {"name": name, "type": str(col.get("type") or "string").lower(), "meaning": meaning, "synonyms": [], "sql": name}
            existing.append(new)
            by_name[name] = new
            added.append(name)
    if t.columns:
        report.missing_columns += [f"{t.id}.{n}" for n in by_name if n not in export_names]
    if existing:
        doc.set_section("Columns", render_columns(existing))
    return added


def _hidden_values(front: dict[str, Any], t: CatalogTable) -> set[str]:
    """Columns whose values never go into pages: entity and key columns, and personal data."""
    hidden = {c for c in t.column_names if ENTITY_LIKE.search(c)}
    if front.get("entity_column"):
        hidden.add(front["entity_column"])
    return hidden | set(front.get("pii_columns") or [])


def _merge_values(doc: PageDoc, t: CatalogTable, hidden: set[str]) -> None:
    section = doc.section("Values")
    if section is not None and section.reviewed:
        return
    values = parse_values(section.content) if section else {}
    for col, items in t.values.items():
        if col in hidden:
            continue
        known = {v for v, _ in values.get(col, [])}
        for raw, _ in items[:MAX_VALUES_PER_COLUMN]:
            value = _one_line(raw)
            if value not in known:
                known.add(value)
                values.setdefault(col, []).append((value, ""))
    if values:
        doc.set_section("Values", render_values(values), after="Columns")


VALUE_CHARS = 120


def _one_line(v: Any) -> str:
    """Values are listed one per line in backticks: no line breaks, no backticks, bounded length."""
    s = " ".join(str(v).split()).replace("`", "'")
    return s if len(s) <= VALUE_CHARS else s[: VALUE_CHARS - 3] + "..."


def _empty_columns(doc: PageDoc, t: CatalogTable) -> None:
    """The only part of the data profile the agents use: columns that are empty in every row. The profile table and
    sample rows of older pages are removed (unless a person marked them reviewed)."""
    for heading in ("Profile", "Sample rows"):
        old = doc.section(heading)
        if old is not None and not old.reviewed:
            doc.sections.remove(old)
    section = doc.section("Empty columns")
    if not t.columns or (section is not None and section.reviewed):
        return
    empty = [f"`{c['column']}`" for c in t.columns if _int(c.get("approx_distinct")) == 0]
    if empty:
        doc.set_section("Empty columns", f"Empty in every row: {', '.join(empty)}. Do not filter or group on them.",
                        after="Values")
    elif section is not None:
        doc.sections.remove(section)


def update_page(existing_text: str | None, t: CatalogTable, report: GenerateReport, domains: set[str] | None = None) -> str:
    if existing_text is None:
        title = f"# {t.table}"
        doc = PageDoc(front=_new_front(t), intro=title + (f"\n\n{t.comment}" if t.comment else ""))
    else:
        doc = parse_page(existing_text)
    _merge_front(doc.front, t, report, domains)
    added = _merge_columns(doc, t, report)
    # safety: personal-data columns are flagged even on reviewed pages (append only, never removed)
    pii = list(doc.front.get("pii_columns") or [])
    candidates = added if _is_reviewed(doc.front, "pii_columns") else t.column_names
    for c in candidates:
        if looks_pii(c) and c not in pii:
            pii.append(c)
            report.auto_pii.append(f"{t.id}.{c}")
    doc.front["pii_columns"] = pii
    hidden = _hidden_values(doc.front, t)
    _merge_values(doc, t, hidden)
    _empty_columns(doc, t)
    return scrub_personal(render_page(doc), pii)


def generate(
    xlsx: Path | str,
    tables_dir: Path | str = KNOWLEDGE_DIR / "tables",
    reviewed_csvs: Iterable[Path | str] = (),
    *,
    dry_run: bool = False,
    domains: set[str] | None = None,
) -> GenerateReport:
    tables_dir = Path(tables_dir)
    report = GenerateReport()
    report.catalog = read_catalog(xlsx, reviewed_csvs)
    for tid, t in sorted(report.catalog.items()):
        path = tables_dir / f"{tid}.md"
        old = path.read_text(encoding="utf-8") if path.exists() else None
        was_broken = old is not None and re.search(r"^status: broken\s*$", old, re.M) is not None
        new = update_page(old, t, report, domains)
        if t.error:
            report.broken.append(tid)
        elif was_broken:
            report.re_enabled.append(tid)
        if old is None:
            report.created.append(tid)
        elif new != old:
            report.updated.append(tid)
        else:
            report.unchanged.append(tid)
        if not dry_run and new != old:
            tables_dir.mkdir(parents=True, exist_ok=True)
            path.write_text(new, encoding="utf-8")
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xlsx")
    ap.add_argument("--reviewed", nargs="*", default=[])
    ap.add_argument("--root", default=str(KNOWLEDGE_DIR), help="knowledge folder (tables/ inside it)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--review", action="store_true", help="also write REVIEW.md, joins_proposed.yaml and INDEX.md")
    args = ap.parse_args()
    from .loader import load_domains

    root = Path(args.root)
    domains = set(load_domains(None)) or None
    r = generate(args.xlsx, root / "tables", args.reviewed, dry_run=args.dry_run, domains=domains)
    for name in ("created", "updated", "unchanged", "broken", "re_enabled", "auto_pii"):
        print(f"{name}: {len(getattr(r, name))}")
    if args.review and not args.dry_run:
        from .review import write_review

        print(write_review(root, r))


if __name__ == "__main__":
    main()
