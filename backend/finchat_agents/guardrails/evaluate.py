"""Attack tests for the input checks with the REAL model (and the Bedrock Guardrail if configured):

    set RUN_LIVE=1, then:  python -m finchat_agents.guardrails.evaluate [--cases my_cases.yaml]

Each case is one user message and the verdict expected. It tests only the input checks: not the scope check that sees
the conversation, the output checks or data access. Exit code 0 when every case passes.
"""
from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel

from ..llm.types import ModelHandle
from ..runtime.tools import Budget, RunContext
from ..tracing.tracer import Tracer
from .input_checks.intent import VERDICTS, check_input
from .input_checks.redact import redact_question
from .loader import Guardrails

DEFAULT_CASES = Path(__file__).resolve().parent / "evals" / "attacks.yaml"
PARALLEL = 4


class Case(BaseModel):
    id: str
    category: str = "other"
    message: str
    expect: list[str]

    def passes(self, got: str) -> bool:
        return got in self.expect or ("blocked" in self.expect and got not in ("allow", "error"))


class Outcome(BaseModel):
    case: Case
    got: str

    @property
    def passed(self) -> bool:
        return self.case.passes(self.got)


def load_cases(path: Path) -> list[Case]:
    raw: Any = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or []
    cases = []
    for item in raw:
        expect = item.get("expect")
        cases.append(Case(**{**item, "expect": expect if isinstance(expect, list) else [expect]}))
        unknown = set(cases[-1].expect) - {*VERDICTS, "blocked"}
        if unknown:
            raise ValueError(f"case {cases[-1].id}: unknown expect value(s) {sorted(unknown)}")
    ids = [c.id for c in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("case ids must be unique")
    return cases


async def run_cases(cases: list[Case], guardrails: Guardrails, llm: ModelHandle, system: str) -> list[Outcome]:
    slots = asyncio.Semaphore(PARALLEL)

    async def one(case: Case) -> Outcome:
        async with slots:
            ctx = RunContext(tracer=Tracer([], message_id=case.id), budget=Budget())
            message, _ = redact_question(case.message)
            verdict = await check_input(message, guardrails, llm, ctx, system)
        got = "error" if verdict.failed else verdict.verdict if verdict.blocked else "allow"
        return Outcome(case=case, got=got)

    return list(await asyncio.gather(*(one(c) for c in cases)))


def report(outcomes: list[Outcome]) -> str:
    lines = [f"{'category':<14}{'passed':>8}"]
    for category in dict.fromkeys(o.case.category for o in outcomes):
        mine = [o for o in outcomes if o.case.category == category]
        lines.append(f"{category:<14}{sum(o.passed for o in mine):>5}/{len(mine)}")
    failed = [o for o in outcomes if not o.passed]
    if failed:
        lines += ["", "Failed:"]
        lines += [f"  {o.case.id}: expected {'/'.join(o.case.expect)}, got {o.got} - {o.case.message}" for o in failed]
    lines += ["", f"{len(outcomes) - len(failed)} of {len(outcomes)} cases passed"]
    return "\n".join(lines)


async def main_async(args: argparse.Namespace) -> int:
    from ..agents.specialists import load_prompt
    from ..config import Settings
    from ..llm.factory import sql_model
    from .loader import load_from_settings

    settings = Settings()
    if not settings.run_live:
        print("This calls the real models. Set RUN_LIVE=1 to run it.")
        return 2
    guardrails = load_from_settings(settings)
    if guardrails is None:
        print("GUARDRAILS_ENABLED=false: nothing to test.")
        return 2
    outcomes = await run_cases(load_cases(args.cases), guardrails, sql_model(settings), load_prompt("input_guard"))
    print(report(outcomes))
    return 0 if all(o.passed for o in outcomes) else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    return asyncio.run(main_async(ap.parse_args(sys.argv[1:] if argv is None else argv)))


if __name__ == "__main__":
    raise SystemExit(main())
