"""The audit trail of guardrail decisions: every check records allow, block, change or error with its rule and reason.

Decisions about a chat message are trace events (agent "guardrails", step name = the check) and are stored in
finance_chat_message_events, with output_payload {"decision", "rule", "reason"}. Decisions about a request that has no
chat message (login, file download, someone else's conversation) go to the application log "finchat_agents.audit".
Removed content itself is never recorded.
"""
from __future__ import annotations

import logging
from typing import Literal

from ..runtime.tools import RunContext
from ..tracing.events import utcnow

Decision = Literal["allow", "block", "change", "error"]
REASON_CHARS = 500
request_log = logging.getLogger("finchat_agents.audit")


def _reason(text: str) -> str:
    return " ".join((text or "").split())[:REASON_CHARS] or "no reason given"


async def log_decision(ctx: RunContext, check: str, decision: Decision, rule: str, reason: str) -> None:
    reason = _reason(reason)
    now = utcnow()
    await ctx.tracer.emit(
        "tool_call", agent="guardrails", step=0, name=check, status="error" if decision == "error" else "ok",
        started_at=now, ended_at=now,
        payload={"decision": decision, "rule": rule, "reason": reason, "output": f"{decision}: {rule} - {reason}"})


def log_request(check: str, decision: Decision, rule: str, reason: str, user_id: str | None = None) -> None:
    request_log.log(logging.INFO if decision == "allow" else logging.WARNING,
                    "guardrail decision=%s check=%s rule=%s user=%s reason=%s",
                    decision, check, rule, user_id or "unknown", _reason(reason))
