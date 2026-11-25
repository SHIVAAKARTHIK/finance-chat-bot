from __future__ import annotations

import json

from finchat_agents.llm import fake
from finchat_agents.llm.fake import FakeProvider
from finchat_agents.runtime.agent import Agent
from finchat_agents.runtime.tools import Budget, RunContext
from finchat_agents.tracing import JsonlFileSink, MemorySink, Tracer

from .conftest import add_tool, handle


async def test_event_order_single_agent(make_ctx, sink):
    p = FakeProvider([fake.tool_call("add", {"a": 2, "b": 2}), fake.text("4")])
    await Agent("math", "s", handle(p), [add_tool]).run("2+2", make_ctx())
    assert [(e.type, e.agent, e.step) for e in sink.events] == [
        ("agent_start", "math", 0),
        ("llm_call", "math", 1),
        ("tool_call", "math", 1),
        ("llm_call", "math", 2),
        ("agent_end", "math", 2),
    ]
    assert {e.run_id for e in sink.events} == {sink.events[0].run_id}
    assert all(e.message_id == "msg-1" for e in sink.events)
    llm = sink.events[1]
    assert llm.name == "fake-model" and llm.input_tokens == 10 and llm.duration_ms is not None
    assert sink.events[2].name == "add" and '"sum": 4' in sink.events[2].payload["output"]


async def test_event_order_nested_agents(make_ctx, sink):
    child = Agent("catalog", "c", handle(FakeProvider([fake.text("tables")])))
    sup = Agent("supervisor", "s", handle(FakeProvider([fake.tool_call("ask_catalog", {"task": "t"}), fake.text("done")])),
                [child.as_tool()])
    await sup.run("q", make_ctx())
    assert [(e.type, e.agent) for e in sink.events] == [
        ("agent_start", "supervisor"),
        ("llm_call", "supervisor"),
        ("agent_start", "catalog"),
        ("llm_call", "catalog"),
        ("agent_end", "catalog"),
        ("tool_call", "supervisor"),
        ("llm_call", "supervisor"),
        ("agent_end", "supervisor"),
    ]
    tool_event = sink.events[5]
    assert sink.events[2].payload["parent_call_id"] == tool_event.payload["call_id"]


async def test_budget_stop_event(make_ctx, sink):
    p = FakeProvider([fake.tool_call("add", {"a": 1, "b": 1}), fake.text("partial")])
    await Agent("a", "s", handle(p), [add_tool], max_steps=1).run("q", make_ctx())
    stops = [e for e in sink.events if e.type == "budget_stop"]
    assert len(stops) == 1 and stops[0].payload["reason"] == "max_steps"


async def test_jsonl_sink_writes_lines(tmp_path):
    path = tmp_path / "traces" / "run.jsonl"
    tracer = Tracer([JsonlFileSink(path)], run_id="r1")
    await Agent("a", "s", handle(FakeProvider([fake.text("hi")]))).run("q", RunContext(tracer=tracer, budget=Budget()))
    lines = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
    assert [line["type"] for line in lines] == ["agent_start", "llm_call", "agent_end"]
    assert all(line["run_id"] == "r1" for line in lines)


async def test_broken_sink_does_not_break_the_run():
    class Broken:
        async def write(self, event):
            raise OSError("disk full")

    good = MemorySink()
    ctx = RunContext(tracer=Tracer([Broken(), good]), budget=Budget())
    r = await Agent("a", "s", handle(FakeProvider([fake.text("hi")]))).run("q", ctx)
    assert r.answer == "hi" and len(good.events) == 3
