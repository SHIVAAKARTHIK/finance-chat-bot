"""Input and output guardrails added on top of the company packs: redaction of typed secrets, harmful content, help
replies, the optional Bedrock Guardrail and the attack-test runner. Fake models and a fake AWS client only."""
from __future__ import annotations

import pytest

from finchat_agents.api.service import ChatService, Identity
from finchat_agents.config import Settings
from finchat_agents.guardrails import GuardrailError, load_from_settings
from finchat_agents.guardrails.bedrock import BedrockContentFilter, ContentFilterError, parse_response
from finchat_agents.guardrails.evaluate import DEFAULT_CASES, Case, load_cases, main as evaluate_main, report, run_cases
from finchat_agents.guardrails.input_checks.redact import redact_question
from finchat_agents.guardrails.patterns import REMOVED
from finchat_agents.guardrails.replies import DEFAULT_HARMFUL, DEFAULT_SUPPORT, UNAVAILABLE_TEXT
from finchat_agents.llm import fake
from finchat_agents.llm.fake import FakeProvider
from finchat_agents.llm.types import ModelHandle
from finchat_agents.storage.aiops import AiopsStore
from finchat_agents.storage.writer import BackgroundWriter

from .test_agents import writer
from .test_guardrails import ALL, QUESTION, build, fast_sql, kb, make_folder, verdict  # noqa: F401 (kb fixture)
from .test_storage_api import ACCESS, FakeExecutor


@pytest.fixture
def folder(tmp_path):
    return make_folder(tmp_path / "g")


class FakeBedrock:
    """Stands in for the boto3 bedrock-runtime client: `rules` maps a source to a response or an exception."""

    def __init__(self, **rules):
        self.rules, self.calls = rules, []

    def apply_guardrail(self, **kw):
        self.calls.append(kw)
        answer = self.rules.get(kw["source"], {"action": "NONE", "outputs": []})
        if isinstance(answer, Exception):
            raise answer
        return answer


def intervened(text, action="BLOCKED"):
    return {"action": "GUARDRAIL_INTERVENED", "outputs": [{"text": text}],
            "assessments": [{"contentPolicy": {"filters": [{"type": "HATE", "action": action}]}}]}


def with_filter(orch, client):
    orch.guardrails.content_filter = BedrockContentFilter("eu-west-1", "g-1", "2", client=client)


# ---------------------------------------------------------------- redaction

@pytest.mark.parametrize("typed, kind, secret", [
    ("my password is Hunter2! show balances", "password or key", "Hunter2"),
    ("api_key=abc123XYZ please", "password or key", "abc123XYZ"),
    ("key AKIA" + "ABCDEFGHIJKLMNOP leaked", "password or key", "ABCDEFGHIJKLMNOP"),  # made up
    ("tasks for jane.doe@corp.com", "email address", "jane.doe"),
    ("card 4111 1111 1111 1111 declined", "card number", "4111"),
    ("card number 4111111111111111", "card number", "4111111111111111"),
    ("SSN: 123-45-6789 for payroll", "social security number", "6789"),
    ("call me on +44 20 7946 0958", "phone number", "7946"),
])
def test_sensitive_data_is_removed_from_questions(typed, kind, secret):
    clean, kinds = redact_question(typed)
    assert kind in kinds and secret not in clean and REMOVED in clean


@pytest.mark.parametrize("typed", [
    "Balance of account 100-10-1000 for entity UK07 in Oct 26",
    "Show invoice 4111111111111111 and journal 1234567890123",
    "Items 1234 5678 9012 3456 are open",  # grouped digits that are not a valid card number
    "What is the password policy for the close process?",
    "Variance of +12345.67 since 2026-10-01 on account 123456789",
])
def test_finance_values_are_not_touched(typed):
    assert redact_question(typed) == (typed, [])


async def test_redacted_text_is_what_gets_stored_and_sent_to_models(kb, folder):
    orch, sql_p, _, guard_p, _, sink = build(kb, folder, fast_sql(), [writer("The count is 97.")], [verdict("allow")])
    ex = FakeExecutor()
    service = ChatService(orch, ACCESS, store=AiopsStore(ex), writer=BackgroundWriter())
    env = await service.chat("my password is Hunter2, how many reconciliations?", Identity(user_id="obj-cfo"))
    await service.writer.flush()
    sent = [m["messages"][0].text for m in [*guard_p.calls, *sql_p.calls]]
    stored = str(ex.statements)
    assert all("Hunter2" not in t for t in sent) and "Hunter2" not in stored and REMOVED in stored
    assert env.notices[0].startswith("Sensitive details were removed") and "password or key" in env.notices[0]
    assert "input_redaction" in stored


# ---------------------------------------------------------------- harmful content and support

@pytest.mark.parametrize("kind, reply", [("harmful", DEFAULT_HARMFUL), ("support", DEFAULT_SUPPORT)])
async def test_harmful_and_support_replies_need_no_company_pack(kb, folder, kind, reply):
    orch, _, resp_p, _, server, _ = build(kb, folder, fast_sql(), [writer("unused")], [verdict(kind)])
    env = await orch.answer("...", ALL)
    assert env.status == "declined" and env.answer == reply and server.queries == [] and resp_p.calls == []


# ---------------------------------------------------------------- Bedrock Guardrail

def test_bedrock_response_parsing():
    assert parse_response({"action": "NONE"}, "t").model_dump() == {"blocked": False, "changed": False, "text": "t"}
    assert parse_response(intervened("No."), "t").blocked
    masked = parse_response(intervened("hi {NAME}", "ANONYMIZED"), "hi Bob")
    assert masked.changed and not masked.blocked and masked.text == "hi {NAME}"
    assert parse_response({"action": "GUARDRAIL_INTERVENED"}, "t").blocked  # no output: never show the original


async def test_filter_calls_aws_with_the_configured_guardrail():
    client = FakeBedrock()
    result = await BedrockContentFilter("eu-west-1", "g-1", "2", client=client).apply("hello", "INPUT")
    assert result.text == "hello"
    assert client.calls == [{"guardrailIdentifier": "g-1", "guardrailVersion": "2", "source": "INPUT",
                             "content": [{"text": {"text": "hello"}}]}]
    with pytest.raises(ContentFilterError):
        await BedrockContentFilter("r", "g", "1", client=FakeBedrock(INPUT=OSError("x"))).apply("hello", "INPUT")


async def test_blocked_question_gets_the_aws_message_and_nothing_runs(kb, folder):
    orch, _, resp_p, _, server, _ = build(kb, folder, fast_sql(), [writer("unused")], [verdict("allow")])
    with_filter(orch, FakeBedrock(INPUT=intervened("Blocked by policy.")))
    env = await orch.answer("bad words", ALL)
    assert env.status == "declined" and env.answer == "Blocked by policy." and server.queries == [] and resp_p.calls == []


async def test_support_reply_wins_over_a_content_block(kb, folder):
    orch, *_ = build(kb, folder, fast_sql(), [writer("unused")], [verdict("support")])
    with_filter(orch, FakeBedrock(INPUT=intervened("Blocked by policy.")))
    assert (await orch.answer("...", ALL)).answer == DEFAULT_SUPPORT


@pytest.mark.parametrize("source", ["INPUT", "OUTPUT"])
async def test_filter_failure_shows_nothing(kb, folder, source):
    orch, *_ = build(kb, folder, fast_sql(), [writer("The count is 97.")], [verdict("allow")])
    with_filter(orch, FakeBedrock(**{source: OSError("down")}))
    env = await orch.answer(QUESTION, ALL)
    assert env.status == "failed" and env.answer == UNAVAILABLE_TEXT and env.tables == []


async def test_answer_is_blocked_or_masked_by_the_filter(kb, folder):
    orch, *_ = build(kb, folder, fast_sql(), [writer("The count is 97.")], [verdict("allow")])
    with_filter(orch, FakeBedrock(OUTPUT=intervened("Cannot show that.")))
    env = await orch.answer(QUESTION, ALL)
    assert env.status == "declined" and env.answer == "Cannot show that." and env.how_calculated == ""
    orch, *_, sink = build(kb, folder, fast_sql(), [writer("The count is 97.")], [verdict("allow")])
    with_filter(orch, FakeBedrock(OUTPUT=intervened("Masked text.", "ANONYMIZED")))
    env = await orch.answer(QUESTION, ALL)
    assert env.status == "answered" and env.answer == "Masked text."
    assert any(e.name == "content_filter_output" and e.payload["output"] == "masked" for e in sink.events)


def test_bedrock_settings(folder):
    base = dict(_env_file=None, guardrails_dir=str(folder))
    assert load_from_settings(Settings(**base)).content_filter is None
    on = load_from_settings(Settings(**base, bedrock_guardrail_id="g-1", bedrock_guardrail_version="3"))
    assert on.content_filter.version == "3"
    with pytest.raises(GuardrailError, match="BEDROCK_GUARDRAIL_VERSION"):
        load_from_settings(Settings(**base, bedrock_guardrail_id="g-1"))


# ---------------------------------------------------------------- attack-test runner

def test_shipped_cases_are_valid_and_cover_blocked_and_allowed():
    cases = load_cases(DEFAULT_CASES)
    assert len(cases) >= 30
    assert sum(c.expect == ["allow"] for c in cases) >= 8
    assert {"injection", "confidential", "scope", "capability", "harmful", "support", "valid"} <= {c.category for c in cases}


async def test_runner_scores_cases(folder):
    from finchat_agents.guardrails import Guardrails

    cases = [Case(id="a", category="injection", message="x", expect=["blocked"]),
             Case(id="b", category="valid", message="y", expect=["allow"])]
    llm = ModelHandle(FakeProvider([verdict("injection"), verdict("out_of_scope")]), "fake")
    outcomes = await run_cases(cases, Guardrails.load(folder), llm, "system")
    assert [o.passed for o in outcomes] == [True, False]
    text = report(outcomes)
    assert "1 of 2 cases passed" in text and "b: expected allow, got out_of_scope" in text


def test_runner_refuses_to_run_without_run_live(monkeypatch, capsys):
    monkeypatch.setenv("RUN_LIVE", "0")
    assert evaluate_main([]) == 2 and "RUN_LIVE=1" in capsys.readouterr().out
    assert fake  # fake models only in this file
