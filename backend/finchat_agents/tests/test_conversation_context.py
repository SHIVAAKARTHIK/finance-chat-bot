"""Token-based conversation context, topic state (e.g. FA questions, then Fynapse questions), topic clarification,
the "Answering for" context, and clear context. Fake models and a fake aiops connector only."""
from __future__ import annotations

import json

import pytest

from finchat_agents.api.service import CLEARED_TEXT, Identity
from finchat_agents.integration import to_ui_body
from finchat_agents.knowledge.loader import Knowledge
from finchat_agents.llm import fake
from finchat_agents.llm.fake import FakeProvider
from finchat_agents.llm.types import ModelHandle
from finchat_agents.memory.context import select_recent, topic_states, topics_text
from finchat_agents.memory.summary import ConversationSummarizer, TurnRecord, turns_from_rows
from finchat_agents.storage.aiops import MISSING_CONTEXT_COLUMN, AiopsStore

from .test_agents import route
from .test_integration_backend import backend_app, client_for
from .test_memory import MemExecutor, service_for

USER = Identity(user_id="obj-cfo")
QUESTION = "How many account reconciliations are there?"


@pytest.fixture(scope="module")


def kb() -> Knowledge:
    return Knowledge.load()


def conv(turn_count, **kw):
    return {"conversation_id": "c1", "user_id": "obj-cfo", "turn_count": turn_count, "summary": None,
            "summary_through_turn": 0, **kw}


def fa_then_fynapse_rows():
    """Turns 1-3 about fixed assets (entity UK07), turns 4-6 about Fynapse subledger journals (entity 561)."""
    rows = []
    for i in range(1, 7):
        fa = i <= 3
        rows.append({"turn_index": i, "question_text": f"{'asset additions' if fa else 'journal lines'} question {i}",
                     "standalone_question": None, "answer_start": f"answer {i}", "domain": "fa" if fa else "subledger",
                     "plan": json.dumps({"entities": ["UK07"] if fa else ["561"], "periods": ["Oct 26"]})})
    return rows


# ---------------------------------------------------------------- pure functions

def test_recent_turns_are_chosen_by_tokens_newest_first():
    turns = [TurnRecord(turn_index=i, question="q" * 40, answer="a" * 360) for i in range(1, 9)]  # 100 tokens each
    assert [t.turn_index for t in select_recent(turns, 300)] == [6, 7, 8]
    assert [t.turn_index for t in select_recent(turns, 10)] == [8]  # the newest turn is always kept
    long = [TurnRecord(turn_index=1, question="q", answer="a" * 50_000)]
    assert len(select_recent(long, 3000)) == 1  # long answers are shortened before they are counted


def test_rows_carry_domain_and_filters_and_topics_are_most_recent_first():
    turns = turns_from_rows(fa_then_fynapse_rows())
    assert turns[0].domains == ["fa"] and turns[0].entities == ["UK07"] and turns[5].periods == ["Oct 26"]
    states = topic_states(turns, {"fa": "Fixed assets", "subledger": "Fynapse subledger journals"})
    assert [(s.domain, s.first_turn, s.last_turn, s.turns) for s in states] == [("subledger", 4, 6, 3), ("fa", 1, 3, 3)]
    text = topics_text(states)
    assert text.splitlines()[1].startswith("- Fynapse subledger journals [subledger] (current topic); turns 4-6")
    assert "entities: UK07" in text and "periods: Oct 26" in text
    assert turns_from_rows([{"turn_index": 1, "question_text": "q", "plan": "not json", "domain": None}])[0].entities == []


async def test_summary_input_names_the_topic_of_each_turn():
    p = FakeProvider([fake.text("Topic: Fixed assets (turns 1-1)")])
    s = ConversationSummarizer(ModelHandle(p, "gptoss"), {"fa": "Fixed assets"})
    await s.summarize(None, [TurnRecord(turn_index=1, question="additions?", answer="12", domains=["fa"]),
                             TurnRecord(turn_index=2, question="what is IFRS 16?", answer="leases")])
    sent = p.calls[0]["messages"][0].text
    assert "[1] Topic: Fixed assets" in sent and "[2] Topic: general (no company data)" in sent
    assert "One section per topic" in p.calls[0]["system"]


# ---------------------------------------------------------------- service: context sent to the agents

async def test_supervisor_sees_topics_and_the_topic_of_each_turn(kb):
    ex = MemExecutor(conversation=conv(6), turns=fa_then_fynapse_rows())
    svc, sql_p, _ = service_for(kb, ex)
    await svc.chat("what about last month?", USER, conversation_id="c1")
    await svc.writer.flush()
    first = sql_p.calls[0]["messages"][0].text
    assert "Topics in this conversation (most recent first):" in first
    assert "- Fynapse subledger journals [subledger] (current topic)" in first and "- Fixed assets [fa]" in first
    assert "User [topic: Fixed assets]: asset additions question 1" in first
    assert "User [topic: Fynapse subledger journals]: journal lines question 6" in first


async def test_turns_outside_the_budget_and_not_summarised_are_listed_as_questions(kb):
    rows = [{"turn_index": i, "question_text": f"question {i}", "standalone_question": None, "answer_start": "a" * 400}
            for i in range(1, 7)]
    ex = MemExecutor(conversation=conv(6), turns=rows)
    svc, sql_p, _ = service_for(kb, ex, history_token_budget=250, summary_token_threshold=100_000)
    await svc.chat(QUESTION, USER, conversation_id="c1")
    await svc.writer.flush()
    first = sql_p.calls[0]["messages"][0].text
    assert "Earlier questions (not in the summary yet):\n- question 1\n- question 2\n- question 3\n- question 4" in first
    assert "User: question 6" in first and "User: question 4" not in first


async def test_summary_trigger_counts_only_the_turns_not_in_it(kb):
    ex = MemExecutor(conversation=conv(2, summary="s" * 40_000, summary_through_turn=1), turns=fa_then_fynapse_rows()[:2])
    svc, _, summarizer = service_for(kb, ex, summary_token_threshold=3000)
    await svc.chat(QUESTION, USER, conversation_id="c1")
    await svc.writer.flush()
    assert summarizer.calls == []  # a long summary alone does not trigger a rewrite on every question


async def test_no_question_limit_by_default(kb):
    rows = [{"turn_index": i, "question_text": f"question {i}", "standalone_question": None, "answer_start": "a"}
            for i in range(1, 41)]
    ex = MemExecutor(conversation=conv(40, summary="Topic: x", summary_through_turn=30), turns=rows)
    svc, _, _ = service_for(kb, ex)
    env = await svc.chat(QUESTION, USER, conversation_id="c1")
    await svc.writer.flush()
    assert env.conversation_id == "c1" and not any("limit" in n for n in env.notices)
    assert ex.merges("finance_chat_messages")[-1][1]["r0_turn_index"] == 41


# ---------------------------------------------------------------- topic clarification and "Answering for"

async def test_ambiguous_topic_returns_clickable_options_without_running_sql(kb):
    options = ["Fixed assets: total for Oct 26", "Fynapse subledger journals: total for Oct 26"]
    sql_script = [fake.tool_calls([("route", {"classification": "simple_data", "options": options})])]
    ex = MemExecutor(conversation=conv(6), turns=fa_then_fynapse_rows())
    svc, sql_p, _ = service_for(kb, ex, sql_script=sql_script, resp_script=[fake.text("unused")])
    env = await svc.chat("what is the total?", USER, conversation_id="c1")
    await svc.writer.flush()
    assert env.status == "clarification" and env.options == options and env.debug.mode == "clarify"
    assert "more than one topic" in env.answer and "- Fixed assets: total for Oct 26" in env.answer
    assert len(sql_p.calls) == 1 and env.debug.sql == []
    body = to_ui_body(env, query="what is the total?", user_id="obj-cfo", session_id=None)
    assert body["status"] == "clarification" and json.loads(body["follow_up_questions"]) == options
    assert body["clarification_options"] == options and body["answer_context"] is None


async def test_answer_context_names_the_topic_filters_and_other_topics(kb):
    northwind = next(e.sql for e in kb.examples if e.id == "adra_pending_closure_count")
    sql_script = [fake.tool_calls([route("simple_data", "How many accounts are pending closure for Feb 25?")]),
                  fake.tool_call("submit_sql", {"sql": northwind, "explanation": "Counted."})]
    ex = MemExecutor(conversation=conv(6), turns=fa_then_fynapse_rows())
    from .test_agents import writer

    svc, _, _ = service_for(kb, ex, sql_script=sql_script, resp_script=[writer("The count is in the table below.")])
    env = await svc.chat("pending closure for Northwind in Feb 25?", USER, conversation_id="c1")
    await svc.writer.flush()
    ctx = env.answer_context
    assert ctx is not None and ctx.topics == [kb.domains["recon"]]
    assert ctx.entities == ["100"] and ctx.periods == ["Feb 25"]
    assert ctx.other_topics == ["Fynapse subledger journals", "Fixed assets"]
    body = to_ui_body(env, query="q", user_id="obj-cfo", session_id=None)
    assert body["answer_context"]["topics"] == [kb.domains["recon"]] and body["clarification_options"] == []


# ---------------------------------------------------------------- clear context

async def test_clear_context_saves_the_turn_and_later_questions_ignore_earlier_turns(kb):
    ex = MemExecutor(conversation=conv(6, summary="Topic: Fixed assets ...", summary_through_turn=5),
                     turns=fa_then_fynapse_rows())
    svc, sql_p, _ = service_for(kb, ex)
    result = await svc.clear_context("c1", USER)
    assert result == {"conversation_id": "c1", "cleared": True, "context_start_turn": 6, "message": CLEARED_TEXT}
    (sql, params), = ex.updates()
    assert sql.startswith("UPDATE lakehouse_mvpai.aiops.finance_chat_conversations SET context_start_turn = CAST(:turn AS INT)")
    assert params["turn"] == 6 and params["cid"] == "c1"

    ex.conversation = conv(6, summary="Topic: Fixed assets ...", summary_through_turn=5, context_start_turn=6)
    await svc.chat(QUESTION, USER, conversation_id="c1")
    await svc.writer.flush()
    first = sql_p.calls[0]["messages"][0].text
    assert first == QUESTION  # no summary, no topics, no earlier turns
    assert ex.merges("finance_chat_messages")[-1][1]["r0_turn_index"] == 7  # the history continues


async def test_turns_after_a_clear_are_used_again(kb):
    ex = MemExecutor(conversation=conv(6, context_start_turn=4), turns=fa_then_fynapse_rows())
    svc, sql_p, _ = service_for(kb, ex)
    await svc.chat("and for last month?", USER, conversation_id="c1")
    first = sql_p.calls[0]["messages"][0].text
    assert "journal lines question 5" in first and "asset additions" not in first and "Fixed assets" not in first


async def test_clear_command_and_other_users(kb):
    ex = MemExecutor(conversation=conv(3))
    svc, sql_p, _ = service_for(kb, ex)
    env = await svc.chat("/clear", USER, conversation_id="c1")
    assert env.answer == CLEARED_TEXT and env.status == "answered" and sql_p.calls == []
    assert ex.updates()[0][1]["turn"] == 3
    with pytest.raises(PermissionError):
        await svc.clear_context("c1", Identity(user_id="someone-else"))
    env = await svc.chat("/clear", Identity(user_id="someone-else"), conversation_id="c1")
    assert env.status == "declined"


class NoColumnExecutor(MemExecutor):
    """Like the live table before the admin adds context_start_turn."""

    async def query(self, sql, params):
        if "context_start_turn" in sql:
            raise RuntimeError("[UNRESOLVED_COLUMN] A column with name `context_start_turn` cannot be resolved.")
        return await super().query(sql, params)

    async def execute(self, statements):
        if any("context_start_turn" in s[0] for s in statements):
            raise RuntimeError("[UNRESOLVED_COLUMN] `context_start_turn` cannot be resolved.")
        await super().execute(statements)


async def test_missing_column_keeps_history_working_and_clear_explains_the_fix(kb):
    ex = NoColumnExecutor(conversation=conv(6), turns=fa_then_fynapse_rows())
    store = AiopsStore(ex)
    assert (await store.conversation("c1"))["turn_count"] == 6  # falls back to the old columns
    with pytest.raises(RuntimeError, match="ALTER TABLE lakehouse_mvpai.aiops.finance_chat_conversations"):
        await store.set_context_start("c1", 6)
    assert "ADD COLUMNS (context_start_turn INT" in MISSING_CONTEXT_COLUMN

    svc, sql_p, _ = service_for(kb, ex)
    await svc.chat(QUESTION, USER, conversation_id="c1")
    assert "journal lines question 6" in sql_p.calls[0]["messages"][0].text
    env = await svc.chat("/clear", USER, conversation_id="c1")
    assert env.status == "failed" and "could not be cleared" in env.answer


async def test_backend_clear_context_route(kb):
    ex = MemExecutor(conversation=conv(2))
    svc, _, _ = service_for(kb, ex)
    async with client_for(backend_app(svc)) as c:
        r = await c.post("/api/invoke/finance-chat/clear-context", json={"conversation_id": "c1"})
    assert r.status_code == 200 and r.json()["status"] == "success" and r.json()["context_start_turn"] == 2
    ex.conversation = conv(2, user_id="someone-else")
    async with client_for(backend_app(svc)) as c:
        r = await c.post("/api/invoke/finance-chat/clear-context", json={"conversation_id": "c1"})
    assert r.status_code == 403
    svc2, _, _ = service_for(kb, NoColumnExecutor(conversation=conv(2)))
    async with client_for(backend_app(svc2)) as c:
        r = await c.post("/api/invoke/finance-chat/clear-context", json={"conversation_id": "c1"})
    assert r.status_code == 503 and r.json() == {"status": "error", "message": "The context could not be cleared right now."}
