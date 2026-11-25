"""The Anthropic SDK ReAct engine, run through the REAL tool runner of the anthropic SDK with an in-process fake network
(no AWS, no API key). Same expectations as the own loop: tool results go back, the finish tool stops the run, budgets give
partial answers, tool errors are readable, calls are traced."""
from __future__ import annotations

import json

try:  # anthropic 2.x uses the httpx2 package; older ones use httpx
    import httpx2 as httpx
except ImportError:  # pragma: no cover
    import httpx

from finchat_agents.llm.claude_api import ClaudeApiProvider
from finchat_agents.llm.types import Message, ModelHandle, ToolSpec
from finchat_agents.runtime.agent import Agent
from finchat_agents.runtime.sdk_loop import run_loop_sdk
from finchat_agents.runtime.tools import RunContext, ToolError, tool
from finchat_agents.tracing import MemorySink, Tracer

from .conftest import add_tool, fake_sql_tool

FINISH = ToolSpec(name="submit_result", description="Finish.", input_schema={
    "type": "object", "properties": {"answer": {"type": "string"}}, "required": ["answer"]})


def _msg(content, stop="tool_use", usage=None):
    return {"id": "msg_1", "type": "message", "role": "assistant", "model": "claude-test", "content": content,
            "stop_reason": stop, "stop_sequence": None, "usage": usage or {"input_tokens": 10, "output_tokens": 5}}


def _use(name, args, call_id="tu_1"):
    return {"type": "tool_use", "id": call_id, "name": name, "input": args}


def _text(t):
    return {"type": "text", "text": t}


def make_llm(responses, bodies=None, status=200):
    queue = list(responses)

    def handler(request: httpx.Request) -> httpx.Response:
        if bodies is not None:
            bodies.append(json.loads(request.content))
        if status != 200:
            return httpx.Response(status, json={"type": "error", "error": {"type": "invalid_request_error", "message": "bad"}})
        return httpx.Response(200, json=queue.pop(0) if len(queue) > 1 else queue[0])

    from anthropic import AsyncAnthropic

    client = AsyncAnthropic(api_key="sk-test-not-real", http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
                            max_retries=0)
    return ModelHandle(ClaudeApiProvider("sk-test-not-real", client=client), "claude-test")


async def _run(llm, ctx, tools=(), max_steps=15, **kw):
    return await run_loop_sdk(llm=llm, system="sys", messages=[Message.user("q")], tools=list(tools), ctx=ctx, agent="test",
                              max_steps=max_steps, **kw)


async def test_tool_call_then_final_answer_through_the_real_runner(make_ctx):
    bodies = []
    llm = make_llm([_msg([_use("add", {"a": 2, "b": 2})]), _msg([_text("The sum is 4.")], "end_turn")], bodies)
    r = await _run(llm, make_ctx(), [add_tool])
    assert (r.status, r.text, r.stop_reason, r.steps, r.llm_calls) == ("final", "The sum is 4.", "final", 2, 2)
    assert [t.name for t in r.tool_calls] == ["add"] and r.tool_calls[0].raw == {"sum": 4} and r.usage.input_tokens == 20
    second = bodies[1]["messages"][-1]
    assert second["role"] == "user" and second["content"][0]["type"] == "tool_result" and '"sum": 4' in second["content"][0]["content"]
    assert bodies[0]["system"][0]["cache_control"] == {"type": "ephemeral"}
    assert bodies[0]["tools"][-1]["cache_control"] == {"type": "ephemeral"} and "temperature" not in bodies[0]
    assert [m["role"] for m in [Message(role=m.role, content=[]).model_dump() for m in r.messages]] == ["user", "assistant", "user", "assistant"]


async def test_finish_tool_stops_before_anything_else_runs(make_ctx):
    ran = []

    @tool("noop", "n", {"type": "object", "properties": {}})
    async def noop(args, tctx):
        ran.append(1)
        return "x"

    llm = make_llm([_msg([_use("noop", {}, "a"), _use("submit_result", {"answer": "Done."}, "b")])])
    r = await _run(llm, make_ctx(), [noop], finish_tool=FINISH)
    assert r.stop_reason == "finish_tool" and r.data == {"answer": "Done."} and r.text == "Done." and ran == []
    assert r.llm_calls == 1


async def test_tool_errors_are_readable_and_the_loop_continues(make_ctx):
    bodies = []

    @tool("strict", "s", {"type": "object", "properties": {}})
    async def strict(args, tctx):
        raise ToolError("Access denied: not your table.")

    llm = make_llm([_msg([_use("strict", {})]), _msg([_text("I cannot access that.")], "end_turn")], bodies)
    r = await _run(llm, make_ctx(), [strict])
    assert r.status == "final" and r.tool_calls[0].is_error and "Access denied" in r.tool_calls[0].output
    block = bodies[1]["messages"][-1]["content"][0]
    assert block["type"] == "tool_result" and block.get("is_error") is True and "Access denied" in json.dumps(block)


async def test_step_limit_and_sql_budget_give_partial_or_error_results(make_ctx):
    llm = make_llm([_msg([_use("add", {"a": 1, "b": 1})])])  # the model never stops calling tools
    r = await _run(llm, make_ctx(), [add_tool], max_steps=3)
    assert r.status == "partial" and r.stop_reason == "max_steps" and r.llm_calls == 3 and "Partial answer" in r.text
    ctx = make_ctx(max_sql_calls=1)
    llm = make_llm([_msg([_use("run_sql", {}, "1")]), _msg([_use("run_sql", {}, "2")]), _msg([_text("done")], "end_turn")])
    r = await _run(llm, ctx, [fake_sql_tool()])
    assert [t.is_error for t in r.tool_calls] == [False, True] and "budget" in r.tool_calls[1].output.lower()


async def test_api_error_gives_a_partial_answer_not_a_crash(make_ctx):
    r = await _run(make_llm([_msg([_text("x")])], status=400), make_ctx(), [add_tool])
    assert r.status == "partial" and r.stop_reason == "model_error"


async def test_initial_route_call_is_continued_by_the_runner(make_ctx):
    from finchat_agents.llm import fake

    bodies = []
    llm = make_llm([_msg([_text("The sum is 4.")], "end_turn")], bodies)
    initial = fake.tool_call("add", {"a": 2, "b": 2}, call_id="c1")
    r = await _run(llm, make_ctx(), [add_tool], initial=initial)
    assert r.status == "final" and r.llm_calls == 2 and [t.name for t in r.tool_calls] == ["add"]
    assert bodies[0]["messages"][-1]["content"][0]["tool_use_id"] == "c1"  # the route call's tool result was sent first


async def test_agent_uses_the_sdk_engine_when_selected_and_traces_every_call(make_ctx):
    sink = MemorySink()
    ctx = RunContext(tracer=Tracer([sink], message_id="m"), extras={"react_engine": "anthropic_sdk"})
    llm = make_llm([_msg([_use("add", {"a": 1, "b": 2})]), _msg([_text("3")], "end_turn")])
    result = await Agent("a", "sys", llm, [add_tool], max_steps=5).run("q", ctx)
    assert result.answer == "3" and result.llm_calls == 2
    start = next(e for e in sink.events if e.type == "agent_start")
    assert start.payload["engine"] == "anthropic_sdk"
    calls = [e for e in sink.events if e.type == "llm_call"]
    assert len(calls) == 2 and calls[0].input_tokens == 10 and ctx.counters.llm_calls == 2
    assert any(e.type == "tool_call" and e.name == "add" for e in sink.events)


async def test_models_without_an_sdk_client_keep_using_the_own_loop(make_ctx):
    from finchat_agents.llm import fake
    from finchat_agents.llm.fake import FakeProvider

    sink = MemorySink()
    ctx = RunContext(tracer=Tracer([sink], message_id="m"), extras={"react_engine": "anthropic_sdk"})
    result = await Agent("a", "sys", ModelHandle(FakeProvider([fake.text("ok")]), "fake"), []).run("q", ctx)
    assert result.answer == "ok"
    assert next(e for e in sink.events if e.type == "agent_start").payload["engine"] == "own"
