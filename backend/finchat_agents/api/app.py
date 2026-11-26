"""Wiring from settings, and a minimal standalone app for local testing:

    cd backend
    .venv\\Scripts\\python -m uvicorn finchat_agents.api.app:app --port 8010

The existing backend should instead mount v3 on its own app (see docs/DEPLOY.md):

    from finchat_agents.api.app import mount_v3
    mount_v3(app, identity=<your Entra identity dependency>)   # routes + startup warm-up + shutdown flush
"""
from __future__ import annotations

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ..access.rbac import AccessConfig
from ..agents.orchestrator import Orchestrator
from ..config import Settings, get_settings
from ..guardrails import load_from_settings
from ..knowledge.loader import Knowledge
from ..llm.factory import response_model, sql_model
from ..storage.aiops import build_store
from ..storage.writer import BackgroundWriter
from ..tools import DataDeps, TTLCache, build_mcp_client
from ..tracing import JsonlFileSink
from .router import IdentityProvider, body_identity, create_router
from .service import ChatService

log = logging.getLogger(__name__)


def build_service(settings: Settings | None = None) -> ChatService:
    s = settings or get_settings()
    guardrails = load_from_settings(s)  # first: a missing or incomplete guardrail folder stops the start
    deps = DataDeps(kb=Knowledge.load(), mcp=build_mcp_client(s), settings=s, cache=TTLCache(s.column_values_cache_seconds),
                    guardrails=guardrails)
    sinks = [JsonlFileSink(s.resolve_path(s.trace_dir) / "events.jsonl")]
    orch = Orchestrator(deps=deps, sql_llm=sql_model(s), response_llm=response_model(s), sinks=sinks)
    store = build_store(s)
    return ChatService(orch, AccessConfig.load(s.resolve_path(s.rbac_file)), store=store,
                       writer=BackgroundWriter() if store else None)


def mount_v3(app: FastAPI, service: ChatService | None = None, *, identity: IdentityProvider = body_identity,
             warm: bool | None = None) -> ChatService:
    """Mount v3 on an existing FastAPI app (the backend's main app):

        from finchat_agents.api.app import mount_v3
        mount_v3(app, identity=<Entra identity dependency>)

    Adds the /v3 routes and wraps the app's lifespan so that, after the app's own startup, the warm-up runs
    (MCP query + Bedrock ping + aiops read; never blocks startup on failure) and, on shutdown, pending aiops writes
    are flushed. `warm` defaults to WARM_UP_ON_START.
    """
    svc = service or build_service()
    app.include_router(create_router(svc, identity=identity), prefix="/v3")
    do_warm = svc.orchestrator.settings.warm_up_on_start if warm is None else warm
    previous = app.router.lifespan_context

    @asynccontextmanager
    async def lifespan(a: FastAPI):
        async with previous(a) as state:
            if do_warm:
                result = await svc.warm_up()
                log.info("finchat v3 warm-up: %s", {k: v.get("status") for k, v in result.get("checks", {}).items()})
            try:
                yield state
            finally:
                await svc.close()

    app.router.lifespan_context = lifespan
    return svc


def create_app(service: ChatService | None = None, *, warm: bool | None = None) -> FastAPI:
    """Standalone app (local testing, or a separate v3 container)."""
    app = FastAPI(title="Finance Chat v3")
    mount_v3(app, service, warm=warm)
    return app


def __getattr__(name: str):  # `uvicorn finchat_agents.api.app:app` builds the app lazily (needs backend/.env)
    if name == "app":
        return create_app()
    raise AttributeError(name)
