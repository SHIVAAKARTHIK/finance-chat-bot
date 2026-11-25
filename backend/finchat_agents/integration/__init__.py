"""Integration with the company backend: serve v3 behind the backend's existing chat URLs and UI stream contract.

    from finchat_agents.integration import install_backend
    install_backend(app, get_current_user=get_current_user, agent_roles=agent_roles,
                    rate_limit=limiter.limit("10/minute"))

See docs/BACKEND_INTEGRATION.md. Only the outward contract the UI already uses is matched (URLs, SSE event names, response
field names); everything behind it is v3. No KPI data is produced: `explanation.kpi` is always null.
"""
from .backend import UiChatRequest, create_backend_router, identity_from_user, install_backend
from .ui_contract import chunk_text, to_ui_body

__all__ = ["UiChatRequest", "chunk_text", "create_backend_router", "identity_from_user", "install_backend", "to_ui_body"]
