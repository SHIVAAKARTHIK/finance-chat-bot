"""Live: one ADRA question through /v3/chat writes one conversation row, one message row and event rows.
RUN_LIVE=1 only. Set AIOPS_CREATE_TABLES=1 to create the aiops tables first if they do not exist."""
from __future__ import annotations

import os

import httpx
import pytest

pytestmark = [pytest.mark.live, pytest.mark.skipif(os.getenv("RUN_LIVE") != "1", reason="live test: set RUN_LIVE=1")]


async def test_chat_writes_aiops_rows():
    from fastapi import FastAPI

    from finchat_agents.access import Role
    from finchat_agents.api.app import build_service
    from finchat_agents.api.router import create_router
    from finchat_agents.api.service import Identity

    service = build_service()
    assert service.store is not None, "aiops storage is not configured (DATABRICKS_SERVER_HOSTNAME / HTTP_PATH / AZURE_*)"
    if os.getenv("AIOPS_CREATE_TABLES") == "1":
        await service.store.ensure_tables()
    # the live test user gets finance_all through the role mapping, whatever rbac.v3.yaml's users block holds
    service.access.users["live-test-user"] = "finance_all"

    app = FastAPI()
    app.include_router(create_router(service), prefix="/v3")
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://t", timeout=300) as client:
        r = await client.post("/v3/chat", json={"message": "How many account reconciliations are in ADRA in total?",
                                                "user_id": "live-test-user"})
    body = r.json()
    assert r.status_code == 200 and body["status"] == "answered", body
    await service.writer.flush(timeout=120)
    assert not service.writer.failures, service.writer.failures

    q = service.store.executor.query
    cid, mid = body["conversation_id"], body["message_id"]
    convs = await q(f"SELECT turn_count FROM {service.store.fqn('finance_chat_conversations')} WHERE conversation_id = :c", {"c": cid})
    msgs = await q(f"SELECT status, answer_path, sql_source FROM {service.store.fqn('finance_chat_messages')} WHERE message_id = :m", {"m": mid})
    events = await q(f"SELECT COUNT(*) AS n FROM {service.store.fqn('finance_chat_message_events')} WHERE message_id = :m", {"m": mid})
    assert len(convs) == 1 and convs[0]["turn_count"] == 1
    assert len(msgs) == 1 and msgs[0]["status"] == "answered" and msgs[0]["answer_path"] == "adhoc"
    assert events[0]["n"] > 0
    await service.close()
