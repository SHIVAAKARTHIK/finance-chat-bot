from __future__ import annotations

import time

from finchat_agents.llm import fake
from finchat_agents.llm.fake import FakeProvider
from finchat_agents.llm.types import LLMError, Message, ToolResultBlock, ToolSpec
from finchat_agents.runtime.loop import run_loop
from finchat_agents.runtime.tools import ToolError, tool

from .conftest import add_tool, fake_sql_tool, handle, sleeper


async def _run(provider, ctx, tools=(), max_steps=15, **kw):
    return await run_loop(
        llm=handle(provider), system="sys", messages=[Message.user("q")], tools=list(tools),
        ctx=ctx, agent="test", max_steps=max_steps, retry_base_delay=0.01, **kw,
    )


async def test_final_answer_without_tools(make_ctx):
    p = FakeProvider([fake.text("4")])
    r = await _run(p, make_ctx())
    assert (r.status, r.text, r.stop_reason, r.steps, r.llm_calls) == ("final", "4", "final", 1, 1)


async def test_tool_loop_appends_results_and_finishes(make_ctx):
    p = FakeProvider([fake.tool_call("add", {"a": 2, "b": 2}, call_id="c1"), fake.text("The sum is 4.")])
    r = await _run(p, make_ctx(), [add_tool])
    assert r.status == "final" and r.text == "The sum is 4."
    assert [t.name for t in r.tool_calls] == ["add"]
    assert r.tool_calls[0].raw == {"sum": 4}
    # second model call saw the tool result in a user message
    last = p.calls[1]["messages"][-1]
    assert last.role == "user"
    block = last.content[0]
    assert isinstance(block, ToolResultBlock) and block.tool_use_id == "c1" and '"sum": 4' in block.content
    assert p.calls[0]["tools"] == ["add"]
    assert r.usage.input_tokens == 20


async def test_independent_tools_run_in_parallel(make_ctx):
    tools = [sleeper("a", 0.3), sleeper("b", 0.3), sleeper("c", 0.3)]
    p = FakeProvider([fake.tool_calls([("a", {}), ("b", {}), ("c", {})]), fake.text("done")])
    t0 = time.perf_counter()
    r = await _run(p, make_ctx(), tools)
    elapsed = time.perf_counter() - t0
    assert r.status == "final"
    assert elapsed < 0.6, f"tools did not run in parallel ({elapsed:.2f}s)"
    assert [t.name for t in r.tool_calls] == ["a", "b", "c"]  # results keep call order


async def test_non_parallel_safe_tools_run_one_at_a_time(make_ctx):
    log: list[str] = []
    tools = [sleeper("x", 0.05, parallel_safe=False, log=log), sleeper("y", 0.05, parallel_safe=False, log=log)]
    p = FakeProvider([fake.tool_calls([("x", {}), ("y", {})]), fake.text("done")])
    await _run(p, make_ctx(), tools)
    assert log == ["start:x", "end:x", "start:y", "end:y"]


async def test_unknown_tool_and_tool_errors_go_back_to_model(make_ctx):
    @tool("boom", "fails", {"type": "object", "properties": {}})
    async def boom(args, ctx):
        raise RuntimeError("kaput")

    @tool("refuse", "refuses", {"type": "object", "properties": {}})
    async def refuse(args, ctx):
        raise ToolError("table X is not in the catalog; did you mean Y?")

    p = FakeProvider([fake.tool_calls([("nope", {}), ("boom", {}), ("refuse", {})]), fake.text("ok")])
    r = await _run(p, make_ctx(), [boom, refuse])
    assert r.status == "final"
    outs = {t.name: t for t in r.tool_calls}
    assert all(t.is_error for t in r.tool_calls)
    assert "Unknown tool 'nope'" in outs["nope"].output
    assert "kaput" in outs["boom"].output
    assert outs["refuse"].output == "table X is not in the catalog; did you mean Y?"


async def test_max_steps_returns_model_written_partial(make_ctx):
    script = [fake.tool_call("add", {"a": 1, "b": 1}) for _ in range(3)] + [fake.text("Partial: sum is 2; total missing.")]
    p = FakeProvider(script)
    r = await _run(p, make_ctx(), [add_tool], max_steps=3)
    assert r.status == "partial" and r.stop_reason == "max_steps"
    assert r.text == "Partial: sum is 2; total missing."
    # the summary call was told to stop calling tools
    assert "Do not call any more tools" in p.calls[-1]["messages"][-1].content[-1].text


async def test_max_steps_falls_back_to_deterministic_partial(make_ctx):
    script = [fake.tool_call("add", {"a": 1, "b": 1}) for _ in range(2)] + [LLMError("down", retryable=False)]
    r = await _run(FakeProvider(script), make_ctx(), [add_tool], max_steps=2)
    assert r.status == "partial" and r.text.startswith("Partial answer:")
    assert "step limit" in r.text and "add" in r.text


async def test_time_budget_returns_partial_never_empty(make_ctx):
    p = FakeProvider([fake.tool_call("slow", {}), fake.text("never")])
    r = await _run(p, make_ctx(max_seconds=0.2), [sleeper("slow", 1.0)])
    assert r.status == "partial" and r.stop_reason == "max_seconds"
    assert r.text and "time limit" in r.text
    assert r.tool_calls[0].is_error


async def test_model_error_returns_partial(make_ctx):
    r = await _run(FakeProvider([LLMError("bad request", retryable=False, status=400)]), make_ctx())
    assert r.status == "partial" and r.stop_reason == "model_error" and r.text


async def test_throttling_is_retried(make_ctx):
    p = FakeProvider([LLMError("throttled", retryable=True, status=429), LLMError("503", retryable=True), fake.text("4")])
    r = await _run(p, make_ctx())
    assert r.status == "final" and r.text == "4" and len(p.calls) == 3


async def test_sql_budget_is_enforced(make_ctx):
    sql = fake_sql_tool()
    p = FakeProvider([fake.tool_call("run_sql", {"sql": "s"}), fake.tool_call("run_sql", {"sql": "s"}), fake.text("97")])
    ctx = make_ctx(max_sql_calls=1)
    r = await _run(p, ctx, [sql])
    assert ctx.counters.sql_calls == 1
    assert not r.tool_calls[0].is_error
    assert r.tool_calls[1].is_error and "SQL call budget reached" in r.tool_calls[1].output


async def test_finish_tool_returns_structured_data(make_ctx):
    finish = ToolSpec(name="submit_result", description="d", input_schema={"type": "object", "properties": {}})
    p = FakeProvider([fake.tool_call("submit_result", {"answer": "97 accounts", "sql": "SELECT 1"})])
    r = await _run(p, make_ctx(), finish_tool=finish)
    assert r.stop_reason == "finish_tool" and r.text == "97 accounts" and r.data["sql"] == "SELECT 1"
    assert p.calls[0]["tools"] == ["submit_result"]


async def test_empty_model_output_becomes_partial(make_ctx):
    p = FakeProvider([fake.text(""), fake.text("")])
    r = await _run(p, make_ctx())
    assert r.status == "partial" and r.stop_reason == "empty" and r.text
