"""Final answer step: gpt-oss writes the user-facing answer and how_calculated from the supervisor's draft and the
query results, then the number check runs: unsupported numbers -> rewrite once -> caveat."""
from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel, Field

from ..llm.types import ModelHandle
from ..runtime.agent import Agent
from ..runtime.tools import RunContext
from ..tools.calculate import CALC_KEY
from ..tools.run_sql import RESULTS_KEY, SqlResult
from ..tracing.events import utcnow
from .number_check import allowed_numbers, unsupported_numbers
from .specialists import KNOWLEDGE_KEY, load_prompt
from .supervisor import SupervisorDraft

ROWS_FOR_WRITER = 20
TABLE_MIN_ROWS = 4  # results with more than 3 rows are shown as a table
TABLE_MAX_ROWS = 200

WRITER_SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {"type": "string"},
        "how_calculated": {"type": "string"},
        "suggestions": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["answer", "how_calculated"],
}


class WrittenAnswer(BaseModel):
    answer: str
    how_calculated: str = ""
    suggestions: list[str] = Field(default_factory=list)
    unsupported: list[str] = Field(default_factory=list)  # numbers still unsupported after the rewrite
    rewrites: int = 0


def results_for(ctx: RunContext, ids: list[str] | None = None) -> list[SqlResult]:
    store: dict[str, SqlResult] = ctx.extras.get(RESULTS_KEY, {})
    if ids:
        picked = [store[i] for i in ids if i in store]
        if picked:
            return picked
    return list(store.values())[-1:] if store else []


def _facts(question: str, draft: SupervisorDraft, results: list[SqlResult], files: list[str] | None = None) -> str:
    payload: dict[str, Any] = {
        "question": question,
        "status": draft.status,
        "analyst_answer": draft.answer,
        "analyst_how_calculated": draft.how_calculated,
        "caveats": draft.caveats,
        "alternatives_to_offer": draft.alternatives,
        "workflow_steps": [s.model_dump() for s in draft.steps],
        "files_saved": files or [],
        "query_results": [
            {
                "columns": r.columns,
                "rows": r.rows[:ROWS_FOR_WRITER],
                "row_count": r.row_count,
                "shown_to_user_as_table": r.row_count >= TABLE_MIN_ROWS,
                "notes": r.notes,
            }
            for r in results
        ],
    }
    return "Write the final answer from these facts:\n\n" + json.dumps(payload, default=str, ensure_ascii=False, indent=1)


class AnswerWriter:
    def __init__(self, llm: ModelHandle, *, max_tokens: int = 2000):
        self.agent = Agent("answer_writer", load_prompt("answer_writer"), llm, [], output_schema=WRITER_SCHEMA,
                           max_steps=2, max_tokens=max_tokens, temperature=0.2)

    async def _write(self, facts: str, ctx: RunContext, feedback: str | None) -> WrittenAnswer:
        result = await self.agent.run(facts, ctx, context=feedback)
        data = result.data or {}
        answer = str(data.get("answer") or result.answer or "").strip()
        sugg = data.get("suggestions") or []
        return WrittenAnswer(
            answer=answer,
            how_calculated=str(data.get("how_calculated") or "").strip(),
            suggestions=[str(s) for s in sugg][:3] if isinstance(sugg, list) else [],
        )

    @staticmethod
    async def _log_rewrite(ctx: RunContext, written: WrittenAnswer, bad: list[str]) -> None:
        """Record which numbers forced a rewrite and where they appear, so wrong rewrites can be diagnosed."""
        text = f"{written.answer}\n{written.how_calculated}"
        snippets = []
        for n in bad[:5]:
            i = text.find(n)
            snippets.append(text[max(0, i - 40): i + len(n) + 40].replace("\n", " ") if i >= 0 else n)
        now = utcnow()
        await ctx.tracer.emit("tool_call", agent="answer_writer", step=0, name="number_check_rewrite", started_at=now,
                              ended_at=now, payload={"input": ", ".join(bad[:10]), "output": " | ".join(snippets)})

    async def write(self, question: str, draft: SupervisorDraft, ctx: RunContext, *, check_numbers: bool = True) -> WrittenAnswer:
        shown = results_for(ctx, draft.result_ids)
        files = [f["name"] for f in ctx.extras.get("files", [])]
        facts = _facts(question, draft, shown, files)
        written = await self._write(facts, ctx, None)
        if not written.answer:  # writer failed: fall back to the analyst's text (still number-checked)
            written.answer = draft.answer
            written.how_calculated = written.how_calculated or draft.how_calculated
        if not written.how_calculated:
            written.how_calculated = draft.how_calculated
        if not check_numbers:
            return written
        allowed = allowed_numbers(
            ctx.extras.get(RESULTS_KEY, {}).values(),
            ctx.extras.get(CALC_KEY, []),
            [question, *ctx.extras.get(KNOWLEDGE_KEY, [])],
        )
        bad = unsupported_numbers(f"{written.answer}\n{written.how_calculated}", allowed)
        if bad:
            await self._log_rewrite(ctx, written, bad)
            feedback = (
                "Your previous answer contained numbers that are not in the facts: " + ", ".join(bad)
                + ". Rewrite it using only numbers that appear in the facts (rounding is fine). Remove any number you cannot find."
            )
            second = await self._write(facts, ctx, feedback)
            if second.answer:
                second.how_calculated = second.how_calculated or written.how_calculated
                written = second
            written.rewrites = 1
            written.unsupported = unsupported_numbers(f"{written.answer}\n{written.how_calculated}", allowed)
        return written


def tables_for(ctx: RunContext, draft: SupervisorDraft) -> list[dict[str, Any]]:
    """Results with more than 3 rows become envelope tables (rows built in code, never by the model)."""
    out = []
    picked = results_for(ctx, draft.result_ids) if draft.result_ids else []
    big = [r for r in picked if r.row_count >= TABLE_MIN_ROWS]
    for i, r in enumerate(big, 1):
        title = "Details" if len(big) == 1 else f"Details ({i})"
        out.append({"title": title, "columns": r.columns, "rows": [[_json(v) for v in row] for row in r.rows[:TABLE_MAX_ROWS]]})
    return out


def _json(v: Any) -> Any:
    if v is None or isinstance(v, (str, int, float, bool)):
        return v
    return str(v)
