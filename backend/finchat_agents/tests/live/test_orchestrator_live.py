"""Live end-to-end smoke test of answer(): real Bedrock models and Databricks. RUN_LIVE=1 only.
The full question-bank run is `python -m finchat_agents.eval.scorecard`."""
from __future__ import annotations

import os

import pytest

pytestmark = [pytest.mark.live, pytest.mark.skipif(os.getenv("RUN_LIVE") != "1", reason="live test: set RUN_LIVE=1")]


async def test_simple_adra_question_end_to_end():
    from finchat_agents.eval.scorecard import build_live_orchestrator

    orch, user = build_live_orchestrator()
    env = await orch.answer("How many account reconciliations are there in ADRA in total?", user)
    print("\n", env.debug.mode, env.debug.latency_ms, "ms", env.debug.llm_calls, "LLM calls\n", env.answer)
    assert env.status == "answered" and "97" in env.answer
    assert env.how_calculated and "select" not in env.how_calculated.lower()


async def test_general_question_end_to_end():
    from finchat_agents.eval.scorecard import build_live_orchestrator

    orch, user = build_live_orchestrator()
    env = await orch.answer("What is the difference between a balance sheet and an income statement?", user)
    assert env.debug.mode == "general" and env.answer.lower().startswith("general knowledge")
