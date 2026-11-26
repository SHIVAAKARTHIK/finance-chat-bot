"""GET /v3/files/{conversation}/{file_name}: owner-only downloads, strict name checks, no path traversal."""
from __future__ import annotations

from types import SimpleNamespace

import httpx
import pytest
from fastapi import FastAPI

from finchat_agents.access import AccessConfig, Role, UserAccess
from finchat_agents.api.router import create_router
from finchat_agents.api.service import Identity
from finchat_agents.config import Settings
from finchat_agents.runtime.tools import Budget, RunContext, ToolContext
from finchat_agents.tools.actions import make_action_tools
from finchat_agents.tools.run_sql import SqlResult, register_result
from finchat_agents.tracing import MemorySink, Tracer

ACCESS = AccessConfig({
    "domains": {"recon": "ADRA"},
    "roles": {"finance_all": {"domains": ["*"]}},
    "users": {"owner": "finance_all", "colleague": "finance_all"},
})


async def make_file(tmp_path) -> dict:
    run = RunContext(tracer=Tracer([MemorySink()], message_id="m1"), budget=Budget(),
                     user=UserAccess(user_id="owner", role=Role(name="finance_all", domains=["*"])))
    run.extras["conversation_id"] = "conv-1"
    register_result(run, SqlResult(columns=["n"], rows=[[97]], row_count=1))
    tool = next(t for t in make_action_tools(tmp_path) if t.name == "export_excel")
    await tool.handler({"title": "Count", "tables": [{"result_id": "r1"}]}, ToolContext(run=run, agent="a", step=1, call_id="c"))
    return run.extras["files"][0]


def client_for(tmp_path, identity=None) -> httpx.AsyncClient:
    service = SimpleNamespace(access=ACCESS, orchestrator=SimpleNamespace(settings=Settings(_env_file=None, output_dir=str(tmp_path), allow_request_identity=True)))
    app = FastAPI()
    app.include_router(create_router(service, identity=identity) if identity else create_router(service), prefix="/v3")
    return httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://t")


async def test_owner_downloads_file(tmp_path):
    f = await make_file(tmp_path)
    assert f["url"] == f"/v3/files/conv-1/{f['name']}"
    async with client_for(tmp_path) as c:
        r = await c.get(f["url"], params={"user_id": "owner"})
    assert r.status_code == 200
    assert r.content == open(f["path"], "rb").read()
    assert r.headers["content-type"].startswith("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    assert f'filename="{f["name"]}"' in r.headers["content-disposition"] and r.headers["cache-control"] == "private, no-store"


async def test_others_get_404_and_identity_is_required(tmp_path):
    f = await make_file(tmp_path)
    async with client_for(tmp_path) as c:
        assert (await c.get(f["url"], params={"user_id": "colleague"})).status_code == 404  # has access, not the owner
        assert (await c.get(f["url"], params={"user_id": "stranger"})).status_code == 404  # no role at all
        assert (await c.get(f["url"])).status_code == 401
        assert (await c.get("/v3/files/conv-1/missing_file.xlsx", params={"user_id": "owner"})).status_code == 404


@pytest.mark.parametrize("url", [
    "/v3/files/conv-1/..%2F..%2Fconfig.py",
    "/v3/files/..%2F..%2Fconfig/rbac.v3.xlsx",
    "/v3/files/conv-1/{name}.meta.json",
    "/v3/files/conv-1/secret.txt",
    "/v3/files/conv%201/{name}",
])
async def test_traversal_and_odd_names_are_refused(tmp_path, url):
    f = await make_file(tmp_path)
    (tmp_path / "config").mkdir()
    (tmp_path / "config" / "rbac.v3.xlsx").write_text("x")
    async with client_for(tmp_path) as c:
        r = await c.get(url.replace("{name}", f["name"]), params={"user_id": "owner"})
    assert r.status_code == 404


async def test_auth_identity_wins_over_query(tmp_path):
    f = await make_file(tmp_path)

    async def entra():
        return Identity(user_id="colleague")

    async with client_for(tmp_path, identity=entra) as c:
        assert (await c.get(f["url"], params={"user_id": "owner"})).status_code == 404  # the query cannot impersonate
