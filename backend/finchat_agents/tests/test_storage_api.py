"""aiops storage (fake connector), ChatService and the /v3 router."""
from __future__ import annotations

import datetime as dt
import json
from types import SimpleNamespace

import httpx
import pytest
from fastapi import FastAPI

from finchat_agents.access import AccessConfig
from finchat_agents.agents.orchestrator import AnswerDebug, AnswerEnvelope
from finchat_agents.api.router import create_router
from finchat_agents.api.service import ChatService, Identity
from finchat_agents.knowledge.loader import Knowledge
from finchat_agents.llm import fake
from finchat_agents.storage.aiops import (
    AiopsStore,
    DatabricksSqlExecutor,
    StorageError,
    build_merge,
    check_target,
    ddl_statements,
    validate_row,
)
from finchat_agents.storage.records import answer_path_of, final_message_row, intent_of
from finchat_agents.storage.writer import BackgroundWriter

from .test_agents import COUNT_SQL, make_orch, route, writer

ACCESS = AccessConfig({
    "domains": {"recon": "ADRA", "subledger": "Fynapse", "fa": "FA"},
    "roles": {"finance_all": {"domains": ["*"]}},
    "group_roles": {"CFO": "finance_all"},
    "users": {"obj-cfo": "finance_all"},
})
NOW = dt.datetime(2026, 11, 21, 10, 0, tzinfo=dt.timezone.utc)


class FakeExecutor:
    def __init__(self, *, fail: bool = False, conversation: dict | None = None, turns: list[dict] | None = None):
        self.fail = fail
        self.statements: list[tuple[str, dict]] = []
        self.queries: list[tuple[str, dict]] = []
        self.conversation = conversation
        self.turns = turns or []

    async def execute(self, statements):
        if self.fail:
            raise RuntimeError("warehouse unavailable")
        self.statements += statements

    async def query(self, sql, params):
        self.queries.append((sql, params))
        if "finance_chat_conversations" in sql:
            return [self.conversation] if self.conversation else []
        return list(reversed(self.turns))  # newest first, like ORDER BY turn_index DESC

    def merges(self, table: str) -> list[tuple[str, dict]]:
        return [s for s in self.statements if f"MERGE INTO lakehouse_mvpai.aiops.{table} " in s[0]]


@pytest.fixture(scope="module")
def kb():
    return Knowledge.load()


# ---------------------------------------------------------------- MERGE building and guards

def test_merge_statement_shape():
    row = {"message_id": "m1", "conversation_id": "c1", "user_id": "u1", "turn_index": 1, "question_text": "q",
           "status": "answered", "visibility": "visible", "retry_count": 0, "llm_call_count": 3, "input_tokens": 10,
           "output_tokens": 5, "models_used": ["claude", "gpt-oss"], "kpi_ids": None, "created_at": NOW}
    sql, params = build_merge("lakehouse_mvpai", "aiops", "finance_chat_messages", [row])
    assert sql.startswith("MERGE INTO lakehouse_mvpai.aiops.finance_chat_messages AS tgt USING (SELECT CAST(:r0_message_id AS STRING) AS message_id")
    assert "ON tgt.message_id = src.message_id" in sql
    assert "CAST(:r0_turn_index AS INT) AS turn_index" in sql and "CAST(:r0_retry_count AS SMALLINT)" in sql
    assert "array(:r0_models_used_0, :r0_models_used_1) AS models_used" in sql
    assert "CAST(NULL AS ARRAY<STRING>) AS kpi_ids" in sql
    update = sql.split("WHEN MATCHED THEN UPDATE SET ")[1].split(" WHEN NOT MATCHED")[0]
    assert "tgt.status = src.status" in update and "created_at" not in update and "tgt.message_id" not in update
    assert "tgt.answer_text" not in update  # columns this write does not provide are left alone
    assert sql.endswith(")") and "WHEN NOT MATCHED THEN INSERT (message_id, conversation_id" in sql
    assert params["r0_message_id"] == "m1" and params["r0_models_used_1"] == "gpt-oss" and params["r0_created_at"] == NOW
    assert params["r0_answer_text"] is None


def test_merge_many_event_rows_and_conversation_insert_only_columns():
    rows = [{"event_id": f"e{i}", "message_id": "m", "conversation_id": "c", "step_name": "run_sql", "step_order": i,
             "attempt": 1, "status": "ok", "started_at": NOW, "created_at": NOW} for i in (1, 2, 3)]
    sql, params = build_merge("lakehouse_mvpai", "aiops", "finance_chat_message_events", rows)
    assert sql.count(" UNION ALL ") == 2 and params["r2_event_id"] == "e3"
    conv = {"conversation_id": "c", "user_id": "u", "title": "t", "visibility": "visible", "turn_count": 2,
            "summary_through_turn": 0, "created_at": NOW, "last_message_at": NOW}
    csql, _ = build_merge("lakehouse_mvpai", "aiops", "finance_chat_conversations", [conv])
    update = csql.split("UPDATE SET ")[1].split(" WHEN NOT MATCHED")[0]
    assert "turn_count" in update and "last_message_at" in update
    assert "title" not in update and "summary_through_turn" not in update and "created_at" not in update


@pytest.mark.parametrize("catalog,schema,table", [
    ("lakehouse_mvpai", "silver", "finance_chat_messages"),
    ("lakehouse_mvpai", "gold", "anything"),
    ("lakehouse_mvpai", "aiops", "other_table"),
    ("lakehouse_mvpai", "aiops", "finance_chat_x; DROP TABLE y"),
])
def test_writes_only_to_aiops_finance_chat(catalog, schema, table):
    with pytest.raises(StorageError):
        check_target(catalog, schema, table)
    with pytest.raises(StorageError):
        AiopsStore(FakeExecutor(), schema="silver")


def test_ddl_only_targets_aiops():
    stmts = ddl_statements()
    creates = [s for s in stmts if s.startswith("CREATE TABLE IF NOT EXISTS")]
    assert len(creates) == 5
    assert all("lakehouse_mvpai.aiops.finance_chat_" in s.split("(")[0] for s in stmts)
    assert not any(w in s for s in stmts for w in ("silver.", "gold."))


async def test_ensure_tables_skips_existing_constraints():
    class Ex(FakeExecutor):
        async def execute(self, statements):
            sql = statements[0][0]
            if sql.startswith("ALTER"):
                raise RuntimeError("CONSTRAINT_ALREADY_EXISTS: constraint already exists")
            self.statements += statements

    ex = Ex()
    await AiopsStore(ex).ensure_tables()
    assert len(ex.statements) == 5


def test_constraint_values():
    with pytest.raises(StorageError, match="check constraint"):
        validate_row("finance_chat_messages", {"status": "partial"})
    with pytest.raises(StorageError, match="check constraint"):
        validate_row("finance_chat_messages", {"answer_path": "general"})
    with pytest.raises(StorageError, match="unknown columns"):
        validate_row("finance_chat_messages", {"nope": 1})
    d = AnswerDebug(mode="fast", classification="simple_data", sql=["SELECT 1"], llm_calls=3, latency_ms=1500.4)
    env = AnswerEnvelope(conversation_id="c", message_id="m", status="partial", answer="a", how_calculated="h", debug=d)
    row = final_message_row(env, user_id="u", turn_index=2, question="q", created_at=NOW, completed_at=NOW)
    validate_row("finance_chat_messages", row)
    assert row["status"] == "answered" and row["error_code"] == "partial_answer" and row["answer_path"] == "adhoc"
    assert row["intent"] == "data" and row["sql_source"] == "generated" and row["kpi_ids"] is None and row["trust_label"] is None
    assert row["answer_text"] == "a\n\nHow this was calculated: h" and row["total_latency_ms"] == 1500
    general = AnswerDebug(mode="general", classification="general")
    assert intent_of(general) == "general" and answer_path_of("answered", general) is None
    assert answer_path_of("declined", general) == "declined" and answer_path_of("clarification", d) == "clarify"
    mixed = AnswerDebug(mode="react", classification="complex", sql=["s"], used_knowledge=True)
    assert intent_of(mixed) == "mixed"


async def test_databricks_executor_uses_fresh_token_and_params():
    calls = []

    class Cursor:
        description = [("n",)]

        def execute(self, sql, params):
            calls.append((sql, params))

        def fetchall(self):
            return [(97,)]

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    class Conn(Cursor):
        def cursor(self):
            return Cursor()

    tokens = iter(["tok1", "tok2"])
    seen = []

    def connect(**kw):
        seen.append(kw["access_token"])
        return Conn()

    async def token():
        return next(tokens)

    ex = DatabricksSqlExecutor("host", "/sql/1.0/warehouses/x", token, connect=connect)
    await ex.execute([("MERGE ...", {"a": 1})])
    assert await ex.query("SELECT 1", {}) == [{"n": 97}]
    assert seen == ["tok1", "tok2"] and calls[0] == ("MERGE ...", {"a": 1})


# ---------------------------------------------------------------- service

def fast_script():
    return ([fake.tool_calls([route("simple_data")]), fake.tool_call("submit_sql", {"sql": COUNT_SQL, "explanation": "Counted."})],
            [writer("There are 97 account reconciliations.")])


def make_service(kb, executor=None, sql_script=None, resp_script=None):
    s, r = fast_script()
    # these tests call /v3 directly with a user id in the request (the local-testing setting)
    orch, sql_p, resp_p, server, sink = make_orch(kb, sql_script or s, resp_script or r, allow_request_identity=True)
    store = AiopsStore(executor) if executor is not None else None
    return ChatService(orch, ACCESS, store=store, writer=BackgroundWriter() if store else None), sql_p


async def test_chat_writes_conversation_message_and_events(kb):
    ex = FakeExecutor()
    service, _ = make_service(kb, ex)
    env = await service.chat("How many account reconciliations are there?", Identity(user_id="obj-cfo"))
    assert env.status == "answered"
    await service.writer.flush()
    convs, msgs, events = ex.merges("finance_chat_conversations"), ex.merges("finance_chat_messages"), ex.merges("finance_chat_message_events")
    assert len(convs) == 2 and len(msgs) == 2 and len(events) == 1
    order = [s[0].split()[2].split(".")[-1] for s in ex.statements]
    assert order[:2] == ["finance_chat_conversations", "finance_chat_messages"]  # processing row first
    proc, final = msgs[0][1], msgs[1][1]
    assert proc["r0_status"] == "processing" and final["r0_status"] == "answered"
    assert final["r0_message_id"] == env.message_id and final["r0_turn_index"] == 1
    assert final["r0_answer_path"] == "adhoc" and final["r0_intent"] == "data" and final["r0_llm_call_count"] == 3
    assert final["r0_sql_text"] == COUNT_SQL + " LIMIT 1000" and final["r0_result_row_count"] == 1
    assert final["r0_domain"] == "recon" and final["r0_models_used_0"] == "claude-fake"
    ev_params = events[0][1]
    steps = [ev_params[k] for k in sorted(ev_params) if k.endswith("_step_name")]
    assert {"supervisor", "fast_path", "run_sql", "answer_writer"} <= set(steps)
    assert all(ev_params[k] == env.conversation_id for k in ev_params if k.endswith("_conversation_id"))
    assert "aws-bedrock" in [ev_params[k] for k in ev_params if k.endswith("_model_provider")]
    assert "load_context" in steps  # context loading is recorded as its own step
    assert convs[0][1]["r0_title"] == "How many account reconciliations are there?"


async def test_background_write_failure_does_not_fail_request(kb):
    service, _ = make_service(kb, FakeExecutor(fail=True))
    env = await service.chat("How many account reconciliations are there?", Identity(user_id="obj-cfo"))
    assert env.status == "answered" and "97" in env.answer
    await service.writer.flush()
    assert service.writer.failures and "warehouse unavailable" in service.writer.failures[0]


async def test_follow_up_loads_last_turns(kb):
    ex = FakeExecutor(conversation={"conversation_id": "c1", "user_id": "obj-cfo", "turn_count": 2, "summary": None},
                      turns=[{"turn_index": 1, "question_text": "q1", "standalone_question": "How many reconciliations?", "answer_start": "97."},
                             {"turn_index": 2, "question_text": "q2", "standalone_question": None, "answer_start": "Approved 7."}])
    service, sql_p = make_service(kb, ex)
    env = await service.chat("How many account reconciliations are there?", Identity(user_id="obj-cfo"), conversation_id="c1")
    assert env.conversation_id == "c1"
    first = sql_p.calls[0]["messages"][0].text
    assert "<conversation>" in first and first.index("How many reconciliations?") < first.index("q2")
    await service.writer.flush()
    assert ex.merges("finance_chat_messages")[-1][1]["r0_turn_index"] == 3
    turns_sql, turns_params = next(q for q in ex.queries if "finance_chat_messages" in q[0])
    assert "visibility = 'visible'" in turns_sql and "LIMIT 5" in turns_sql
    assert "user_id = :uid" in turns_sql and turns_params["uid"] == "obj-cfo"  # only this user's turns are read


async def test_other_users_conversation_is_not_continued(kb):
    ex = FakeExecutor(conversation={"conversation_id": "c1", "user_id": "someone-else", "turn_count": 4})
    service, sql_p = make_service(kb, ex)
    env = await service.chat("How many account reconciliations are there?", Identity(user_id="obj-cfo"), conversation_id="c1")
    assert env.conversation_id != "c1" and "<conversation>" not in sql_p.calls[0]["messages"][0].text


async def test_unknown_user_is_declined(kb):
    service, sql_p = make_service(kb, FakeExecutor())
    env = await service.chat("How many?", Identity(user_id="stranger", groups=["Unknown group"]))
    assert env.status == "declined" and sql_p.calls == []


# ---------------------------------------------------------------- API

def app_for(service: ChatService) -> FastAPI:
    app = FastAPI()
    app.include_router(create_router(service), prefix="/v3")
    return app


async def test_post_chat_returns_spec_envelope(kb):
    service, _ = make_service(kb, FakeExecutor())
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app_for(service)), base_url="http://t") as client:
        r = await client.post("/v3/chat", json={"message": "How many account reconciliations are there?", "user_id": "obj-cfo"})
        assert r.status_code == 200
        body = r.json()
        assert set(body) == {"conversation_id", "message_id", "status", "answer", "how_calculated", "tables", "files",
                             "suggestions", "notices", "options", "answer_context"}
        assert body["status"] == "answered" and "97" in body["answer"] and "SELECT" not in json.dumps(body)
        assert (await client.post("/v3/chat", json={"message": "hi"})).status_code == 401
        assert (await client.post("/v3/chat", json={"message": "", "user_id": "obj-cfo"})).status_code == 422
        assert (await client.get("/v3/health")).json()["storage"] == "enabled"


async def test_stream_emits_steps_then_final(kb):
    service, _ = make_service(kb, None)
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app_for(service)), base_url="http://t") as client:
        r = await client.post("/v3/chat/stream", json={"message": "How many account reconciliations are there?",
                                                       "user_id": "x", "groups": ["CFO"]})
    assert r.headers["content-type"].startswith("text/event-stream")
    events = [(b.split("\n")[0][7:], json.loads(b.split("\n")[1][6:])) for b in r.text.strip().split("\n\n")]
    kinds = [e for e, _ in events]
    assert kinds[-1] == "final" and kinds.count("final") == 1 and "step" in kinds
    steps = [d for e, d in events if e == "step"]
    assert any(s.get("tool") == "run_sql" for s in steps) and any(s["type"] == "route" for s in steps)
    assert not any("input" in s or "output" in s for s in steps)  # no payloads or SQL in the stream
    assert events[-1][1]["status"] == "answered" and "debug" not in events[-1][1]


async def test_identity_dependency_wins_over_body(kb):
    service, _ = make_service(kb, None)

    async def entra_identity():
        return Identity(user_id="obj-cfo")

    app = FastAPI()
    app.include_router(create_router(service, identity=entra_identity), prefix="/v3")
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://t") as client:
        r = await client.post("/v3/chat", json={"message": "How many account reconciliations are there?", "user_id": "stranger"})
    assert r.json()["status"] == "answered"


# ---------------------------------------------------------------- latency phase 1: pooled connections, parallel reads

class PoolConn:
    def __init__(self, log, fail_next=False):
        self.log, self.fail_next, self.closed = log, fail_next, False

    def cursor(self):
        conn = self

        class Cur:
            description = [("n",)]

            def execute(self, sql, params):
                if conn.fail_next:
                    conn.fail_next = False
                    raise RuntimeError("connection reset")
                conn.log.append(sql)

            def fetchall(self):
                return [(1,)]

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

        return Cur()

    def close(self):
        self.closed = True


async def test_executor_reuses_one_connection_until_the_token_changes():
    opened, log = [], []

    def connect(**kw):
        conn = PoolConn(log)
        opened.append((kw["access_token"], conn))
        return conn

    token = {"v": "tok1"}

    async def get_token():
        return token["v"]

    ex = DatabricksSqlExecutor("host", "/path", get_token, connect=connect)
    for _ in range(3):
        assert await ex.query("SELECT 1", {}) == [{"n": 1}]
    await ex.execute([("MERGE x", {})])
    assert len(opened) == 1 and log == ["SELECT 1"] * 3 + ["MERGE x"]  # one connection for four statements
    token["v"] = "tok2"  # the token provider refreshed the token
    await ex.query("SELECT 1", {})
    assert [t for t, _ in opened] == ["tok1", "tok2"] and opened[0][1].closed  # old connection closed, new one opened
    await ex.aclose()
    assert opened[1][1].closed


async def test_executor_reopens_old_connections_and_retries_a_stale_one_once():
    opened = []
    now = {"t": 0.0}

    def connect(**kw):
        conn = PoolConn([])
        opened.append(conn)
        return conn

    async def get_token():
        return "tok"

    ex = DatabricksSqlExecutor("host", "/path", get_token, connect=connect, max_age_s=100, clock=lambda: now["t"])
    await ex.query("SELECT 1", {})
    now["t"] = 150  # older than max_age_s: reopened
    await ex.query("SELECT 1", {})
    assert len(opened) == 2 and opened[0].closed
    opened[1].fail_next = True  # the pooled connection dropped: closed and retried once on a fresh connection
    assert await ex.query("SELECT 1", {}) == [{"n": 1}]
    assert len(opened) == 3 and opened[1].closed


async def test_executor_does_not_retry_a_failure_on_a_brand_new_connection():
    opened = []

    def connect(**kw):
        conn = PoolConn([], fail_next=True)
        opened.append(conn)
        return conn

    async def get_token():
        return "tok"

    ex = DatabricksSqlExecutor("host", "/path", get_token, connect=connect)
    with pytest.raises(RuntimeError, match="connection reset"):
        await ex.query("SELECT 1", {})
    assert len(opened) == 1 and opened[0].closed  # a real error is raised, not retried endlessly


async def test_context_reads_run_together_and_user_memory_is_cached(kb):
    ex = FakeExecutor(conversation={"conversation_id": "c1", "user_id": "obj-cfo", "turn_count": 1, "summary": None},
                      turns=[{"turn_index": 1, "question_text": "q1", "standalone_question": None, "answer_start": "a1"}])
    s, r = fast_script()
    service, _ = make_service(kb, ex, sql_script=s + s, resp_script=r + r)
    env = await service.chat("How many account reconciliations are there?", Identity(user_id="obj-cfo"), conversation_id="c1")
    assert env.debug.context_ms >= 0
    memory_reads = [q for q in ex.queries if "finance_chat_user_memory" in q[0]]
    assert len(memory_reads) == 1
    await service.chat("How many account reconciliations are there?", Identity(user_id="obj-cfo"), conversation_id="c1")
    assert len([q for q in ex.queries if "finance_chat_user_memory" in q[0]]) == 1  # cached for 10 minutes
    await service.writer.flush()
    final = ex.merges("finance_chat_messages")[-1][1]
    assert final["r0_total_latency_ms"] >= 0  # agent time plus context loading
