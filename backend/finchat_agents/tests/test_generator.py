"""Generator tests with a small fake catalog Excel (same sheets as scripts/export_table_catalog.py)."""
from __future__ import annotations

import csv
from pathlib import Path

import pytest
from openpyxl import Workbook

from finchat_agents.knowledge.generator import generate
from finchat_agents.knowledge.loader import Knowledge
from finchat_agents.knowledge.page import parse_columns, parse_page

FILL_HEADER = ["schema", "table", "layer", "domain (ar/ap/gl/fa/cash/recon/subledger)", "purpose",
               "grain (one row = ?)", "primary_key", "entity_column", "period_columns", "pii_columns",
               "built_from", "known_issues"]


def make_xlsx(path: Path, *, broken: bool = True, extra_column: bool = False) -> Path:
    wb = Workbook()
    wb.remove(wb.active)

    def sheet(title, header, rows):
        ws = wb.create_sheet(title)
        ws.append(header)
        for r in rows:
            ws.append(r)

    sheet("Tables", ["schema", "table", "type", "comment", "row_count", "column_count", "primary_key_hint", "exact_duplicate_rows"], [
        ["gold", "vendor_spend", "MANAGED", "Vendor spend by month", 120, 4, "VENDOR_ID, MONTH", 0],
        ["silver", "fa_books", "MANAGED", "", 600, 3, "none found", 300],
        ["gold", "v_broken", "VIEW", "Broken view", None, 2, "", None],
    ])
    cols = [
        ["gold", "vendor_spend", 1, "VENDOR_ID", "string", "YES", "Vendor id", 40, "V001", "V040", 0],
        ["gold", "vendor_spend", 2, "MONTH", "date", "YES", "", 3, "2026-07-31", "2026-09-30", 0],
        ["gold", "vendor_spend", 3, "SPEND", "decimal(38,2)", "YES", "", 118, "10.00", "99999.00", 2],
        ["gold", "vendor_spend", 4, "BUYER_NAME", "string", "YES", "", 5, "Ann", "Zed", 0],
        ["silver", "fa_books", 1, "ASSET", "string", "YES", "", 300, "A1", "A9", 0],
        ["silver", "fa_books", 2, "BOOK", "string", "YES", "", 2, "TAX", "GAAP", 0],
        ["silver", "fa_books", 3, "STATUS", "string", "YES", "", 2, "Open", "Sold", 0],
        ["gold", "v_broken", 1, "X", "string", "YES", "", None, None, None, None],
        ["gold", "v_broken", 2, "Y", "string", "YES", "", None, None, None, None],
    ]
    if extra_column:
        cols.append(["silver", "fa_books", 4, "NEW_COL", "int", "YES", "Added later", 5, "1", "5", 0])
    sheet("Columns", ["schema", "table", "position", "column", "type", "nullable", "comment", "approx_distinct", "min", "max", "null_count"], cols)
    sheet("Values", ["schema", "table", "column", "value", "count"], [
        ["silver", "fa_books", "STATUS", "Open", 400],
        ["silver", "fa_books", "STATUS", "Sold", 200],
        ["gold", "vendor_spend", "BUYER_NAME", "Ann", 30],
    ])
    sheet("Samples", ["schema", "table", "row", "column", "value"], [
        ["gold", "vendor_spend", 1, "VENDOR_ID", "V001"],
        ["gold", "vendor_spend", 1, "MONTH", "2026-07-31"],
        ["gold", "vendor_spend", 1, "SPEND", "10.00"],
        ["gold", "vendor_spend", 1, "BUYER_NAME", "Ann Example"],
    ])
    sheet("Fill_in", FILL_HEADER, [
        ["gold", "vendor_spend", "gold", "", "", "proposed: one row per VENDOR_ID + MONTH", "proposed: VENDOR_ID, MONTH", "", "", "", "", ""],
        ["silver", "fa_books", "silver", "fa", "Draft purpose from Fill_in", "", "", "", "", "", "", "proposed: 300 exact duplicate rows (50.0%)"],
        ["gold", "v_broken", "gold", "", "", "", "", "", "", "", "", ""],
    ])
    errors = [["gold.v_broken: [UNRESOLVED_COLUMN] A column with name `Z` cannot be resolved"],
              ["gold.vendor_spend.SPEND values: timeout"]] if broken else [["gold.vendor_spend samples: timeout"]]
    sheet("Errors", ["problem"], errors)
    wb.save(path)
    return path


def make_csv(path: Path) -> Path:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(FILL_HEADER + ["confidence", "notes"])
        w.writerow(["gold", "vendor_spend", "gold", "ap", "Monthly spend per vendor.", "", "", "", "MONTH", "BUYER_NAME", "", "", "high", ""])
        w.writerow(["silver", "fa_books", "silver", "fa", "Purpose from the reviewed CSV", "one row per asset per book",
                    "ASSET, BOOK", "", "", "", "", "", "medium", ""])
    return path


EXISTING_FA_PAGE = """---
name: fa_books
schema: silver
layer: silver
domain: fa
type: dim
status: active
purpose: Hand-written purpose that must survive.
grain: old grain
primary_key: []
entity_column: null
period_columns: []
pii_columns: []
synonyms: [asset books]
known_issues: []
reviewed: [purpose]
---
# fa_books

Hand-written intro.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ASSET` | string | Asset number (person wrote this). | asset id | `trim(ASSET)` |
| `BOOK` | string |  |  | `BOOK` |

## Notes
<!-- reviewed -->

Person notes stay.
"""


@pytest.fixture
def env(tmp_path):
    tables = tmp_path / "knowledge" / "tables"
    tables.mkdir(parents=True)
    (tables / "silver.fa_books.md").write_text(EXISTING_FA_PAGE, encoding="utf-8")
    return tmp_path, tables


def test_generate_creates_updates_and_marks_broken(env):
    tmp, tables = env
    report = generate(make_xlsx(tmp / "cat.xlsx"), tables, [make_csv(tmp / "fill_in_reviewed_gold.csv")])
    assert sorted(report.created) == ["gold.v_broken", "gold.vendor_spend"]
    assert report.updated == ["silver.fa_books"]
    assert report.broken == ["gold.v_broken"]
    assert "silver.fa_books: purpose" in report.kept_reviewed

    # existing page: reviewed field and sections kept, other fields filled from the reviewed CSV
    fa = parse_page((tables / "silver.fa_books.md").read_text(encoding="utf-8"))
    assert fa.front["purpose"] == "Hand-written purpose that must survive."
    assert fa.front["grain"] == "one row per asset per book"  # CSV wins over Fill_in (empty) and old value
    assert fa.front["primary_key"] == ["ASSET", "BOOK"]
    assert fa.front["row_count"] == 600
    assert [i["code"] for i in fa.front["known_issues"]] == ["duplicates"]
    assert fa.section("Notes").reviewed and fa.section("Notes").content == "Person notes stay."
    assert "Hand-written intro." in fa.intro
    cols = {c["name"]: c for c in parse_columns(fa.section("Columns").content)}
    assert cols["ASSET"]["meaning"] == "Asset number (person wrote this)." and cols["ASSET"]["sql"] == "trim(ASSET)"
    assert "STATUS" in cols  # new column added
    assert "`Open`: 400 rows" in fa.section("Values").content
    assert "Exact duplicate rows: 300." in fa.section("Profile").content

    # new page: proposals flagged, PII masked in samples and values
    vs = parse_page((tables / "gold.vendor_spend.md").read_text(encoding="utf-8"))
    assert vs.front["domain"] == "ap" and vs.front["purpose"] == "Monthly spend per vendor."
    assert vs.front["grain"] == "one row per VENDOR_ID + MONTH"
    assert vs.front["primary_key"] == ["VENDOR_ID", "MONTH"]
    assert set(vs.front["proposed_fields"]) == {"grain", "primary_key"}
    assert vs.front["pii_columns"] == ["BUYER_NAME"]
    assert "Ann Example" not in (tables / "gold.vendor_spend.md").read_text(encoding="utf-8")
    assert "<masked>" in vs.section("Sample rows").content
    assert vs.section("Values") is None  # the only listed values were PII

    # broken object
    br = parse_page((tables / "gold.v_broken.md").read_text(encoding="utf-8"))
    assert br.front["status"] == "broken" and "UNRESOLVED_COLUMN" in br.front["broken_error"]
    assert br.front["type"] == "view" and br.front["domain"] is None


def test_generated_pages_load_and_are_excluded_from_search_when_needed(env):
    tmp, tables = env
    generate(make_xlsx(tmp / "cat.xlsx"), tables, [make_csv(tmp / "r.csv")])
    kb = Knowledge.load(tables.parent, strict=False)
    errors, warnings = kb.validate()
    assert errors == []
    assert any("gold.v_broken: no domain" in w for w in warnings)
    searchable = kb.searchable()
    assert "gold.v_broken" not in searchable  # broken and no domain
    assert {"gold.vendor_spend", "silver.fa_books"} <= searchable


def test_second_run_is_idempotent_and_re_enables(env):
    tmp, tables = env
    xlsx = make_xlsx(tmp / "cat.xlsx")
    csvs = [make_csv(tmp / "r.csv")]
    generate(xlsx, tables, csvs)
    again = generate(xlsx, tables, csvs)
    assert again.created == [] and again.updated == []

    fixed = generate(make_xlsx(tmp / "cat2.xlsx", broken=False, extra_column=True), tables, csvs)
    assert fixed.re_enabled == ["gold.v_broken"]
    br = parse_page((tables / "gold.v_broken.md").read_text(encoding="utf-8"))
    assert br.front["status"] == "active" and "broken_error" not in br.front
    fa = parse_page((tables / "silver.fa_books.md").read_text(encoding="utf-8"))
    assert "NEW_COL" in fa.section("Columns").content
    assert fa.front["purpose"] == "Hand-written purpose that must survive."


def test_fully_reviewed_page_front_matter_untouched(env):
    tmp, tables = env
    page = tables / "silver.fa_books.md"
    page.write_text(EXISTING_FA_PAGE.replace("reviewed: [purpose]", "reviewed: true"), encoding="utf-8")
    report = generate(make_xlsx(tmp / "cat.xlsx"), tables, [make_csv(tmp / "r.csv")])
    fa = parse_page(page.read_text(encoding="utf-8"))
    assert fa.front["grain"] == "old grain" and fa.front["primary_key"] == [] and fa.front["known_issues"] == []
    assert fa.front["row_count"] == 600  # generator-owned
    assert "silver.fa_books: known_issues" in report.kept_reviewed
