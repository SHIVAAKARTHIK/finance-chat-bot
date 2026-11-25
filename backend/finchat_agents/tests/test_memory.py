"""Task 07: rolling summaries, follow-up rewriting, the optional question-limit rollover, user-memory hints.
Token-based context, topics and clear context are in test_conversation_context.py."""
from __future__ import annotations

import json

import pytest

from finchat_agents.api.service import ChatService, Identity, limit_reached_notice, rollover_notice
from finchat_agents.knowledge.loader import Knowledge
from finchat_agents.llm import fake
from finchat_agents.llm.fake import FakeProvider
from finchat_agents.llm.types import ModelHandle
from finchat_agents.memory.filters import extract_filters
from finchat_agents.memory.summary import ConversationSummarizer, TurnRecord, context_tokens, fallback_seed, needs_summary
from finchat_agents.memory.user_memory import UserMemory, assumed_entity_notice, build_memory, memory_hint
from finchat_agents.storage.aiops import AiopsStore, build_summary_update
from finchat_agents.storage.writer import BackgroundWriter

from .test_agents import COUNT_SQL, make_orch, route, writer
from .test_storage_api import ACCESS

NORTHWIND_SQL = next(e.sql for e in Knowledge.load().examples if e.id == "adra_pending_closure_count")


@pytest.fixture(scope="module")
def kb() -> Knowledge:
    return Knowledge.load()


class MemExecutor:
    """Fake connector: canned conversation, turns, user memory and plans; records statements."""

    def __init__(self, *, conversation=None, turns=None, memory=None, plans=None):
        self.conversation, self.turns, self.memory, self.plans = conversation, turns or [], memory, plans or []
        self.statements: list[tuple[str, dict]] = []
        self.queries: list[str] = []

    async def execute(self, statements):
        self.statements += statements

    async def query(self, sql, params):
        self.queries.append(sql)
        if "finance_chat_user_memory" in sql:
            return [self.memory] if self.memory else []
        if "finance_chat_conversations" in sql:
            return [self.conversation] if self.conversation else []
        if "SELECT plan" in sql:
            return [{"plan": p} for p in self.plans]
        return list(reversed(self.turns))

    def updates(self):
        return [s for s in self.statements if s[0].startswith("UPDATE")]

    def merges(self, table):
        return [s for s in self.statements if f"MERGE INTO lakehouse_mvpai.aiops.{table} " in s[0]]


class FakeSummarizer:
    def __init__(self):
        self.calls = []

    async def summarize(self, previous, turns):
        self.calls.append((previous, [t.turn_index for t in turns]))
        return "Entities: 100-Northwind\nKey numbers: 97 reconciliations (How many reconciliations?)"


def fast_scripts(standalone="How many account reconciliations are there?", sql=COUNT_SQL):
    return ([fake.tool_calls([route("simple_data", standalone)]), fake.tool_call("submit_sql", {"sql": sql, "explanation": "Counted."})],
            [writer("The count is in the table below.", how="Counted the reconciliations.")])


def service_for(kb, executor, *, sql_script=None, resp_script=None, **settings):
    s, r = fast_scripts()
    orch, sql_p, resp_p, server, sink = make_orch(kb, sql_script or s, resp_script or r, **settings)
    summarizer = FakeSummarizer()
    svc = ChatService(orch, ACCESS, store=AiopsStore(executor), writer=BackgroundWriter(), summarizer=summarizer)
    return svc, sql_p, summarizer


def turn_rows(n, answer_chars=40):
    return [{"turn_index": i, "question_text": f"question {i}", "standalone_question": None, "answer_start": "a" * answer_chars}
            for i in range(1, n + 1)]


# ---------------------------------------------------------------- summary threshold

def test_token_estimate_and_threshold():
    turns = [TurnRecord(turn_index=1, question="q" * 400, answer="a" * 400)]
    assert context_tokens("s" * 40, turns) == 10 + 100 + 100
    assert needs_summary(None, turns, 150) and not needs_summary(None, turns, 500) and not needs_summary(None, [], 0)


async def test_summary_written_when_context_passes_threshold(kb):
    ex = MemExecutor(conversation={"conversation_id": "c1", "user_id": "obj-cfo", "turn_count": 3, "summary": None,
                                   "summary_through_turn": 0}, turns=turn_rows(3, answer_chars=4000))
    svc, _, summarizer = service_for(kb, ex, summary_token_threshold=2000)
    env = await svc.chat("How many account reconciliations are there?", Identity(user_id="obj-cfo"), conversation_id="c1")
    await svc.writer.flush()
    assert summarizer.calls == [(None, [1, 2, 3, 4])]  # every unsummarised turn plus this one
    (sql, params), = ex.updates()
    assert sql.startswith("UPDATE lakehouse_mvpai.aiops.finance_chat_conversations SET summary = CAST(:summary AS STRING)")
    assert params["through"] == 4 and params["cid"] == "c1" and params["summary"].startswith("Entities:")
    assert env.conversation_id == "c1"


async def test_no_summary_below_threshold_and_summary_reaches_the_agents(kb):
    ex = MemExecutor(conversation={"conversation_id": "c1", "user_id": "obj-cfo", "turn_count": 8,
                                   "summary": "Entities: 100-Northwind", "summary_through_turn": 6},
                     turns=turn_rows(8, answer_chars=400))  # about 100 tokens per turn
    svc, sql_p, summarizer = service_for(kb, ex, summary_token_threshold=6000, history_token_budget=350)
    await svc.chat("How many account reconciliations are there?", Identity(user_id="obj-cfo"), conversation_id="c1")
    await svc.writer.flush()
    assert summarizer.calls == [] and ex.updates() == []
    first = sql_p.calls[0]["messages"][0].text
    assert "Summary of the earlier conversation:\nEntities: 100-Northwind" in first
    assert "question 8" in first and "question 6" in first and "question 5" not in first  # the turns that fit 350 tokens


async def test_summarizer_uses_previous_summary_and_turns():
    p = FakeProvider([fake.text("Entities: 561 - Cars USA Shipping\nKey numbers: 6 finalized (How many finalized?)")])
    s = ConversationSummarizer(ModelHandle(p, "gptoss"))
    text = await s.summarize("Entities: 100-Northwind", [TurnRecord(turn_index=7, question="How many finalized?", answer="6 accounts")])
    assert text.startswith("Entities: 561")
    sent = p.calls[0]["messages"][0].text
    assert "Previous summary:\nEntities: 100-Northwind" in sent and "[7] User: How many finalized?" in sent
    assert "Key numbers" in p.calls[0]["system"] and p.calls[0]["tools"] == []


async def test_summary_update_is_guarded_to_aiops():
    sql, params = build_summary_update("lakehouse_mvpai", "aiops", "c1", "s", 3, "now")
    assert "WHERE conversation_id = CAST(:cid AS STRING)" in sql
    with pytest.raises(Exception):
        build_summary_update("lakehouse_mvpai", "silver", "c1", "s", 3, "now")


# ---------------------------------------------------------------- follow-ups

async def test_follow_up_is_rewritten_and_stored(kb):
    standalone = "Split the Feb 25 100-Northwind reconciliation status counts by account type"
    ex = MemExecutor(conversation={"conversation_id": "c1", "user_id": "obj-cfo", "turn_count": 1, "summary": None,
                                   "summary_through_turn": 0},
                     turns=[{"turn_index": 1, "question_text": "How many Northwind accounts per status in Feb 25?",
                             "standalone_question": None, "answer_start": "Approved 7, Not prepared 24, Prepared 9."}])
    s, r = fast_scripts(standalone)
    svc, sql_p, _ = service_for(kb, ex, sql_script=s, resp_script=r)
    env = await svc.chat("split that by account type", Identity(user_id="obj-cfo"), conversation_id="c1")
    await svc.writer.flush()
    assert env.debug.standalone_question == standalone
    assert "Approved 7, Not prepared 24" in sql_p.calls[0]["messages"][0].text  # the previous turn reached the supervisor
    assert sql_p.calls[1]["messages"][0].text.startswith(f"Question: {standalone}")  # fast path works on the rewrite
    final = ex.merges("finance_chat_messages")[-1][1]
    assert final["r0_standalone_question"] == standalone and final["r0_question_text"] == "split that by account type"


# ---------------------------------------------------------------- question limit

async def test_question_30_gets_limit_notice_and_forced_summary(kb):
    ex = MemExecutor(conversation={"conversation_id": "c1", "user_id": "obj-cfo", "turn_count": 29, "summary": None,
                                   "summary_through_turn": 0}, turns=turn_rows(29))
    svc, _, summarizer = service_for(kb, ex, conversation_question_limit=30)
    env = await svc.chat("How many account reconciliations are there?", Identity(user_id="obj-cfo"), conversation_id="c1")
    await svc.writer.flush()
    assert env.conversation_id == "c1" and env.notices[-1] == limit_reached_notice(30)
    assert summarizer.calls and ex.updates()[0][1]["through"] == 30  # summary ready to seed the next conversation


async def test_question_31_starts_a_new_conversation_seeded_with_the_summary(kb):
    ex = MemExecutor(conversation={"conversation_id": "c1", "user_id": "obj-cfo", "turn_count": 30,
                                   "summary": "Entities: 100-Northwind", "summary_through_turn": 30}, turns=turn_rows(30))
    svc, sql_p, _ = service_for(kb, ex, conversation_question_limit=30)
    env = await svc.chat("How many account reconciliations are there?", Identity(user_id="obj-cfo"), conversation_id="c1")
    await svc.writer.flush()
    assert env.conversation_id != "c1" and env.notices[0] == rollover_notice(30)
    first = sql_p.calls[0]["messages"][0].text
    assert "Summary of the earlier conversation:\nEntities: 100-Northwind" in first and "question 30" not in first
    conv_insert = ex.merges("finance_chat_conversations")[0][1]
    assert conv_insert["r0_conversation_id"] == env.conversation_id and conv_insert["r0_summary"] == "Entities: 100-Northwind"
    assert ex.merges("finance_chat_messages")[-1][1]["r0_turn_index"] == 1


def test_rollover_seed_without_model_summary():
    turns = [TurnRecord(turn_index=i, question=f"q{i}") for i in range(1, 8)]
    seed = fallback_seed("old summary", turns)
    assert seed.startswith("old summary") and "- q7" in seed and "- q2" not in seed


# ---------------------------------------------------------------- user memory

def test_extract_filters_reads_entities_and_periods(kb):
    f = extract_filters([NORTHWIND_SQL], kb)
    assert f == {"entities": ["100"], "periods": ["Feb 25"]}
    like = next(e.sql for e in kb.examples if e.id == "adra_pct_finalized")
    assert extract_filters([like], kb)["entities"] == ["cars usa shipping"]
    fy = next(e.sql for e in kb.examples if e.id == "fynapse_journal_types_in_month")
    assert extract_filters([fy], kb)["periods"] == ["FISCAL_YEAR=2026", "PERIOD=9"]
    assert extract_filters([COUNT_SQL], kb) == {"entities": [], "periods": []}


def test_build_memory_needs_a_clear_habit():
    habit = [json.dumps({"entities": ["100"], "periods": ["Feb 25"]})] * 6 + [json.dumps({"entities": ["561"]})] * 2
    mem = build_memory("u", habit)
    assert mem.default_entity == "100" and mem.default_period == "Feb 25"
    assert mem.frequent_entities[0] == {"entity": "100", "count": 6}
    mixed = [json.dumps({"entities": ["100"]})] * 5 + [json.dumps({"entities": ["561"]})] * 5
    assert build_memory("u", mixed).default_entity is None  # 50% is not a clear habit
    assert build_memory("u", [json.dumps({"entities": ["100"]})] * 4).default_entity is None  # too few


def test_memory_hint_and_assumed_entity_wording():
    mem = UserMemory(user_id="u", frequent_entities=[{"entity": "100-Northwind", "count": 18}], default_entity="100-Northwind")
    assert memory_hint(mem) == ("User habit (hint only): when the question names no entity, this user usually means "
                                "'100-Northwind' (18 of their last 30 questions). Use it only if the question names no "
                                "entity, and say in the answer that you assumed it.")
    notice = assumed_entity_notice(mem, ["100-Northwind"], "How many accounts are pending closure in Feb 25?")
    assert notice == ("I assumed 100-Northwind, the entity you usually ask about, because the question did not name one. "
                      "Ask again with another entity if you meant something else.")
    assert assumed_entity_notice(mem, ["100-Northwind"], "How many Northwind accounts are pending closure?") is None
    assert assumed_entity_notice(mem, ["561"], "How many accounts are pending closure?") is None
    assert memory_hint(UserMemory(user_id="u")) is None


async def test_service_applies_hint_and_adds_assumed_notice(kb):
    ex = MemExecutor(memory={"user_id": "obj-cfo", "frequent_entities": json.dumps([{"entity": "100", "count": 12}]),
                             "default_entity": "100", "default_period": "Feb 25", "recent_window_size": 30},
                     plans=[json.dumps({"entities": ["100"], "periods": ["Feb 25"]})] * 12)
    s, r = fast_scripts("How many accounts are pending closure for Feb 25?", NORTHWIND_SQL)
    svc, sql_p, _ = service_for(kb, ex, sql_script=s, resp_script=r)
    env = await svc.chat("How many accounts are pending closure for Feb 25?", Identity(user_id="obj-cfo"))
    await svc.writer.flush()
    assert "User habit (hint only)" in sql_p.calls[0]["messages"][0].text  # supervisor
    assert "User habit (hint only)" in sql_p.calls[1]["messages"][0].text  # fast path
    assert env.debug.filters == {"entities": ["100"], "periods": ["Feb 25"]}
    assert env.notices[0].startswith("I assumed 100, the entity you usually ask about")
    final = ex.merges("finance_chat_messages")[-1][1]
    assert json.loads(final["r0_plan"]) == {"entities": ["100"], "periods": ["Feb 25"]}
    mem_row = ex.merges("finance_chat_user_memory")[0][1]
    assert mem_row["r0_default_entity"] == "100" and mem_row["r0_frequent_kpis"] is None
