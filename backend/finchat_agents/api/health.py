"""Connectivity checks for /v3/health and the startup warm-up: MCP (data), Bedrock (both models) and aiops (app storage).

Output never contains secrets, hosts, URLs or exception messages: only a status, the time taken and the error *type*
(the full error goes to the server log). Results are cached for `health_cache_seconds` so a load balancer or Docker
probing /v3/health does not call Bedrock on every probe.
"""
from __future__ import annotations

import asyncio
import logging
import time
from typing import Any, Awaitable, Callable

from ..llm.types import Message, ModelHandle

log = logging.getLogger(__name__)

PING_SYSTEM = "Health check. Reply with the single word OK."
PING_MAX_TOKENS = 32
CheckFn = Callable[[], Awaitable[Any]]


async def ping_model(model: ModelHandle) -> None:
    """One tiny completion; raises on any failure."""
    await model.provider.complete(PING_SYSTEM, [Message.user("ping")], [], model.model, PING_MAX_TOKENS, 0.0)


class HealthChecker:
    def __init__(self, checks: dict[str, CheckFn | None], *, timeout_s: float = 30.0, cache_s: float = 60.0,
                 clock: Callable[[], float] = time.monotonic):
        # A check set to None is reported as "disabled" (e.g. aiops when the warehouse settings are missing).
        self.checks = checks
        self.timeout_s = timeout_s
        self.cache_s = cache_s
        self._clock = clock
        self._cached: dict[str, Any] | None = None
        self._cached_at = 0.0
        self._lock = asyncio.Lock()

    async def _one(self, name: str, fn: CheckFn | None, timeout_s: float) -> dict[str, Any]:
        if fn is None:
            return {"status": "disabled"}
        t0 = time.monotonic()
        try:
            result = await asyncio.wait_for(fn(), timeout=timeout_s)
            if result is False:  # e.g. McpClient.warm_up() swallows errors and returns False
                raise RuntimeError("check returned False")
            status: dict[str, Any] = {"status": "ok"}
        except Exception as exc:  # noqa: BLE001 - every failure becomes "down"
            log.warning("health check %s failed: %s: %s", name, type(exc).__name__, exc)
            status = {"status": "down", "error": "timeout" if isinstance(exc, asyncio.TimeoutError) else type(exc).__name__}
        status["ms"] = int((time.monotonic() - t0) * 1000)
        return status

    async def run(self, *, force: bool = False, timeout_s: float | None = None) -> dict[str, Any]:
        """All checks in parallel. `force` skips the cache; the startup warm-up passes a longer timeout because a
        stopped SQL warehouse can take a few minutes to start."""
        async with self._lock:
            now = self._clock()
            if not force and self._cached is not None and now - self._cached_at < self.cache_s:
                return {**self._cached, "cached": True}
            names = list(self.checks)
            results = await asyncio.gather(*(self._one(n, self.checks[n], timeout_s or self.timeout_s) for n in names))
            checks = dict(zip(names, results))
            states = {c["status"] for c in checks.values()}
            overall = "ok" if states <= {"ok", "disabled"} else ("down" if "ok" not in states else "degraded")
            self._cached = {"status": overall, "checks": checks}
            self._cached_at = now
            return {**self._cached, "cached": False}


def build_checker(service: Any) -> HealthChecker:
    """Checks for a ChatService: mcp, bedrock_sql (Claude), bedrock_response (gpt-oss), aiops."""
    orch = service.orchestrator
    s = orch.settings
    mcp = orch.deps.mcp
    store = service.store

    async def check_mcp() -> bool:
        return await mcp.warm_up() if hasattr(mcp, "warm_up") else bool(await mcp.query("SELECT 1 AS health"))

    async def check_aiops() -> None:
        # Reads the conversations table: proves the warehouse, the token and the table grants in one cheap query.
        await store.executor.query(f"SELECT 1 AS health FROM {store.fqn('finance_chat_conversations')} LIMIT 1", {})

    return HealthChecker(
        {
            "mcp": check_mcp,
            "bedrock_sql": lambda: ping_model(orch.sql_llm),
            "bedrock_response": lambda: ping_model(orch.response_llm),
            "aiops": check_aiops if store is not None else None,
        },
        timeout_s=max(s.sql_timeout_seconds, 30.0),
        cache_s=s.health_cache_seconds,
    )
