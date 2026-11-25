"""Shared dependencies for the data tools, and a small TTL cache."""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Callable

from ..access.rbac import UserAccess
from ..config import Settings
from ..knowledge.loader import Knowledge
from ..runtime.tools import ToolContext, ToolError
from .mcp_client import DatabricksMcpClient, EntraTokenProvider


class TTLCache:
    def __init__(self, ttl_s: float, clock: Callable[[], float] = time.monotonic, max_items: int = 2000):
        self.ttl_s = ttl_s
        self.clock = clock
        self.max_items = max_items
        self._items: dict[Any, tuple[float, Any]] = {}

    def get(self, key: Any) -> Any:
        hit = self._items.get(key)
        if hit is None:
            return None
        if self.clock() >= hit[0]:
            self._items.pop(key, None)
            return None
        return hit[1]

    def set(self, key: Any, value: Any) -> None:
        if len(self._items) >= self.max_items:
            self._items.pop(next(iter(self._items)))
        self._items[key] = (self.clock() + self.ttl_s, value)


@dataclass
class DataDeps:
    kb: Knowledge
    mcp: Any  # DatabricksMcpClient or a fake with `async query(sql, timeout_s=...)`
    settings: Settings
    cache: TTLCache = field(default_factory=lambda: TTLCache(3600))
    today: Callable[[], Any] | None = None  # date provider for relative periods (tests inject one)


def access_of(tctx: ToolContext) -> UserAccess:
    user = tctx.run.user
    if not isinstance(user, UserAccess) or not user.has_access:
        raise ToolError("Access denied: this user has no data access configured. Tell the user to ask an administrator for a role.")
    return user


def build_mcp_client(settings: Settings) -> Any:
    """The data client chosen by DATA_ACCESS: the MCP bridge (default) or the SQL connector. Both expose `query`."""
    if settings.data_access == "sql_connector":
        return _build_sql_connector_client(settings)
    return _build_mcp(settings)


def _build_sql_connector_client(settings: Settings) -> Any:
    missing = [
        n for n, v in (
            ("DATABRICKS_SERVER_HOSTNAME", settings.databricks_server_hostname),
            ("DATABRICKS_HTTP_PATH", settings.databricks_http_path),
            ("AZURE_TENANT_ID", settings.azure_tenant_id),
            ("AZURE_CLIENT_ID", settings.azure_client_id),
            ("AZURE_CLIENT_SECRET", settings.azure_client_secret),
        ) if not v
    ]
    if missing:
        raise RuntimeError(f"missing environment variables for the SQL connector: {', '.join(missing)}")
    from ..storage.aiops import DatabricksSqlExecutor
    from .sql_connector_client import SqlConnectorClient

    tokens = EntraTokenProvider(
        settings.azure_tenant_id, settings.azure_client_id, settings.azure_client_secret, settings.azure_databricks_scope  # type: ignore[arg-type]
    )
    executor = DatabricksSqlExecutor(settings.databricks_server_hostname, settings.databricks_http_path, tokens.get_token)  # type: ignore[arg-type]
    return SqlConnectorClient(executor, timeout_s=settings.sql_timeout_seconds)


def _build_mcp(settings: Settings) -> DatabricksMcpClient:
    missing = [
        n for n, v in (
            ("DATABRICKS_MCP_URL", settings.databricks_mcp_url),
            ("AZURE_TENANT_ID", settings.azure_tenant_id),
            ("AZURE_CLIENT_ID", settings.azure_client_id),
            ("AZURE_CLIENT_SECRET", settings.azure_client_secret),
        ) if not v
    ]
    if missing:
        raise RuntimeError(f"missing environment variables for Databricks MCP: {', '.join(missing)}")
    tokens = EntraTokenProvider(
        settings.azure_tenant_id, settings.azure_client_id, settings.azure_client_secret, settings.azure_databricks_scope  # type: ignore[arg-type]
    )
    return DatabricksMcpClient(
        settings.databricks_mcp_url,  # type: ignore[arg-type]
        tokens,
        timeout_s=settings.sql_timeout_seconds,
        poll_interval_s=settings.mcp_poll_interval_seconds,
    )
