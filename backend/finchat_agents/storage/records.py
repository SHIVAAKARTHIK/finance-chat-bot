"""Map v3 answers and trace events onto the aiops table rows (respecting the check constraints)."""
from __future__ import annotations

import datetime as dt
import json
from typing import Any

from ..tracing.events import TraceEvent

PREVIEW_CHARS = 2000
PAYLOAD_CHARS = 8000

# v3 envelope status -> finance_chat_messages.status (no 'partial' in the constraint)
STATUS_MAP = {"answered": "answered", "partial": "answered", "clarification": "clarification",
              "declined": "declined", "failed": "failed"}


def _cap(text: str | None, n: int) -> str | None:
    if text is None:
        return None
    return text if len(text) <= n else text[: n - 15] + "...[truncated]"


def intent_of(debug: Any) -> str | None:
    """data | general | mixed | workflow."""
    has_sql = bool(debug.sql)
    if debug.classification == "workflow":
        return "workflow"
    if debug.mode == "general" or (debug.used_knowledge and not has_sql):
        return "general"
    if debug.used_knowledge and has_sql:
        return "mixed"
    if debug.classification in ("simple_data", "complex") or has_sql:
        return "data"
    return None


def answer_path_of(status: str, debug: Any) -> str | None:
    if status == "declined":
        return "declined"
    if status == "clarification":
        return "clarify"
    if debug.sql or intent_of(debug) in ("data", "mixed"):
        return "adhoc"
    return None  # general knowledge


def processing_message_row(*, message_id: str, conversation_id: str, user_id: str, turn_index: int, question: str,
                           created_at: dt.datetime) -> dict[str, Any]:
    return {
        "message_id": message_id, "conversation_id": conversation_id, "user_id": user_id, "turn_index": turn_index,
        "question_text": question, "status": "processing", "visibility": "visible", "retry_count": 0,
        "llm_call_count": 0, "input_tokens": 0, "output_tokens": 0, "created_at": created_at,
    }


def final_message_row(env: Any, *, user_id: str, turn_index: int, question: str, created_at: dt.datetime,
                      completed_at: dt.datetime) -> dict[str, Any]:
    d = env.debug
    status = STATUS_MAP.get(env.status, "failed")
    answer_text = env.answer
    if env.how_calculated:
        answer_text = f"{answer_text}\n\nHow this was calculated: {env.how_calculated}"
    error_code = None
    if env.status == "partial":
        error_code = "partial_answer"
    elif env.status == "failed":
        error_code = "failed"
    return {
        "message_id": env.message_id,
        "conversation_id": env.conversation_id,
        "user_id": user_id,
        "turn_index": turn_index,
        "question_text": question,
        "standalone_question": d.standalone_question or None,
        "intent": intent_of(d),
        "answer_path": answer_path_of(env.status, d),
        "domain": ",".join(d.domains) or None,
        "kpi_ids": None,
        # v3 stores the entity/period filters the answer used (read from its SQL); feeds user memory
        "plan": json.dumps(d.filters) if getattr(d, "filters", None) and any(d.filters.values()) else None,
        "sql_text": ";\n".join(d.sql) or None,  # audit only, never shown to users
        "sql_source": "generated" if d.sql else None,
        "result_row_count": d.result_row_count,
        "result_preview": _cap(json.dumps(d.result_preview, default=str), PREVIEW_CHARS) if d.result_preview else None,
        "answer_text": answer_text,
        "trust_label": None,
        "clarification_text": env.answer if env.status == "clarification" else None,
        "status": status,
        "visibility": "visible",
        "hidden_reason": None,
        "error_code": error_code,
        "error_message": _cap(d.error, 1000) or None,
        "retry_count": 0,
        "llm_call_count": min(d.llm_calls, 32767),
        "input_tokens": d.input_tokens,
        "output_tokens": d.output_tokens,
        "models_used": d.models_used or None,
        "first_token_ms": None,
        "total_latency_ms": int(d.latency_ms + getattr(d, "context_ms", 0.0)),
        "created_at": created_at,
        "completed_at": completed_at,
    }


def conversation_row(*, conversation_id: str, user_id: str, title: str | None, turn_count: int, now: dt.datetime,
                     created_at: dt.datetime | None = None, domain: str | None = None,
                     seed_summary: str | None = None) -> dict[str, Any]:
    """title, summary_through_turn and created_at are insert-only (see storage.aiops.NEVER_UPDATE)."""
    row = {
        "conversation_id": conversation_id, "user_id": user_id, "visibility": "visible", "turn_count": turn_count,
        "title": _cap(title, 120) if title else None, "summary_through_turn": 0, "created_at": created_at or now,
        "last_message_at": now,
    }
    if domain:
        row["domain"] = domain
    if seed_summary:  # a conversation continued after the question limit starts with the previous summary
        row["summary"] = seed_summary
    return row


def event_row(event: TraceEvent, *, conversation_id: str, step_order: int) -> dict[str, Any]:
    """One row per LLM call or tool call. step_name = agent name (LLM calls) or tool name (tool calls)."""
    is_llm = event.type == "llm_call"
    payload = dict(event.payload)
    if is_llm:
        input_payload = {"agent": event.agent, "step": event.step}
        output_payload = {k: payload.get(k) for k in ("stop_reason", "text", "tool_calls") if k in payload}
    else:
        input_payload = {"agent": event.agent, "step": event.step, "call_id": payload.get("call_id"), "input": payload.get("input")}
        output_payload = {"output": payload.get("output")}
    return {
        "event_id": event.event_id,
        "message_id": event.message_id,
        "conversation_id": conversation_id,
        "step_name": event.agent if is_llm else (event.name or "tool"),
        "step_order": step_order,
        "attempt": 1,
        "status": "failed" if event.status == "error" else "ok",
        "started_at": event.started_at,
        "ended_at": event.ended_at,
        "duration_ms": int(event.duration_ms) if event.duration_ms is not None else None,
        "input_payload": _cap(json.dumps(input_payload, default=str), PAYLOAD_CHARS),
        "output_payload": _cap(json.dumps(output_payload, default=str), PAYLOAD_CHARS),
        "error_message": _cap(str(payload.get("error")), 1000) if payload.get("error") else None,
        "model_provider": (("anthropic-api" if str(event.name).startswith("claude-") else "aws-bedrock") if is_llm else None),
        "model_name": event.name if is_llm else None,
        "prompt_version": None,
        "temperature": None,
        "input_tokens": event.input_tokens if is_llm else None,
        "output_tokens": event.output_tokens if is_llm else None,
        "cache_read_tokens": event.cache_read_tokens if is_llm else None,
        "created_at": event.ended_at or event.started_at,
    }
