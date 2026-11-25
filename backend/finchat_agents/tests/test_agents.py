"""Agents and orchestrator with fake LLM providers and the fake MCP server."""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from finchat_agents.access import Role, UserAccess
from finchat_agents.agents.number_check import allowed_numbers, extract_numbers, unsupported_numbers
from finchat_agents.agents.orchestrator import ConversationContext, Orchestrator, Turn
from finchat_agents.config import PACKAGE_DIR
from finchat_agents.knowledge.loader import Knowledge
from finchat_agents.llm import fake
from finchat_agents.llm.fake import FakeProvider
from finchat_agents.llm.types import ModelHandle
from finchat_agents.tools.run_sql import SqlResult
from finchat_agents.tracing import MemorySink

from .fakes import L, S, FakeMcpServer, data_responder, make_deps

FACTS = "lakehouse_mvpai.silver.adra_account_facts"
COUNT_SQL = f"SELECT COUNT(*) AS n FROM {FACTS}"
ALL = UserAccess(user_id="u", role=Role(name="finance_all", domains=["*"]))


@pytest.fixture(scope="module")
def kb() -> Knowledge:
    return Knowledge.load()


def route(cls: str, q: str = "How many account reconciliations are there?", call_id: str = "route1"):
    return ("route", {"classification": cls, "standalone_question": q, "reason": "test"})


def writer(answer: str, how: str = "Counted all account reconciliations.", sugg=None):
    return fake.tool_call("submit_result", {"answer": answer, "how_calculated": how, "suggestions": sugg or ["By status?"]})


def make_orch(kb, sql_script, resp_script, server=None, **settings):
    deps, server = make_deps(server, kb=kb, **settings)
    sql_p, resp_p = FakeProvider(sql_script), FakeProvider(resp_script)
    sink = MemorySink()
    orch = Orchestrator(deps=deps, sql_llm=ModelHandle(sql_p, "claude-fake"), response_llm=ModelHandle(resp_p, "gptoss-fake"), sinks=[sink])
    return orch, sql_p, resp_p, server, sink


async def test_general_question_goes_to_knowledge_agent(kb):
    orch, sql_p, resp_p, server, sink = make_orch(
        kb, [fake.tool_calls([route("general", "What is IFRS 16?")])],
        [fake.text("General knowledge: IFRS 16 is the leases standard.")],
    )
    env = await orch.answer("What is IFRS 16?", ALL)
    assert env.status == "answered" and env.answer.startswith("General knowledge:")
    assert env.debug.mode == "general" and env.debug.llm_calls == 2 and server.queries == []
    assert "route" in [t for t in sql_p.calls[0]["tools"]]


async def test_fast_path_success_three_llm_calls(kb):
    orch, sql_p, resp_p, server, sink = make_orch(
        kb,
        [fake.tool_calls([route("simple_data")]),
         fake.tool_call("submit_sql", {"sql": COUNT_SQL, "explanation": "Counted all account reconciliations."})],
        [writer("There are 97 account reconciliations.")],
    )
    env = await orch.answer("How many account reconciliations are there?", ALL)
    assert env.status == "answered" and env.answer == "There are 97 account reconciliations."
    assert env.debug.mode == "fast" and env.debug.llm_calls == 3 and env.debug.sql_calls == 1
    assert env.how_calculated == "Counted all account reconciliations." and env.suggestions == ["By status?"]
    assert env.debug.sql == [COUNT_SQL + " LIMIT 1000"]
    prompt = sql_p.calls[1]["messages"][0].text
    assert "## Candidate tables" in prompt and "lakehouse_mvpai." in prompt and "## Approved joins" in prompt
    assert sql_p.calls[1]["tools"] == ["submit_sql"]
    facts = json.loads(resp_p.calls[0]["messages"][0].text.split("\n\n", 1)[1])
    assert facts["query_results"][0]["rows"] == [[97]]
    assert "debug" not in env.model_dump()  # traces only, never in the API payload
    events = [(e.type, e.agent) for e in sink.events]
    assert ("route", "supervisor") in events and events[-1] == ("answer", "orchestrator")
    assert sink.events[-1].payload["mode"] == "fast"


async def test_fast_path_failure_escalates_with_attempt(kb):
    bad = f"SELECT error_me FROM {FACTS}"
    orch, sql_p, resp_p, server, sink = make_orch(
        kb,
        [fake.tool_calls([route("simple_data")]),
         fake.tool_call("submit_sql", {"sql": bad, "explanation": "x"}),
         fake.tool_call("submit_sql", {"sql": "", "explanation": "", "cannot_answer": "column unknown"}),
         # supervisor ReAct loop (fresh), gets the attempt in its context
         fake.tool_call("submit_result", {"status": "partial", "answer": "The requested column does not exist.", "result_ids": []})],
        [writer("I could not answer this: the requested column does not exist.", how="")],
        server=FakeMcpServer(data_responder),
    )
    env = await orch.answer("How many account reconciliations are there?", ALL)
    assert env.debug.mode == "fast->react" and env.status == "partial"
    attempt = env.debug.fast_path
    assert attempt.sql_tried == [bad] and "UNRESOLVED_COLUMN" in attempt.errors[0] and attempt.reason == "column unknown"
    sup_msg = sql_p.calls[3]["messages"][0].text
    assert "A quick attempt already ran" in sup_msg and "error_me" in sup_msg
    # the repair call saw the error as a tool result
    repair = sql_p.calls[2]["messages"][-1].content[0]
    assert repair.is_error and "UNRESOLVED_COLUMN" in repair.content


async def test_complex_react_reuses_first_call_and_delegates(kb):
    sql_script = [
        fake.tool_calls([route("complex"), ("ask_catalog_agent", {"task": "find reconciliation tables"})]),
        fake.tool_call("submit_result", {"answer": "Use adra_account_facts.", "tables": [FACTS]}),        # catalog
        fake.tool_call("ask_sql_agent", {"task": "count reconciliations", "context": "table: " + FACTS}),  # supervisor
        fake.tool_call("run_sql", {"sql": COUNT_SQL}),                                                     # sql agent
        fake.tool_call("submit_result", {"answer": "97", "status": "ok", "result_ids": ["r1"], "explanation": "Counted rows."}),
        fake.tool_call("submit_result", {"status": "answered", "answer": "There are 97 reconciliations.",
                                         "how_calculated": "Counted rows.", "result_ids": ["r1"]}),
    ]
    orch, sql_p, resp_p, server, sink = make_orch(kb, sql_script, [writer("There are 97 account reconciliations.")])
    env = await orch.answer("Compare reconciliations and explain them", ALL)
    assert env.debug.mode == "react" and env.status == "answered"
    assert env.debug.llm_calls == 7  # 6 Claude calls (one classification, not repeated) + 1 writer
    assert len(sql_p.calls) == 6
    sql_agent_task = sql_p.calls[3]["messages"][0].text
    assert "count reconciliations" in sql_agent_task and "Similar verified examples" in sql_agent_task
    assert "<context>" in sql_agent_task and FACTS in sql_agent_task
    assert sql_p.calls[3]["tools"] == ["describe_table", "get_join_path", "get_column_values", "resolve_period",
                                       "resolve_entity", "run_sql", "calculate", "submit_result"]
    assert set(sql_p.calls[1]["tools"]) >= {"search_tables", "describe_table", "get_join_path", "get_column_values", "get_glossary"}


async def test_sql_agent_repairs_after_error(kb):
    from finchat_agents.runtime.tools import Budget, RunContext
    from finchat_agents.tracing import Tracer

    orch, sql_p, *_ = make_orch(kb, [
        fake.tool_call("run_sql", {"sql": f"SELECT error_me FROM {FACTS}"}),
        fake.tool_call("run_sql", {"sql": COUNT_SQL}),
        fake.tool_call("submit_result", {"answer": "97", "status": "ok", "result_ids": ["r1"], "explanation": "Counted rows."}),
    ], [])
    ctx = RunContext(tracer=Tracer([MemorySink()]), budget=Budget(), user=ALL)
    r = await orch.sql_agent.run("count reconciliations", ctx)
    assert r.data["result_ids"] == ["r1"] and r.data["status"] == "ok"
    first_result = sql_p.calls[1]["messages"][-1].content[0]
    assert first_result.is_error and "UNRESOLVED_COLUMN" in first_result.content and "Fix the SQL" in first_result.content
    assert ctx.counters.sql_calls == 2 and ctx.extras["sql_results"]["r1"].rows == [[97]]


async def test_partial_answer_on_budget(kb):
    loops = [fake.tool_call("ask_catalog_agent", {"task": "t"}), fake.tool_call("submit_result", {"answer": "x", "tables": []})]
    sql_script = [fake.tool_calls([route("complex"), ("ask_catalog_agent", {"task": "t"})]),
                  fake.tool_call("submit_result", {"answer": "x", "tables": []}),
                  *loops,
                  fake.text("Partial: I found the tables but could not run the query; the count is missing.")]
    orch, *_ = make_orch(kb, sql_script, [writer("I could not finish: the count is missing.")], agent_max_steps=2)
    env = await orch.answer("complex question", ALL)
    assert env.status == "partial" and "missing" in env.answer


async def test_number_check_rewrites_once(kb):
    orch, sql_p, resp_p, *_ = make_orch(
        kb,
        [fake.tool_calls([route("simple_data")]), fake.tool_call("submit_sql", {"sql": COUNT_SQL, "explanation": "Counted."})],
        [writer("There are 98 account reconciliations."), writer("There are 97 account reconciliations.")],
    )
    env = await orch.answer("How many account reconciliations are there?", ALL)
    assert env.answer == "There are 97 account reconciliations." and env.notices == []
    assert "98" in resp_p.calls[1]["messages"][0].text  # feedback named the bad number


async def test_number_check_caveat_after_failed_rewrite(kb):
    orch, *_ = make_orch(
        kb,
        [fake.tool_calls([route("simple_data")]), fake.tool_call("submit_sql", {"sql": COUNT_SQL, "explanation": "Counted."})],
        [writer("There are 98 reconciliations."), writer("There are about 120 reconciliations.")],
    )
    env = await orch.answer("How many account reconciliations are there?", ALL)
    assert env.debug.unsupported_numbers == ["120"]
    assert any("could not be checked" in n and "120" in n for n in env.notices)


async def test_user_without_access_is_declined_without_llm(kb):
    orch, sql_p, resp_p, server, _ = make_orch(kb, [], [])
    env = await orch.answer("How many reconciliations?", UserAccess(user_id="x", role=None))
    assert env.status == "declined" and env.debug.llm_calls == 0 and sql_p.calls == [] and server.queries == []


async def test_supervisor_decline(kb):
    orch, *_ = make_orch(
        kb,
        [fake.tool_calls([route("complex", "Delete account 103300")]),
         fake.tool_call("submit_result", {"status": "declined", "answer": "The assistant is read-only; it cannot delete data."})],
        [],
    )
    env = await orch.answer("Delete account 103300", ALL)
    assert env.status == "declined" and "read-only" in env.answer


async def test_conversation_context_is_passed(kb):
    orch, sql_p, *_ = make_orch(kb, [fake.tool_calls([route("general", "What does it mean?")])], [fake.text("General knowledge: ok")])
    conv = ConversationContext(turns=[Turn(question="What is IFRS 16?", answer="Leases standard.")])
    await orch.answer("And what about IFRS 9?", ALL, conv)
    assert "<conversation>" in sql_p.calls[0]["messages"][0].text and "IFRS 16" in sql_p.calls[0]["messages"][0].text


async def test_tables_only_for_more_than_three_rows(kb):
    rows = [[f"S{i}", i] for i in range(6)]
    server = FakeMcpServer(lambda sql: ([("ACCOUNT_STATUS", S), ("n", L)], rows) if "group by" in sql.lower() else data_responder(sql))
    sql = f"SELECT ACCOUNT_STATUS, COUNT(*) AS n FROM {FACTS} GROUP BY ACCOUNT_STATUS"
    orch, *_ = make_orch(
        kb,
        [fake.tool_calls([route("simple_data")]), fake.tool_call("submit_sql", {"sql": sql, "explanation": "By status."})],
        [writer("Six statuses; the largest has 5 accounts.")], server=server,
    )
    env = await orch.answer("How many accounts per status?", ALL)
    assert env.tables[0]["columns"] == ["ACCOUNT_STATUS", "n"] and len(env.tables[0]["rows"]) == 6


async def test_model_failure_gives_failed_envelope(kb):
    from finchat_agents.llm.types import LLMError

    orch, *_ = make_orch(kb, [LLMError("bad request", retryable=False)], [])
    env = await orch.answer("anything", ALL)
    assert env.status == "failed" and env.answer


# ---------------------------------------------------------------- number check

def test_extract_numbers():
    nums = [(n.text, float(n.value)) for n in extract_numbers("Total -455,376.16 and 1.98 million, 26.1% of 23; (500)")]
    assert nums == [("-455,376.16", -455376.16), ("1.98 million", 1980000.0), ("26.1%", 26.1), ("23", 23.0), ("(500)", -500.0)]


def test_allowed_numbers_rounding_and_sources():
    r = SqlResult(columns=["ACCOUNT_NUMBER", "BALANCE", "share_ratio"], rows=[["141111", 1981646.00, 0.261], ["103300", 5.5, 0.5]])
    allowed = allowed_numbers([r], [194], ["for 100-Northwind in Feb 25"])
    ok = "Balance 1,981,646 (1.98 million), 26.1% share, account 141111, total 1,981,651.5, 2 accounts, 194, Feb 25, entity 100"
    assert unsupported_numbers(ok, allowed) == []
    assert unsupported_numbers("Balance 1,981,700 and 3 accounts", allowed) == ["1,981,700", "3"]


# ---------------------------------------------------------------- no KPI code

def test_no_kpi_code_anywhere():
    roots = [PACKAGE_DIR / d for d in ("agents", "runtime", "tools", "llm", "knowledge", "access", "tracing", "eval")]
    generated = {"INDEX.md", "REVIEW.md", "joins_proposed.yaml"}  # real table names (e.g. *_kpi views) are data
    files = [p for r in roots for p in r.rglob("*") if p.suffix in (".py", ".md", ".yaml")
             and p.name not in generated and "tables" not in p.parts]
    hits = [str(p) for p in files if re.search(r"\bkpi", p.read_text(encoding="utf-8"), re.I)]
    assert files and hits == []
