"""v3 chat API. Mount on the existing app:

    from finchat_agents.api.router import create_router
    app.include_router(create_router(service), prefix="/v3")

POST /v3/chat         JSON request -> JSON envelope (SPEC section 7)
POST /v3/chat/stream  SSE: `step` events while working, then one `final` event with the envelope
POST /v3/conversations/{conversation_id}/clear-context   later questions ignore everything asked so far
GET  /v3/files/{conversation}/{file}, GET /v3/cards
GET  /v3/health       readiness (MCP, Bedrock, aiops; 503 unless green)   GET /v3/health/live  liveness

Identity: pass `identity=` (a FastAPI dependency returning Identity from the existing Entra auth). Without a verified
identity every route except health answers 401. For local testing only, ALLOW_REQUEST_IDENTITY=true trusts the
user_id / groups sent in the request.
"""
from __future__ import annotations

import asyncio
import json
import logging
from typing import Any, AsyncIterator, Awaitable, Callable

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel, Field

from ..agents.orchestrator import AnswerEnvelope
from ..guardrails.audit import log_request
from ..tracing.events import TraceEvent
from .service import ChatService, Identity

log = logging.getLogger(__name__)

MAX_MESSAGE_CHARS = 4000


class ChatRequest(BaseModel):
    conversation_id: str | None = None
    message: str = Field(min_length=1, max_length=MAX_MESSAGE_CHARS)
    user_id: str | None = Field(default=None, description="Entra object id; used only with ALLOW_REQUEST_IDENTITY=true")
    groups: list[str] | None = None


IdentityProvider = Callable[..., Awaitable[Identity | None]]


async def body_identity() -> None:
    """Default: no identity from auth (refused unless ALLOW_REQUEST_IDENTITY=true)."""
    return None


class QueueSink:
    """Trace sink feeding the SSE stream. Only a safe subset of each event is sent (no payloads, no SQL). With
    `hide_internals` (company guardrails: no pipeline details) agent and tool names are not sent either."""

    def __init__(self, hide_internals: bool = False) -> None:
        self.queue: asyncio.Queue[dict[str, Any]] = asyncio.Queue()
        self.hide_internals = hide_internals

    async def write(self, event: TraceEvent) -> None:
        if event.type in ("agent_start", "agent_end", "llm_call", "tool_call", "route", "answer"):
            step: dict[str, Any] = {"type": event.type, "agent": event.agent, "status": event.status}
            if event.type == "tool_call":
                step["tool"] = event.name
            if event.type == "route":
                step["classification"] = event.payload.get("classification")
            if event.duration_ms is not None:
                step["duration_ms"] = event.duration_ms
            if self.hide_internals:
                step = {k: v for k, v in step.items() if k in ("type", "status", "duration_ms")}
            await self.queue.put(step)


def _sse(event: str, data: Any) -> str:
    return f"event: {event}\ndata: {json.dumps(data, default=str, ensure_ascii=False)}\n\n"


def create_router(service: ChatService, identity: IdentityProvider = body_identity) -> APIRouter:
    router = APIRouter(tags=["finance-chat-v3"])
    trust_request = service.orchestrator.settings.allow_request_identity
    if trust_request:
        log.warning("ALLOW_REQUEST_IDENTITY=true: user ids sent in requests are trusted (local testing only)")

    def caller(auth: Identity | None, user_id: str | None, groups: list[str] | None = None) -> Identity:
        if auth is not None:  # the verified login always wins over anything in the request
            return auth
        if not trust_request:
            log_request("login", "block", "verified_login", "request without a verified login", user_id)
            raise HTTPException(status_code=401, detail="A verified login is required")
        if not user_id:
            raise HTTPException(status_code=401, detail="user_id is required (no authenticated identity on the request)")
        return Identity(user_id=user_id, groups=groups or [])

    @router.post("/chat", response_model=AnswerEnvelope)
    async def chat(req: ChatRequest, auth: Identity | None = Depends(identity)) -> AnswerEnvelope:
        who = caller(auth, req.user_id, req.groups)
        return await service.chat(req.message, who, conversation_id=req.conversation_id)

    @router.post("/conversations/{conversation_id}/clear-context")
    async def clear_context(conversation_id: str, user_id: str | None = None,
                            auth: Identity | None = Depends(identity)) -> dict[str, Any]:
        who = caller(auth, user_id)
        try:
            return await service.clear_context(conversation_id, who)
        except PermissionError as exc:
            raise HTTPException(status_code=403, detail=str(exc)) from exc
        except Exception as exc:  # noqa: BLE001 - e.g. the context_start_turn column is missing
            raise HTTPException(status_code=503, detail=str(exc)[:500]) from exc

    @router.post("/chat/stream")
    async def chat_stream(req: ChatRequest, request: Request, auth: Identity | None = Depends(identity)) -> StreamingResponse:
        who = caller(auth, req.user_id, req.groups)
        sink = QueueSink(hide_internals=getattr(service.orchestrator, "guardrails", None) is not None)

        async def events() -> AsyncIterator[str]:
            task = asyncio.create_task(service.chat(req.message, who, conversation_id=req.conversation_id, extra_sinks=[sink]))
            try:
                while not task.done() or not sink.queue.empty():
                    try:
                        step = await asyncio.wait_for(sink.queue.get(), timeout=0.25)
                        yield _sse("step", step)
                    except asyncio.TimeoutError:
                        if await request.is_disconnected():
                            task.cancel()
                            return
                env = await task
                yield _sse("final", env.model_dump(mode="json"))
            finally:
                if not task.done():
                    task.cancel()

        return StreamingResponse(events(), media_type="text/event-stream",
                                 headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})

    @router.get("/files/{conversation}/{file_name}")
    async def download_file(conversation: str, file_name: str, user_id: str | None = None,
                            auth: Identity | None = Depends(identity)):
        """Download a file created by export_excel / save_report. Only its creator may download it."""
        from .files import file_response, not_found, resolve_file

        identity_ = caller(auth, user_id)
        who = identity_.user_id
        if not service.access.user_access(who, identity_.groups).has_access:
            log_request("file_download", "block", "role_access", f"no role; asked for {file_name}", who)
            raise not_found()
        settings = service.orchestrator.settings
        try:
            path = resolve_file(settings.resolve_path(settings.output_dir), conversation, file_name, who)
        except HTTPException:
            log_request("file_download", "block", "own_files_only", f"not the owner, or no such file: {file_name}", who)
            raise
        log_request("file_download", "allow", "own_files_only", file_name, who)
        return file_response(path)

    @router.get("/cards")
    async def summary_cards(user_id: str | None = None, auth: Identity | None = Depends(identity)) -> dict[str, Any]:
        """Active summary cards for the caller's role domains (filtered at read time)."""
        from ..storage.summary_store import SummaryStore, SummaryTablesMissing

        identity_ = caller(auth, user_id)
        access = service.access.user_access(identity_.user_id, identity_.groups)
        if not access.has_access:
            return {"cards": []}
        if service.store is None:
            raise HTTPException(status_code=503, detail="Card storage is not configured")
        domains = None if "*" in access.domains else access.domains
        try:
            rows = await SummaryStore.from_store(service.store).active_cards(domains)
        except Exception as exc:
            raise HTTPException(status_code=503, detail="Summary cards are not available yet") from exc
        cards = [r for r in rows if access.role.allows_domain(r.get("domain"))]  # second check in code
        return {"cards": [{k: (str(v) if v is not None and not isinstance(v, (str, int, float, bool)) else v)
                           for k, v in r.items()} for r in cards]}

    @router.get("/health")
    async def health_check(refresh: bool = False) -> JSONResponse:
        """Readiness: MCP, Bedrock (both models) and aiops connectivity. 200 when every enabled check is ok, else 503.
        Cached for HEALTH_CACHE_SECONDS; `?refresh=true` re-runs the checks. No secrets, hosts or error messages."""
        from .service import health

        result = await service.health_checker.run(force=refresh)
        body = {**result, **health(service)}
        return JSONResponse(body, status_code=200 if result["status"] == "ok" else 503)

    @router.get("/health/live")
    async def liveness() -> dict[str, str]:
        """Liveness for the Docker HEALTHCHECK: the process answers. Calls nothing external."""
        return {"status": "ok"}

    return router
