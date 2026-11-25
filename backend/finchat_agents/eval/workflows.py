"""Run the sample workflows end to end (live) and check per-step status and files in code.

    cd backend
    $env:RUN_LIVE="1"; .venv\\Scripts\\python -m finchat_agents.eval.workflows [--only wf01_...]

Writes eval_reports/workflows_<time>.md.
"""
from __future__ import annotations

import argparse
import asyncio
import datetime as dt
import os
import re
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field

from ..config import PACKAGE_DIR

WORKFLOWS_FILE = Path(__file__).resolve().parent / "workflows.yaml"
REPORT_DIR = PACKAGE_DIR / "eval_reports"
STEP_LINE = re.compile(r"^\s*(\d+)\. .*\((done|done, with a caveat|not done)\)", re.M)


class WorkflowCase(BaseModel):
    id: str
    message: str
    min_steps: int = 1
    files: list[str] = Field(default_factory=list)
    must_not_do: list[int] = Field(default_factory=list)


class WorkflowCheck(BaseModel):
    ok: bool
    problems: list[str] = Field(default_factory=list)
    steps: dict[int, str] = Field(default_factory=dict)


def load_workflows(path: Path = WORKFLOWS_FILE) -> list[WorkflowCase]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return [WorkflowCase(**w) for w in data.get("workflows", [])]


def _file_opens(path: str) -> bool:
    p = Path(path)
    if not p.exists():
        return False
    if p.suffix == ".xlsx":
        from openpyxl import load_workbook

        try:
            load_workbook(p, read_only=True).close()
            return True
        except Exception:
            return False
    return p.read_text(encoding="utf-8").strip() != ""


def check_workflow(case: WorkflowCase, status: str, answer: str, files: list[dict[str, str]],
                   local_paths: list[str] | None = None) -> WorkflowCheck:
    """`files`: the envelope entries (name, download path); `local_paths`: where they were saved on the server."""
    problems = []
    steps = {int(n): s for n, s in STEP_LINE.findall(answer)}
    if status == "failed":
        problems.append("the answer failed")
    if len(steps) < case.min_steps:
        problems.append(f"{len(steps)} step(s) reported with a status, expected at least {case.min_steps}")
    for n in case.must_not_do:
        if steps.get(n) != "not done":
            problems.append(f"step {n} must be reported as not done (got {steps.get(n, 'nothing')})")
    for n, s in steps.items():
        if s == "not done" and n not in case.must_not_do:
            problems.append(f"step {n} was not done")
    exts = [Path(f["name"]).suffix.lstrip(".") for f in files]
    for ext in case.files:
        if ext not in exts:
            problems.append(f"no .{ext} file was saved")
    for p in local_paths or []:
        if not _file_opens(p):
            problems.append(f"file {Path(p).name} does not open")
    for f in files:
        if not str(f.get("path", "")).startswith("/v3/files/"):
            problems.append(f"file {f['name']} has no download URL")
    if re.search(r"\b(sent|emailed|shared) (it|the|this|them)\b", answer, re.I) and case.must_not_do:
        problems.append("the answer claims something was sent or shared")
    return WorkflowCheck(ok=not problems, problems=problems, steps=steps)


async def run_all(cases: list[WorkflowCase]) -> list[dict[str, Any]]:
    from .scorecard import build_live_orchestrator

    orch, user = build_live_orchestrator()
    out = []
    for case in cases:
        env = await orch.answer(case.message, user)
        chk = check_workflow(case, env.status, env.answer, env.files, env.debug.local_files)
        print(f"{case.id}: {'OK' if chk.ok else 'FAIL'} ({env.debug.mode}, {round(env.debug.latency_ms / 1000, 1)}s)")
        out.append({"case": case, "env": env, "check": chk})
    return out


def to_markdown(results: list[dict[str, Any]]) -> str:
    ok = sum(r["check"].ok for r in results)
    lines = [f"# Workflow run {dt.datetime.now():%Y-%m-%d %H:%M}", "", f"{ok} of {len(results)} workflows passed.", "",
             "| Workflow | Result | Status | Steps | Files | Latency (s) | LLM calls | Problems |", "|---|---|---|---|---|---|---|---|"]
    for r in results:
        env, chk = r["env"], r["check"]
        lines.append(f"| {r['case'].id} | {'pass' if chk.ok else 'FAIL'} | {env.status} | "
                     f"{', '.join(f'{k}:{v}' for k, v in sorted(chk.steps.items()))} | {', '.join(f['name'] for f in env.files)} | "
                     f"{round(env.debug.latency_ms / 1000, 1)} | {env.debug.llm_calls} | {'; '.join(chk.problems)} |")
    lines += ["", "## Answers", ""]
    for r in results:
        lines += [f"### {r['case'].id}", "", "**Request:**", "", r["case"].message.strip(), "", "**Answer:**", "", r["env"].answer, ""]
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", nargs="*", default=[])
    args = ap.parse_args()
    if os.getenv("RUN_LIVE") != "1":
        raise SystemExit("The workflow run calls live services: set RUN_LIVE=1 first.")
    cases = [c for c in load_workflows() if not args.only or c.id in args.only]
    results = asyncio.run(run_all(cases))
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORT_DIR / f"workflows_{dt.datetime.now():%Y%m%d_%H%M%S}.md"
    path.write_text(to_markdown(results), encoding="utf-8")
    print(f"report: {path}")


if __name__ == "__main__":
    main()
