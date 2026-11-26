"""After a catalog run: propose joins, list lineage, and write knowledge/REVIEW.md for Karthik.

Proposed joins come from declared foreign keys (Keys sheet) and from key-name matches (a table holding every column
of another table's primary key). They go to joins_proposed.yaml with status `proposed`; get_join_path only uses
approved joins in joins.yaml. Approve a join by moving it to joins.yaml and setting `status: approved`.
"""
from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Any

import yaml

from .generator import CatalogTable, GenerateReport
from .loader import Knowledge

GENERIC_KEYS = {"id", "key", "hash_key", "month", "year", "section", "line_sort", "name", "code", "status",
                "row_id", "date", "period", "value", "type", "description"}
MAX_PROPOSALS_PER_TARGET = 15


def _cols(t: CatalogTable) -> dict[str, str]:
    return {c.lower(): c for c in t.column_names}


def propose_joins(kb: Knowledge, catalog: dict[str, CatalogTable]) -> list[dict[str, Any]]:
    existing = {(frozenset((j.from_, j.to)), frozenset(a.lower() for a, _ in j.keys)) for j in kb.joins if j.status != "proposed"}
    out: dict[str, dict[str, Any]] = {}

    def add(frm: str, to: str, pairs: list[tuple[str, str]], cardinality: str, source: str) -> None:
        sig = (frozenset((frm, to)), frozenset(a.lower() for a, _ in pairs))
        if sig in existing or frm == to:
            return
        existing.add(sig)
        jid = f"{frm.split('.')[1]}__{to.split('.')[1]}__{'_'.join(a.lower() for a, _ in pairs)}"[:120]
        out[jid] = {"id": jid, "from": frm, "to": to, "keys": [list(p) for p in pairs], "cardinality": cardinality,
                    "status": "proposed", "note": source}

    # 1. declared foreign keys
    for tid, t in catalog.items():
        for k in t.keys:
            if str(k.get("kind", "")).upper() != "FOREIGN KEY" or not k.get("references"):
                continue
            parts = str(k["references"]).split(".")
            if len(parts) != 3:
                continue
            target = f"{parts[0]}.{parts[1]}"
            if target in catalog and tid in kb.tables and target in kb.tables:
                add(tid, target, [(str(k["column"]), parts[2])], "many_to_one", "declared foreign key")

    # 2. key-name matches: `src` holds every column of `target`'s primary key
    for target_id, target in kb.tables.items():
        if target_id not in catalog or target.meta.status != "active" or target.meta.superseded_by:
            continue
        pk = target.meta.primary_key
        if not pk or len(pk) > 3 or (len(pk) == 1 and pk[0].lower() in GENERIC_KEYS):
            continue
        count = 0
        for src_id, src in catalog.items():
            if (src_id == target_id or src_id not in kb.tables or kb.tables[src_id].meta.status != "active"
                    or kb.tables[src_id].meta.superseded_by):
                continue
            cols = _cols(src)
            if all(c.lower() in cols for c in pk):
                same_key = [c.lower() for c in kb.tables[src_id].meta.primary_key] == [c.lower() for c in pk]
                add(src_id, target_id, [(cols[c.lower()], c) for c in pk], "one_to_one" if same_key else "many_to_one",
                    "key-name match: " + ("same primary key" if same_key else f"holds the full key of {target_id}"))
                count += 1
                if count >= MAX_PROPOSALS_PER_TARGET:
                    break
    return sorted(out.values(), key=lambda j: j["id"])


def lineage(kb: Knowledge) -> list[dict[str, Any]]:
    out = []
    for tid, p in sorted(kb.tables.items()):
        for src in p.meta.built_from:
            src_page = kb.resolve_table(src) or kb.resolve_table(f"silver.{src}")
            out.append({"table": tid, "built_from": src_page.id if src_page else src, "known": src_page is not None})
    return out


def _row(*cells: Any) -> str:
    return "| " + " | ".join(" ".join(str(c if c is not None else "").split()).replace("|", "/") for c in cells) + " |"


def review_markdown(kb: Knowledge, report: GenerateReport, joins: list[dict[str, Any]], lin: list[dict[str, Any]]) -> str:
    cat = report.catalog
    pages = {tid: p for tid, p in kb.tables.items() if tid in cat}
    no_domain = sorted(t for t, p in pages.items() if not p.meta.domain)
    broken = sorted(t for t, p in pages.items() if p.meta.status == "broken")
    low = sorted(t for t, c in cat.items() if c.confidence == "low" or c.repaired)
    proposed = sorted(t for t, p in pages.items() if p.meta.proposed_fields)
    dropped = sorted((t, d) for t, c in cat.items() for d in c.dropped)
    dups = sorted(t for t, p in pages.items() if p.meta.has_issue("duplicates"))
    stale_dups = [t for t in dups if pages[t].meta.reviewed and not cat[t].duplicate_rows]
    searchable = kb.searchable()
    superseded = sorted(t for t, p in pages.items() if p.meta.superseded_by)
    L = [
        "# Catalog review",
        "",
        f"Generated {dt.date.today().isoformat()} from the catalog export by `knowledge/generator.py` + `knowledge/review.py`.",
        "Approve by editing the table pages (set the field, add it to `reviewed`, remove it from `proposed_fields`) or by",
        "moving joins from `joins_proposed.yaml` to `joins.yaml` with `status: approved`. Rerun the generator afterwards.",
        "",
        "## Summary",
        "",
        f"- Tables in the export: {len(cat)}; pages: {len(kb.tables)}; searchable now: {len(searchable)}",
        f"- Without a domain (excluded from search): {len(no_domain)}",
        f"- Broken (excluded from search and run_sql): {len(broken)}",
        f"- Superseded copies (excluded from search and run_sql): {len(superseded)}",
        f"- Low confidence or repaired draft rows: {len(low)}",
        f"- Tables with proposed keys / grains: {len(proposed)}",
        f"- Duplicate warnings: {len(dups)} (of which {len(stale_dups)} reviewed pages where the export shows 0 duplicates)",
        f"- Personal-data columns (masked, never listed): {sum(len(p.meta.pii_columns) for p in pages.values())} in "
        f"{sum(1 for p in pages.values() if p.meta.pii_columns)} tables",
        f"- Tables with values altered by Excel: {sum(1 for c in cat.values() if c.excel_altered)}",
        f"- Proposed joins: {len(joins)}; lineage links: {len(lin)}",
        "",
        "## 1. Missing domains (excluded from search until set)",
        "",
        _row("Table", "Purpose (draft)", "Confidence", "Notes"),
        "|---|---|---|---|",
        *[_row(f"`{t}`", pages[t].meta.purpose[:120], cat[t].confidence, cat[t].notes[:160]) for t in no_domain],
        "",
        "## 2. Broken objects (for the data team)",
        "",
        _row("Table", "Error"),
        "|---|---|",
        *[_row(f"`{t}`", pages[t].meta.broken_error) for t in broken],
        "",
        "## 2b. Superseded copies (decision: use the source of truth)",
        "",
        _row("Table", "Use instead"),
        "|---|---|",
        *[_row(f"`{t}`", ", ".join(f"`{x}`" for x in pages[t].meta.superseded_by)) for t in superseded],
        "",
        "## 3. Low-confidence and repaired rows",
        "",
        "Repaired = the draft row was misaligned (values in the wrong columns) and was rebuilt from what each cell contains:",
        "check entity, period and PII columns in particular.",
        "",
        _row("Table", "Confidence", "Repaired", "Domain", "Notes"),
        "|---|---|---|---|---|",
        *[_row(f"`{t}`", cat[t].confidence, "yes" if cat[t].repaired else "", pages[t].meta.domain or "-", cat[t].notes[:200])
          for t in low if t in pages],
        "",
        "## 4. Proposed keys and grains",
        "",
        _row("Table", "Proposed", "Grain", "Primary key"),
        "|---|---|---|---|",
        *[_row(f"`{t}`", ", ".join(pages[t].meta.proposed_fields), pages[t].meta.grain[:140], ", ".join(pages[t].meta.primary_key))
          for t in proposed],
        "",
        "## 5. Draft values not used",
        "",
        _row("Table", "Problem"),
        "|---|---|",
        *[_row(f"`{t}`", d) for t, d in dropped],
        "",
        "## 6. Personal-data columns",
        "",
        "Masked in results and never listed. Columns are flagged from the drafts and by name (names, usernames, emails,",
        "contact people, created/modified-by). Remove one from `pii_columns` only if it holds no personal data.",
        "",
        _row("Table", "Personal-data columns"),
        "|---|---|",
        *[_row(f"`{t}`", ", ".join(p.meta.pii_columns)) for t, p in sorted(pages.items()) if p.meta.pii_columns],
        "",
        "## 7. Duplicate tables",
        "",
        _row("Table", "Exact duplicate rows (export)", "Rows", "Note"),
        "|---|---|---|---|",
        *[_row(f"`{t}`", cat[t].duplicate_rows or 0, cat[t].row_count,
               "reviewed page says duplicates but the export shows none: still true?" if t in stale_dups else "")
          for t in dups],
        "",
        "## 8. Values altered by Excel (not written to pages)",
        "",
        "The workbook went through Excel, which turned text such as 'Feb 25' into dates. These columns had such values;",
        "they were left out of Values. Re-export without opening the file in Excel (or import the",
        "CSV as text) to get them back. Agents always check live values with get_column_values.",
        "",
        *[f"- `{t}`: {', '.join(sorted(c.excel_altered))}" for t, c in sorted(cat.items()) if c.excel_altered],
        "",
        "## 9. Columns on pages that are not in the export",
        "",
        *[f"- `{c}`" for c in sorted(report.missing_columns)],
        "",
        "## 10. Proposed joins (joins_proposed.yaml)",
        "",
        _row("Id", "From", "To", "Keys", "Cardinality", "Source"),
        "|---|---|---|---|---|---|",
        *[_row(j["id"], f"`{j['from']}`", f"`{j['to']}`", ", ".join(f"{a}={b}" for a, b in j["keys"]), j["cardinality"], j["note"])
          for j in joins],
        "",
        "## 11. Lineage (built_from)",
        "",
        _row("Table", "Built from", "Source page exists"),
        "|---|---|---|",
        *[_row(f"`{x['table']}`", f"`{x['built_from']}`", "yes" if x["known"] else "no") for x in lin],
        "",
    ]
    return "\n".join(L)


def write_review(root: Path, report: GenerateReport) -> str:
    root = Path(root)
    kb = Knowledge.load(root, strict=False)
    joins = propose_joins(kb, report.catalog)
    header = ("# Proposed joins from the catalog export (knowledge/review.py). Not used by get_join_path.\n"
              "# Approve: move an entry to joins.yaml and set status: approved (check cardinality and the full key).\n")
    body = yaml.safe_dump({"joins": joins}, sort_keys=False, allow_unicode=True, width=200) if joins else "joins: []\n"
    (root / "joins_proposed.yaml").write_text(header + body, encoding="utf-8")
    kb = Knowledge.load(root, strict=False)  # reload with the proposals, to validate them
    lin = lineage(kb)
    (root / "REVIEW.md").write_text(review_markdown(kb, report, joins, lin), encoding="utf-8")
    (root / "INDEX.md").write_text(kb.index_markdown(), encoding="utf-8")
    errors, warnings = kb.validate()
    return f"REVIEW.md, joins_proposed.yaml and INDEX.md written ({len(errors)} errors, {len(warnings)} warnings)"
