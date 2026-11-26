"""Run question-bank cases through Orchestrator.answer() and write a scorecard to eval_reports/.

Live only (real Bedrock models and the Databricks MCP server):

    $env:RUN_LIVE="1"; ..\\.venv\\Scripts\\python -m finchat_agents.eval.scorecard --banks adra fynapse
    ... --limit 5            # first 5 cases only
    ... --no-paraphrases     # main questions only
    ... --repeat 3 --limit 5 # consistency: each case asked 3 times must agree

Each case gets its own trace file (JSON lines) under eval_reports/traces/<run>/.
"""
from __future__ import annotations

import argparse
import asyncio
import datetime as dt
import json
import os
import statistics
from collections import Counter
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from ..config import PACKAGE_DIR
from .scoring import EvalCase, Score, load_cases, score

BANKS = {
    "adra": ["question_bank_adra_part1.yaml", "question_bank_adra_part2.yaml"],
    "fynapse": ["question_bank_fynapse.yaml"],
}
BANK_DIR = PACKAGE_DIR / "reference" / "question_bank"
REPORT_DIR = PACKAGE_DIR / "eval_reports"


class CaseResult(BaseModel):
    case: EvalCase
    score: Score
    status: str
    mode: str
    latency_s: float
    llm_calls: int
    sql_calls: int
    answer: str
    how_calculated: str = ""
    tables: list[dict[str, Any]] = Field(default_factory=list)
    sql: list[str] = Field(default_factory=list)
    trace_file: str = ""
    run: int = 1


async def run_case(orchestrator: Any, user: Any, case: EvalCase, trace_dir: Path, run: int = 1) -> CaseResult:
    from ..tracing import JsonlFileSink

    trace_file = trace_dir / f"{case.id.replace('~', '_')}_{run}.jsonl"
    try:
        env = await orchestrator.answer(case.question, user, extra_sinks=[JsonlFileSink(trace_file)])
    except Exception as exc:  # the orchestrator should never raise; record it as an error
        return CaseResult(case=case, score=Score(category="error", note=str(exc)[:300]), status="failed", mode="failed",
                          latency_s=0, llm_calls=0, sql_calls=0, answer="", trace_file=str(trace_file), run=run)
    sc = score(case, env.status, env.answer, env.tables)
    return CaseResult(
        case=case, score=sc, status=env.status, mode=env.debug.mode, latency_s=round(env.debug.latency_ms / 1000, 2),
        llm_calls=env.debug.llm_calls, sql_calls=env.debug.sql_calls, answer=env.answer,
        how_calculated=env.how_calculated, tables=env.tables, sql=env.debug.sql, trace_file=str(trace_file), run=run,
    )


def summarize(results: list[CaseResult]) -> dict[str, Any]:
    first = [r for r in results if r.run == 1]
    cats = Counter(r.score.category for r in first)
    by_mode: dict[str, dict[str, Any]] = {}
    for mode in sorted({r.mode for r in first}):
        rs = [r for r in first if r.mode == mode]
        by_mode[mode] = {
            "cases": len(rs),
            "avg_llm_calls": round(statistics.mean(r.llm_calls for r in rs), 2),
            "avg_latency_s": round(statistics.mean(r.latency_s for r in rs), 2),
            "correct": sum(r.score.category == "correct" for r in rs),
        }
    consistency = {}
    runs = {r.run for r in results}
    if len(runs) > 1:
        for cid in sorted({r.case.id for r in results}):
            rs = [r for r in results if r.case.id == cid]
            consistency[cid] = len({(r.score.category, tuple(r.score.found_numbers)) for r in rs}) == 1
    return {
        "cases": len(first),
        "categories": {c: cats.get(c, 0) for c in ("correct", "partial", "could_not_answer", "wrong", "error")},
        "by_mode": by_mode,
        "p50_latency_s": round(statistics.median(r.latency_s for r in first), 2) if first else 0,
        "max_latency_s": max((r.latency_s for r in first), default=0),
        "consistency": consistency,
    }


def to_markdown(results: list[CaseResult], summary: dict[str, Any], title: str) -> str:
    c = summary["categories"]
    lines = [
        f"# {title}", "",
        f"Cases: {summary['cases']} | correct {c['correct']} | partial {c['partial']} | could not answer "
        f"{c['could_not_answer']} | **wrong {c['wrong']}** | error {c['error']}",
        f"Latency p50 {summary['p50_latency_s']} s, max {summary['max_latency_s']} s", "",
        "## By mode", "", "| Mode | Cases | Correct | Avg LLM calls | Avg latency (s) |", "|---|---|---|---|---|",
    ]
    for mode, m in summary["by_mode"].items():
        lines.append(f"| {mode} | {m['cases']} | {m['correct']} | {m['avg_llm_calls']} | {m['avg_latency_s']} |")
    if summary["consistency"]:
        bad = [k for k, ok in summary["consistency"].items() if not ok]
        lines += ["", f"## Consistency\n\n{len(summary['consistency']) - len(bad)} of {len(summary['consistency'])} cases agree across runs."
                  + (f" Disagree: {', '.join(bad)}" if bad else "")]
    lines += ["", "## Cases", "", "| Case | Category | Status | Mode | Latency (s) | LLM calls | Missing |", "|---|---|---|---|---|---|---|"]
    for r in (r for r in results if r.run == 1):
        missing = ", ".join(r.score.missing_numbers + r.score.missing_text) or r.score.note
        lines.append(f"| {r.case.id} | {r.score.category} | {r.status} | {r.mode} | {r.latency_s} | {r.llm_calls} | {missing[:120]} |")
    problems = [r for r in results if r.run == 1 and r.score.category in ("wrong", "error", "partial")]
    if problems:
        lines += ["", "## Wrong, error and partial answers", ""]
        for r in problems:
            lines += [
                f"### {r.case.id} ({r.score.category})", "",
                f"**Question:** {r.case.question}", "",
                f"**Expected:** {json.dumps(r.case.expect, default=str)}", "",
                f"**Answer:** {r.answer}", "",
                f"**How calculated:** {r.how_calculated}", "",
                f"**Note:** {r.score.note}", "",
                f"**Trace:** `{r.trace_file}`", "",
                "**SQL:**", "", *[f"```sql\n{s}\n```" for s in r.sql], "",
            ]
    return "\n".join(lines) + "\n"


def build_live_orchestrator() -> tuple[Any, Any]:
    from ..access import Role, UserAccess
    from ..config import Settings
    from ..guardrails import load_from_settings
    from ..knowledge.loader import Knowledge
    from ..llm.factory import response_model, sql_model
    from ..tools import DataDeps, TTLCache, build_mcp_client
    from ..agents.orchestrator import Orchestrator

    s = Settings()
    deps = DataDeps(kb=Knowledge.load(), mcp=build_mcp_client(s), settings=s, cache=TTLCache(s.column_values_cache_seconds),
                    guardrails=load_from_settings(s))
    orch = Orchestrator(deps=deps, sql_llm=sql_model(s), response_llm=response_model(s))
    user = UserAccess(user_id="scorecard", role=Role(name="finance_all", domains=["*"], pii_allowed=False))
    return orch, user


async def main_async(args: argparse.Namespace) -> Path:
    paths = [BANK_DIR / f for b in args.banks for f in BANKS[b]]
    cases = load_cases(paths, include_paraphrases=not args.no_paraphrases)
    if args.only:
        cases = [c for c in cases if c.id in set(args.only) or (c.paraphrase_of or "") in set(args.only)]
    if args.limit:
        cases = cases[: args.limit]
    orch, user = build_live_orchestrator()
    from ..tools import warm_up

    await warm_up(orch.deps)
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    trace_dir = REPORT_DIR / "traces" / stamp
    results: list[CaseResult] = []
    for run in range(1, args.repeat + 1):
        for case in cases:
            r = await run_case(orch, user, case, trace_dir, run)
            print(f"[{run}] {case.id}: {r.score.category} ({r.mode}, {r.latency_s}s, {r.llm_calls} LLM calls)")
            results.append(r)
    summary = summarize(results)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    md = REPORT_DIR / f"scorecard_{stamp}.md"
    md.write_text(to_markdown(results, summary, f"Scorecard {stamp} ({', '.join(args.banks)})"), encoding="utf-8")
    (REPORT_DIR / f"scorecard_{stamp}.json").write_text(
        json.dumps({"summary": summary, "results": [r.model_dump() for r in results]}, default=str, indent=1), encoding="utf-8")
    print(json.dumps(summary, indent=1))
    print(f"report: {md}")
    return md


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--banks", nargs="+", default=["adra", "fynapse"], choices=sorted(BANKS))
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", nargs="*", default=[])
    ap.add_argument("--repeat", type=int, default=1)
    ap.add_argument("--no-paraphrases", action="store_true")
    args = ap.parse_args()
    if os.getenv("RUN_LIVE") != "1":
        raise SystemExit("The scorecard calls live services: set RUN_LIVE=1 first.")
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
