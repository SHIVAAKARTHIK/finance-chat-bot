"""ChatService: identity -> role, conversation context (summary + recent turns + topics, chosen by tokens), answer,
background persistence, rolling summaries, clear context, the optional question limit, and user-memory hints."""
from __future__ import annotations

import asyncio
import logging
import time
import uuid
from typing import Any

from pydantic import BaseModel, Field

from ..access.rbac import AccessConfig, Role, UserAccess
from ..agents.orchestrator import AnswerEnvelope, ConversationContext, Orchestrator, Turn
from ..guardrails.audit import log_decision, log_request
from ..guardrails.input_checks.redact import redact_question, redaction_notice
from ..memory.context import select_recent, topic_label, topic_states
from ..memory.summary import ConversationSummarizer, TurnRecord, fallback_seed, needs_summary, turns_from_rows
from ..memory.user_memory import UserMemory, assumed_entity_notice, build_memory, memory_hint, memory_row
from ..storage.aiops import AiopsStore, utcnow
from ..storage.records import conversation_row, final_message_row, processing_message_row
from ..storage.trace_sink import AiopsTraceSink
from ..storage.writer import BackgroundWriter
from ..tracing.sinks import TraceSink
from ..tools.resolve import prewarm_lookups
from ..tracing.tracer import Tracer
from ..runtime.tools import RunContext

log = logging.getLogger(__name__)

LOAD_TURNS = 50  # newest turns read per question: enough for the token budget, the topics and the summary input
CLEAR_COMMANDS = {"/clear", "/new"}  # typed in the chat box: same as the "Clear context" button
CLEARED_TEXT = ("Context cleared. Your next questions start fresh: earlier questions and answers stay in the history "
                "but are no longer used to answer.")
CONTEXT_TIMEOUT_S = 5.0
MEMORY_CACHE_S = 600.0  # a user's habits change slowly: re-read at most every 10 minutes


class Identity(BaseModel):
    user_id: str
    groups: list[str] = Field(default_factory=list)


class LoadedContext(BaseModel):
    conversation_id: str
    context: ConversationContext
    turn_count: int = 0  # turns already in the conversation
    is_new: bool = True
    summary_through_turn: int = 0
    unsummarised: list[TurnRecord] = Field(default_factory=list)
    all_turns: list[TurnRecord] = Field(default_factory=list)
    seed_summary: str | None = None  # set when this conversation continues one that hit the question limit
    context_start_turn: int = 0  # turns up to this index were cleared by the user (not used as context)
    notices: list[str] = Field(default_factory=list)


def limit_reached_notice(limit: int) -> str:
    return (f"This conversation has reached the {limit}-question limit. Your next question will start a new "
            "conversation, and a summary of this one will be carried over.")


def rollover_notice(limit: int) -> str:
    return (f"The previous conversation reached the {limit}-question limit, so this question starts a new conversation. "
            "A summary of the earlier conversation was carried over.")


class ChatService:
    def __init__(
        self,
        orchestrator: Orchestrator,
        access: AccessConfig,
        *,
        store: AiopsStore | None = None,
        writer: BackgroundWriter | None = None,
        summarizer: ConversationSummarizer | None = None,
        context_timeout_s: float = CONTEXT_TIMEOUT_S,
    ):
        self.orchestrator = orchestrator
        self.access = access
        self.store = store
        self.writer = writer or (BackgroundWriter() if store else None)
        self.labels: dict[str, str] = dict(getattr(orchestrator.kb, "domains", {}) or {})  # domain -> business name
        self.summarizer = summarizer or ConversationSummarizer(orchestrator.response_llm, self.labels)
        self.context_timeout_s = context_timeout_s
        guardrails = getattr(orchestrator, "guardrails", None)
        if guardrails is not None and hasattr(self.summarizer, "system"):
            rules = guardrails.prompt_for("summarizer")
            if rules:
                self.summarizer.system = f"{self.summarizer.system}\n\n---\n\n{rules}"
        settings = orchestrator.settings
        self.question_limit = settings.conversation_question_limit  # 0 = no limit
        self.summary_threshold = settings.summary_token_threshold
        self.history_budget = settings.history_token_budget
        self._memory_cache: dict[str, tuple[float, UserMemory | None]] = {}

    # ------------------------------------------------------------ context

    async def load_context(self, conversation_id: str | None, user_id: str) -> LoadedContext:
        """Summary and recent turns of the user's own conversation. Never fails: on errors, a fresh context."""
        if not conversation_id:
            return LoadedContext(conversation_id=str(uuid.uuid4()), context=ConversationContext())
        if self.store is None:
            return LoadedContext(conversation_id=conversation_id, context=ConversationContext(conversation_id=conversation_id))
        try:
            # Both reads at once; the turns query is limited to this user's rows, so nothing of another user is read.
            conv, rows = await asyncio.gather(
                asyncio.wait_for(self.store.conversation(conversation_id), self.context_timeout_s),
                asyncio.wait_for(self.store.recent_turns(conversation_id, LOAD_TURNS, user_id=user_id), self.context_timeout_s),
            )
            if conv is None:
                return LoadedContext(conversation_id=conversation_id, context=ConversationContext(conversation_id=conversation_id))
            if str(conv.get("user_id")) != user_id:  # never continue (or reveal) someone else's conversation
                log.warning("conversation %s belongs to another user; starting a new one", conversation_id)
                log_request("conversation_access", "block", "own_conversations_only",
                            f"asked to continue another user's conversation {conversation_id}", user_id)
                return LoadedContext(conversation_id=str(uuid.uuid4()), context=ConversationContext())
        except Exception:
            log.exception("could not load conversation %s; answering without history", conversation_id)
            return LoadedContext(conversation_id=conversation_id, context=ConversationContext(conversation_id=conversation_id),
                                 is_new=False)
        start = int(conv.get("context_start_turn") or 0)
        turns = [t for t in turns_from_rows(rows) if t.turn_index > start]  # nothing from before a "clear context"
        through = int(conv.get("summary_through_turn") or 0)
        summary = conv.get("summary") if through > start else None  # a summary written before the clear is ignored
        unsummarised = [t for t in turns if t.turn_index > max(through, start)]
        recent = select_recent(turns, self.history_budget)
        shown = {t.turn_index for t in recent}
        ctx = ConversationContext(
            conversation_id=conversation_id,
            turns=[Turn(question=t.question, answer=t.answer, topic=topic_label(t, self.labels)) for t in recent],
            summary=summary or None,
            topics=topic_states(turns, self.labels),
            earlier_questions=[t.question for t in unsummarised if t.turn_index not in shown][-20:],  # never a gap
        )
        return LoadedContext(conversation_id=conversation_id, context=ctx, turn_count=int(conv.get("turn_count") or 0),
                             is_new=False, summary_through_turn=max(through, start) if summary else start,
                             all_turns=turns, unsummarised=unsummarised, context_start_turn=start)

    def _rollover(self, loaded: LoadedContext) -> LoadedContext:
        """The conversation is full: start a new one seeded with the summary (or a plain seed if none exists yet)."""
        summary = loaded.context.summary
        up_to_date = summary and loaded.summary_through_turn >= loaded.turn_count
        seed = summary if up_to_date else fallback_seed(summary, loaded.all_turns)
        new_id = str(uuid.uuid4())
        return LoadedContext(conversation_id=new_id, context=ConversationContext(conversation_id=new_id, summary=seed or None),
                             seed_summary=seed or None, notices=[rollover_notice(self.question_limit)])

    async def _user_memory(self, user_id: str) -> UserMemory | None:
        if self.store is None:
            return None
        cached = self._memory_cache.get(user_id)
        if cached is not None and time.monotonic() - cached[0] < MEMORY_CACHE_S:
            return cached[1]
        mem = await self._read_user_memory(user_id)
        self._memory_cache[user_id] = (time.monotonic(), mem)
        return mem

    async def _read_user_memory(self, user_id: str) -> UserMemory | None:
        try:
            row = await asyncio.wait_for(self.store.user_memory(user_id), self.context_timeout_s)
        except Exception:
            log.exception("could not load user memory for %s", user_id)
            return None
        if not row:
            return None
        import json

        try:
            freq = json.loads(row.get("frequent_entities") or "[]")
        except ValueError:
            freq = []
        return UserMemory(user_id=user_id, frequent_entities=freq, default_entity=row.get("default_entity"),
                          default_period=row.get("default_period"), recent_window_size=int(row.get("recent_window_size") or 30))

    # ------------------------------------------------------------ chat

    async def chat(
        self,
        message: str,
        identity: Identity,
        *,
        conversation_id: str | None = None,
        extra_sinks: list[TraceSink] | None = None,
    ) -> AnswerEnvelope:
        if message.strip().lower() in CLEAR_COMMANDS:
            return await self._clear_command(identity, conversation_id)
        removed: list[str] = []
        if getattr(self.orchestrator, "guardrails", None) is not None:
            # before anything else: the title, the stored question, the traces and the models get the redacted text
            message, removed = redact_question(message)
        user = self.access.user_access(identity.user_id, identity.groups)
        context_started, t0 = utcnow(), time.monotonic()
        # The conversation reads and the user-memory read are independent: run them together.
        if user.has_access:
            loaded, mem = await asyncio.gather(self.load_context(conversation_id, identity.user_id),
                                               self._user_memory(identity.user_id))
        else:
            loaded, mem = await self.load_context(conversation_id, identity.user_id), None
        context_ms, context_ended = (time.monotonic() - t0) * 1000, utcnow()
        if self.question_limit > 0 and not loaded.is_new and loaded.turn_count >= self.question_limit:
            loaded = self._rollover(loaded)
        loaded.context.user_hint = memory_hint(mem)

        conv_id = loaded.conversation_id
        message_id = str(uuid.uuid4())
        turn_index = loaded.turn_count + 1
        created_at = utcnow()
        sinks: list[TraceSink] = list(extra_sinks or [])
        if self.store is not None and self.writer is not None:
            store, writer = self.store, self.writer
            conv = conversation_row(conversation_id=conv_id, user_id=identity.user_id, title=message, turn_count=turn_index,
                                    now=created_at, seed_summary=loaded.seed_summary)
            proc = processing_message_row(message_id=message_id, conversation_id=conv_id, user_id=identity.user_id,
                                          turn_index=turn_index, question=message, created_at=created_at)
            writer.submit(f"conversation {conv_id}", lambda: store.upsert("finance_chat_conversations", [conv]))
            writer.submit(f"message {message_id} processing", lambda: store.upsert("finance_chat_messages", [proc]))
            sinks.append(AiopsTraceSink(store, writer, conversation_id=conv_id))

        # Recorded as its own step, so the per-step timings show how long loading the conversation took.
        await Tracer(sinks, message_id=message_id).emit(
            "tool_call", agent="chat_service", name="load_context", started_at=context_started, ended_at=context_ended,
            payload={"context_ms": round(context_ms, 1), "has_history": not loaded.is_new})
        if getattr(self.orchestrator, "guardrails", None) is not None:
            audit = RunContext(tracer=Tracer([*self.orchestrator.sinks, *sinks], message_id=message_id))
            await log_decision(audit, "input_redaction", "change" if removed else "allow", "sensitive_data",
                               ("removed: " + ", ".join(removed)) if removed else "nothing to remove")
        env = await self.orchestrator.answer(message, user, loaded.context, conversation_id=conv_id, message_id=message_id,
                                             extra_sinks=sinks)
        env.debug.context_ms = round(context_ms, 1)

        assumed = assumed_entity_notice(mem, env.debug.filters.get("entities", []), message)
        env.notices = [*([redaction_notice(removed)] if removed else []), *loaded.notices,
                       *([assumed] if assumed else []), *env.notices]
        if self.question_limit > 0 and turn_index >= self.question_limit:
            env.notices.append(limit_reached_notice(self.question_limit))

        if self.store is not None and self.writer is not None:
            self._persist_after(env, identity, loaded, message, turn_index, created_at)
        return env

    def _persist_after(self, env: AnswerEnvelope, identity: Identity, loaded: LoadedContext, message: str,
                       turn_index: int, created_at: Any) -> None:
        store, writer = self.store, self.writer
        assert store is not None and writer is not None
        done = utcnow()
        final = final_message_row(env, user_id=identity.user_id, turn_index=turn_index, question=message,
                                  created_at=created_at, completed_at=done)
        conv = conversation_row(conversation_id=env.conversation_id, user_id=identity.user_id, title=message,
                                turn_count=turn_index, now=done, domain=final.get("domain"))
        writer.submit(f"message {env.message_id} final", lambda: store.upsert("finance_chat_messages", [final]))
        writer.submit(f"conversation {env.conversation_id} update", lambda: store.upsert("finance_chat_conversations", [conv]))

        # rolling summary: when the turns not yet in it pass the token threshold (and at the question limit, if one is set)
        if env.status in ("answered", "partial", "clarification"):
            filters = env.debug.filters or {}
            current = TurnRecord(turn_index=turn_index, question=env.debug.standalone_question or message, answer=env.answer,
                                 domains=list(env.debug.domains), entities=list(filters.get("entities", [])),
                                 periods=list(filters.get("periods", [])))
            unsummarised = [*loaded.unsummarised, current]
            previous = loaded.context.summary
            at_limit = self.question_limit > 0 and turn_index >= self.question_limit
            if at_limit or needs_summary(None, unsummarised, self.summary_threshold):
                async def summarise() -> None:
                    text = await self.summarizer.summarize(previous, unsummarised)
                    if text:
                        await store.update_summary(env.conversation_id, text, turn_index)

                writer.submit(f"summary {env.conversation_id} through {turn_index}", summarise)

        # user memory: recomputed from the last 30 answered questions when this answer used entity/period filters
        if env.status == "answered" and any(env.debug.filters.values()):
            async def refresh_memory() -> None:
                plans = await store.user_plans(identity.user_id, 30)
                await store.upsert("finance_chat_user_memory", [memory_row(build_memory(identity.user_id, plans), utcnow())])
                self._memory_cache.pop(identity.user_id, None)  # read the new habits on the next question

            writer.submit(f"user memory {identity.user_id}", refresh_memory)

    # ------------------------------------------------------------ clear context

    async def clear_context(self, conversation_id: str | None, identity: Identity) -> dict[str, Any]:
        """The user's "Clear context": later questions ignore everything asked so far in this conversation (summary,
        recent turns, topics). The history stays stored and visible. Only the owner can clear a conversation."""
        if not conversation_id or self.store is None:
            return {"conversation_id": conversation_id, "cleared": True, "context_start_turn": 0, "message": CLEARED_TEXT}
        conv = await asyncio.wait_for(self.store.conversation(conversation_id), self.context_timeout_s)
        if conv is None:  # nothing asked yet: nothing to clear
            return {"conversation_id": conversation_id, "cleared": True, "context_start_turn": 0, "message": CLEARED_TEXT}
        if str(conv.get("user_id")) != identity.user_id:
            log_request("conversation_access", "block", "own_conversations_only",
                        f"asked to clear another user's conversation {conversation_id}", identity.user_id)
            raise PermissionError("This conversation belongs to another user.")
        turn = int(conv.get("turn_count") or 0)
        await self.store.set_context_start(conversation_id, turn)
        return {"conversation_id": conversation_id, "cleared": True, "context_start_turn": turn, "message": CLEARED_TEXT}

    async def _clear_command(self, identity: Identity, conversation_id: str | None) -> AnswerEnvelope:
        env = AnswerEnvelope(conversation_id=conversation_id or str(uuid.uuid4()), message_id=str(uuid.uuid4()))
        try:
            result = await self.clear_context(conversation_id, identity)
            env.answer = result["message"]
        except PermissionError:
            env.status, env.answer = "declined", "This conversation belongs to another user."
        except Exception as exc:  # noqa: BLE001 - e.g. the context_start_turn column is missing
            log.error("clear context failed: %s", exc)
            env.status, env.answer = "failed", "The context could not be cleared right now. Please try again later."
        return env

    async def close(self) -> None:
        if self.writer is not None:
            await self.writer.stop()
        closer = getattr(getattr(self.store, "executor", None), "aclose", None)
        if closer is not None:
            await closer()  # pooled Databricks connections

    @property
    def health_checker(self):
        """Connectivity checks (MCP, Bedrock, aiops), built on first use."""
        if getattr(self, "_health_checker", None) is None:
            from .health import build_checker

            self._health_checker = build_checker(self)
        return self._health_checker

    async def warm_up(self) -> dict[str, Any]:
        """Startup: wake the SQL warehouse, ping both Bedrock models, read aiops. Never raises; the result is logged
        and primes the /v3/health cache."""
        try:
            result = await self.health_checker.run(force=True, timeout_s=self.orchestrator.settings.warm_up_timeout_seconds)
        except Exception as exc:  # noqa: BLE001 - startup must not fail because a dependency is down
            return {"status": "down", "error": type(exc).__name__}
        try:  # preload entity values and period lists so the first question skips those lookups
            access = UserAccess(user_id="warm-up", role=Role(name="warm-up", domains=["*"]))
            result["preloaded"] = await asyncio.wait_for(
                prewarm_lookups(self.orchestrator.deps, access), self.orchestrator.settings.warm_up_timeout_seconds)
        except Exception as exc:  # noqa: BLE001
            result["preloaded"] = {"error": type(exc).__name__}
        return result


def health(service: ChatService) -> dict[str, Any]:
    return {"storage": "enabled" if service.store else "disabled",
            "write_failures": len(service.writer.failures) if service.writer else 0}
