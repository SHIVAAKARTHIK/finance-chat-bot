"""The backend's existing finance-chat URLs, served by v3 (mount with prefix "/api/invoke"):

POST /finance-chat           JSON -> UI body
POST /finance-chat/stream    SSE: status / delta / complete / error (the path the UI uses)
GET  /finance-chat/history   the caller's recent exchanges (limit, threads)
POST /finance-chat/clear-context   {conversation_id}: later questions ignore everything asked so far (history stays)

Identity comes from the backend's own `get_current_user` dependency (validated Entra token) and its `agent_roles(user)`
role labels; the request body never carries a trusted user id or roles. The role labels are the "groups" that
config/rbac.v3.yaml maps to v3 roles (`group_roles`).
"""
# NOTE: no `from __future__ import annotations` here, on purpose. slowapi (the backend's rate limiter) wraps each route function
# with functools.wraps; FastAPI 0.115 then resolves STRING annotations in the wrapper's module and fails to find
# `UiChatRequest` / `Request`, so it treats `body` and `request` as missing query parameters (422 "Field required").
# Real (non-string) annotations avoid that.
import logging
import time
from contextlib import asynccontextmanager
from typing import Any, Callable

from fastapi import APIRouter, Depends, FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel, Field

from ..api.service import ChatService, Identity
from .stream import stream_chat
from .ui_contract import to_ui_body

log = logging.getLogger(__name__)

MAX_QUERY_CHARS = 4000
MAX_ID_CHARS = 128
HISTORY_MAX = 50


class UiChatRequest(BaseModel):
    """The UI's request body (unchanged): query, session_id, conversation_id, clarifications."""
    query: str = Field(min_length=1, max_length=MAX_QUERY_CHARS)
    session_id: str | None = Field(default=None, max_length=MAX_ID_CHARS)
    conversation_id: str | None = Field(default=None, max_length=MAX_ID_CHARS)
    clarifications: Any = None


class ClearContextRequest(BaseModel):
    conversation_id: str | None = Field(default=None, max_length=MAX_ID_CHARS)


def question_text(req: UiChatRequest) -> str:
    """The question sent to v3. Clarification answers from the UI are appended as plain text (v3 reads them with the
    conversation history)."""
    q = req.query.strip()
    c = req.clarifications
    if not c:
        return q
    if isinstance(c, str):
        extra = c
    elif isinstance(c, dict):
        extra = "; ".join(f"{k}: {v}" for k, v in c.items() if v not in (None, ""))
    elif isinstance(c, list):
        parts = []
        for item in c:
            if isinstance(item, dict):
                parts.append(" ".join(str(v) for v in item.values() if v not in (None, "")))
            elif item not in (None, ""):
                parts.append(str(item))
        extra = "; ".join(p for p in parts if p)
    else:
        extra = str(c)
    return f"{q}\n(Clarification: {extra})" if extra else q


def identity_from_user(user: dict[str, Any], agent_roles: Callable[[dict[str, Any]], Any]) -> Identity:
    """Entra object id (oid, else sub) + the backend's resolved role labels."""
    user_id = str(user.get("oid") or user.get("sub") or "")
    if not user_id:
        raise HTTPException(status_code=401, detail="No user identity on the request")
    roles = agent_roles(user) or []
    return Identity(user_id=user_id, groups=[str(r) for r in roles])


def history_body(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """The UI's FinanceChatHistoryWireItem list (it groups the items itself). Never any SQL (`generated_sql` is null) and
    no KPI explanation (the field is omitted)."""
    out = []
    for r in rows:
        when = r.get("created_at")
        out.append({
            "conversation_id": r.get("conversation_id"),
            "message_time": when.isoformat() if hasattr(when, "isoformat") else when,
            "user_question": r.get("question_text") or "",
            "answer": r.get("answer_text") or "",
            "source_used": None,
            "resolved_question": r.get("standalone_question"),
            "generated_sql": None,
            "category": None,
            "citation": None,
            "data_row_count": r.get("result_row_count"),
            "status": "answered" if r.get("status") in ("answered", "partial") else r.get("status"),
        })
    return out


def create_backend_router(
    service: ChatService,
    *,
    get_current_user: Callable[..., Any],
    agent_roles: Callable[[dict[str, Any]], Any],
    rate_limit: Callable[[Callable[..., Any]], Callable[..., Any]] | None = None,
) -> APIRouter:
    """`rate_limit` is the backend's decorator, e.g. `limiter.limit("10/minute")` (slowapi needs `request`)."""
    router = APIRouter(tags=["finance-chat"])
    limit = rate_limit or (lambda fn: fn)

    async def chat(request: Request, body: UiChatRequest, user: dict = Depends(get_current_user)) -> JSONResponse:
        who = identity_from_user(user, agent_roles)
        started = time.monotonic()
        try:
            env = await service.chat(question_text(body), who, conversation_id=body.conversation_id)
        except Exception as exc:  # noqa: BLE001
            log.exception("finance chat failed: %s", type(exc).__name__)
            return JSONResponse(status_code=500, content={"error": "internal_error",
                                                          "message": "The finance assistant could not answer this question."})
        return JSONResponse(to_ui_body(env, query=body.query, user_id=who.user_id, session_id=body.session_id,
                                       total_ms=(time.monotonic() - started) * 1000, domain_labels=service.access.domains))

    async def chat_stream(request: Request, body: UiChatRequest, user: dict = Depends(get_current_user)) -> StreamingResponse:
        who = identity_from_user(user, agent_roles)
        events = stream_chat(service, query=question_text(body), display_query=body.query, identity=who,
                             conversation_id=body.conversation_id, session_id=body.session_id,
                             is_disconnected=request.is_disconnected)
        return StreamingResponse(events, media_type="text/event-stream",
                                 headers={"Cache-Control": "no-cache", "Connection": "keep-alive",
                                          "X-Accel-Buffering": "no"})

    async def history(request: Request, limit_: int = Query(5, alias="limit", ge=1, le=HISTORY_MAX),
                      threads: bool = False, user: dict = Depends(get_current_user)) -> list[dict[str, Any]]:
        """The caller's recent exchanges, newest first. `threads=true`: the most recent `limit` conversations with all
        their fetched exchanges; otherwise the last `limit` exchanges."""
        who = identity_from_user(user, agent_roles)
        if service.store is None:
            return []
        try:
            rows = await service.store.user_history(who.user_id, limit=limit_ * (8 if threads else 1))
        except Exception as exc:  # noqa: BLE001
            log.warning("history read failed: %s", type(exc).__name__)
            raise HTTPException(status_code=503, detail="History is not available right now") from exc
        if threads:
            keep = list(dict.fromkeys(r.get("conversation_id") for r in rows))[:limit_]
            rows = [r for r in rows if r.get("conversation_id") in keep]
        return history_body(rows)

    async def clear_context(request: Request, body: ClearContextRequest, user: dict = Depends(get_current_user)) -> JSONResponse:
        """The UI's "Clear context" button. The conversation and its history stay; only the context used for answering
        is reset."""
        who = identity_from_user(user, agent_roles)
        try:
            result = await service.clear_context(body.conversation_id, who)
        except PermissionError:
            return JSONResponse(status_code=403, content={"status": "error", "message": "This conversation belongs to another user."})
        except Exception as exc:  # noqa: BLE001 - e.g. the context_start_turn column is missing (logged with the fix)
            log.error("clear context failed: %s", exc)
            return JSONResponse(status_code=503, content={"status": "error",
                                                          "message": "The context could not be cleared right now."})
        return JSONResponse({"status": "success", **result})

    router.add_api_route("/finance-chat", limit(chat), methods=["POST"])
    router.add_api_route("/finance-chat/stream", limit(chat_stream), methods=["POST"])
    router.add_api_route("/finance-chat/history", limit(history), methods=["GET"])
    router.add_api_route("/finance-chat/clear-context", limit(clear_context), methods=["POST"])
    return router


def install_backend(
    app: FastAPI,
    *,
    get_current_user: Callable[..., Any],
    agent_roles: Callable[[dict[str, Any]], Any],
    rate_limit: Callable[[Callable[..., Any]], Callable[..., Any]] | None = None,
    prefix: str = "/api/invoke",
    service: ChatService | None = None,
    warm: bool | None = None,
    mount_v3_routes: bool = True,
) -> ChatService:
    """One call in the backend's main.py:
    - the finance-chat routes at `prefix` (the UI's existing URLs),
    - optionally /v3 (health, cards, file downloads) with the same Entra identity,
    - startup warm-up after the app's own startup, aiops write flush on shutdown (via mount_v3)."""
    from ..api.app import build_service, mount_v3

    svc = service or build_service()

    async def v3_identity(user: dict = Depends(get_current_user)) -> Identity:
        return identity_from_user(user, agent_roles)

    app.include_router(create_backend_router(svc, get_current_user=get_current_user, agent_roles=agent_roles,
                                             rate_limit=rate_limit), prefix=prefix)
    if mount_v3_routes:
        mount_v3(app, svc, identity=v3_identity, warm=warm)
    else:  # still warm up and flush on shutdown
        _wrap_lifespan(app, svc, warm)
    return svc


def _wrap_lifespan(app: FastAPI, svc: ChatService, warm: bool | None) -> None:
    previous = app.router.lifespan_context
    do_warm = svc.orchestrator.settings.warm_up_on_start if warm is None else warm

    @asynccontextmanager
    async def lifespan(a: FastAPI):
        async with previous(a) as state:
            if do_warm:
                await svc.warm_up()
            try:
                yield state
            finally:
                await svc.close()

    app.router.lifespan_context = lifespan
