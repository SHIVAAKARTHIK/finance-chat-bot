"""Every Databricks call made for a question is recorded with its time and caller; cached lookups are marked."""
from __future__ import annotations

import pytest

from finchat_agents.knowledge.loader import Knowledge
from finchat_agents.storage.records import event_row
from finchat_agents.tools.run_sql import execute_guarded
from finchat_agents.tracing import MemorySink, Tracer
from finchat_agents.tracing.databricks import CACHE_EVENT, QUERY_EVENT, called_by, traced_question

from .fakes import FakeMcpServer, data_responder, make_deps
from .test_agents import ALL, COUNT_SQL, make_orch, route, writer
from finchat_agents.llm import fake
from finchat_agents.tools.catalog import column_values
from finchat_agents.tools.resolve import resolve_period


@pytest.fixture(scope="module")
def kb() -> Knowledge:
    return Knowledge.load()


def named(sink, name):
    return [e for e in sink.events if e.name == name]


async def test_a_query_is_recorded_with_time_caller_and_rows(kb):
    deps, server = make_deps(kb=kb)
    sink = MemorySink()
    with traced_question(Tracer([sink], message_id="m1")), called_by("sql_agent:run_sql"):
        await execute_guarded(COUNT_SQL, deps, ALL)
    event, = named(sink, QUERY_EVENT)
    assert event.agent == "sql_agent:run_sql" and event.status == "ok" and event.duration_ms is not None
    assert "COUNT(*)" in event.payload["input"] and event.payload["output"] == "1 rows via mcp"
    row = event_row(event, conversation_id="c", step_order=1)
    assert row["step_name"] == "databricks_query" and "sql_agent:run_sql" in row["input_payload"]


async def test_cached_lookups_are_marked_and_run_no_query(kb):
    deps, server = make_deps(kb=kb)
    sink = MemorySink()
    table = "lakehouse_mvpai.silver.adra_account_facts"
    with traced_question(Tracer([sink], message_id="m1")):
        await column_values(deps, ALL, table, "ACCOUNT_STATUS")
        await column_values(deps, ALL, table, "ACCOUNT_STATUS")
        await resolve_period(deps, ALL, "Feb 25", table)
        await resolve_period(deps, ALL, "Feb 25", table)
    assert len(named(sink, QUERY_EVENT)) == len(server.queries)  # one event per real query
    assert len(named(sink, CACHE_EVENT)) >= 2


async def test_outside_a_question_nothing_is_recorded(kb):
    deps, _ = make_deps(kb=kb)
    await execute_guarded(COUNT_SQL, deps, ALL)  # warm-up and the summary job: no tracer, no error


async def test_a_failed_query_is_recorded(kb):
    def broken(sql):
        raise RuntimeError("boom")

    deps, _ = make_deps(FakeMcpServer(broken), kb=kb)
    sink = MemorySink()
    with traced_question(Tracer([sink], message_id="m1")):
        with pytest.raises(Exception):
            await execute_guarded(COUNT_SQL, deps, ALL)
    event, = named(sink, QUERY_EVENT)
    assert event.status == "error" and event.payload["output"].startswith("failed via mcp")


async def test_a_whole_question_records_all_its_queries(kb):
    server = FakeMcpServer(data_responder)
    sql_script = [fake.tool_calls([route("simple_data", "How many reconciliations for Northwind in Feb 25?")]),
                  fake.tool_call("submit_sql", {"sql": COUNT_SQL, "explanation": "Counted."})]
    orch, _, _, server, sink = make_orch(kb, sql_script, [writer("The count is 97.")], server=server)
    env = await orch.answer("How many reconciliations for Northwind in Feb 25?", ALL)
    assert env.status == "answered"
    queries = named(sink, QUERY_EVENT)
    assert len(queries) == len(server.queries) >= 2  # the name / period lookups and the answer query
    callers = {e.agent for e in queries}
    assert "fast_path:run_sql" in callers and any(c.startswith("fast_path:resolve_") for c in callers)
