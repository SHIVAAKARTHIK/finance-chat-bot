from __future__ import annotations

import json

from finchat_agents.llm import fake
from finchat_agents.llm.fake import FakeProvider
from finchat_agents.runtime.agent import Agent, AgentResult

from .conftest import add_tool, fake_sql_tool, handle


async def test_agent_run_returns_structured_result(make_ctx):
    a = Agent("math", "You add.", handle(FakeProvider([fake.tool_call("add", {"a": 2, "b": 2}), fake.text("4")])), [add_tool])
    r = await a.run("2+2?", make_ctx())
    assert isinstance(r, AgentResult)
    assert (r.agent, r.status, r.answer, r.llm_calls) == ("math", "final", "4", 2)


async def test_agent_as_tool_fresh_context_per_call(make_ctx):
    child_p = FakeProvider([fake.text("child answer 1"), fake.text("child answer 2")])
    child = Agent("catalog", "Find tables.", handle(child_p))
    sup_p = FakeProvider([
        fake.tool_call("ask_catalog", {"task": "find adra tables"}),
        fake.tool_call("ask_catalog", {"task": "find fynapse tables", "context": "adra done"}),
        fake.text("final"),
    ])
    sup = Agent("supervisor", "Route.", handle(sup_p), [child.as_tool()])
    r = await sup.run("question", make_ctx())

    assert r.status == "final" and r.answer == "final"
    # each child call starts with exactly one user message (no memory of the earlier call)
    assert [len(c["messages"]) for c in child_p.calls] == [1, 1]
    assert child_p.calls[1]["messages"][0].text.startswith("find fynapse tables")
    assert "<context>\nadra done\n</context>" in child_p.calls[1]["messages"][0].text
    # the supervisor sees the structured result, not the child's transcript
    seen = json.loads(sup_p.calls[1]["messages"][-1].content[0].content)
    assert seen == {"agent": "catalog", "status": "final", "answer": "child answer 1"}
    # callers can still reach the full child result
    assert isinstance(r.tool_calls[0].raw, AgentResult)
    assert sup.as_tool().spec.input_schema["required"] == ["task"]


async def test_agent_with_output_schema_returns_data(make_ctx):
    schema = {"type": "object", "properties": {"answer": {"type": "string"}, "sql": {"type": "string"}}, "required": ["answer"]}
    p = FakeProvider([fake.tool_call("submit_result", {"answer": "97", "sql": "SELECT COUNT(*) ..."})])
    a = Agent("sql", "Write SQL.", handle(p), output_schema=schema)
    r = await a.run("count rows", make_ctx())
    assert r.data == {"answer": "97", "sql": "SELECT COUNT(*) ..."} and r.answer == "97"
    assert r.for_model()["data"]["sql"].startswith("SELECT")


async def test_nested_agents_share_sql_budget(make_ctx):
    sql_p = FakeProvider([
        fake.tool_call("run_sql", {"sql": "a"}), fake.text("first"),
        fake.tool_call("run_sql", {"sql": "b"}), fake.text("second"),
    ])
    sql_agent = Agent("sql", "SQL.", handle(sql_p), [fake_sql_tool()])
    sup_p = FakeProvider([
        fake.tool_call("ask_sql", {"task": "q1"}), fake.tool_call("ask_sql", {"task": "q2"}), fake.text("done"),
    ])
    ctx = make_ctx(max_sql_calls=1)
    await Agent("supervisor", "s", handle(sup_p), [sql_agent.as_tool()]).run("q", ctx)
    assert ctx.counters.sql_calls == 1
    second_child_result = sql_p.calls[3]["messages"][-1].content[0]
    assert second_child_result.is_error and "SQL call budget reached" in second_child_result.content


async def test_partial_child_is_reported_to_parent(make_ctx):
    child = Agent("sql", "s", handle(FakeProvider([fake.tool_call("add", {"a": 1, "b": 1}), fake.text("got 2, missing rest")])),
                  [add_tool], max_steps=1)
    sup_p = FakeProvider([fake.tool_call("ask_sql", {"task": "q"}), fake.text("done")])
    await Agent("supervisor", "s", handle(sup_p), [child.as_tool()]).run("q", make_ctx())
    seen = json.loads(sup_p.calls[1]["messages"][-1].content[0].content)
    assert seen["status"] == "partial" and seen["stop_reason"] == "max_steps"


# ---------------------------------------------------------------- structured output written as plain JSON text

def test_recover_structured_accepts_plain_fenced_and_surrounded_json():
    from finchat_agents.runtime.agent import recover_structured

    schema = {"type": "object", "properties": {"answer": {}, "how_calculated": {}}, "required": ["answer", "how_calculated"]}
    raw = '{"answer": "Done.", "how_calculated": "From the records.", "suggestions": ["Show by entity"]}'
    assert recover_structured(raw, schema)["answer"] == "Done."
    assert recover_structured("```json\n" + raw + "\n```", schema)["suggestions"] == ["Show by entity"]
    assert recover_structured("Here is the result:\n" + raw + "\nThanks", schema)["how_calculated"] == "From the records."
    assert recover_structured('{"answer": "only one key"}', schema) is None  # required keys missing
    assert recover_structured("Just a sentence with {braces}.", schema) is None
    assert recover_structured("[1, 2]", schema) is None and recover_structured("", schema) is None and recover_structured(raw, None) is None


async def test_writer_that_answers_in_json_text_never_shows_the_json_to_the_user():
    import json

    from finchat_agents.agents.answer import AnswerWriter
    from finchat_agents.agents.supervisor import SupervisorDraft
    from finchat_agents.llm import fake
    from finchat_agents.llm.fake import FakeProvider
    from finchat_agents.llm.types import ModelHandle
    from finchat_agents.runtime.tools import RunContext
    from finchat_agents.tracing import MemorySink, Tracer

    raw = json.dumps({"answer": "I could not find commission figures for UK07.", "how_calculated": "Commission records for the latest period.",
                      "suggestions": ["Show commission for entity 100"]})
    writer = AnswerWriter(ModelHandle(FakeProvider([fake.text(raw)]), "gptoss-fake"))  # plain text, no submit_result call
    draft = SupervisorDraft(status="answered", answer="none found", how_calculated="", result_ids=[])
    out = await writer.write("What is the commission of UK07?", draft, RunContext(tracer=Tracer([MemorySink()])), check_numbers=False)
    assert out.answer == "I could not find commission figures for UK07." and "{" not in out.answer
    assert out.how_calculated == "Commission records for the latest period." and out.suggestions == ["Show commission for entity 100"]


def test_writer_prompt_requires_business_language_questions_and_the_tool():
    from finchat_agents.agents.specialists import load_prompt

    p = " ".join(load_prompt("answer_writer").split())  # one line: the prompt wraps its lines
    for needle in ("not an engineer", "I could not find", "follow-up QUESTIONS", "Never write the result as JSON text"):
        assert needle in p, needle


async def test_number_check_rewrite_is_logged_with_the_numbers_and_their_context():
    import json

    from finchat_agents.agents.answer import AnswerWriter
    from finchat_agents.agents.supervisor import SupervisorDraft
    from finchat_agents.llm import fake
    from finchat_agents.llm.fake import FakeProvider
    from finchat_agents.llm.types import ModelHandle
    from finchat_agents.runtime.tools import RunContext
    from finchat_agents.tracing import MemorySink, Tracer

    bad = json.dumps({"answer": "Revenue grew by 987654 last year.", "how_calculated": "Summed."})
    good = json.dumps({"answer": "I do not have that figure.", "how_calculated": "Summed."})
    sink = MemorySink()
    writer = AnswerWriter(ModelHandle(FakeProvider([fake.text(bad), fake.text(good)]), "gptoss-fake"))
    draft = SupervisorDraft(status="answered", answer="x", how_calculated="", result_ids=[])
    out = await writer.write("How did revenue change?", draft, RunContext(tracer=Tracer([sink])))
    assert out.rewrites == 1
    ev = [e for e in sink.events if getattr(e, "name", None) == "number_check_rewrite"]
    assert len(ev) == 1 and "987654" in ev[0].payload["input"] and "Revenue grew" in ev[0].payload["output"]
