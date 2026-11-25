from __future__ import annotations

import pytest

from finchat_agents.config import Settings
from finchat_agents.llm.types import LLMError
from finchat_agents.runtime.retry import call_with_retry
from finchat_agents.runtime.tools import Budget


def test_settings_from_env(monkeypatch):
    monkeypatch.setenv("AGENT_MAX_STEPS", "7")
    monkeypatch.setenv("AWS_REGION", "")  # empty means not set
    monkeypatch.setenv("AZURE_CLIENT_SECRET", "not-a-real-secret")
    monkeypatch.setenv("GPT_OSS_TRANSPORT", "openai")
    s = Settings(_env_file=None)
    assert s.agent_max_steps == 7 and s.aws_region is None and s.gpt_oss_transport == "openai"
    assert "not-a-real-secret" not in repr(s)  # SecretStr never prints
    assert s.azure_client_secret.get_secret_value() == "not-a-real-secret"
    assert Budget.from_settings(s).max_steps == 7
    assert s.bedrock_model_sql.startswith("us.anthropic.claude-sonnet-4-5")


async def test_retry_backoff_then_success():
    delays: list[float] = []
    calls = {"n": 0}

    async def fn():
        calls["n"] += 1
        if calls["n"] < 3:
            raise LLMError("throttled", retryable=True)
        return "ok"

    async def fake_sleep(d):
        delays.append(d)

    assert await call_with_retry(fn, base_delay=1.0, sleep=fake_sleep) == "ok"
    assert len(delays) == 2 and 0.75 <= delays[0] <= 1.25 and 1.5 <= delays[1] <= 2.5


async def test_retry_stops_on_non_retryable_and_deadline():
    async def bad():
        raise LLMError("400", retryable=False)

    with pytest.raises(LLMError):
        await call_with_retry(bad, sleep=lambda d: None)

    async def throttled():
        raise LLMError("429", retryable=True)

    slept: list[float] = []

    async def fake_sleep(d):
        slept.append(d)

    with pytest.raises(LLMError):
        await call_with_retry(throttled, base_delay=5.0, deadline=1.0, clock=lambda: 0.0, sleep=fake_sleep)
    assert slept == []  # the wait would pass the deadline, so it gives up at once
