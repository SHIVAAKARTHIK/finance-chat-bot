"""Task 06: analyst agent, action agent (export_excel, save_report), workflows with per-step status."""
from __future__ import annotations

from pathlib import Path

import pytest
from openpyxl import load_workbook

from finchat_agents.access import Role, UserAccess
from finchat_agents.agents.orchestrator import AnswerDebug, format_steps
from finchat_agents.agents.supervisor import SupervisorDraft, WorkflowStep
from finchat_agents.eval.workflows import WorkflowCase, check_workflow, load_workflows
from finchat_agents.knowledge.loader import Knowledge
from finchat_agents.llm import fake
from finchat_agents.runtime.tools import Budget, RunContext, ToolContext, ToolError
from finchat_agents.storage.records import intent_of
from finchat_agents.tools.actions import FILES_KEY, QUESTION_KEY, make_action_tools
from finchat_agents.tools.run_sql import SqlResult, register_result
from finchat_agents.tracing import MemorySink, Tracer

from .test_agents import ALL, COUNT_SQL, make_orch, route, writer

PLAN = ["Count the account reconciliations", "Email the result to the finance team", "Export the count to Excel"]


@pytest.fixture(scope="module")
def kb() -> Knowledge:
    return Knowledge.load()


async def test_workflow_end_to_end_with_plan_files_and_not_done_step(kb, tmp_path):
    sql_script = [
        fake.tool_calls([route("workflow", "count, email, export"), ("record_plan", {"steps": PLAN})]),
        fake.tool_call("ask_sql_agent", {"task": "Count all account reconciliations"}),
        fake.tool_call("run_sql", {"sql": COUNT_SQL}),                                                       # sql agent
        fake.tool_call("submit_result", {"answer": "97", "status": "ok", "result_ids": ["r1"], "explanation": "Counted rows."}),
        fake.tool_call("ask_action_agent", {"task": "Export result r1 to Excel, title 'Reconciliation count'"}),
        fake.tool_call("export_excel", {"title": "Reconciliation count", "tables": [{"result_id": "r1", "title": "Count"}]}),
        fake.tool_call("submit_result", {"answer": "Saved the Excel file.", "status": "ok"}),                 # action agent
        fake.tool_call("submit_result", {
            "status": "answered", "answer": "There are 97 account reconciliations.", "result_ids": ["r1"],
            "steps": [
                {"step": PLAN[0], "status": "done", "detail": "97 account reconciliations"},
                {"step": PLAN[1], "status": "not_done", "detail": "Sending email is not allowed; nothing was sent."},
                {"step": PLAN[2], "status": "done", "detail": "Saved the Excel file"},
            ]}),
    ]
    orch, sql_p, resp_p, server, sink = make_orch(kb, sql_script, [writer("There are 97 account reconciliations.")],
                                                  output_dir=str(tmp_path))
    env = await orch.answer("1. Count reconciliations 2. Email the result 3. Export to Excel", ALL)
    assert env.debug.classification == "workflow" and env.debug.mode == "react"
    assert env.status == "partial"  # one step not done
    assert "Steps:\n1. Count the account reconciliations (done): 97 account reconciliations" in env.answer
    assert "2. Email the result to the finance team (not done): Sending email is not allowed" in env.answer
    assert len(env.files) == 1 and env.files[0]["name"].endswith(".xlsx")
    assert env.files[0]["path"] == f"/v3/files/{env.conversation_id}/{env.files[0]['name']}"  # URL, not a server path
    local = env.debug.local_files[0]
    wb = load_workbook(local, read_only=True)
    assert wb.sheetnames == ["Count"] and list(wb["Count"].iter_rows(values_only=True)) == [("n",), (97,)]
    assert Path(local).parent.name == env.conversation_id  # saved per conversation
    plan_events = [e for e in sink.events if e.type == "plan"]
    assert plan_events and plan_events[0].payload["steps"] == PLAN
    case = WorkflowCase(id="t", message="m", min_steps=3, files=["xlsx"], must_not_do=[2])
    assert check_workflow(case, env.status, env.answer, env.files, env.debug.local_files).ok
    assert "files_saved" in resp_p.calls[0]["messages"][0].text  # the writer was told about the file
    assert "record_plan" in sql_p.calls[0]["tools"] and "ask_analyst_agent" in sql_p.calls[0]["tools"]


def action_ctx(tmp_path, message_id="msg-1") -> tuple[ToolContext, dict]:
    run = RunContext(tracer=Tracer([MemorySink()], message_id=message_id), budget=Budget(), user=ALL)
    run.extras["conversation_id"] = "conv-1"
    run.extras[QUESTION_KEY] = "How many reconciliations per status in Feb 25?"
    register_result(run, SqlResult(columns=["ACCOUNT_STATUS", "n"], rows=[["Approved", 7], ["Not prepared", 24], ["Prepared", 9]], row_count=3))
    tools = {t.name: t for t in make_action_tools(tmp_path)}
    return ToolContext(run=run, agent="action_agent", step=1, call_id="c1"), tools


async def test_export_is_idempotent_on_retry(tmp_path):
    tctx, tools = action_ctx(tmp_path)
    args = {"title": "Status counts Feb 25", "tables": [{"result_id": "r1", "title": "By status"}]}
    first = await tools["export_excel"].handler(args, tctx)
    second = await tools["export_excel"].handler(args, tctx)  # retried step
    assert first == second and len(tctx.run.extras[FILES_KEY]) == 1
    assert len(list((tmp_path / "conv-1").glob("*.xlsx"))) == 1
    assert len(list((tmp_path / "conv-1").glob("*.meta.json"))) == 1
    other, _ = action_ctx(tmp_path, message_id="msg-2")  # a new question gets its own file
    await tools["export_excel"].handler(args, other)
    assert len(list((tmp_path / "conv-1").glob("*.xlsx"))) == 2
    with pytest.raises(ToolError, match="Unknown result_id"):
        await tools["export_excel"].handler({"title": "x", "tables": [{"result_id": "r9"}]}, tctx)
    with pytest.raises(ToolError, match="result_id"):
        await tools["export_excel"].handler({"title": "x", "tables": [{"rows": [[1, 2]]}]}, tctx)  # no typed rows


async def test_save_report_checks_numbers_and_writes_files(tmp_path):
    tctx, tools = action_ctx(tmp_path)
    bad = {"title": "Feb 25 status", "sections": [{"heading": "Summary", "text": "There are 45 accounts.", "result_ids": ["r1"]}]}
    with pytest.raises(ToolError, match="numbers that are not in this question's results: 45"):
        await tools["save_report"].handler(bad, tctx)
    good = {"title": "Feb 25 status", "sections": [
        {"heading": "Summary", "text": "24 accounts are not prepared, 7 are approved and 9 are prepared (3 statuses).", "result_ids": ["r1"]}]}
    out = await tools["save_report"].handler(good, tctx)
    assert len(out["files"]) == 2
    md = next(Path(f["path"]) for f in tctx.run.extras[FILES_KEY] if f["path"].endswith(".md"))
    text = md.read_text(encoding="utf-8")
    assert text.startswith("# Feb 25 status") and "| ACCOUNT_STATUS | n |" in text and "| Not prepared | 24 |" in text


async def test_analyst_runs_two_queries_and_calculates(kb, tmp_path):
    sql_script = [
        fake.tool_call("ask_sql_agent", {"task": "count reconciliations Feb 25"}),
        fake.tool_call("run_sql", {"sql": COUNT_SQL}),
        fake.tool_call("submit_result", {"answer": "97", "status": "ok", "result_ids": ["r1"], "explanation": "e"}),
        fake.tool_call("ask_sql_agent", {"task": "count reconciliations Oct 26"}),
        fake.tool_call("run_sql", {"sql": COUNT_SQL}),
        fake.tool_call("submit_result", {"answer": "97", "status": "ok", "result_ids": ["r2"], "explanation": "e"}),
        fake.tool_call("calculate", {"expression": "pct_change(r1[0]['n'], r2[0]['n'])"}),
        fake.tool_call("submit_result", {"answer": "No change: 97 in both periods (0% change).", "status": "ok",
                                         "steps": ["Counted Feb 25", "Counted Oct 26", "Computed the change"],
                                         "result_ids": ["r1", "r2"]}),
    ]
    orch, sql_p, *_ = make_orch(kb, sql_script, [], output_dir=str(tmp_path))
    ctx = RunContext(tracer=Tracer([MemorySink()]), budget=Budget(), user=ALL)
    r = await orch.analyst_agent.run("Compare reconciliation counts between Feb 25 and Oct 26", ctx)
    assert r.data["status"] == "ok" and r.data["result_ids"] == ["r1", "r2"] and len(r.data["steps"]) == 3
    assert ctx.counters.sql_calls == 2 and ctx.extras["calc_results"] == [0.0]
    assert [t for t in sql_p.calls[0]["tools"]] == ["ask_sql_agent", "calculate", "get_glossary", "submit_result"]


def test_format_steps_reports_every_planned_step():
    draft = SupervisorDraft(steps=[WorkflowStep(step="Count", status="done", detail="97")])
    text = format_steps(draft, ["Count", "Export"])
    assert text == "Steps:\n1. Count (done): 97\n2. Export (not done): no result was reported for this step"
    assert format_steps(SupervisorDraft(), None) == ""


def test_workflow_intent_and_sample_workflows():
    assert intent_of(AnswerDebug(classification="workflow", sql=["s"])) == "workflow"
    cases = load_workflows()
    assert len(cases) == 10 and {c.id for c in cases if c.must_not_do} == {"wf08_send_is_not_allowed", "wf09_write_is_not_allowed"}
    ok = WorkflowCase(id="x", message="m", min_steps=2, files=[])
    assert not check_workflow(ok, "answered", "Steps:\n1. A (done)", []).ok  # too few steps
    assert check_workflow(ok, "answered", "Steps:\n1. A (done)\n2. B (done, with a caveat): c", []).ok
