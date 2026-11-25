"""Task 10: health checks, startup warm-up via mount_v3, smoke script, image exclusions."""
from __future__ import annotations

import asyncio
import json
from pathlib import Path

import httpx
from fastapi import FastAPI

from finchat_agents.api.app import create_app, mount_v3
from finchat_agents.api.health import HealthChecker
from finchat_agents.api.service import ChatService
from finchat_agents.deploy.smoke import run_smoke
from finchat_agents.llm import fake
from finchat_agents.storage.aiops import AiopsStore

from .test_agents import make_orch
from .test_storage_api import ACCESS, FakeExecutor, kb  # noqa: F401  (kb fixture)

PKG = Path(__file__).resolve().parents[1]
SECRETISH = ("secret", "token", "https://", "password", "Bearer")


def service_with(kb, *, sql_script, resp_script, executor=None, mcp_fail=False):
    orch, sql_p, resp_p, server, _ = make_orch(kb, sql_script, resp_script)
    if mcp_fail:
        async def broken(*_a, **_k):
            return False
        orch.deps.mcp.warm_up = broken
    store = AiopsStore(executor) if executor is not None else None
    return ChatService(orch, ACCESS, store=store), sql_p, resp_p, server


# ---------------------------------------------------------------- HealthChecker

async def test_all_ok_and_disabled_is_green():
    async def ok():
        return True
    h = HealthChecker({"a": ok, "b": None})
    r = await h.run()
    assert r["status"] == "ok" and r["checks"]["a"]["status"] == "ok" and r["checks"]["b"] == {"status": "disabled"}


async def test_failure_shows_error_type_only_never_message():
    async def boom():
        raise RuntimeError("connect to https://adb-123.azuredatabricks.net failed, token=abc secret")
    async def ok():
        return None
    r = await HealthChecker({"mcp": boom, "bedrock": ok}).run()
    assert r["status"] == "degraded" and r["checks"]["mcp"] == {"status": "down", "error": "RuntimeError", "ms": r["checks"]["mcp"]["ms"]}
    dumped = json.dumps(r)
    assert not any(s in dumped for s in SECRETISH) and "adb-123" not in dumped


async def test_all_down_and_timeout_and_false_result():
    async def slow():
        await asyncio.sleep(1)
    async def false():
        return False
    r = await HealthChecker({"a": slow, "b": false}, timeout_s=0.01).run()
    assert r["status"] == "down" and r["checks"]["a"]["error"] == "timeout" and r["checks"]["b"]["status"] == "down"


async def test_results_are_cached_until_refresh():
    calls = []
    now = [0.0]
    async def ok():
        calls.append(1)
    h = HealthChecker({"a": ok}, cache_s=60, clock=lambda: now[0])
    assert (await h.run())["cached"] is False
    now[0] = 30
    assert (await h.run())["cached"] is True and len(calls) == 1
    assert (await h.run(force=True))["cached"] is False and len(calls) == 2
    now[0] = 200
    await h.run()
    assert len(calls) == 3


# ---------------------------------------------------------------- build_checker on a real ChatService

async def test_service_checks_ping_both_models_mcp_and_aiops(kb):
    ex = FakeExecutor()
    svc, sql_p, resp_p, server = service_with(kb, sql_script=[fake.text("OK")], resp_script=[fake.text("OK")], executor=ex)
    r = await svc.warm_up()
    assert r["status"] == "ok", r
    assert set(r["checks"]) == {"mcp", "bedrock_sql", "bedrock_response", "aiops"}
    assert len(sql_p.calls) == 1 and sql_p.calls[0]["tools"] == [] and len(resp_p.calls) == 1
    assert any("SELECT 1" in q for q in server.queries)
    assert ex.queries and "lakehouse_mvpai.aiops.finance_chat_conversations" in ex.queries[0][0]
    assert ex.statements == []  # health never writes


async def test_service_without_store_reports_aiops_disabled_and_bedrock_down(kb):
    svc, *_ = service_with(kb, sql_script=[RuntimeError("throttled")], resp_script=[fake.text("OK")], mcp_fail=True)
    r = await svc.warm_up()
    c = r["checks"]
    assert c["aiops"] == {"status": "disabled"} and c["bedrock_sql"]["status"] == "down" and c["mcp"]["status"] == "down"
    assert c["bedrock_response"]["status"] == "ok" and r["status"] == "degraded"


async def test_health_endpoint_200_when_green_503_otherwise(kb):
    svc, *_ = service_with(kb, sql_script=[fake.text("OK"), RuntimeError("x")], resp_script=[fake.text("OK"), fake.text("OK")])
    app = FastAPI()
    mount_v3(app, svc, warm=False)
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://t") as client:
        assert (await client.get("/v3/health/live")).json() == {"status": "ok"}
        r = await client.get("/v3/health")
        assert r.status_code == 200 and r.json()["status"] == "ok" and r.json()["storage"] == "disabled"
        r = await client.get("/v3/health", params={"refresh": "true"})
        assert r.status_code == 503 and r.json()["checks"]["bedrock_sql"]["status"] == "down"


# ---------------------------------------------------------------- mount_v3 lifespan

async def test_mount_v3_warms_up_after_existing_startup_and_flushes_on_shutdown(kb):
    order: list[str] = []
    svc, sql_p, resp_p, _ = service_with(kb, sql_script=[fake.text("OK")], resp_script=[fake.text("OK")], executor=FakeExecutor())

    from contextlib import asynccontextmanager

    @asynccontextmanager
    async def existing(app):
        order.append("existing-start")
        yield
        order.append("existing-stop")

    app = FastAPI(lifespan=existing)
    original_close = svc.close

    async def close():
        order.append("v3-close")
        await original_close()
    svc.close = close
    mount_v3(app, svc, warm=True)
    async with app.router.lifespan_context(app):
        order.append("serving")
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://t") as client:
            assert (await client.get("/v3/health/live")).status_code == 200  # /v3 routes are mounted
    assert order == ["existing-start", "serving", "v3-close", "existing-stop"]
    assert len(sql_p.calls) == 1 and len(resp_p.calls) == 1  # warm-up pinged both models
    assert svc.health_checker._cached["status"] == "ok"  # warm-up primed the health cache


async def test_warm_up_failure_never_blocks_startup(kb):
    svc, *_ = service_with(kb, sql_script=[RuntimeError("down")], resp_script=[RuntimeError("down")], mcp_fail=True)
    app = create_app(svc, warm=True)
    async with app.router.lifespan_context(app):
        pass  # no exception


# ---------------------------------------------------------------- smoke script

def smoke_app(*, health_status=200, answer_status="answered") -> FastAPI:
    app = FastAPI()

    @app.get("/v3/health/live")
    async def live():
        return {"status": "ok"}

    @app.get("/v3/health")
    async def health():
        from fastapi.responses import JSONResponse
        return JSONResponse({"status": "ok" if health_status == 200 else "degraded",
                             "checks": {"mcp": {"status": "ok"}}}, status_code=health_status)

    @app.post("/v3/chat")
    async def chat(body: dict):
        assert body["user_id"] == "smoke-user"
        return {"status": answer_status, "answer": "Some answer."}

    return app


async def test_smoke_passes_on_green_and_fails_otherwise():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=smoke_app()), base_url="http://t") as c:
        ok, lines = await run_smoke(c, "smoke-user")
    assert ok and lines[1].startswith("health: ok") and len(lines) == 2 + 4
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=smoke_app(health_status=503)), base_url="http://t") as c:
        assert (await run_smoke(c, "smoke-user"))[0] is False
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=smoke_app(answer_status="failed")), base_url="http://t") as c:
        ok, lines = await run_smoke(c, "smoke-user")
    assert not ok and any(l.startswith("FAIL") for l in lines)


# ---------------------------------------------------------------- image contents

def test_image_excludes_secrets_and_local_data():
    ignore = (PKG / "deploy" / "Dockerfile.v3.dockerignore").read_text(encoding="utf-8").splitlines()
    for entry in ("**/.env", "finchat_agents/traces", "finchat_agents/outputs", "finchat_agents/tests",
                  "finchat_agents/eval", "finchat_agents/reference", ".venv"):
        assert entry in ignore
    dockerfile = (PKG / "deploy" / "Dockerfile.v3").read_text(encoding="utf-8")
    assert "ENV AWS_" not in dockerfile and "AZURE_CLIENT_SECRET" not in dockerfile and "COPY .env" not in dockerfile
    assert "/v3/health/live" in dockerfile


def test_runtime_never_imports_excluded_folders():
    """eval/, tests/ and reference/ are not in the image, so runtime modules must not import them."""
    for py in PKG.rglob("*.py"):
        rel = py.relative_to(PKG).parts
        if rel[0] in {"tests", "eval", "reference", ".venv"}:
            continue
        text = py.read_text(encoding="utf-8")
        assert "finchat_agents.eval" not in text and "from ..eval" not in text and "from .tests" not in text, py
