"""Fast path for simple_data questions (SPEC section 3), plain Python:

search_tables (code) -> resolve entity/period hints (code, cached lookups) -> SQL writer (1 LLM call) -> run_sql
-> on error or empty result, one repair (1 LLM call) -> success, or None plus the attempt for the ReAct loop.
The answer writer is the third LLM call (in the orchestrator).
"""
from __future__ import annotations

import json
import re
from pydantic import BaseModel, Field

from ..access.rbac import UserAccess
from ..llm.types import LLMError, LLMResult, Message, ModelHandle, ToolResultBlock, ToolSpec
from ..runtime.llm_call import traced_complete
from ..runtime.tools import GuardrailRefusal, RunContext, ToolError
from ..tools.deps import DataDeps
from ..tools.resolve import resolve_entity, resolve_period
from ..tracing.databricks import called_by
from ..guardrails.audit import log_decision
from ..tools.run_sql import SqlResult, audit_query, execute_guarded, register_result
from ..tracing.events import utcnow
from ..tracing.tracer import preview
from .specialists import format_examples, load_prompt, with_rules

AGENT = "fast_path"
MAX_TABLES = 3
ENTITY_MIN_SCORE = 0.7

SUBMIT_SQL = ToolSpec(
    name="submit_sql",
    description="Submit the single SQL query (or explain why it cannot be answered here).",
    input_schema={
        "type": "object",
        "properties": {
            "sql": {"type": "string", "description": "One SELECT statement, or empty."},
            "explanation": {"type": "string", "description": "One sentence, at most 25 words, business language."},
            "cannot_answer": {"type": "string", "description": "Why the question needs the full analysis, if so."},
        },
        "required": ["sql", "explanation"],
    },
)


class FastPathAttempt(BaseModel):
    tables: list[str] = Field(default_factory=list)
    sql_tried: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
    reason: str = ""

    def as_context(self) -> str:
        lines = ["A quick attempt already ran (do not repeat it; use what it found):"]
        if self.tables:
            lines.append(f"- candidate tables: {', '.join(self.tables)}")
        for i, sql in enumerate(self.sql_tried, 1):
            lines.append(f"- SQL tried ({i}):\n{sql}")
        for e in self.errors:
            lines.append(f"- problem: {e}")
        if self.reason:
            lines.append(f"- why it stopped: {self.reason}")
        return "\n".join(lines)


class FastPathSuccess(BaseModel):
    result: SqlResult
    sql: str
    explanation: str
    tables: list[str] = Field(default_factory=list)


async def _hints(deps: DataDeps, access: UserAccess, question: str, table: str) -> list[str]:
    hints = []
    try:
        with called_by(f"{AGENT}:resolve_entity"):
            ent = await resolve_entity(deps, access, question, table)
        good = [m for m in ent["matches"] if m["score"] >= ENTITY_MIN_SCORE]
        if good:
            vals = "; ".join(f"{m['column']} = '{m['value']}' (match {m['score']})" for m in good[:4])
            hints.append(f"Entity ({ent['entity_table']}): {vals}")
    except ToolError:
        pass
    try:
        with called_by(f"{AGENT}:resolve_period"):
            per = await resolve_period(deps, access, question, table)
        if per["matches"] and per["interpretation"] != "matched against period labels":
            vals = "; ".join(f"{m['label']}: {m['filters']}" for m in per["matches"][:6])
            hints.append(f"Period ({per['period_table']}, {per['interpretation']}): {vals}")
        elif not per["matches"] and per["interpretation"] != "matched against period labels":
            hints.append(f"Period '{per['interpretation']}' has NO data. Latest available: {', '.join(per['available_latest_first'][:6])}")
    except ToolError:
        pass
    return hints


def _context(deps: DataDeps, access: UserAccess, question: str, tables: list[str], hints: list[str]) -> str:
    kb = deps.kb
    parts = ["## Candidate tables"]
    for tid in tables:
        body = kb.tables[tid].body
        body = re.split(r"\n## (Profile|Sample rows)\b", body)[0]
        parts.append(f"### {kb.tables[tid].meta.fqn}\n{body}")
    joins = []
    for other in tables[1:]:
        path = kb.join_path(tables[0], other)
        for j in path or []:
            f, t = kb.tables[j.from_].meta.fqn, kb.tables[j.to].meta.fqn
            joins.append(f"- {f} -> {t}: {j.condition(f, t)}")
    parts.append("## Approved joins\n" + ("\n".join(dict.fromkeys(joins)) or "(none between these tables)"))
    parts.append("## Resolved values\n" + ("\n".join(f"- {h}" for h in hints) or "(none found; filter only on what the question asks)"))
    gloss = kb.glossary_lookup(question)
    if gloss:
        parts.append("## Glossary\n" + "\n".join(f"- {g.term}: {' '.join(g.text.split())}" for g in gloss[:6]))
    examples = kb.similar_examples(question, k=3, domains=access.domains)
    if examples:
        parts.append("## " + format_examples(examples))
    return "\n\n".join(parts)


def _parse(result: LLMResult) -> tuple[str, str, str, str | None]:
    """(sql, explanation, cannot_answer, tool_call_id)"""
    call = next((c for c in result.tool_calls if c.name == SUBMIT_SQL.name), None)
    if call is not None:
        return (str(call.input.get("sql") or "").strip(), str(call.input.get("explanation") or "").strip(),
                str(call.input.get("cannot_answer") or "").strip(), call.id)
    m = re.search(r"```(?:sql)?\s*(.+?)```", result.text or "", re.S | re.I)
    return (m.group(1).strip() if m else "", "", "" if m else "no SQL returned", None)


async def _run(sql: str, deps: DataDeps, access: UserAccess, ctx: RunContext, step: int) -> SqlResult:
    if ctx.counters.sql_calls >= ctx.budget.max_sql_calls:
        raise ToolError("SQL call budget reached.")
    ctx.counters.sql_calls += 1
    started = utcnow()
    try:
        with called_by(f"{AGENT}:run_sql"):
            result = await execute_guarded(sql, deps, access)
    except ToolError as exc:
        await ctx.tracer.emit("tool_call", agent=AGENT, step=step, name="run_sql", status="error", started_at=started,
                              ended_at=utcnow(), payload={"input": preview(sql, 2000), "output": preview(str(exc), 1000)})
        if isinstance(exc, GuardrailRefusal):
            await log_decision(ctx, "data_check", "block", "data_access", str(exc))
        raise
    await audit_query(ctx, result)
    register_result(ctx, result)
    await ctx.tracer.emit("tool_call", agent=AGENT, step=step, name="run_sql", started_at=started, ended_at=utcnow(),
                          payload={"input": preview(sql, 2000), "output": preview(json.dumps(result.for_model(), default=str), 1000)})
    return result


async def run_fast_path(
    question: str, *, deps: DataDeps, llm: ModelHandle, ctx: RunContext, extra_hints: list[str] | None = None
) -> tuple[FastPathSuccess | None, FastPathAttempt]:
    access: UserAccess = ctx.user
    attempt = FastPathAttempt()
    hits = deps.kb.search_tables(question, k=MAX_TABLES, domains=access.domains)
    if not hits:
        attempt.reason = "no accessible table matches the question"
        return None, attempt
    attempt.tables = [h.fqn for h in hits]
    tables = [h.table for h in hits]
    hints = await _hints(deps, access, question, tables[0]) + list(extra_hints or [])
    system = with_rules(load_prompt("fast_sql"), deps.kb)
    messages = [Message.user(f"Question: {question}\n\n{_context(deps, access, question, tables, hints)}")]

    for step in (1, 2):
        try:
            llm_result = await traced_complete(llm, ctx, agent=AGENT, step=step, system=system, messages=messages,
                                               tools=[SUBMIT_SQL], max_tokens=2000)
        except (LLMError, TimeoutError) as exc:
            attempt.reason = f"model call failed: {type(exc).__name__}"
            return None, attempt
        sql, explanation, cannot, call_id = _parse(llm_result)
        if cannot or not sql:
            attempt.reason = cannot or "the SQL writer returned no query"
            return None, attempt
        attempt.sql_tried.append(sql)
        problem = ""
        try:
            result = await _run(sql, deps, access, ctx, step)
            if result.row_count > 0:
                return FastPathSuccess(result=result, sql=result.sql, explanation=explanation, tables=result.tables), attempt
            problem = "The query ran but returned no rows. " + " ".join(result.notes)
        except ToolError as exc:
            problem = str(exc)
        attempt.errors.append(problem)
        if step == 2:
            break
        # one repair: show the model its attempt and what went wrong
        messages.append(llm_result.to_message())
        feedback = f"Previous attempt failed: {problem}\nFix the query, or set cannot_answer."
        if call_id:
            messages.append(Message(role="user", content=[ToolResultBlock(tool_use_id=call_id, content=feedback, is_error=True)]))
        else:
            messages.append(Message.user(feedback))
    attempt.reason = "the query still failed or returned no rows after one repair"
    return None, attempt

