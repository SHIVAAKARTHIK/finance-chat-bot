"""Fake Databricks DBSQL MCP server (httpx.MockTransport) and helpers shared by tests."""
from __future__ import annotations

import datetime as dt
import json
import re

import sqlglot
from decimal import Decimal
from typing import Any, Callable

import httpx

from finchat_agents.config import Settings
from finchat_agents.knowledge.loader import Knowledge
from finchat_agents.tools.deps import DataDeps, TTLCache
from finchat_agents.tools.mcp_client import DatabricksMcpClient

Table = tuple[list[tuple[str, str]], list[list[Any]]]  # ([(name, TYPE_NAME)], rows)


def _cell(v: Any) -> dict[str, Any]:
    if v is None:
        return {}
    if isinstance(v, bool):
        return {"str": "true" if v else "false"}
    return {"str": str(v)}


def statement(columns: list[tuple[str, str]], rows: list[list[Any]], *, statement_id: str = "st-1", state: str = "SUCCEEDED",
              truncated: bool = False) -> dict[str, Any]:
    return {
        "statement_id": statement_id,
        "status": {"state": state},
        "manifest": {"schema": {"columns": [{"name": n, "type_name": t, "type_text": t.lower(), "position": i}
                                            for i, (n, t) in enumerate(columns)]}},
        "result": {"data_typed_array": [{"values": [_cell(v) for v in r]} for r in rows]},
        "total_row_count": len(rows),
        "truncated": truncated,
    }


class FakeTokens:
    def __init__(self) -> None:
        self.calls: list[bool] = []
        self.n = 0

    async def get_token(self, force_refresh: bool = False) -> str:
        self.calls.append(force_refresh)
        if force_refresh or not self.n:
            self.n += 1
        return f"token-{self.n}"


class FakeMcpServer:
    """Answers tools/call for execute_sql_read_only / poll_sql_result. `responder(sql)` returns a Table, raises
    ValueError (-> FAILED statement), or returns a raw statement dict. Options simulate polling, 401s and SSE."""

    def __init__(self, responder: Callable[[str], Any], *, pending_polls: int = 0, reject_tokens: set[str] | None = None,
                 sse: bool = False, text_only: bool = False):
        self.responder = responder
        self.pending_polls = pending_polls
        self.reject_tokens = reject_tokens or set()
        self.sse = sse
        self.text_only = text_only
        self.requests: list[dict[str, Any]] = []
        self.queries: list[str] = []
        self._pending: dict[str, tuple[int, dict]] = {}

    def __call__(self, request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content)
        self.requests.append({"headers": dict(request.headers), "body": body})
        token = request.headers.get("authorization", "").removeprefix("Bearer ")
        if token in self.reject_tokens:
            return httpx.Response(401, json={"error": "Token is expired"})
        name = body["params"]["name"]
        args = body["params"]["arguments"]
        if name == "execute_sql_read_only":
            sql = args["query"]
            self.queries.append(sql)
            try:
                out = self.responder(sql)
                data = out if isinstance(out, dict) else statement(*out, statement_id=f"st-{len(self.queries)}")
            except ValueError as exc:
                data = {"statement_id": f"st-{len(self.queries)}", "status": {"state": "FAILED", "error": {"message": str(exc)}}}
            if self.pending_polls:
                sid = data["statement_id"]
                self._pending[sid] = (self.pending_polls, data)
                data = {"statement_id": sid, "status": {"state": "PENDING"}}
        elif name == "poll_sql_result":
            sid = args["statement_id"]
            left, final = self._pending[sid]
            if left > 1:
                self._pending[sid] = (left - 1, final)
                data = {"statement_id": sid, "status": {"state": "RUNNING"}}
            else:
                data = final
        else:
            return httpx.Response(200, json={"jsonrpc": "2.0", "id": body["id"], "error": {"code": -32601, "message": "unknown tool"}})
        result: dict[str, Any] = {"content": [{"type": "text", "text": json.dumps(data)}], "isError": False}
        if not self.text_only:
            result["structuredContent"] = data
        message = {"jsonrpc": "2.0", "id": body["id"], "result": result}
        if self.sse:
            return httpx.Response(200, text=f"event: message\ndata: {json.dumps(message)}\n\n",
                                  headers={"content-type": "text/event-stream"})
        return httpx.Response(200, json=message)


async def _no_sleep(_: float) -> None:
    return None


def make_client(server: FakeMcpServer, tokens: Any = None, **kw: Any) -> DatabricksMcpClient:
    http = httpx.AsyncClient(transport=httpx.MockTransport(server))
    kw.setdefault("sleep", _no_sleep)
    return DatabricksMcpClient("https://fake/api/2.0/mcp/sql", tokens or FakeTokens(), http=http, **kw)


# ---------------------------------------------------------------- canned data for the real knowledge pages

S, L, D, DT, B = "STRING", "LONG", "DECIMAL", "DATE", "BOOLEAN"


def data_responder(sql: str) -> Table:
    s = sql.lower()
    if "adra_period_dimensions" in s and "distinct" in s:
        return [("PERIOD_NAME", S), ("PERIOD_END", DT)], [["Feb 25", "2025-02-01"], ["Oct 26", "2026-10-01"], ["Feb 25", "2025-02-01"]]
    if "fact_fynapse_slr_journals" in s and "distinct" in s:
        return [("FISCAL_YEAR", L), ("PERIOD", L), ("CORE_DATE", DT)], [[2026, 8, "2026-08-01"], [2026, 9, "2026-09-01"]]
    if "adra_legal_entity_dimensions" in s and "`entity_code` as value" in s:
        return [("value", S), ("row_count", L)], [["100", 1], ["561", 1]]
    if "adra_legal_entity_dimensions" in s and "`entity_name` as value" in s:
        return [("value", S), ("row_count", L)], [["100-Northwind", 1], ["Cars USA Shipping, LLC", 1]]
    if "fact_fynapse_slr_journals" in s and "`parent_entity` as value" in s:
        return [("value", S), ("row_count", L)], [["UK03", 283], ["UK07", 280]]
    if "as value" in s and "account_status" in s:
        return [("value", S), ("row_count", L)], [["Not prepared", 24], ["Approved", 7]]
    if "preparer_name" in s or "approved_by_name" in s:
        names = sqlglot.parse_one(sql, read="databricks").named_selects
        cols = [(c, S) for c in names]
        return cols, [["Real Person" if "name" in c.lower() or c.lower() == "who" else "103300" for c, _ in cols]]
    if "count(*)" in s and "as value" not in s:
        return [("n", L)], [[97]]
    if "as value" in s:  # get_column_values on any other column
        return [("value", S), ("row_count", L)], [["x", 1]]
    if "error_me" in s:
        raise ValueError("[UNRESOLVED_COLUMN.WITH_SUGGESTION] A column with name `error_me` cannot be resolved.")
    return [("value", S)], [["x"]]


def make_deps(server: FakeMcpServer | None = None, *, kb: Knowledge | None = None, today: dt.date | None = None,
              **settings: Any) -> tuple[DataDeps, FakeMcpServer]:
    server = server or FakeMcpServer(data_responder)
    s = Settings(_env_file=None, **settings)
    deps = DataDeps(kb=kb or Knowledge.load(), mcp=make_client(server), settings=s, cache=TTLCache(3600),
                    today=(lambda: today) if today else None)
    return deps, server


__all__ = ["B", "D", "DT", "Decimal", "FakeMcpServer", "FakeTokens", "L", "S", "data_responder", "make_client", "make_deps", "statement"]
