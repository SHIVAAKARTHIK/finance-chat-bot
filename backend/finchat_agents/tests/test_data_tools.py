"""Guardrails and data tools against the real knowledge pages and a fake MCP server."""
from __future__ import annotations

import datetime as dt
import json

import pytest

from finchat_agents.access import Role, UserAccess
from finchat_agents.knowledge.loader import Knowledge
from finchat_agents.llm import fake
from finchat_agents.llm.fake import FakeProvider
from finchat_agents.runtime.agent import Agent
from finchat_agents.runtime.tools import Budget, RunContext, ToolContext, ToolError
from finchat_agents.tools import build_data_tools, warm_up
from finchat_agents.tools.calculate import CalcError, evaluate
from finchat_agents.tools.run_sql import execute_guarded
from finchat_agents.tools.sql_guard import GuardError, guard_sql
from finchat_agents.tracing import MemorySink, Tracer

from .conftest import handle
from .fakes import L, S, FakeMcpServer, data_responder, make_deps

FACTS = "lakehouse_mvpai.silver.adra_account_facts"
ALL = UserAccess(user_id="u", role=Role(name="finance_all", domains=["*"]))
PII = UserAccess(user_id="p", role=Role(name="pii", domains=["*"], pii_allowed=True))
FA_ONLY = UserAccess(user_id="f", role=Role(name="fa_reader", domains=["fa"]))
NOBODY = UserAccess(user_id="n", role=None)


@pytest.fixture(scope="module")
def kb() -> Knowledge:
    return Knowledge.load()


def guard(kb, sql, access=ALL, limit=1000):
    return guard_sql(sql, kb, access, limit)


# ---------------------------------------------------------------- read-only and statement checks

@pytest.mark.parametrize("sql,message", [
    (f"DROP TABLE {FACTS}", "DROP"),
    (f"INSERT INTO {FACTS} SELECT * FROM {FACTS}", "INSERT"),
    (f"DELETE FROM {FACTS}", "DELETE"),
    (f"UPDATE {FACTS} SET BALANCE = '0'", "UPDATE"),
    (f"MERGE INTO {FACTS} t USING {FACTS} s ON t.ACCOUNT_KEY = s.ACCOUNT_KEY WHEN MATCHED THEN DELETE", "MERGE"),
    (f"CREATE TABLE lakehouse_mvpai.aiops.x AS SELECT * FROM {FACTS}", "CREATE"),
    (f"SELECT * INTO lakehouse_mvpai.aiops.x FROM {FACTS}", "INTO"),
    (f"SELECT COUNT(*) FROM {FACTS}; DROP TABLE {FACTS}", "exactly one"),
    (f"SELECT 1 FROM {FACTS}; SELECT 2 FROM {FACTS}", "exactly one"),
    ("SHOW TABLES IN lakehouse_mvpai.silver", "SELECT"),
    ("SELECT * FROM read_files('s3://bucket/x')", "Table functions"),
    ("SELEC broken", "SELECT"),
])
def test_write_and_multi_statements_refused(kb, sql, message):
    with pytest.raises(GuardError) as ei:
        guard(kb, sql)
    assert message.lower() in str(ei.value).lower()


def test_unknown_and_unqualified_tables(kb):
    with pytest.raises(GuardError, match="not in the catalog. Did you mean lakehouse_mvpai.silver.adra_account_facts"):
        guard(kb, "SELECT COUNT(*) FROM lakehouse_mvpai.silver.adra_account_fact")
    with pytest.raises(GuardError, match=f"Use the fully qualified name {FACTS}"):
        guard(kb, "SELECT COUNT(*) FROM adra_account_facts")
    with pytest.raises(GuardError, match="not in the catalog"):
        guard(kb, "SELECT * FROM lakehouse_mvpai.aiops.finance_chat_messages")
    with pytest.raises(GuardError, match="at least one catalog table"):
        guard(kb, "SELECT 1")
    ok = guard(kb, f"WITH c AS (SELECT ACCOUNT_KEY FROM {FACTS}) SELECT COUNT(*) FROM c")
    assert [p.id for p in ok.tables] == ["silver.adra_account_facts"]


def test_domain_access(kb):
    with pytest.raises(GuardError, match="Access denied.*adra_account_facts.*'recon'"):
        guard(kb, f"SELECT COUNT(*) FROM {FACTS}", FA_ONLY)
    assert guard(kb, "SELECT COUNT(*) FROM lakehouse_mvpai.silver.dim_fixed_assets", FA_ONLY)
    for nobody in (NOBODY, None):
        with pytest.raises(GuardError, match="no data access"):
            guard(kb, f"SELECT COUNT(*) FROM {FACTS}", nobody)


def test_limit_added_capped_or_kept(kb):
    g = guard(kb, f"SELECT ACCOUNT_KEY FROM {FACTS}", limit=1000)
    assert g.sql.endswith("LIMIT 1000") and g.limit_added
    assert guard(kb, f"SELECT ACCOUNT_KEY FROM {FACTS} LIMIT 5000").sql.endswith("LIMIT 1000")
    small = guard(kb, f"SELECT ACCOUNT_KEY FROM {FACTS} ORDER BY ACCOUNT_KEY LIMIT 5")
    assert small.sql.endswith("LIMIT 5") and not small.limit_added
    union = guard(kb, f"SELECT ACCOUNT_KEY FROM {FACTS} UNION ALL SELECT ACCOUNT_KEY FROM {FACTS}")
    assert union.sql.endswith("LIMIT 1000")


# ---------------------------------------------------------------- personal data

def test_pii_output_columns_masked(kb):
    assert guard(kb, f"SELECT PREPARER_NAME, ACCOUNT_KEY FROM {FACTS}").masked_columns == {"preparer_name"}
    assert guard(kb, f"SELECT f.APPROVED_BY_NAME AS who, f.APPROVED_DATE FROM {FACTS} f").masked_columns == {"who"}
    nested = guard(kb, f"SELECT x FROM (SELECT PREPARER_NAME AS x FROM {FACTS}) s")
    assert nested.masked_columns == {"x"}
    star = guard(kb, f"SELECT * FROM {FACTS}")
    assert {"preparer_name", "approver_name", "prepared_by_name", "approved_by_name"} <= star.masked_columns
    assert guard(kb, f"SELECT COUNT(*) AS n FROM {FACTS}").masked_columns == set()
    assert guard(kb, f"SELECT PREPARER_NAME FROM {FACTS}", PII).masked_columns == set()


@pytest.mark.parametrize("clause", [
    "WHERE PREPARER_NAME = 'Someone'",
    "GROUP BY APPROVER_NAME",
    "ORDER BY PREPARED_BY_NAME",
])
def test_pii_filter_group_sort_refused(kb, clause):
    sel = "APPROVER_NAME, COUNT(*)" if "GROUP" in clause else "ACCOUNT_KEY"
    with pytest.raises(GuardError, match="personal data"):
        guard(kb, f"SELECT {sel} FROM {FACTS} {clause}")
    guard(kb, f"SELECT {sel} FROM {FACTS} {clause}", PII)  # allowed with PII permission


def test_pii_window_refused(kb):
    with pytest.raises(GuardError, match="personal data"):
        guard(kb, f"SELECT COUNT(*) OVER (PARTITION BY PREPARER_NAME) AS n FROM {FACTS}")


# ---------------------------------------------------------------- execute_guarded / run_sql

async def test_execute_masks_rows_and_reports(kb):
    deps, server = make_deps(kb=kb)
    r = await execute_guarded(f"SELECT PREPARER_NAME AS who, ACCOUNT_KEY FROM {FACTS}", deps, ALL)
    assert r.rows == [["<masked>", "103300"]]
    assert any("masked" in n for n in r.notes)
    assert server.queries[0].endswith("LIMIT 1000")
    r2 = await execute_guarded(f"SELECT PREPARER_NAME AS who, ACCOUNT_KEY FROM {FACTS}", deps, PII)
    assert r2.rows == [["Real Person", "103300"]]


async def test_duplicate_hint_for_fixed_assets(kb):
    deps, _ = make_deps(kb=kb)
    r = await execute_guarded("SELECT COUNT(*) AS n FROM lakehouse_mvpai.silver.dim_fixed_asset_books", deps, ALL)
    assert any("duplicate loads" in n and "DATA_AREA_ID, FIXED_ASSET_NUMBER, BOOK_ID" in n for n in r.notes)
    r2 = await execute_guarded(f"SELECT COUNT(*) AS n FROM {FACTS}", deps, ALL)
    assert not any("duplicate" in n for n in r2.notes) and r2.rows == [[97]]


async def test_database_error_is_fixable(kb):
    deps, _ = make_deps(kb=kb)
    with pytest.raises(ToolError, match="Databricks rejected the query.*UNRESOLVED_COLUMN.*Fix the SQL"):
        await execute_guarded(f"SELECT error_me FROM {FACTS}", deps, ALL)


async def test_refused_queries_never_reach_databricks(kb):
    deps, server = make_deps(kb=kb)
    for sql in (f"DROP TABLE {FACTS}", f"SELECT COUNT(*) FROM {FACTS}"):
        with pytest.raises(ToolError):
            await execute_guarded(sql, deps, FA_ONLY if "COUNT" in sql else ALL)
    assert server.queries == []


async def test_empty_result_note(kb):
    deps, _ = make_deps(FakeMcpServer(lambda s: ([("n", L)], [])), kb=kb)
    r = await execute_guarded(f"SELECT ACCOUNT_KEY FROM {FACTS} WHERE ACCOUNT_STATUS = 'x'", deps, ALL)
    assert r.row_count == 0 and any("get_column_values" in n for n in r.notes)


async def test_run_sql_tool_in_agent_loop_counts_budget_and_limits_rows(kb, sink):
    rows = [[i] for i in range(120)]
    deps, server = make_deps(FakeMcpServer(lambda s: ([("n", L)], rows)), kb=kb)
    tools = build_data_tools(deps)
    p = FakeProvider([
        fake.tool_call("run_sql", {"sql": f"SELECT ACCOUNT_KEY FROM {FACTS}"}),
        fake.tool_call("run_sql", {"sql": f"SELECT ACCOUNT_KEY FROM {FACTS}"}),
        fake.text("done"),
    ])
    ctx = RunContext(tracer=Tracer([sink]), budget=Budget(max_sql_calls=1), user=ALL)
    r = await Agent("sql", "s", handle(p), [tools["run_sql"]]).run("q", ctx)
    first = json.loads(p.calls[1]["messages"][-1].content[0].content)
    assert first["result_id"] == "r1" and len(first["rows"]) == 50 and first["row_count"] == 120 and first["rows_shown"] == 50
    assert r.tool_calls[1].is_error and "SQL call budget" in r.tool_calls[1].output
    assert len(server.queries) == 1
    assert ctx.extras["sql_results"]["r1"].row_count == 120


def tctx(user=ALL, extras=None) -> ToolContext:
    run = RunContext(tracer=Tracer([MemorySink()]), user=user)
    if extras:
        run.extras.update(extras)
    return ToolContext(run=run, agent="t", step=1, call_id="c1")


async def test_tools_refuse_users_without_access(kb):
    deps, _ = make_deps(kb=kb)
    tools = build_data_tools(deps)
    for name, args in (("run_sql", {"sql": f"SELECT 1 FROM {FACTS}"}), ("search_tables", {"query": "x"})):
        with pytest.raises(ToolError, match="no data access"):
            await tools[name].handler(args, tctx(NOBODY))


# ---------------------------------------------------------------- catalog tools

async def test_search_and_describe_respect_domains(kb):
    deps, _ = make_deps(kb=kb)
    tools = build_data_tools(deps)
    out = await tools["search_tables"].handler({"query": "fixed asset books acquisition price"}, tctx(FA_ONLY))
    assert out["tables"][0]["fqn"] == "lakehouse_mvpai.silver.dim_fixed_asset_books"
    assert all(t["domain"] == "fa" for t in out["tables"])
    ar = await tools["search_tables"].handler({"query": "reconciliation status"}, tctx(UserAccess(user_id="a", role=Role(name="ar", domains=["ar"]))))
    assert all(t["domain"] == "ar" for t in ar["tables"])  # recon tables never shown to an AR-only role
    none = await tools["search_tables"].handler({"query": "fynapse"}, tctx(UserAccess(user_id="a", role=Role(name="ar", domains=["ar"]))))
    assert none["tables"] == []
    with pytest.raises(ToolError, match="Access denied"):
        await tools["describe_table"].handler({"table": "adra_account_facts"}, tctx(FA_ONLY))
    d = await tools["describe_table"].handler({"table": "adra_account_facts"}, tctx())
    assert d["table"] == FACTS and "PREPARER_NAME" in d["pii_columns"] and "## Columns" in d["page"]
    with pytest.raises(ToolError, match="not in the catalog"):
        await tools["describe_table"].handler({"table": "adra_acount_facts"}, tctx())


async def test_join_path_tool(kb):
    deps, _ = make_deps(kb=kb)
    tools = build_data_tools(deps)
    out = await tools["get_join_path"].handler({"from_table": "adra_account_facts", "to_table": "adra_period_dimensions"}, tctx())
    cond = out["joins"][0]["condition"]
    assert cond.count(" AND ") == 2 and "lakehouse_mvpai.silver.adra_account_facts.PERIOD_KEY" in cond
    none = await tools["get_join_path"].handler({"from_table": "fact_fynapse_slr_journals", "to_table": "adra_account_facts"}, tctx())
    assert none["joins"] == [] and "No approved join" in none["note"]


async def test_column_values_cached_and_pii_refused(kb):
    deps, server = make_deps(kb=kb)
    tools = build_data_tools(deps)
    args = {"table": "adra_account_facts", "column": "account_status"}
    out = await tools["get_column_values"].handler(args, tctx())
    assert out["column"] == "ACCOUNT_STATUS" and out["values"][0] == {"value": "Not prepared", "rows": 24}
    await tools["get_column_values"].handler(args, tctx())
    assert len(server.queries) == 1  # second call served from cache
    with pytest.raises(ToolError, match="personal data"):
        await tools["get_column_values"].handler({"table": "adra_account_facts", "column": "PREPARER_NAME"}, tctx(PII))
    with pytest.raises(ToolError, match="Did you mean ACCOUNT_STATUS"):
        await tools["get_column_values"].handler({"table": "adra_account_facts", "column": "ACOUNT_STATUS"}, tctx())
    with pytest.raises(ToolError, match="Access denied"):
        await tools["get_column_values"].handler(args, tctx(FA_ONLY))  # cache never bypasses access
    await tools["get_column_values"].handler({**args, "search": "app'roved; DROP"}, tctx())
    assert "'%approved drop%'" in server.queries[-1]  # quotes and semicolons stripped from the search text


async def test_glossary_tool(kb):
    deps, _ = make_deps(kb=kb)
    out = await build_data_tools(deps)["get_glossary"].handler({"term": "pending closure"}, tctx())
    assert out["entries"][0]["term"] == "pending closure"


# ---------------------------------------------------------------- resolve tools

@pytest.mark.parametrize("text", ["Feb 25", "February 2025", "2025-02", "feb 2025"])
async def test_resolve_period_adra_via_period_dimension(kb, text):
    deps, _ = make_deps(kb=kb)
    out = await build_data_tools(deps)["resolve_period"].handler({"text": text, "table": "adra_account_facts"}, tctx())
    assert out["period_table"] == "lakehouse_mvpai.silver.adra_period_dimensions"
    assert [m["label"] for m in out["matches"]] == ["Feb 25"]
    assert out["matches"][0]["filters"]["PERIOD_NAME"] == "Feb 25"


async def test_resolve_period_latest_fiscal_and_relative(kb):
    deps, server = make_deps(kb=kb, today=dt.date(2026, 11, 21))
    rp = build_data_tools(deps)["resolve_period"].handler
    latest = await rp({"text": "latest", "table": "adra_account_facts"}, tctx())
    assert [m["label"] for m in latest["matches"]] == ["Oct 26"]
    fy = await rp({"text": "FY2026 P9", "table": "fact_fynapse_slr_journals"}, tctx())
    assert fy["matches"][0]["filters"]["FISCAL_YEAR"] == "2026" and fy["matches"][0]["filters"]["PERIOD"] == "9"
    sep = await rp({"text": "Sep 26", "table": "fact_fynapse_slr_journals"}, tctx())
    assert sep["matches"][0]["label"] == "FY2026 P9"
    q = await rp({"text": "last quarter", "table": "fact_fynapse_slr_journals"}, tctx())
    assert sorted(m["label"] for m in q["matches"]) == ["FY2026 P8", "FY2026 P9"]  # Q3 2026
    missing = await rp({"text": "March 2023", "table": "adra_account_facts"}, tctx())
    assert missing["matches"] == [] and "No data" in missing["note"] and missing["available_latest_first"][0] == "Oct 26"
    assert len([q for q in server.queries if "adra_period_dimensions" in q]) == 1  # period rows cached


async def test_resolve_period_needs_period_columns(kb):
    deps, _ = make_deps(kb=kb)
    with pytest.raises(ToolError, match="no period columns"):
        await build_data_tools(deps)["resolve_period"].handler({"text": "Feb 25", "table": "adra_engagement_dimensions"}, tctx())


async def test_resolve_entity_fuzzy(kb):
    deps, _ = make_deps(kb=kb)
    re_ = build_data_tools(deps)["resolve_entity"].handler
    fy = await re_({"text": "UK3", "table": "fact_fynapse_slr_journals"}, tctx())
    assert fy["matches"][0] == {"column": "PARENT_ENTITY", "value": "UK03", "score": 1.0, "rows": 283}
    adra = await re_({"text": "561 - Cars USA Shipping, LLC", "table": "adra_account_facts"}, tctx())
    assert adra["entity_table"] == "lakehouse_mvpai.silver.adra_legal_entity_dimensions"
    top = {(m["column"], m["value"]) for m in adra["matches"][:2]}
    assert top == {("ENTITY_CODE", "561"), ("ENTITY_NAME", "Cars USA Shipping, LLC")}
    nw = await re_({"text": "northwind", "table": "adra_account_facts"}, tctx())
    assert nw["matches"][0]["value"] == "100-Northwind"
    none = await re_({"text": "UK99", "table": "fact_fynapse_slr_journals"}, tctx())
    assert none["matches"] == [] and "not found" in none["note"]


# ---------------------------------------------------------------- calculate

def test_calculate_expressions():
    rows = [{"BALANCE": 10.5, "n": 2}, {"BALANCE": 4.5, "n": 3}]
    assert evaluate("sum(r['BALANCE'] for r in r1)", {"r1": rows}) == 15.0
    assert evaluate("pct_change(207, 610)", {}) == pytest.approx(194.6859903382)
    assert evaluate("round(pct(6, 23), 1)", {}) == 26.1
    assert evaluate("[r['n'] * 2 for r in r1 if r['n'] > 2]", {"r1": rows}) == [6]
    assert evaluate("max(x) - min(x)", {"x": [3, 9, 4]}) == 6
    assert evaluate("1 / 0", {}) is None


@pytest.mark.parametrize("expr", [
    "__import__('os').system('dir')",
    "().__class__.__bases__",
    "open('secrets.txt')",
    "(lambda: 1)()",
    "2 ** 100000",
    "'a' * 10**8",
    "eval('1')",
    "x.real",
])
def test_calculate_refuses_unsafe(expr):
    with pytest.raises(CalcError):
        evaluate(expr, {"x": 1})


async def test_calculate_tool_reads_previous_results(kb):
    deps, _ = make_deps(kb=kb)
    tools = build_data_tools(deps)
    ctx = tctx()
    await tools["run_sql"].handler({"sql": f"SELECT COUNT(*) AS n FROM {FACTS}"}, ctx)
    out = await tools["calculate"].handler({"expression": "r1[0]['n'] * factor", "variables": {"factor": 2}}, ctx)
    assert out["result"] == 194
    with pytest.raises(ToolError, match="calculate"):
        await tools["calculate"].handler({"expression": "import os"}, ctx)


async def test_warm_up(kb):
    deps, server = make_deps(kb=kb)
    assert (await warm_up(deps))["mcp"] == "ok" and server.queries == ["SELECT 1 AS warm_up"]


def test_tool_set():
    deps, _ = make_deps()
    assert set(build_data_tools(deps)) == {
        "run_sql", "search_tables", "describe_table", "get_join_path", "get_column_values",
        "get_glossary", "resolve_period", "resolve_entity", "calculate",
    }
    assert build_data_tools(deps)["run_sql"].counts_as_sql


async def test_superseded_copy_is_refused_with_the_source(kb):
    with pytest.raises(GuardError, match="is a copy; the source of truth is lakehouse_mvpai.silver.adra_account_facts"):
        guard(kb, "SELECT COUNT(*) FROM lakehouse_mvpai.gold.manage_close_adra_reconciliation")
    deps, server = make_deps(kb=kb)
    with pytest.raises(ToolError, match="use the source of truth lakehouse_mvpai.silver.adra_account_facts"):
        await build_data_tools(deps)["describe_table"].handler({"table": "gold.manage_close_adra_reconciliation"}, tctx())
    assert server.queries == []


# ---------------------------------------------------------------- latency phase 2

async def test_prewarm_fills_the_caches_the_resolvers_use(kb):
    from finchat_agents.access.rbac import Role, UserAccess
    from finchat_agents.tools.resolve import prewarm_lookups, resolve_entity

    deps, server = make_deps(kb=kb)
    access = UserAccess(user_id="w", role=Role(name="all", domains=["*"]))
    done = await prewarm_lookups(deps, access)
    assert done["entities"] + done["periods"] > 0
    n = len(server.queries)
    page = next(p for p in kb.tables.values() if p.meta.entity_column)
    await resolve_entity(deps, access, "x", page.meta.fqn)
    assert len(server.queries) == n  # served from the cache, no new query


def test_route_and_sql_tool_schemas_are_short():
    from finchat_agents.agents.fast_path import SUBMIT_SQL
    from finchat_agents.agents.supervisor import ROUTE_SPEC

    assert ROUTE_SPEC.input_schema["required"] == ["classification"]
    assert "25 words" in SUBMIT_SQL.input_schema["properties"]["explanation"]["description"]


# ---------------------------------------------------------------- SQL connector option

class _ConnCur:
    def __init__(self, log):
        self.log, self.description = log, None

    def execute(self, sql, params=None):
        self.log.append(sql)
        if "boom" in sql:
            raise RuntimeError("[UNRESOLVED_COLUMN] cannot resolve x")
        self.description = [("account", "string"), ("total", "decimal")]

    def fetchall(self):
        import decimal
        return [("A1", decimal.Decimal("12.50")), ("A2", decimal.Decimal("7"))]

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class _Conn:
    def __init__(self, log):
        self.log = log

    def cursor(self):
        return _ConnCur(self.log)

    def close(self):
        pass


async def _connector(log):
    from finchat_agents.storage.aiops import DatabricksSqlExecutor
    from finchat_agents.tools.sql_connector_client import SqlConnectorClient

    async def token():
        return "tok"

    ex = DatabricksSqlExecutor("host", "/path", token, connect=lambda **kw: _Conn(log))
    return SqlConnectorClient(ex, timeout_s=5)


async def test_sql_connector_returns_typed_results_and_reuses_the_connection():
    log = []
    client = await _connector(log)
    res = await client.query("SELECT account, total FROM t")
    assert [c.name for c in res.columns] == ["account", "total"] and res.columns[1].type == "DECIMAL"
    assert str(res.rows[0][1]) == "12.50" and res.total_row_count == 2 and res.truncated is False
    assert await client.warm_up() is True and len(log) == 2


async def test_sql_connector_refuses_writes_and_reports_driver_errors_as_query_errors():
    import pytest
    from finchat_agents.tools.mcp_client import McpQueryError

    client = await _connector([])
    for bad in ("DELETE FROM t", "UPDATE t SET a=1", "DROP TABLE t", "", "  insert into t values (1)"):
        with pytest.raises(McpQueryError, match="read-only"):
            await client.query(bad)
    assert (await client.query("WITH x AS (SELECT 1) SELECT * FROM x")).rows
    with pytest.raises(McpQueryError, match="UNRESOLVED_COLUMN"):
        await client.query("SELECT boom")


def test_data_access_setting_selects_the_client(monkeypatch):
    from finchat_agents.config import Settings
    from finchat_agents.tools.deps import build_mcp_client
    from finchat_agents.tools.sql_connector_client import SqlConnectorClient

    base = dict(azure_tenant_id="t", azure_client_id="c", azure_client_secret="s", databricks_mcp_url="https://x/mcp",
                databricks_server_hostname="h", databricks_http_path="/p")
    assert type(build_mcp_client(Settings(_env_file=None, **base))).__name__ == "DatabricksMcpClient"
    assert isinstance(build_mcp_client(Settings(_env_file=None, data_access="sql_connector", **base)), SqlConnectorClient)
    import pytest
    with pytest.raises(RuntimeError, match="DATABRICKS_HTTP_PATH"):
        build_mcp_client(Settings(_env_file=None, data_access="sql_connector", azure_tenant_id="t", azure_client_id="c",
                                  azure_client_secret="s", databricks_server_hostname="h"))
