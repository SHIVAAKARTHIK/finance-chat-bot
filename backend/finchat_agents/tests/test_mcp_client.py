from __future__ import annotations

import datetime as dt
import json
from decimal import Decimal

import httpx
import pytest
from pydantic import SecretStr

from finchat_agents.tools.mcp_client import EntraTokenProvider, McpError, McpQueryError, McpTimeout

from .fakes import B, D, DT, L, S, FakeMcpServer, FakeTokens, make_client, statement

TYPED = (
    [("n", L), ("amt", D), ("ratio", "DOUBLE"), ("flag", B), ("day", DT), ("ts", "TIMESTAMP"), ("txt", S), ("empty", S)],
    [[97, "1981646.00", "0.5", True, "2025-02-28", "2026-10-25T04:59:14Z", "Approved ", None]],
)


async def test_query_converts_types_and_nulls():
    client = make_client(FakeMcpServer(lambda sql: TYPED))
    r = await client.query("SELECT 1")
    assert [c.name for c in r.columns] == ["n", "amt", "ratio", "flag", "day", "ts", "txt", "empty"]
    n, amt, ratio, flag, day, ts, txt, empty = r.rows[0]
    assert n == 97 and amt == Decimal("1981646.00") and ratio == 0.5 and flag is True
    assert day == dt.date(2025, 2, 28) and ts.year == 2026 and ts.tzinfo is not None
    assert txt == "Approved " and empty is None


async def test_text_content_fallback_and_sse():
    for server in (FakeMcpServer(lambda s: TYPED, text_only=True), FakeMcpServer(lambda s: TYPED, sse=True)):
        r = await make_client(server).query("SELECT 1")
        assert r.rows[0][0] == 97


async def test_request_shape_and_allowlist():
    server = FakeMcpServer(lambda s: ([("n", L)], [[1]]))
    client = make_client(server)
    await client.query("SELECT 1")
    req = server.requests[0]
    assert req["body"]["method"] == "tools/call" and req["body"]["params"]["name"] == "execute_sql_read_only"
    assert req["headers"]["authorization"] == "Bearer token-1"
    assert "text/event-stream" in req["headers"]["accept"]
    for forbidden in ("execute_sql", "tools/list", "drop_table"):
        with pytest.raises(McpError, match="not allowed"):
            await client.call_tool(forbidden, {"query": "DROP TABLE x"})
    assert len(server.requests) == 1  # nothing was sent for forbidden tools


async def test_poll_until_succeeded():
    server = FakeMcpServer(lambda s: ([("n", L)], [[97]]), pending_polls=3)
    slept = []

    async def sleep(d):
        slept.append(d)

    r = await make_client(server, sleep=sleep, poll_interval_s=0.5).query("SELECT COUNT(*)")
    assert r.rows == [[97]]
    names = [q["body"]["params"]["name"] for q in server.requests]
    assert names == ["execute_sql_read_only", "poll_sql_result", "poll_sql_result", "poll_sql_result"]
    assert slept == [0.25, 0.5, 0.5]  # short first waits, never longer than poll_interval_s


async def test_poll_timeout():
    server = FakeMcpServer(lambda s: ([("n", L)], [[1]]), pending_polls=100)
    t = {"now": 0.0}

    async def sleep(d):
        t["now"] += d

    client = make_client(server, sleep=sleep, clock=lambda: t["now"], poll_interval_s=1.0, timeout_s=3)
    with pytest.raises(McpTimeout):
        await client.query("SELECT 1")


async def test_failed_statement_is_a_fixable_query_error():
    def boom(sql):
        raise ValueError("[UNRESOLVED_COLUMN] A column with name `X` cannot be resolved.")

    with pytest.raises(McpQueryError, match="UNRESOLVED_COLUMN"):
        await make_client(FakeMcpServer(boom)).query("SELECT X FROM t")


async def test_retry_once_with_fresh_token_on_401():
    server = FakeMcpServer(lambda s: ([("n", L)], [[1]]), reject_tokens={"token-1"})
    tokens = FakeTokens()
    r = await make_client(server, tokens).query("SELECT 1")
    assert r.rows == [[1]] and tokens.calls == [False, True]
    assert [q["headers"]["authorization"] for q in server.requests] == ["Bearer token-1", "Bearer token-2"]


async def test_truncated_flag():
    server = FakeMcpServer(lambda s: statement([("n", L)], [[1]], truncated=True))
    assert (await make_client(server).query("SELECT 1")).truncated


async def test_entra_token_cache_and_early_refresh():
    posts = []

    def handler(request: httpx.Request) -> httpx.Response:
        posts.append(dict(x.split("=", 1) for x in request.content.decode().split("&")))
        return httpx.Response(200, json={"access_token": f"tok{len(posts)}", "expires_in": 3600})

    now = {"t": 1000.0}
    provider = EntraTokenProvider("tenant", "client", SecretStr("s3cret"), "scope/.default",
                                  http=httpx.AsyncClient(transport=httpx.MockTransport(handler)), clock=lambda: now["t"])
    assert await provider.get_token() == "tok1"
    now["t"] += 3000  # 10 minutes before expiry: still cached
    assert await provider.get_token() == "tok1"
    now["t"] += 400  # inside the 5-minute margin: refresh
    assert await provider.get_token() == "tok2"
    assert await provider.get_token(force_refresh=True) == "tok3"
    assert posts[0]["grant_type"] == "client_credentials" and posts[0]["scope"] == "scope%2F.default"
    assert "s3cret" not in repr(provider.__dict__.get("_secret"))


async def test_token_failure_does_not_leak_secret():
    provider = EntraTokenProvider("t", "c", SecretStr("s3cret"), "scope",
                                  http=httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(400, json={}))))
    with pytest.raises(McpError) as ei:
        await provider.get_token()
    assert "s3cret" not in str(ei.value)


async def test_warm_up():
    assert await make_client(FakeMcpServer(lambda s: ([("warm_up", L)], [[1]]))).warm_up() is True

    def boom(sql):
        raise ValueError("warehouse stopped")

    assert await make_client(FakeMcpServer(boom)).warm_up() is False


def test_json_rpc_error_is_mcp_error():
    async def run():
        def handler(request):
            body = json.loads(request.content)
            return httpx.Response(200, json={"jsonrpc": "2.0", "id": body["id"], "error": {"code": -1, "message": "bad"}})

        from finchat_agents.tools.mcp_client import DatabricksMcpClient

        client = DatabricksMcpClient("https://x", FakeTokens(), http=httpx.AsyncClient(transport=httpx.MockTransport(handler)))
        with pytest.raises(McpError, match="bad"):
            await client.query("SELECT 1")

    import asyncio

    asyncio.run(run())


# ---------------------------------------------------------------- transient connection errors are retried

class FlakyThenServer:
    """Raises `error` for the first `failures` requests, then behaves like the fake MCP server."""

    def __init__(self, server, failures, error):
        self.server, self.failures, self.error, self.calls = server, failures, error, 0

    def __call__(self, request):
        self.calls += 1
        if self.calls <= self.failures:
            raise self.error("simulated network drop", request=request)
        return self.server(request)


def flaky_client(failures, error=None):
    import httpx

    from .fakes import FakeTokens, data_responder
    from finchat_agents.tools.mcp_client import DatabricksMcpClient

    server = FakeMcpServer(data_responder)
    flaky = FlakyThenServer(server, failures, error or httpx.ConnectError)
    delays = []

    async def sleep(seconds):
        delays.append(seconds)

    client = DatabricksMcpClient("https://fake/api/2.0/mcp/sql", FakeTokens(), http=httpx.AsyncClient(transport=httpx.MockTransport(flaky)),
                                 sleep=sleep)
    return client, flaky, delays


async def test_connect_error_is_retried_with_backoff_then_succeeds():
    client, flaky, delays = flaky_client(2)
    result = await client.query("SELECT COUNT(*) AS n FROM lakehouse_mvpai.silver.adra_account_facts")
    assert result.rows == [[97]] and flaky.calls == 3 and delays == [1.0, 3.0]


async def test_connect_error_gives_up_after_three_attempts_with_a_plain_error():
    import httpx

    client, flaky, delays = flaky_client(99, httpx.ConnectTimeout)
    with pytest.raises(McpError, match="MCP request failed: ConnectTimeout"):
        await client.query("SELECT 1")
    assert flaky.calls == 3 and delays == [1.0, 3.0]


async def test_a_read_timeout_is_not_retried():
    import httpx

    client, flaky, delays = flaky_client(99, httpx.ReadTimeout)  # a slow statement must not be submitted three times
    with pytest.raises(McpError, match="ReadTimeout"):
        await client.query("SELECT 1")
    assert flaky.calls == 1 and delays == []
