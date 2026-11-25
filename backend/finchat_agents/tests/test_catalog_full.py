"""Task 08 generator features with a small fake workbook: draft sheets, misaligned rows, Excel-altered dates,
broken objects without an Errors sheet, PII auto-flagging, hidden entity values, review files, proposed joins."""
from __future__ import annotations

import datetime as dt
from pathlib import Path

from openpyxl import Workbook

from finchat_agents.knowledge.generator import CatalogTable, generate, read_catalog, repair_draft_cells
from finchat_agents.knowledge.loader import Knowledge
from finchat_agents.knowledge.page import parse_page
from finchat_agents.knowledge.review import write_review

FILL_HEADER = ["schema", "table", "layer", "domain (ar/ap/gl/fa/cash/recon/subledger", "purpose",
               "grain (one row = ?)", "primary_key", "entity_column", "period_columns", "pii_columns",
               "built_from", "known_issues"]
DRAFT_HEADER = FILL_HEADER + ["confidence", "notes"]
DOMAINS = {"fa", "recon"}


def make_full_xlsx(path: Path) -> Path:
    wb = Workbook()
    wb.remove(wb.active)

    def sheet(title, header, rows):
        ws = wb.create_sheet(title)
        ws.append(header)
        for r in rows:
            ws.append(r)

    sheet("Tables", ["schema", "table", "type", "comment", "row_count", "column_count", "primary_key_hint", "exact_duplicate_rows"], [
        ["gold", "journal_view", "VIEW", "", 100.0, 5.0, "proposed: JOURNAL_ID, ASSET_ID", 0.0],
        ["silver", "periods", "MANAGED", "", 3.0, 3.0, "PERIOD_KEY", 0.0],
        ["gold", "dead_view", "VIEW", "", None, 1.0, "", None],
    ])
    sheet("Columns", ["schema", "table", "position", "column", "type", "nullable", "comment", "approx_distinct", "min", "max", "null_count"], [
        ["gold", "journal_view", 0.0, "JOURNAL_ID", "STRING", "YES", "", 10, "J1", "J9", 0],
        ["gold", "journal_view", 1.0, "ASSET_ID", "STRING", "YES", "", 10, "A1", "A9", 0],
        ["gold", "journal_view", 2.0, "LEGAL_ENTITY", "STRING", "YES", "", 2, "E1", "E2", 0],
        ["gold", "journal_view", 3.0, "APPROVER_USERNAME", "STRING", "YES", "", 3, "a@x", "c@x", 0],
        ["gold", "journal_view", 4.0, "AMOUNT", "DECIMAL(38,2)", "YES", "", 90, "1.00", "9.00", 0],
        ["silver", "periods", 0.0, "PERIOD_KEY", "STRING", "YES", "", 3, "1", "3", 0],
        ["silver", "periods", 1.0, "PERIOD_NAME", "STRING", "YES", "", 3, dt.datetime(2026, 2, 25), dt.datetime(2026, 9, 26), 0],
        ["silver", "periods", 2.0, "PERIOD_END", "DATE", "YES", "", 3, dt.datetime(2025, 2, 28), dt.datetime(2026, 9, 30), 0],
        ["gold", "dead_view", 0.0, "X", "STRING", "YES", "", None, None, None, None],
    ])
    sheet("values", ["schema", "table", "column", "value", "count"], [
        ["silver", "periods", "PERIOD_NAME", dt.datetime(2026, 2, 25), 1.0],
        ["gold", "journal_view", "LEGAL_ENTITY", "E1", 60.0],
        ["gold", "journal_view", "APPROVER_USERNAME", "a@x", 50.0],
    ])
    sheet("Samples", ["schema", "table", "row", "column", "value"], [
        ["gold", "journal_view", 1.0, "JOURNAL_ID", "J1"],
        ["gold", "journal_view", 1.0, "LEGAL_ENTITY", "E1"],
        ["gold", "journal_view", 1.0, "APPROVER_USERNAME", "a@x"],
        ["silver", "periods", 1.0, "PERIOD_NAME", dt.datetime(2026, 2, 25)],
        ["silver", "periods", 1.0, "PERIOD_END", dt.datetime(2025, 2, 28)],
    ])
    sheet("keys", ["schema", "table", "kind", "constraint", "column", "position", "references", "note"], [
        ["gold", "journal_view", "FOREIGN KEY", "fk", "ASSET_ID", 1.0, "silver.periods.PERIOD_KEY", "declared"],
    ])
    sheet("fill_in", FILL_HEADER, [["gold", "journal_view", "gold", "", "", "", "", "", "", "", "", ""]])
    # misaligned: the primary key "JOURNAL_ID, ASSET_ID" was split into two cells and everything after slid right
    sheet("fill_in_draft_gold", DRAFT_HEADER, [
        ["gold", "journal_view", "gold", "fa", "Depreciation journal lines.", "proposed: one row per JOURNAL_ID + ASSET_ID",
         "proposed: JOURNAL_ID", "ASSET_ID", "LEGAL_ENTITY", None, None, "periods", None, "high"],
        ["gold", "dead_view", "gold", "nowhere", "A view that fails.", "one row per X", "X", "", "", "", "", "", "low", "guess"],
    ])
    sheet("fill_in_draft_silver", DRAFT_HEADER, [
        ["silver", "periods", "silver", "recon", "Periods.", "one row per period", "PERIOD_KEY", "", "PERIOD_NAME; PERIOD_END",
         "", "", "", "high", ""],
    ])
    wb.save(path)
    return path


def test_misaligned_draft_row_is_repaired(tmp_path):
    cat = read_catalog(make_full_xlsx(tmp_path / "c.xlsx"))
    jv = cat["gold.journal_view"]
    assert jv.repaired and jv.confidence == "high"
    assert jv.fill["primary_key"] == "proposed: JOURNAL_ID, ASSET_ID"
    assert jv.fill["entity_column"] == "LEGAL_ENTITY" and jv.fill["built_from"] == "periods" and jv.fill["domain"] == "fa"
    assert not cat["silver.periods"].repaired and cat["silver.periods"].fill["period_columns"] == "PERIOD_NAME; PERIOD_END"


def test_repair_classifies_cells_by_content():
    t = CatalogTable("gold", "x", columns=[{"column": c} for c in ("SECTION", "KPI", "LEGAL_ENTITY", "YEAR", "MONTH", "OWNER_NAME")])
    out = repair_draft_cells(["gold", "x", "gold", "gl", "p", "g", "SECTION, KPI", "LEGAL_ENTITY", "YEAR, MONTH",
                              "OWNER_NAME", "medium", "only seven rows"], t, set())
    assert out["primary_key"] == "SECTION, KPI" and out["entity_column"] == "LEGAL_ENTITY"
    assert out["period_columns"] == "YEAR, MONTH" and out["pii_columns"] == "OWNER_NAME"
    assert out["confidence"] == "medium" and out["notes"] == "only seven rows"


def test_excel_altered_dates_are_dropped(tmp_path):
    tables = tmp_path / "tables"
    report = generate(make_full_xlsx(tmp_path / "c.xlsx"), tables, domains=DOMAINS)
    assert report.catalog["silver.periods"].excel_altered == {"PERIOD_NAME"}
    text = (tables / "silver.periods.md").read_text(encoding="utf-8")
    assert "2026-02-25" not in text  # not in Values, Profile min/max or samples
    assert "(altered in export)" in text and "2025-02-28" in text  # real DATE columns keep their dates


def test_broken_without_errors_sheet_domains_pii_and_hidden_values(tmp_path):
    tables = tmp_path / "tables"
    report = generate(make_full_xlsx(tmp_path / "c.xlsx"), tables, domains=DOMAINS)
    assert report.broken == ["gold.dead_view"]
    dead = parse_page((tables / "gold.dead_view.md").read_text(encoding="utf-8"))
    assert dead.front["status"] == "broken" and dead.front["domain"] is None  # 'nowhere' is not a domain
    assert any("not a domain" in d for d in report.catalog["gold.dead_view"].dropped)
    jv_text = (tables / "gold.journal_view.md").read_text(encoding="utf-8")
    jv = parse_page(jv_text)
    assert "APPROVER_USERNAME" in jv.front["pii_columns"] and "gold.journal_view.APPROVER_USERNAME" in report.auto_pii
    assert "a@x" not in jv_text  # personal data never written
    assert jv.front["entity_column"] == "LEGAL_ENTITY" and "**LEGAL_ENTITY**" not in jv_text  # entity values hidden
    assert "| E1 |" not in jv_text and "| E2 |" not in jv_text


def test_reviewed_page_gets_new_pii_columns_flagged(tmp_path):
    tables = tmp_path / "tables"
    tables.mkdir()
    (tables / "gold.journal_view.md").write_text(
        "---\nname: journal_view\nschema: gold\nlayer: gold\ndomain: fa\npurpose: p\ngrain: g\nprimary_key: [JOURNAL_ID]\n"
        "pii_columns: []\nreviewed: true\n---\n# journal_view\n\n## Columns\n\n| Column | Type | Meaning | Also called | SQL expression |\n"
        "|---|---|---|---|---|\n| `JOURNAL_ID` | string | Journal. |  | `JOURNAL_ID` |\n", encoding="utf-8")
    generate(make_full_xlsx(tmp_path / "c.xlsx"), tables, domains=DOMAINS)
    jv = parse_page((tables / "gold.journal_view.md").read_text(encoding="utf-8"))
    assert jv.front["pii_columns"] == ["APPROVER_USERNAME"]  # appended for safety although the page is reviewed
    assert jv.front["purpose"] == "p" and jv.front["primary_key"] == ["JOURNAL_ID"]


def test_review_files_and_proposed_joins(tmp_path):
    root = tmp_path / "knowledge"
    report = generate(make_full_xlsx(tmp_path / "c.xlsx"), root / "tables", domains=DOMAINS)
    assert "0 errors" in write_review(root, report)
    review = (root / "REVIEW.md").read_text(encoding="utf-8")
    for heading in ("Missing domains", "Broken objects", "Low-confidence and repaired rows", "Proposed keys and grains",
                    "Personal-data columns", "Values altered by Excel", "Proposed joins", "Lineage"):
        assert heading in review
    assert "`gold.dead_view`" in review and "silver.periods`: PERIOD_NAME" in review
    kb = Knowledge.load(root, strict=False)
    proposed = [j for j in kb.joins if j.status == "proposed"]
    assert proposed, "the declared foreign key should become a proposed join"
    assert kb.join_path("gold.journal_view", "silver.periods") is None  # proposals are never used
    assert (root / "INDEX.md").exists()


def test_values_roundtrip_with_spaces_and_line_breaks(tmp_path):
    """Column names with spaces and multi-line values must read back, so reruns change nothing."""
    from finchat_agents.knowledge.generator import GenerateReport, update_page
    from finchat_agents.knowledge.page import parse_values, render_values

    assert parse_values(render_values({"Elimination ID": [("ELM-1", "6 rows")]})) == {"Elimination ID": [("ELM-1", "6 rows")]}
    t = CatalogTable("gold", "v", row_count=2, columns=[{"column": "Elimination ID", "type": "STRING"}, {"column": "TEXT", "type": "STRING"}],
                     values={"Elimination ID": [("ELM-1", 6)], "TEXT": [("line one\nline `two`", 1), ("short", 1)]})
    first = update_page(None, t, GenerateReport())
    assert "- `line one line 'two'`: 1 rows" in first
    assert update_page(first, t, GenerateReport()) == first



# ---------------------------------------------------------------- latency phase 1: compact describe_table pages

def test_compact_pages_are_much_smaller_and_keep_what_the_agents_use():
    from finchat_agents.knowledge.loader import Knowledge
    from finchat_agents.tools.catalog import VALUES_PER_COLUMN, compact_page

    kb = Knowledge.load()
    full = sum(len(p.body) for p in kb.tables.values())
    small = sum(len(compact_page(p.body)) for p in kb.tables.values())
    assert small < full * 0.7  # at least 30% less text across all pages
    fy = compact_page(kb.resolve_table("silver.fact_fynapse_slr_journals").body)
    assert "`FISCAL_YEAR`" in fy and "Empty in every row" in fy and "Rows in the latest export: 1200" in fy
    adra = kb.resolve_table("silver.adra_account_facts").body
    small_adra = compact_page(adra)
    for section in ("## Columns", "## Values", "## Joins", "## Named metrics", "## Notes"):
        assert section in small_adra, section
    assert "Not prepared" in small_adra  # stored values the SQL needs for filters stay
    assert "## Sample rows" in small_adra and "detail='full'" in small_adra
    for block in small_adra.split("## Values", 1)[1].split("## ", 1)[0].split("**")[2::2]:
        assert block.count("\n- ") <= VALUES_PER_COLUMN + 1


async def test_describe_table_is_compact_by_default_and_full_on_request():
    from .fakes import make_deps
    from finchat_agents.access.rbac import Role, UserAccess
    from finchat_agents.runtime.tools import RunContext, ToolContext
    from finchat_agents.tools import build_data_tools
    from finchat_agents.tracing import MemorySink, Tracer

    deps, _ = make_deps()
    tool = build_data_tools(deps)["describe_table"]
    run = RunContext(tracer=Tracer([MemorySink()]), user=UserAccess(user_id="u", role=Role(name="all", domains=["*"])))
    tctx = ToolContext(run=run, agent="t", step=1, call_id="c")
    compact = await tool.handler({"table": "silver.adra_account_facts"}, tctx)
    full = await tool.handler({"table": "silver.adra_account_facts", "detail": "full"}, tctx)
    assert len(compact["page"]) < len(full["page"]) and full["page"] == deps.kb.resolve_table("silver.adra_account_facts").body
    assert "detail" in tool.spec.input_schema["properties"]
