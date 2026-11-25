"""v3 AnswerEnvelope -> the response object the existing UI renders (its field names and types).

UI contract (from the backend's integration report):
- status: success | clarification | declined | error
- breakdown and follow_up_questions are JSON-encoded *strings*
- table: {columns: [{key, label, numeric}], rows, total_rows, truncated} or null
- source: {tables, row_count, truncated, description, period}; explanation: {kpi, calculation_steps, filters, period,
  caveats, approval, row_count, truncated}; timing: {total_ms, total_seconds, ...}

Rules kept from v3: never any SQL in the payload (`source.sql` is omitted), never KPI data (`explanation.kpi` is null),
every number comes from the envelope (built from tool results), nothing is invented here.
"""
from __future__ import annotations

import json
import re
from typing import Any

from ..agents.orchestrator import AnswerEnvelope

STATUS_TO_UI = {"answered": "success", "partial": "success", "clarification": "clarification",
                "declined": "declined", "failed": "error"}
DELTA_CHARS = 64


def chunk_text(text: str, size: int = DELTA_CHARS) -> list[str]:
    """Split the answer into delta pieces of at most `size` characters, on word boundaries where possible.
    Joining the pieces gives back exactly `text`."""
    if not text:
        return []
    out, start = [], 0
    while start < len(text):
        end = min(start + size, len(text))
        if end < len(text):
            space = text.rfind(" ", start + 1, end)
            if space > start:
                end = space + 1  # keep the space with the left piece
        out.append(text[start:end])
        start = end
    return out


def _label(key: str) -> str:
    return re.sub(r"[_\s]+", " ", str(key)).strip().capitalize() or str(key)


def _numeric(values: list[Any]) -> bool:
    present = [v for v in values if v is not None and v != ""]
    if not present:
        return False
    for v in present:
        if isinstance(v, bool):
            return False
        if isinstance(v, (int, float)):
            continue
        try:
            float(str(v).replace(",", ""))
        except ValueError:
            return False
    return True


def _cell(v: Any) -> str:
    """The UI types table cells as strings (Record<string, string>[]): None becomes an empty string."""
    return "" if v is None else str(v)


def _notes_markdown(notices: list[str]) -> str:
    """The UI hides `explanation` when it has no KPI, so notices (caveats) are also added to the answer text."""
    return "\n\n" + "\n".join(f"Note: {n}" for n in notices) if notices else ""


def ui_table(table: dict[str, Any] | None, total_rows: int | None) -> dict[str, Any] | None:
    if not table:
        return None
    cols = [str(c) for c in table.get("columns") or []]
    rows = table.get("rows") or []
    keys = list(dict.fromkeys(cols))
    columns = [{"key": k, "label": _label(k), "numeric": _numeric([r[i] if i < len(r) else None for r in rows])}
               for i, k in enumerate(keys)]
    records = [{k: _cell(r[i] if i < len(r) else None) for i, k in enumerate(keys)} for r in rows]
    total = max(total_rows or 0, len(records))
    return {"columns": columns, "rows": records, "total_rows": total, "truncated": total > len(records)}


def _files_markdown(files: list[dict[str, str]]) -> str:
    if not files:
        return ""
    return "\n\nFiles: " + ", ".join(f"[{f.get('name')}]({f.get('path')})" for f in files)


def _short(table: str) -> str:
    return table.split(".")[-1]


def to_ui_body(env: AnswerEnvelope, *, query: str, user_id: str, session_id: str | None,
               total_ms: float | None = None, domain_labels: dict[str, str] | None = None) -> dict[str, Any]:
    d = env.debug
    status = STATUS_TO_UI.get(env.status, "error")
    answer = (env.answer or "").strip() + _notes_markdown(env.notices) + _files_markdown(env.files)
    tables_used = list(dict.fromkeys(d.tables_used))
    # Users see business names only: the domain (for example "Accounts receivable"), never table or column names.
    labels = [(domain_labels or {}).get(x, x) for x in dict.fromkeys(d.domains)] if tables_used else []
    row_count = d.result_row_count
    table = ui_table(env.tables[0] if env.tables else None, row_count if len(env.tables) == 1 else None)
    truncated = bool(table and table["truncated"])
    steps = [s.strip(" -•\t") for s in (env.how_calculated or "").splitlines() if s.strip(" -•\t")]
    verified = env.status == "answered" and not d.unsupported_numbers
    seconds = round(total_ms / 1000, 3) if total_ms is not None else None
    return {
        "status": status,
        "message": answer,
        "conversation_id": env.conversation_id,
        "user_id": user_id,
        "session_id": session_id,
        "user_question": query,
        "resolved_question": d.standalone_question or query,
        "role": "assistant",
        "answer": answer,
        "breakdown_title": None,
        "breakdown": json.dumps([]),
        "table": table,
        "source_message": env.how_calculated or None,
        "source_label": ", ".join(labels) or None,
        "source_used": ", ".join(labels) or None,
        # for a clarification the follow-ups are the choices (each is a complete question the UI can send as is)
        "follow_up_questions": json.dumps(list(env.options if env.status == "clarification" and env.options
                                               else env.suggestions), ensure_ascii=False),
        "clarification_options": list(env.options),
        # "Answering for" line: business names only; other_topics are the topics the user can switch to
        "answer_context": env.answer_context.model_dump() if env.answer_context else None,
        "clarification_question": answer if env.status == "clarification" else None,
        "trace_id": env.message_id,
        "source": ({"tables": labels, "row_count": row_count, "truncated": truncated,
                    "description": None, "period": None} if tables_used else None),
        "verification": "verified" if verified else "unverified",
        "explanation": {
            "kpi": None,  # v3 has no KPIs
            "calculation_steps": steps,
            "filters": [],  # column names are technical; the "how calculated" text carries the business description
            "period": None,
            "caveats": list(env.notices),
            "approval": None,
            "row_count": row_count,
            "truncated": truncated,
        },
        "timing": {"total_ms": int(total_ms) if total_ms is not None else None, "total_seconds": seconds,
                   "llm_ms": None, "databricks_ms": None, "memory_ms": None, "code_ms": None, "steps": []},
    }
