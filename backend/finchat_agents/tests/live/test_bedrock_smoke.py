"""Live Bedrock smoke tests. Run only with RUN_LIVE=1 and working AWS credentials:

    RUN_LIVE=1 pytest tests/live -v

Each model answers "2+2" and calls a toy add(a, b) tool exactly once. The gpt-oss test runs on both transports
(converse and openai) so the result shows which one supports tool calling in AWS_REGION.
"""
from __future__ import annotations

import os
from typing import Any

import pytest

from finchat_agents.config import Settings
from finchat_agents.llm.factory import response_model, sql_model
from finchat_agents.llm.types import Message, ModelHandle
from finchat_agents.runtime.agent import Agent
from finchat_agents.runtime.tools import Budget, RunContext, ToolContext, tool
from finchat_agents.tracing import MemorySink, Tracer

pytestmark = [
    pytest.mark.live,
    pytest.mark.skipif(os.getenv("RUN_LIVE") != "1", reason="live test: set RUN_LIVE=1"),
]


def _settings() -> Settings:
    return Settings()


def _models() -> list[tuple[str, ModelHandle]]:
    s = _settings()
    return [
        ("claude", sql_model(s)),
        ("gpt-oss/converse", response_model(s, "converse")),
        ("gpt-oss/openai", response_model(s, "openai")),
    ]


@pytest.mark.parametrize("label,model", _models() if os.getenv("RUN_LIVE") == "1" else [], ids=lambda v: v if isinstance(v, str) else "")
async def test_two_plus_two(label: str, model: ModelHandle):
    r = await model.complete("Answer with just the number.", [Message.user("What is 2+2?")], [], 64, 0.0)
    assert "4" in r.text, f"{label}: {r.text!r}"


@pytest.mark.parametrize("label,model", _models() if os.getenv("RUN_LIVE") == "1" else [], ids=lambda v: v if isinstance(v, str) else "")
async def test_calls_add_tool_once(label: str, model: ModelHandle):
    calls: list[dict[str, Any]] = []

    @tool("add", "Add two integers and return the sum.", {
        "type": "object",
        "properties": {"a": {"type": "integer"}, "b": {"type": "integer"}},
        "required": ["a", "b"],
    })
    async def add(args: dict[str, Any], ctx: ToolContext) -> dict[str, int]:
        calls.append(args)
        return {"sum": int(args["a"]) + int(args["b"])}

    agent = Agent(
        "smoke",
        "You must use the add tool for arithmetic. Call it once, then answer with the sum.",
        model,
        [add],
        max_steps=4,
    )
    ctx = RunContext(tracer=Tracer([MemorySink()]), budget=Budget(max_seconds=120))
    r = await agent.run("What is 17 + 25? Use the add tool.", ctx)
    assert len(calls) == 1, f"{label}: add called {len(calls)} times"
    assert r.status == "final" and "42" in r.answer, f"{label}: {r.answer!r}"
