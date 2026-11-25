"""Backend integration: the UI's existing finance-chat URLs and SSE contract served by v3 (fake models and MCP)."""
from __future__ import annotations

import asyncio
import datetime as dt
import json

import httpx
import pytest
from fastapi import FastAPI, HTTPException, Request

from finchat_agents.agents.orchestrator import AnswerDebug, AnswerEnvelope
from finchat_agents.api.service import ChatService
from finchat_agents.integration import UiChatRequest, chunk_text, create_backend_router, install_backend, to_ui_body
from finchat_agents.integration.backend import history_body, question_text
from finchat_agents.integration.stream import stage_of
from finchat_agents.llm import fake
from finchat_agents.storage.aiops import AiopsStore
from finchat_agents.tracing.events import TraceEvent

from .test_storage_api import ACCESS, FakeExecutor, fast_script, kb, make_service  # noqa: F401 (kb fixture)
from .test_agents import make_orch

QUESTION = "How many account reconciliations are there?"
URL = "/api/invoke/finance-chat"
CFO_USER = {"oid": "obj-cfo", "sub": "sub-x", "name": "Test User", "groups": ["g-1"]}


def roles_of(user: dict) -> list[str]:  # stands in for the backend's agent_roles(user)
    return {"g-1": ["CFO"]}.get((user.get("groups") or [""])[0], [])


def backend_app(service: ChatService, *, user: dict | None = CFO_USER, rate_limit=None) -> FastAPI:
    async def get_current_user(request: Request) -> dict:
        if user is None:
            raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")
        return dict(user)

    app = FastAPI()
    app.include_router(create_backend_router(service, get_current_user=get_current_user, agent_roles=roles_of,
                                             rate_limit=rate_limit), prefix="/api/invoke")
    return app


def client_for(app: FastAPI) -> httpx.AsyncClient:
    return httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://t")


def parse_sse(text: str) -> list[tuple[str, dict]]:
    out = []
    for block in text.strip().split("\n\n"):
        lines = block.split("\n")
        out.append((lines[0].removeprefix("event: "), json.loads(lines[1].removeprefix("data: "))))
    return out


# ---------------------------------------------------------------- stream contract (mirrors the backend's own test)

async def test_stream_returns_status_deltas_and_complete_in_the_ui_format(kb):
    ex = FakeExecutor()
    service, _ = make_service(kb, ex)
    async with client_for(backend_app(service)) as c:
        r = await c.post(f"{URL}/stream", json={"query": QUESTION, "session_id": "s-1"})
    assert r.status_code == 200 and r.headers["content-type"].startswith("text/event-stream")
    assert r.headers["x-accel-buffering"] == "no" and r.headers["cache-control"] == "no-cache"
    for name in ("event: status", "event: delta", "event: complete"):
        assert name in r.text
    events = parse_sse(r.text)
    assert events[0] == ("status", {"stage": "processing"})
    assert [e for e, _ in events][-1] == "complete" and [e for e, _ in events].count("complete") == 1
    stages = [d["stage"] for e, d in events if e == "status"]
    assert {"intent", "database", "results", "answer"} <= set(stages)
    assert set(stages) <= {"processing", "domain", "exploration", "intent", "sql", "validation", "database", "results",
                           "answer", "clarification"}
    body = events[-1][1]
    deltas = "".join(d["text"] for e, d in events if e == "delta")
    assert deltas == body["answer"] == body["message"] and "97" in deltas
    assert body["status"] == "success" and body["session_id"] == "s-1" and body["user_id"] == "obj-cfo"
    assert body["user_question"] == QUESTION and body["role"] == "assistant"
    assert json.loads(body["breakdown"]) == [] and isinstance(json.loads(body["follow_up_questions"]), list)
    assert body["explanation"]["kpi"] is None  # never any KPI data
    assert "SELECT" not in r.text and "sql" not in (body["source"] or {})  # never SQL to the UI
    await service.writer.flush()
    msgs = ex.merges("finance_chat_messages")
    assert msgs and msgs[-1][1]["r0_user_id"] == "obj-cfo"  # identity from the validated token, not the body


async def test_non_stream_route_returns_the_same_body(kb):
    service, _ = make_service(kb, None)
    async with client_for(backend_app(service)) as c:
        r = await c.post(URL, json={"query": QUESTION, "user_id": "attacker", "roles": ["admin"]})
        body = r.json()
        assert r.status_code == 200 and body["status"] == "success" and body["user_id"] == "obj-cfo"
        assert body["timing"]["total_ms"] is not None and body["trace_id"]
        assert (await c.post(URL, json={"query": ""})).status_code == 422
        assert (await c.post(URL, json={"query": "x" * 4001})).status_code == 422
        assert (await c.post(URL, json={"query": "q", "session_id": "s" * 129})).status_code == 422


async def test_auth_failure_and_unknown_role(kb):
    service, _ = make_service(kb, None)
    async with client_for(backend_app(service, user=None)) as c:
        assert (await c.post(f"{URL}/stream", json={"query": QUESTION})).status_code == 401
    async with client_for(backend_app(service, user={"sub": "nobody", "groups": ["g-unknown"]})) as c:
        body = (await c.post(URL, json={"query": QUESTION})).json()
    assert body["status"] == "declined" and body["user_id"] == "nobody"
    async with client_for(backend_app(service, user={"name": "no id"})) as c:
        assert (await c.post(URL, json={"query": QUESTION})).status_code == 401


async def test_stream_error_is_generic_and_ends_the_stream(kb):
    service, _ = make_service(kb, None)

    async def boom(*_a, **_k):
        raise RuntimeError("connect https://adb-1.azuredatabricks.net token=abc failed")
    service.chat = boom
    async with client_for(backend_app(service)) as c:
        r = await c.post(f"{URL}/stream", json={"query": QUESTION})
    events = parse_sse(r.text)
    assert events[-1][0] == "error" and events[-1][1]["status_code"] == 500
    assert "adb-1" not in r.text and "token" not in r.text and "complete" not in [e for e, _ in events]


async def test_heartbeat_resends_the_current_stage_while_waiting(kb):
    service, _ = make_service(kb, None)
    from finchat_agents.integration.stream import stream_chat

    async def slow_chat(question, identity, *, conversation_id=None, extra_sinks=None):
        await asyncio.sleep(0.9)
        return AnswerEnvelope(conversation_id="c1", message_id="m1", answer="Done.")
    service.chat = slow_chat
    from finchat_agents.api.service import Identity
    chunks = [c async for c in stream_chat(service, query="q", identity=Identity(user_id="u"), conversation_id=None,
                                           session_id=None, heartbeat_s=0.3)]
    events = parse_sse("".join(chunks))
    assert [d["stage"] for e, d in events if e == "status"].count("processing") >= 3  # start + heartbeats
    assert events[-1][0] == "complete"


async def test_rate_limit_decorator_is_applied_to_every_route(kb):
    service, _ = make_service(kb, None)
    wrapped = []

    def rate_limit(fn):
        wrapped.append(fn.__name__)
        return fn
    backend_app(service, rate_limit=rate_limit)
    assert sorted(wrapped) == ["chat", "chat_stream", "clear_context", "history"]


# ---------------------------------------------------------------- response mapping

def test_ui_body_mapping_tables_files_status_and_no_kpi():
    env = AnswerEnvelope(
        conversation_id="c1", message_id="m1", status="partial", answer="Top accounts below.",
        how_calculated="- Summed balances\n- Grouped by account", suggestions=["Show by entity"], notices=["Duplicate rows"],
        tables=[{"title": "Details", "columns": ["ACCOUNT_NAME", "balance"], "rows": [["Cash", "10.5"], ["AR", None]]}],
        files=[{"name": "report.xlsx", "path": "/v3/files/c1/report.xlsx"}],
        debug=AnswerDebug(tables_used=["lakehouse_mvpai.silver.adra_account_facts"], domains=["recon"], result_row_count=40,
                          filters={"ENTITY": ["100"]}, standalone_question="Top accounts?"))
    b = to_ui_body(env, query="top?", user_id="u", session_id=None, total_ms=1234.0,
                   domain_labels={"recon": "ADRA account reconciliation"})
    assert b["status"] == "success" and b["verification"] == "unverified"
    assert b["answer"] == ("Top accounts below.\n\nNote: Duplicate rows\n\n"
                           "Files: [report.xlsx](/v3/files/c1/report.xlsx)")  # the UI hides explanation without a KPI
    t = b["table"]
    assert t["columns"] == [{"key": "ACCOUNT_NAME", "label": "Account name", "numeric": False},
                            {"key": "balance", "label": "Balance", "numeric": True}]
    assert t["rows"] == [{"ACCOUNT_NAME": "Cash", "balance": "10.5"}, {"ACCOUNT_NAME": "AR", "balance": ""}]
    assert all(isinstance(v, str) for row in t["rows"] for v in row.values())  # UI type: Record<string, string>[]
    assert t["total_rows"] == 40 and t["truncated"] is True
    assert b["source"] == {"tables": ["ADRA account reconciliation"], "row_count": 40, "truncated": True,
                           "description": None, "period": None}
    assert b["source_label"] == "ADRA account reconciliation" and b["resolved_question"] == "Top accounts?"
    assert "adra_account_facts" not in json.dumps(b) and "lakehouse_mvpai" not in json.dumps(b)  # users never see table names
    ex = b["explanation"]
    assert ex["kpi"] is None and ex["calculation_steps"] == ["Summed balances", "Grouped by account"]
    assert ex["filters"] == [] and ex["caveats"] == ["Duplicate rows"]  # column names are technical: not shown
    assert b["timing"]["total_ms"] == 1234 and b["timing"]["total_seconds"] == 1.234
    for status, ui in (("answered", "success"), ("clarification", "clarification"), ("declined", "declined"), ("failed", "error")):
        out = to_ui_body(AnswerEnvelope(status=status, answer="Which entity?"), query="q", user_id="u", session_id="s")
        assert out["status"] == ui and out["table"] is None and out["source"] is None
        assert out["clarification_question"] == ("Which entity?" if status == "clarification" else None)


def test_chunk_text_round_trips_and_respects_size():
    text = "Net revenue for Q3 FY2026 is in the breakdown below. " * 5 + "Averyveryverylongtokenwithoutanyspaces" * 3
    pieces = chunk_text(text, 64)
    assert "".join(pieces) == text and all(len(p) <= 64 for p in pieces)
    assert chunk_text("") == [] and chunk_text("short") == ["short"]


def test_clarifications_are_appended_as_text():
    assert question_text(UiChatRequest(query="Revenue?")) == "Revenue?"
    assert question_text(UiChatRequest(query="Revenue?", clarifications={"entity": "Cars USA"})) == \
        "Revenue?\n(Clarification: entity: Cars USA)"
    assert question_text(UiChatRequest(query="Q", clarifications=[{"question": "Which?", "answer": "Oct 26"}, "UK"])) == \
        "Q\n(Clarification: Which? Oct 26; UK)"


def test_stage_mapping():
    def ev(**kw):
        return TraceEvent(run_id="r", agent=kw.pop("agent", "x"), **kw)
    assert stage_of(ev(type="route")) == "intent"
    assert stage_of(ev(type="agent_start", agent="catalog_agent")) == "exploration"
    assert stage_of(ev(type="agent_start", agent="fast_path")) == "sql"
    assert stage_of(ev(type="agent_start", agent="answer_writer")) == "answer"
    assert stage_of(ev(type="tool_call", name="run_sql")) == "results"
    assert stage_of(ev(type="tool_call", name="run_sql", status="error")) == "database"
    assert stage_of(ev(type="tool_call", name="get_column_values")) == "exploration"
    assert stage_of(ev(type="llm_call")) is None


# ---------------------------------------------------------------- history

class HistoryExecutor(FakeExecutor):
    def __init__(self, rows):
        super().__init__()
        self.rows = rows

    async def query(self, sql, params):
        self.queries.append((sql, params))
        return self.rows if "WHERE user_id = :uid" in sql else []


ROWS = [
    {"message_id": "m3", "conversation_id": "c2", "turn_index": 1, "question_text": "Q3", "answer_text": "A3",
     "status": "answered", "created_at": dt.datetime(2026, 11, 21, 10, 0)},
    {"message_id": "m2", "conversation_id": "c1", "turn_index": 2, "question_text": "Q2", "answer_text": "A2",
     "status": "clarification", "created_at": dt.datetime(2026, 11, 20, 9, 0)},
    {"message_id": "m1", "conversation_id": "c1", "turn_index": 1, "question_text": "Q1", "answer_text": "A1",
     "status": "partial", "created_at": dt.datetime(2026, 11, 20, 8, 0)},
]


async def test_history_is_the_ui_wire_array_scoped_to_the_caller(kb):
    ex = HistoryExecutor(ROWS)
    service, _ = make_service(kb, ex)
    async with client_for(backend_app(service)) as c:
        flat = (await c.get(f"{URL}/history", params={"limit": 5})).json()
        threaded = (await c.get(f"{URL}/history", params={"limit": 1, "threads": "true"})).json()
        assert (await c.get(f"{URL}/history", params={"limit": 0})).status_code == 422
    sql, params = ex.queries[0]
    assert params == {"uid": "obj-cfo"} and "lakehouse_mvpai.aiops.finance_chat_messages" in sql
    assert isinstance(flat, list) and [i["user_question"] for i in flat] == ["Q3", "Q2", "Q1"]  # newest first
    first = flat[0]
    assert set(first) == {"conversation_id", "message_time", "user_question", "answer", "source_used", "resolved_question",
                          "generated_sql", "category", "citation", "data_row_count", "status"}
    assert first["message_time"] == "2026-11-21T10:00:00" and first["status"] == "answered" and first["answer"] == "A3"
    assert first["generated_sql"] is None and "explanation" not in first  # never SQL, never KPI
    assert flat[1]["status"] == "clarification" and flat[2]["status"] == "answered"  # partial -> answered
    assert {i["conversation_id"] for i in threaded} == {"c2"}  # threads=true & limit=1: the newest conversation only


def test_history_without_rows():
    assert history_body([]) == []


def test_shared_databricks_schema_env_is_ignored(monkeypatch):
    """The backend's .env has DATABRICKS_SCHEMA=silver; v3 must still write only to aiops."""
    from finchat_agents.config import Settings
    from finchat_agents.storage.aiops import build_store

    monkeypatch.setenv("DATABRICKS_SCHEMA", "silver")
    s = Settings(_env_file=None, databricks_server_hostname="h", databricks_http_path="/p", azure_tenant_id="t",
                 azure_client_id="c", azure_client_secret="x")
    store = build_store(s)
    assert store is not None and store.schema == "aiops"
    assert store.fqn("finance_chat_messages") == "lakehouse_mvpai.aiops.finance_chat_messages"


async def test_routes_work_behind_a_rate_limiter_that_wraps_them_like_slowapi(kb):
    """Regression: with FastAPI 0.115 a wrapper from another module (slowapi) made FastAPI read `body` and `request` as missing
    query parameters (HTTP 422 "Field required") when this module used string annotations."""
    from ._ratelimit_wrapper import wrapping_limit

    service, _ = make_service(kb, None)
    async with client_for(backend_app(service, rate_limit=wrapping_limit)) as c:
        r = await c.post(URL, json={"query": QUESTION, "session_id": "s-1", "conversation_id": None, "clarifications": {}})
        assert r.status_code == 200 and r.json()["status"] == "success"
        s = await c.post(f"{URL}/stream", json={"query": QUESTION, "session_id": "s-1"})
        assert s.status_code == 200 and "event: complete" in s.text
        h = await c.get(f"{URL}/history", params={"limit": 5, "threads": "true"})
        assert h.status_code == 200 and h.json() == []
