"""Async JSON-RPC client for the Databricks DBSQL MCP server (see docs/MCP_NOTES.md).

- Only `execute_sql_read_only` and `poll_sql_result` can be called (hard allowlist; `execute_sql` never).
- Service-principal token (Entra client credentials), cached and refreshed ~5 minutes before expiry;
  one retry with a fresh token on HTTP 401.
- Polls until SUCCEEDED / FAILED / CANCELED or the timeout; converts typed values by type_name.
"""
from __future__ import annotations

import asyncio
import datetime as dt
import itertools
import json
import time
from decimal import Decimal, InvalidOperation
from typing import Any, Callable, Protocol

import httpx
from pydantic import BaseModel, Field, SecretStr

ALLOWED_TOOLS = frozenset({"execute_sql_read_only", "poll_sql_result"})
TOKEN_REFRESH_MARGIN_S = 300
# Polling a running statement: short waits first (most queries finish within a second), then every poll_interval_s.
FIRST_POLL_DELAYS_S = (0.25, 0.5)
# Connection-level failures are retried (backoff in seconds between attempts: 3 attempts in total).
TRANSIENT_ERRORS = (httpx.ConnectError, httpx.ConnectTimeout, httpx.ReadError, httpx.RemoteProtocolError, httpx.PoolTimeout)
CONNECT_RETRY_DELAYS_S = (1.0, 3.0)
DONE_STATES = {"SUCCEEDED", "FAILED", "CANCELED", "CLOSED"}


class McpError(Exception):
    """Transport, protocol or auth failure (not the SQL's fault)."""


class McpQueryError(McpError):
    """The statement itself failed (syntax, unknown column, ...). The message is fixable by the agent."""


class McpTimeout(McpError):
    pass


# ---------------------------------------------------------------- auth

class TokenProvider(Protocol):
    async def get_token(self, force_refresh: bool = False) -> str: ...


class EntraTokenProvider:
    """OAuth client credentials against Entra ID. The secret is never logged."""

    def __init__(
        self,
        tenant_id: str,
        client_id: str,
        client_secret: SecretStr,
        scope: str,
        *,
        http: httpx.AsyncClient | None = None,
        clock: Callable[[], float] = time.time,
    ):
        self._url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
        self._client_id = client_id
        self._secret = client_secret
        self._scope = scope
        self._http = http
        self._clock = clock
        self._token: str | None = None
        self._expires_at = 0.0
        self._lock = asyncio.Lock()

    async def get_token(self, force_refresh: bool = False) -> str:
        async with self._lock:
            if not force_refresh and self._token and self._clock() < self._expires_at - TOKEN_REFRESH_MARGIN_S:
                return self._token
            http = self._http or httpx.AsyncClient(timeout=30)
            try:
                resp = await http.post(
                    self._url,
                    data={
                        "grant_type": "client_credentials",
                        "client_id": self._client_id,
                        "client_secret": self._secret.get_secret_value(),
                        "scope": self._scope,
                    },
                )
            finally:
                if self._http is None:
                    await http.aclose()
            if resp.status_code != 200:
                raise McpError(f"token request failed with HTTP {resp.status_code}")
            body = resp.json()
            self._token = body["access_token"]
            self._expires_at = self._clock() + float(body.get("expires_in", 3600))
            return self._token


# ---------------------------------------------------------------- results

class ColumnInfo(BaseModel):
    name: str
    type: str = "STRING"


class QueryResult(BaseModel):
    columns: list[ColumnInfo] = Field(default_factory=list)
    rows: list[list[Any]] = Field(default_factory=list)
    total_row_count: int | None = None
    truncated: bool = False
    statement_id: str | None = None


_INT = {"LONG", "INT", "INTEGER", "SHORT", "BYTE", "BIGINT", "SMALLINT", "TINYINT"}
_FLOAT = {"DOUBLE", "FLOAT", "REAL"}


def convert_value(cell: Any, type_name: str) -> Any:
    """{'str': '97'} -> 97 for LONG, Decimal for DECIMAL, ...; a missing 'str' key means NULL."""
    if isinstance(cell, dict):
        if "str" not in cell:
            return None
        raw = cell["str"]
    else:
        raw = cell
    if raw is None:
        return None
    t = (type_name or "STRING").upper()
    try:
        if t in _INT:
            return int(raw)
        if t == "DECIMAL":
            return Decimal(str(raw))
        if t in _FLOAT:
            return float(raw)
        if t == "BOOLEAN":
            return str(raw).strip().lower() == "true"
        if t == "DATE":
            return dt.date.fromisoformat(str(raw)[:10])
        if t in ("TIMESTAMP", "TIMESTAMP_NTZ"):
            return dt.datetime.fromisoformat(str(raw).replace("Z", "+00:00"))
    except (ValueError, InvalidOperation):
        return raw
    return raw


def parse_statement(data: dict[str, Any]) -> QueryResult:
    manifest = data.get("manifest") or {}
    cols = [
        ColumnInfo(name=c.get("name", f"col{i}"), type=(c.get("type_name") or "STRING").upper())
        for i, c in enumerate((manifest.get("schema") or {}).get("columns") or [])
    ]
    result = data.get("result") or {}
    rows = []
    for r in result.get("data_typed_array") or []:
        values = r.get("values", []) if isinstance(r, dict) else r
        rows.append([convert_value(v, cols[i].type if i < len(cols) else "STRING") for i, v in enumerate(values)])
    truncated = bool(data.get("truncated") or result.get("truncated") or manifest.get("truncated"))
    total = data.get("total_row_count", manifest.get("total_row_count"))
    return QueryResult(columns=cols, rows=rows, total_row_count=total, truncated=truncated, statement_id=data.get("statement_id"))


# ---------------------------------------------------------------- client

class DatabricksMcpClient:
    def __init__(
        self,
        url: str,
        tokens: TokenProvider,
        *,
        http: httpx.AsyncClient | None = None,
        timeout_s: float = 60.0,
        poll_interval_s: float = 1.0,
        sleep: Callable[[float], Any] = asyncio.sleep,
        clock: Callable[[], float] = time.monotonic,
    ):
        self.url = url
        self.tokens = tokens
        self._http = http or httpx.AsyncClient(timeout=httpx.Timeout(timeout_s + 10))
        self.timeout_s = timeout_s
        self.poll_interval_s = poll_interval_s
        self._sleep = sleep
        self._clock = clock
        self._ids = itertools.count(1)

    async def aclose(self) -> None:
        await self._http.aclose()

    async def _post(self, payload: dict[str, Any]) -> httpx.Response:
        """POST with: one retry on HTTP 401 (fresh token) and retries with a short backoff on connection-level errors
        (a corporate network or VPN can drop a connection for a moment). Everything sent here is a read, so repeating it is safe."""
        refreshed = False
        network_failures = 0
        while True:
            token = await self.tokens.get_token(force_refresh=refreshed)
            try:
                resp = await self._http.post(
                    self.url,
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {token}",
                        "Content-Type": "application/json",
                        "Accept": "application/json, text/event-stream",
                    },
                )
            except TRANSIENT_ERRORS as exc:
                if network_failures < len(CONNECT_RETRY_DELAYS_S):
                    await self._sleep(CONNECT_RETRY_DELAYS_S[network_failures])
                    network_failures += 1
                    continue
                raise McpError(f"MCP request failed: {type(exc).__name__}") from exc
            except httpx.HTTPError as exc:
                raise McpError(f"MCP request failed: {type(exc).__name__}") from exc
            if resp.status_code == 401 and not refreshed:
                refreshed = True  # token expired early: refresh once
                continue
            return resp

    @staticmethod
    def _decode(resp: httpx.Response) -> dict[str, Any]:
        ctype = resp.headers.get("content-type", "")
        if "text/event-stream" in ctype:
            message = None
            for line in resp.text.splitlines():
                if line.startswith("data:"):
                    chunk = line[5:].strip()
                    if chunk:
                        message = json.loads(chunk)
            if message is None:
                raise McpError("empty event stream from MCP server")
            return message
        return resp.json()

    async def call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        if name not in ALLOWED_TOOLS:
            raise McpError(f"MCP tool '{name}' is not allowed (read-only tools only)")
        payload = {"jsonrpc": "2.0", "id": next(self._ids), "method": "tools/call", "params": {"name": name, "arguments": arguments}}
        resp = await self._post(payload)
        if resp.status_code >= 400:
            raise McpError(f"MCP server returned HTTP {resp.status_code}")
        message = self._decode(resp)
        if "error" in message:
            err = message["error"] or {}
            raise McpError(f"MCP error {err.get('code')}: {str(err.get('message', ''))[:300]}")
        result = message.get("result") or {}
        data = result.get("structuredContent")
        if data is None:
            content = result.get("content") or []
            text = content[0].get("text", "") if content else ""
            try:
                data = json.loads(text) if text else {}
            except json.JSONDecodeError:
                data = {"message": text}
        if result.get("isError"):
            raise McpQueryError(_error_text(data))
        return data

    async def query(self, sql: str, *, timeout_s: float | None = None) -> QueryResult:
        deadline = self._clock() + (timeout_s or self.timeout_s)
        data = await self.call_tool("execute_sql_read_only", {"query": sql})
        polls = 0
        while _state(data) not in DONE_STATES:
            statement_id = data.get("statement_id")
            if not statement_id:
                raise McpError("statement is not finished and has no statement_id to poll")
            if self._clock() >= deadline:
                raise McpTimeout(f"query did not finish within {timeout_s or self.timeout_s:.0f} seconds")
            delay = FIRST_POLL_DELAYS_S[polls] if polls < len(FIRST_POLL_DELAYS_S) else self.poll_interval_s
            await self._sleep(min(delay, self.poll_interval_s))
            polls += 1
            data = await self.call_tool("poll_sql_result", {"statement_id": statement_id})
        state = _state(data)
        if state != "SUCCEEDED":
            raise McpQueryError(_error_text(data) or f"statement {state.lower()}")
        return parse_statement(data)

    async def warm_up(self) -> bool:
        """One cheap query so the SQL warehouse starts before the first user question."""
        try:
            await self.query("SELECT 1 AS warm_up", timeout_s=max(self.timeout_s, 120))
            return True
        except McpError:
            return False


def _state(data: dict[str, Any]) -> str:
    status = data.get("status") or {}
    return str(status.get("state") or ("SUCCEEDED" if data.get("result") or data.get("manifest") else "")).upper()


def _error_text(data: dict[str, Any]) -> str:
    status = data.get("status") or {}
    err = status.get("error") or data.get("error") or {}
    if isinstance(err, dict):
        msg = err.get("message") or ""
    else:
        msg = str(err)
    return str(msg or data.get("message") or "").strip()[:1000]
