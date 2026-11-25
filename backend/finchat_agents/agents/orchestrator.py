"""answer(message, user, conversation_context) -> AnswerEnvelope (SPEC section 7, without API wiring).

Flow (plain Python, no framework):
1. Supervisor's first model call classifies (route tool) and may start its first action.
2. general     -> knowledge agent.                                      mode: general
   simple_data -> fast path; on success the answer writer.               mode: fast
                  on failure the supervisor ReAct loop with the attempt. mode: fast->react
   complex     -> the supervisor ReAct loop continues from its first call. mode: react
3. Answer writer (gpt-oss) + number check; tables built in code from the query results.
"""
from __future__ import annotations

import time
import uuid
from typing import Any, Literal

from pydantic import BaseModel, Field

from ..access.rbac import UserAccess
from ..config import Settings
from ..knowledge.loader import Knowledge
from ..llm.types import LLMError, Message, ModelHandle
from ..runtime.llm_call import traced_complete
from ..runtime.tools import Budget, RunContext
from ..tools import DataDeps, build_data_tools
from ..tools.run_sql import RESULTS_KEY
from ..tracing.sinks import TraceSink
from ..tracing.tracer import Tracer, preview
from .answer import AnswerWriter, tables_for
from .fast_path import FastPathAttempt, run_fast_path
from ..memory.context import TopicState, topics_text
from ..memory.filters import extract_filters
from ..tools.actions import CONVERSATION_KEY, FILES_KEY, QUESTION_KEY, make_action_tools
from .specialists import build_action_agent, build_analyst_agent
from .specialists import KNOWLEDGE_KEY, build_catalog_agent, build_knowledge_agent, build_sql_agent, knowledge_tool
from .supervisor import PLAN_KEY, SupervisorDraft, build_supervisor, parse_route

Mode = Literal["general", "fast", "react", "fast->react", "clarify", "declined", "failed"]
Status = Literal["answered", "partial", "clarification", "declined", "failed"]
MAX_TURNS = 30  # safety cap; ChatService already chooses the turns by token budget


class Turn(BaseModel):
    question: str
    answer: str = ""
    topic: str = ""  # business area(s) of the data the answer used, e.g. "Fixed assets"


class ConversationContext(BaseModel):
    """What the agents see of the conversation (chosen by ChatService within a token budget)."""

    conversation_id: str | None = None
    turns: list[Turn] = Field(default_factory=list)  # recent turns, oldest first
    summary: str | None = None  # rolling summary of the earlier turns, one section per topic
    topics: list[TopicState] = Field(default_factory=list)  # most recent topic first
    earlier_questions: list[str] = Field(default_factory=list)  # older turns not yet in the summary (questions only)
    user_hint: str | None = None  # from user memory: a clear habit (e.g. usual entity), hint only

    def as_text(self) -> str:
        parts = []
        if self.user_hint:
            parts.append(self.user_hint)
        if self.summary:
            parts.append(f"Summary of the earlier conversation:\n{self.summary}")
        if self.earlier_questions:
            parts.append("Earlier questions (not in the summary yet):\n" + "\n".join(f"- {q}" for q in self.earlier_questions))
        topics = topics_text(self.topics)
        if topics:
            parts.append(topics)
        for t in self.turns[-MAX_TURNS:]:
            label = f" [topic: {t.topic}]" if t.topic else ""
            parts.append(f"User{label}: {t.question}\nAssistant: {preview(t.answer, 1500)}")
        return "\n\n".join(parts)


class AnswerDebug(BaseModel):
    run_id: str = ""
    mode: Mode = "failed"
    classification: str = ""
    standalone_question: str = ""
    latency_ms: float = 0.0
    context_ms: float = 0.0  # loading the conversation and user memory, before the agents start (ChatService)
    llm_calls: int = 0
    sql_calls: int = 0
    sql: list[str] = Field(default_factory=list)
    tables_used: list[str] = Field(default_factory=list)
    unsupported_numbers: list[str] = Field(default_factory=list)
    input_tokens: int = 0
    output_tokens: int = 0
    models_used: list[str] = Field(default_factory=list)
    result_row_count: int | None = None
    result_preview: list[list[Any]] = Field(default_factory=list)
    domains: list[str] = Field(default_factory=list)
    used_knowledge: bool = False
    local_files: list[str] = Field(default_factory=list)  # server paths of saved files (traces only)
    filters: dict[str, list[str]] = Field(default_factory=dict)  # entity / period filters read from the SQL
    fast_path: FastPathAttempt | None = None
    error: str = ""


class AnswerContext(BaseModel):
    """What this answer was about, for the "Answering for" line in the UI (business names only, never table names)."""

    topics: list[str] = Field(default_factory=list)  # business areas of the data used, e.g. ["Fixed assets"]
    entities: list[str] = Field(default_factory=list)
    periods: list[str] = Field(default_factory=list)
    other_topics: list[str] = Field(default_factory=list)  # other topics of this conversation the user can switch to


class AnswerEnvelope(BaseModel):
    conversation_id: str = ""
    message_id: str = ""
    status: Status = "answered"
    answer: str = ""
    how_calculated: str = ""
    tables: list[dict[str, Any]] = Field(default_factory=list)
    files: list[dict[str, str]] = Field(default_factory=list)
    suggestions: list[str] = Field(default_factory=list)
    notices: list[str] = Field(default_factory=list)
    options: list[str] = Field(default_factory=list)  # clarification choices; the UI sends the chosen one as the next question
    answer_context: AnswerContext | None = None
    debug: AnswerDebug = Field(default_factory=AnswerDebug, exclude=True)  # traces only, never in the API response


STEP_LABELS = {"done": "done", "done_with_caveat": "done, with a caveat", "not_done": "not done"}


def format_steps(draft: SupervisorDraft, plan: list[str] | None) -> str:
    """Per-step status list for workflows, built in code so every planned step is reported."""
    if not draft.steps and not plan:
        return ""
    reported = {s.step.strip().lower(): s for s in draft.steps}
    lines = ["Steps:"]
    used = set()
    for i, planned in enumerate(plan or [], 1):
        match = reported.get(planned.strip().lower()) or (draft.steps[i - 1] if i - 1 < len(draft.steps) else None)
        if match is not None:
            used.add(id(match))
        status = STEP_LABELS[match.status] if match else "not done"
        detail = (match.detail if match else "no result was reported for this step").strip()
        lines.append(f"{i}. {planned} ({status})" + (f": {detail}" if detail else ""))
    extra = [s for s in draft.steps if id(s) not in used]
    start = len(plan or []) + 1
    for j, s in enumerate(extra, start):
        lines.append(f"{j}. {s.step} ({STEP_LABELS[s.status]})" + (f": {s.detail}" if s.detail else ""))
    return "\n".join(lines)


CLARIFY_TEXT = "Your question could refer to more than one topic in this conversation. Which one do you mean?"


def answer_context(env: AnswerEnvelope, conversation: ConversationContext | None,
                   labels: dict[str, str]) -> AnswerContext | None:
    """Built in code from the tables the answer used and the filters in its SQL."""
    if env.status not in ("answered", "partial") or not env.debug.domains:
        return None
    current = list(dict.fromkeys(env.debug.domains))
    others = [t.label for t in (conversation.topics if conversation else []) if t.domain not in current]
    return AnswerContext(topics=[labels.get(d, d) for d in current], entities=env.debug.filters.get("entities", [])[:5],
                         periods=env.debug.filters.get("periods", [])[:5], other_topics=others[:5])


def supervisor_input(message: str, conversation: ConversationContext | None) -> str:
    history = conversation.as_text() if conversation else ""
    if not history:
        return message
    return f"{message}\n\n<conversation>\n{history}\n</conversation>"


class Orchestrator:
    def __init__(
        self,
        *,
        deps: DataDeps,
        sql_llm: ModelHandle,
        response_llm: ModelHandle,
        sinks: list[TraceSink] | None = None,
    ):
        self.deps = deps
        self.kb: Knowledge = deps.kb
        self.settings: Settings = deps.settings
        self.sql_llm = sql_llm
        self.response_llm = response_llm
        self.sinks = list(sinks or [])
        self.tools = build_data_tools(deps)
        self.catalog_agent = build_catalog_agent(sql_llm, self.tools, self.kb)
        self.sql_agent = build_sql_agent(sql_llm, self.tools, self.kb)
        self.knowledge_agent = build_knowledge_agent(response_llm, self.tools)
        self.analyst_agent = build_analyst_agent(sql_llm, self.sql_agent.as_tool(), self.tools, kb=self.kb)
        self.action_agent = build_action_agent(sql_llm, make_action_tools(self.settings.resolve_path(self.settings.output_dir)))
        self.supervisor = build_supervisor(sql_llm, [
            self.catalog_agent.as_tool(), self.sql_agent.as_tool(), self.analyst_agent.as_tool(),
            knowledge_tool(self.knowledge_agent), self.action_agent.as_tool(),
        ])
        self.writer = AnswerWriter(response_llm)

    async def answer(
        self,
        message: str,
        user: UserAccess,
        conversation_context: ConversationContext | None = None,
        *,
        conversation_id: str | None = None,
        message_id: str | None = None,
        extra_sinks: list[TraceSink] | None = None,
    ) -> AnswerEnvelope:
        t0 = time.monotonic()
        conv_id = conversation_id or (conversation_context.conversation_id if conversation_context else None) or str(uuid.uuid4())
        msg_id = message_id or str(uuid.uuid4())
        tracer = Tracer([*self.sinks, *(extra_sinks or [])], message_id=msg_id)
        env = AnswerEnvelope(conversation_id=conv_id, message_id=msg_id)
        env.debug.run_id = tracer.run_id
        ctx = RunContext(tracer=tracer, budget=Budget.from_settings(self.settings), user=user,
                         extras={"react_engine": self.settings.react_engine})
        ctx.extras[QUESTION_KEY] = message
        ctx.extras[CONVERSATION_KEY] = conv_id
        try:
            await self._answer(message, user, conversation_context, ctx, env)
        except Exception as exc:  # never an exception to the user
            env.status, env.answer = "failed", "Sorry, something went wrong while answering. Please try again."
            env.debug.mode, env.debug.error = "failed", f"{type(exc).__name__}: {str(exc)[:300]}"
            await tracer.emit("error", agent="orchestrator", status="error", payload={"error": env.debug.error})
        results = list(ctx.extras.get(RESULTS_KEY, {}).values())
        env.debug.sql = [r.sql for r in results]
        env.debug.tables_used = sorted({t for r in results for t in r.tables})
        env.debug.llm_calls = ctx.counters.llm_calls
        env.debug.input_tokens = ctx.counters.input_tokens
        env.debug.output_tokens = ctx.counters.output_tokens
        env.debug.models_used = list(ctx.counters.models)
        env.debug.used_knowledge = bool(ctx.extras.get(KNOWLEDGE_KEY)) or env.debug.mode == "general"
        last = list(results)[-1:] if results else []
        if last:
            env.debug.result_row_count = last[0].row_count
            env.debug.result_preview = [[v if isinstance(v, (str, int, float, bool)) or v is None else str(v) for v in row]
                                        for row in last[0].rows[:5]]
        env.debug.domains = sorted({p.meta.domain for t in env.debug.tables_used
                                    if (p := self.kb.resolve_table(t)) is not None and p.meta.domain})
        env.debug.sql_calls = ctx.counters.sql_calls
        env.debug.filters = extract_filters(env.debug.sql, self.kb) if env.debug.sql else {}
        env.answer_context = answer_context(env, conversation_context, self.kb.domains)
        saved = ctx.extras.get(FILES_KEY, [])
        env.files = [{"name": f["name"], "path": f["url"]} for f in saved]  # download URL, never a server path
        env.debug.local_files = [f["path"] for f in saved]
        env.debug.latency_ms = round((time.monotonic() - t0) * 1000, 1)
        await tracer.emit("answer", agent="orchestrator", payload={
            "mode": env.debug.mode, "status": env.status, "classification": env.debug.classification,
            "latency_ms": env.debug.latency_ms, "llm_calls": env.debug.llm_calls, "sql_calls": env.debug.sql_calls,
        })
        return env

    async def _answer(self, message: str, user: UserAccess, conversation: ConversationContext | None,
                      ctx: RunContext, env: AnswerEnvelope) -> None:
        if not user.has_access:
            env.status, env.debug.mode = "declined", "declined"
            env.answer = "You do not have access to Finance Chat data yet. Please ask an administrator to assign you a role."
            return
        task = supervisor_input(message, conversation)
        sup = self.supervisor
        specs = [t.spec for t in sup.tools] + ([sup.finish_tool] if sup.finish_tool else [])
        try:
            first = await traced_complete(self.sql_llm, ctx, agent="supervisor", step=1, system=sup.system_prompt,
                                          messages=[Message.user(task)], tools=specs, max_tokens=sup.max_tokens)
        except (LLMError, TimeoutError) as exc:
            env.status, env.debug.mode, env.debug.error = "failed", "failed", f"supervisor: {exc}"
            env.answer = "The assistant is not available right now. Please try again in a moment."
            return
        route = parse_route(first, message)
        env.debug.classification, env.debug.standalone_question = route.classification, route.standalone_question
        await ctx.tracer.emit("route", agent="supervisor", step=1, payload=route.model_dump())
        question = route.standalone_question

        if len(route.options) >= 2:  # the request could belong to more than one earlier topic: let the user choose
            env.status, env.debug.mode = "clarification", "clarify"
            env.options = route.options
            env.answer = CLARIFY_TEXT + "\n" + "\n".join(f"- {o}" for o in route.options)
            return

        if route.classification == "general":
            env.debug.mode = "general"
            result = await self.knowledge_agent.run(question, ctx)
            env.status = "partial" if result.status == "partial" else "answered"
            env.answer = result.answer
            return

        draft: SupervisorDraft
        if route.classification == "simple_data":
            hints = [conversation.user_hint] if conversation and conversation.user_hint else []
            success, attempt = await run_fast_path(question, deps=self.deps, llm=self.sql_llm, ctx=ctx, extra_hints=hints)
            env.debug.fast_path = attempt
            if success is not None:
                env.debug.mode = "fast"
                draft = SupervisorDraft(status="answered", how_calculated=success.explanation,
                                        result_ids=[success.result.result_id])
            else:
                env.debug.mode = "fast->react"
                result = await sup.run(question, ctx, context="\n\n".join(
                    c for c in (attempt.as_context(), conversation.as_text() if conversation else "") if c))
                draft = SupervisorDraft.from_data(result.data, result.answer, result.status == "partial")
        else:  # complex and workflow
            env.debug.mode = "react"
            # continue from the classification call: its route call (and any first agent call) runs as step 1
            result = await sup.run(task, ctx, initial=first)
            draft = SupervisorDraft.from_data(result.data, result.answer, result.status == "partial")

        await self._finish(question, draft, ctx, env)

    async def _finish(self, question: str, draft: SupervisorDraft, ctx: RunContext, env: AnswerEnvelope) -> None:
        env.status = draft.status
        if draft.status == "clarification":
            env.options = [a for a in draft.alternatives if a][:5]
        if draft.status == "declined":
            env.answer = draft.answer or "This request is outside what you can access or what the assistant may do."
            return
        written = await self.writer.write(question, draft, ctx)
        env.answer = written.answer or draft.answer
        steps_text = format_steps(draft, ctx.extras.get(PLAN_KEY))
        if steps_text:
            env.answer = f"{env.answer}\n\n{steps_text}"
            if any(s.status == "not_done" for s in draft.steps) and env.status == "answered":
                env.status = "partial"
        env.how_calculated = written.how_calculated
        env.suggestions = written.suggestions
        env.tables = tables_for(ctx, draft)
        env.notices += [c for c in draft.caveats if c][:3]
        if written.unsupported:
            env.debug.unsupported_numbers = written.unsupported
            env.notices.append("Some figures in this answer could not be checked against the data: "
                               + ", ".join(written.unsupported) + ". Please verify them before use.")
        if not env.answer:
            env.status = "failed"
            env.answer = "I could not produce an answer to this question."
