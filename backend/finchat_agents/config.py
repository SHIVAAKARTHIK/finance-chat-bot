"""Settings for finchat_agents, read from environment variables (and backend/.env if present).

Names follow config/.env.example. Secrets are only ever read from the environment; never log Settings.
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Literal, NamedTuple

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

PACKAGE_DIR = Path(__file__).resolve().parent
BACKEND_DIR = PACKAGE_DIR.parent


class AwsCredentials(NamedTuple):
    access_key_id: str
    secret_access_key: str
    session_token: str | None = None

    def __repr__(self) -> str:  # never print keys
        return "AwsCredentials(<redacted>)"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
        env_ignore_empty=True,  # `AWS_REGION=` in .env means "not set", not an empty string
    )

    # AWS Bedrock
    aws_region: str | None = None
    # Named AWS profile (e.g. an SSO profile). The SDKs do not read backend/.env, so it is passed explicitly.
    aws_profile: str | None = None
    # Optional explicit keys (AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_SESSION_TOKEN). When set they are passed to the
    # SDKs directly, so keys that only exist in backend/.env work without being exported; they win over AWS_PROFILE.
    aws_access_key_id: SecretStr | None = None
    aws_secret_access_key: SecretStr | None = None
    aws_session_token: SecretStr | None = None
    # Which Claude endpoint to use: "bedrock" (default) or "anthropic_api" (Anthropic API key from ANTHROPIC_API_KEY).
    # gpt-oss always stays on Bedrock.
    claude_provider: Literal["bedrock", "anthropic_api"] = "bedrock"
    anthropic_api_key: SecretStr | None = None
    anthropic_model_sql: str = "claude-sonnet-4-5"
    # Who runs the ReAct loop of the Claude agents: our own loop (default) or the Anthropic SDK tool runner. The SDK engine
    # needs a Claude provider (bedrock or anthropic_api); other models always use our loop.
    react_engine: Literal["own", "anthropic_sdk"] = "own"
    bedrock_model_sql: str = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"
    bedrock_model_response: str = "openai.gpt-oss-120b-1:0"
    # How gpt-oss is called: boto3 Converse (default) or the openai SDK on Bedrock's OpenAI-compatible endpoint.
    gpt_oss_transport: Literal["converse", "openai"] = "converse"
    llm_timeout_seconds: float = 120.0

    # Databricks (service principal only)
    databricks_server_hostname: str | None = None
    databricks_http_path: str | None = None
    databricks_catalog: str = "lakehouse_mvpai"
    # The aiops schema is fixed in code (storage.aiops.ALLOWED_SCHEMA). DATABRICKS_SCHEMA in a shared backend/.env
    # (the backend uses "silver") is deliberately ignored by v3.
    databricks_auth: str = "azure_spn"
    azure_tenant_id: str | None = None
    azure_client_id: str | None = None
    azure_client_secret: SecretStr | None = None
    databricks_mcp_url: str | None = None
    # How data is read: "mcp" (Databricks MCP bridge, default) or "sql_connector" (databricks-sql-connector with the same
    # service principal; needs DATABRICKS_SERVER_HOSTNAME and DATABRICKS_HTTP_PATH).
    data_access: Literal["mcp", "sql_connector"] = "mcp"
    # Entra scope of the Azure Databricks resource (public application id, not a secret)
    azure_databricks_scope: str = "2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default"
    sql_timeout_seconds: float = 60.0
    mcp_poll_interval_seconds: float = 1.0
    column_values_cache_seconds: float = 21600.0  # 6 h; stored values and period lists change rarely

    # Agent budgets
    agent_max_steps: int = 15
    agent_max_seconds: float = 300.0
    agent_max_sql_calls: int = 10
    sql_row_limit: int = 1000
    sql_rows_to_model: int = 50
    # Conversation memory (token based). One continuous chat per user: 0 = no question limit (a number > 0 brings back
    # the old behaviour: at that many questions a new conversation starts, seeded with the summary).
    conversation_question_limit: int = 0
    # Recent turns shown word for word to the agents: the newest turns that fit this many tokens (about 4 characters each).
    history_token_budget: int = 3000
    # The rolling summary is rewritten when the turns not yet in it pass this many tokens.
    summary_token_threshold: int = 3000

    # Company guardrails: pack text and project values are read from this folder (not part of the repository).
    # With guardrails enabled the app does not start if the folder is missing or incomplete.
    guardrails_enabled: bool = True
    guardrails_dir: str = "guardrails_local"

    # Access file (relative paths resolve against the package directory)
    rbac_file: str = "config/rbac.v3.yaml"

    # Tracing
    trace_dir: str = "traces"

    # Files created by actions (export_excel, save_report); one folder per conversation
    output_dir: str = "outputs"

    # Summary agent (task 09): metric definitions for the scheduled cards
    summary_metrics_file: str = "config/summary_metrics.yaml"

    # Deploy (task 10): warm-up at startup (MCP query + Bedrock ping + aiops read) and /v3/health result cache
    warm_up_on_start: bool = True
    warm_up_timeout_seconds: float = 180.0
    health_cache_seconds: float = 60.0

    # Tests
    run_live: bool = False

    def aws_credentials(self) -> "AwsCredentials | None":
        """Explicit keys if both are set, else None (the SDKs then use the profile, the role or exported env keys)."""
        if self.aws_access_key_id and self.aws_secret_access_key:
            token = self.aws_session_token.get_secret_value() if self.aws_session_token else None
            return AwsCredentials(self.aws_access_key_id.get_secret_value(), self.aws_secret_access_key.get_secret_value(), token)
        return None

    def resolve_path(self, value: str) -> Path:
        path = Path(value)
        return path if path.is_absolute() else PACKAGE_DIR / path


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
