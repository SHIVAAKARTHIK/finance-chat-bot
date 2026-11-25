from __future__ import annotations

import re
from pathlib import Path

import pytest
from sqlglot import exp, parse_one

from finchat_agents.knowledge.loader import KNOWLEDGE_DIR, Knowledge, KnowledgeError, parse_glossary


@pytest.fixture(scope="module")
def kb() -> Knowledge:
    return Knowledge.load()


HAND_PAGES = {
    "silver.adra_account_facts", "silver.adra_transaction_facts", "silver.adra_account_dimensions",
    "silver.adra_legal_entity_dimensions", "silver.adra_period_dimensions", "silver.adra_engagement_dimensions",
    "silver.fact_fynapse_slr_journals", "silver.dim_fixed_asset_books", "silver.dim_fixed_assets",
    "silver.fact_asset_master_transactions",
}


def test_all_pages_valid_and_complete(kb):
    assert len(kb.tables) >= 143 and HAND_PAGES <= set(kb.tables)
    errors, warnings = kb.validate()
    assert errors == []
    assert all("no domain" in w or "purpose and grain" in w for w in warnings), warnings
    for tid in HAND_PAGES:
        page = kb.tables[tid]
        m = page.meta
        assert m.domain in {"recon", "subledger", "fa"}, tid
        assert m.status == "active" and m.purpose and m.grain and m.primary_key, tid
        for c in m.pii_columns:
            assert page.column(c).pii, f"{tid}.{c} must be flagged pii"


def test_expected_domains(kb):
    by_domain = {}
    for tid, p in kb.tables.items():
        if tid in HAND_PAGES:
            by_domain.setdefault(p.meta.domain, set()).add(tid.split(".")[1])
    assert by_domain["recon"] == {
        "adra_account_facts", "adra_transaction_facts", "adra_account_dimensions",
        "adra_legal_entity_dimensions", "adra_period_dimensions", "adra_engagement_dimensions",
    }
    assert by_domain["subledger"] == {"fact_fynapse_slr_journals"}
    assert by_domain["fa"] == {"dim_fixed_asset_books", "dim_fixed_assets", "fact_asset_master_transactions"}


def test_known_issues_flags(kb):
    for name in ("dim_fixed_asset_books", "dim_fixed_assets", "fact_asset_master_transactions"):
        assert kb.resolve_table(name).meta.has_issue("duplicates")
    assert kb.resolve_table("fact_fynapse_slr_journals").meta.has_issue("entity_values_changing")
    assert kb.resolve_table("adra_account_facts").meta.has_issue("orphans")


# Entity scopes that came from v2 RBAC must not appear in hand-written knowledge.
FORBIDDEN = re.compile(r"\b(581|14781|14782|UK0?3|UK06|UK07|UK13|UK14|UK17)\b|DATA_AREA_ID\s*(=|IN)\s*\(?\s*'(100|dat)'", re.I)
GENERATED_SECTIONS = re.compile(r"\n## (Values|Profile|Sample rows)\n.*?(?=\n## |\Z)", re.S)
GENERATED_FILES = {"INDEX.md", "REVIEW.md", "joins_proposed.yaml"}


def _hand_written_text(path: Path) -> str:
    """Generated data profiles (Values, Profile, Sample rows) and generated files hold real data values, which may
    include entity codes or table names such as *_kpi; the rules are about hard-coded scopes, filters and KPI logic."""
    return GENERATED_SECTIONS.sub("\n", path.read_text(encoding="utf-8"))


def _knowledge_files() -> list[Path]:
    files = [p for p in sorted(KNOWLEDGE_DIR.glob("*")) if p.suffix in (".md", ".yaml") and p.name not in GENERATED_FILES]
    return files + [KNOWLEDGE_DIR / "tables" / f"{t}.md" for t in sorted(HAND_PAGES)]


@pytest.mark.parametrize("path", _knowledge_files(), ids=lambda p: p.name)
def test_no_hardcoded_entity_values(path: Path):
    hits = [m.group(0) for m in FORBIDDEN.finditer(_hand_written_text(path))]
    assert hits == [], f"{path.name} contains hardcoded entity values: {hits}"


def test_generated_pages_hide_entity_and_key_values(kb):
    """Values never list entity or key columns on generated pages (entity codes change; check them live)."""
    for tid, page in kb.tables.items():
        if page.meta.reviewed:
            continue
        values = re.search(r"\n## Values\n(.*?)(?=\n## |\Z)", page.body, re.S)
        if not values:
            continue
        hidden = [c.name for c in page.columns if re.search(r"(ENTITY|DATA_AREA|COMPANY|_KEY$)", c.name, re.I)]
        hidden += [page.meta.entity_column] if page.meta.entity_column else []
        hidden += page.meta.pii_columns
        for c in hidden:
            assert f"**{c}**" not in values.group(1), f"{tid}: values listed for {c}"


@pytest.mark.parametrize("path", _knowledge_files(), ids=lambda p: p.name)
def test_no_kpi_content(path: Path):
    assert not re.search(r"\bkpi", _hand_written_text(path), re.I), path.name


def test_joins_reference_known_tables_and_columns(kb):
    approved = [j for j in kb.joins if j.status == "approved"]
    assert len(approved) == 9
    for j in kb.joins:
        for idx, tid in ((0, j.from_), (1, j.to)):
            page = kb.tables[tid]
            assert all(page.has_column(pair[idx]) for pair in j.keys), j.id
    # ADRA joins keep the full composite key
    by_id = {j.id: j for j in kb.joins}
    assert len(by_id["account_fact_to_account"].keys) == 3
    assert len(by_id["account_fact_to_period"].keys) == 3
    assert by_id["asset_books_by_data_area_only"].status == "blocked"


def test_join_path(kb):
    path = kb.join_path("adra_transaction_facts", "silver.adra_engagement_dimensions")
    assert [j.id for j in path] == ["transaction_fact_to_legal_entity", "legal_entity_to_engagement"]
    assert kb.join_path("adra_account_facts", "adra_account_facts") == []
    assert kb.join_path("fact_fynapse_slr_journals", "adra_account_facts") is None
    assert kb.join_path("dim_fixed_asset_books", "fact_asset_master_transactions") is not None
    cond = path[0].condition("t", "le")
    assert cond == "t.LEGAL_ENTITY_KEY = le.LEGAL_ENTITY_KEY AND t.ENGAGEMENT_KEY = le.ENGAGEMENT_KEY"


def _aliases(tree: exp.Expression) -> dict[str, str]:
    out = {}
    for t in tree.find_all(exp.Table):
        out[(t.alias or t.name).lower()] = f"{t.db}.{t.name}".lower()
    return out


def test_example_joins_use_full_approved_keys(kb):
    """Every JOIN in an example uses an approved join with its complete key."""
    approved = {}
    for j in kb.joins:
        if j.status == "approved":
            pairs = {(j.from_.lower(), a.lower(), j.to.lower(), b.lower()) for a, b in j.keys}
            approved[frozenset((j.from_.lower(), j.to.lower()))] = (j, pairs)
    for e in kb.examples:
        tree = parse_one(e.sql, read="databricks")
        aliases = _aliases(tree)
        for join in tree.find_all(exp.Join):
            on = join.args.get("on")
            assert on is not None, f"{e.id}: join without ON"
            eqs = set()
            for eq in on.find_all(exp.EQ):
                left, right = eq.left, eq.right
                if isinstance(left, exp.Column) and isinstance(right, exp.Column):
                    lt, rt = aliases[left.table.lower()], aliases[right.table.lower()]
                    eqs.add((lt, left.name.lower(), rt, right.name.lower()))
                    eqs.add((rt, right.name.lower(), lt, left.name.lower()))
            tables = {t for q in eqs for t in (q[0], q[2])}
            assert len(tables) == 2, f"{e.id}: join condition must link exactly two tables"
            found = approved.get(frozenset(tables))
            assert found, f"{e.id}: no approved join between {tables}"
            assert found[1] <= eqs, f"{e.id}: join {found[0].id} must use the full key"


def test_examples_have_no_rbac_scope_filters(kb):
    for e in kb.examples:
        assert not re.search(r"(ENGAGEMENT_KEY|LEGAL_ENTITY_KEY)\s*=\s*'", e.sql, re.I), e.id
    assert len(kb.examples) >= 20


SEARCH_CASES = [
    ("What is the balance of account 141111 for 100-Northwind in Feb 25?", "adra_account_facts"),
    ("What is the reconciliation status of account 213130 for 561 - Cars USA Shipping, LLC in Oct 26?", "adra_account_facts"),
    ("How many Northwind accounts are in each reconciliation status for Feb 25?", "adra_account_facts"),
    ("Which 5 accounts have the largest absolute balance for 561 - Cars USA Shipping, LLC in Oct 26?", "adra_account_facts"),
    ("How many Northwind accounts are there for each risk type in Feb 25?", "adra_account_dimensions"),
    ("What is the total absolute unidentified balance for 100-Northwind in Feb 25?", "adra_account_facts"),
    ("How many transactions are recorded on account 222120 for Northwind in Feb 25?", "adra_transaction_facts"),
    ("What is the oldest transaction age in days across all Northwind accounts in Feb 25?", "adra_transaction_facts"),
    ("How are Cars USA Shipping transactions distributed across age groups in Oct 26?", "adra_transaction_facts"),
    ("How many Fynapse journal lines and what net reporting amount does each parent entity have?", "fact_fynapse_slr_journals"),
    ("Which journal types were posted in Fynapse in Sep 26, and how many lines each?", "fact_fynapse_slr_journals"),
    ("How many distinct Fynapse journals were posted in Sep 26?", "fact_fynapse_slr_journals"),
    ("Which 5 business events have the most Fynapse journal lines?", "fact_fynapse_slr_journals"),
    ("How many rejections have there been in total across Northwind accounts in Feb 25?", "adra_account_facts"),
    ("How many Northwind accounts have no supporting documents in Feb 25?", "adra_account_facts"),
]




@pytest.mark.parametrize("question,table", SEARCH_CASES, ids=[t for _, t in SEARCH_CASES])
def test_search_finds_table_in_top_3(kb, question, table):
    hits = [h.table for h in kb.search_tables(question, k=3)]
    assert f"silver.{table}" in hits, hits


GOLD_CASES = [
    ("Which customer invoices are overdue and need collection follow-up?", {"gold.managed_coll_overdue", "gold.vw_managed_coll_overdue", "gold.vw_managed_coll_overdue_filter"}),
    ("Which customer invoices are due soon?", {"gold.managed_coll_due_soon_accounts", "gold.vw_managed_coll_due_soon_accounts", "gold.vw_managed_coll_due_soon_accounts_filter"}),
    ("Which invoices are eligible for an early payment discount?", {"gold.managed_coll_early_payment_discounts", "gold.vw_managed_coll_early_payment_discounts", "gold.vw_managed_coll_early_payment_discounts_filter"}),
    ("Show vendor invoices with their due dates and status", {"gold.fact_ap_invoices"}),
    ("What is the actual cash balance for each bank account?", {"gold.mc_actual_cash_balance_by_bank_ac", "gold.mc_actual_cash_balance_by_bank_ac_new"}),
    ("Show liquid investment balances by asset", {"gold.mc_liquidity"}),
    ("Does the cash in the subledger reconcile to the general ledger by month?", {"gold.vw_cash_reconciliation"}),
    ("What is the net book value of each fixed asset in the asset register?", {"gold.fa_asset_register"}),
    ("How many fixed assets were disposed each month?", {"gold.fa_disposal_trends", "gold.disposal_workbench"}),
    ("What is the monthly depreciation total?", {"gold.fa_monthly_depreciation_trend"}),
    ("Which fixed assets are ready to be capitalized?", {"gold.capitalization_workbench"}),
    ("Show the balance sheet by entity and account", {"gold.vw_balance_sheet", "gold.vw_balance_sheet_logistics"}),
    ("What is net income on the income statement?", {"gold.vw_income_statement", "gold.vw_income_statement_logistics"}),
    ("What are the trial balance amounts by company?", {"gold.fact_trail_balance_extractions"}),
    ("Show the chart of accounts hierarchy", {"gold.dim_coa", "gold.dim_coa_logistics"}),
    ("How many journal entries were manual versus automated?", {"gold.manage_close_journal_entries", "gold.vw_manage_close_journal_entry_kpi"}),
    ("What were total expenses by expense account this year?", {"gold.vw_expense_analysis", "gold.vw_expense_analysis_gl"}),
    ("Which ADRA accounts are unreconciled and what is the difference?", {"silver.adra_account_facts"}),  # adra_* only
    ("How many close tasks are open by legal entity?", {"silver.adra_tasks_task_facts", "silver.adra_tasks_task_list_dimension"}),
    ("What was written and earned premium by period?", {"gold.vw_premium_analysis"}),
    ("Show IBNR and ultimate losses", {"gold.vw_ultimates_analysis"}),
    ("Does the Fynapse subledger reconcile to the GL by main account?", {"gold.vw_slr_gl_reconciliation"}),
    ("What commission income did we earn from brokerage?", {"gold.vw_commission_analysis_slr_mga", "gold.vw_commissions_analysis"}),
]


@pytest.mark.parametrize("question,accepted", GOLD_CASES, ids=[q[:40] for q, _ in GOLD_CASES])
def test_search_gold_domains_top_3(kb, question, accepted):
    hits = [h.table for h in kb.search_tables(question, k=3)]
    assert accepted & set(hits), hits


def test_broken_and_domainless_tables_are_excluded(kb):
    searchable = kb.searchable()
    broken = {t for t, p in kb.tables.items() if p.meta.status == "broken"}
    no_domain = {t for t, p in kb.tables.items() if not p.meta.domain}
    assert broken and no_domain and not (broken | no_domain) & searchable
    for t in broken:
        assert t not in {h.table for h in kb.search_tables(t.split(".")[1].replace("_", " "), k=10)}


def test_search_respects_domains_and_status(kb):
    hits = kb.search_tables("fynapse journal lines", domains=["recon"])
    assert all(h.domain == "recon" for h in hits)
    assert kb.search_tables("fynapse journal lines", domains=["*"])[0].table == "silver.fact_fynapse_slr_journals"
    assert kb.search_tables("fixed assets", domains=["ar"]) == []


def test_resolve_table_names(kb):
    for name in ("adra_account_facts", "silver.adra_account_facts", "lakehouse_mvpai.silver.adra_account_facts", "ADRA_ACCOUNT_FACTS"):
        assert kb.resolve_table(name).id == "silver.adra_account_facts"
    assert kb.resolve_table("silver.nope") is None


def test_glossary(kb):
    terms = [g.term for g in kb.glossary_lookup("How many Northwind accounts are pending closure and what is the total unidentified balance?")]
    assert "pending closure" in terms and "unreconciled difference" in terms
    rev = next(g for g in kb.glossary if g.term == "reversal")
    assert rev.status == "draft" and rev.tables == ["silver.fact_fynapse_slr_journals"]
    entries = parse_glossary("## x\nAliases: a, b\nStatus: draft\nText line.\n")
    assert entries[0].aliases == ["a", "b"] and entries[0].text == "Text line."


def test_similar_examples(kb):
    ex = kb.similar_examples("How many Cars USA Shipping accounts are pending closure in Oct 26?", k=3)
    assert ex and ex[0].id == "adra_pending_closure_count"
    assert all(e.tables == ["silver.fact_fynapse_slr_journals"] for e in kb.similar_examples("fynapse journals", domains=["subledger"]))


def test_index_md_is_in_sync(kb):
    assert (KNOWLEDGE_DIR / "INDEX.md").read_text(encoding="utf-8") == kb.index_markdown(), (
        "INDEX.md is stale: run python -m finchat_agents.knowledge.loader --write-index"
    )


def test_invalid_page_is_reported(tmp_path):
    (tmp_path / "tables").mkdir()
    (tmp_path / "tables" / "silver.bad.md").write_text(
        "---\nname: bad\nschema: silver\nlayer: silver\ndomain: nowhere\npurpose: p\ngrain: g\n"
        "primary_key: [MISSING]\n---\n# bad\n\n## Columns\n\n| Column | Type | Meaning | Also called | SQL expression |\n"
        "|---|---|---|---|---|\n| `A` | string | a |  | `A` |\n",
        encoding="utf-8",
    )
    with pytest.raises(KnowledgeError) as ei:
        Knowledge.load(tmp_path)
    text = "\n".join(ei.value.problems)
    assert "domain 'nowhere'" in text and "primary_key column 'MISSING'" in text


def test_superseded_copies_point_to_adra_and_are_not_searchable(kb):
    copies = {t: p for t, p in kb.tables.items() if p.meta.superseded_by}
    assert len(copies) == 11 and all(t.split(".")[1].startswith(("manage_close_", "vw_manage_close_task")) for t in copies)
    assert all(target.split(".")[1].startswith("adra_") for p in copies.values() for target in p.meta.superseded_by)
    assert not set(copies) & kb.searchable()
    for q in ("ADRA account reconciliation status", "unreconciled accounts", "close tasks by legal entity"):
        assert not {h.table for h in kb.search_tables(q, k=10)} & set(copies)
    # journal-entry tables are GL data, not ADRA copies
    assert "gold.manage_close_journal_entries" in kb.searchable()
