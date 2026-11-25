"""Build the two model handles from settings: SQL/reasoning (Claude) and response (gpt-oss)."""
from __future__ import annotations

from ..config import Settings
from .claude_api import ClaudeApiProvider
from .claude_bedrock import ClaudeBedrockProvider
from .gpt_oss_bedrock import GptOssBedrockProvider
from .types import ModelHandle


def sql_model(settings: Settings) -> ModelHandle:
    """Claude Sonnet: supervisor, catalog, SQL, analyst, investigator. Bedrock by default, or the Anthropic API key."""
    if settings.claude_provider == "anthropic_api":
        if not settings.anthropic_api_key:
            raise RuntimeError("CLAUDE_PROVIDER=anthropic_api needs ANTHROPIC_API_KEY in the environment")
        api = ClaudeApiProvider(settings.anthropic_api_key.get_secret_value(), timeout=settings.llm_timeout_seconds)
        return ModelHandle(provider=api, model=settings.anthropic_model_sql)
    provider = ClaudeBedrockProvider(settings.aws_region, profile=settings.aws_profile, credentials=settings.aws_credentials(),
                                    timeout=settings.llm_timeout_seconds)
    return ModelHandle(provider=provider, model=settings.bedrock_model_sql)


def response_model(settings: Settings, transport: str | None = None) -> ModelHandle:
    """gpt-oss: routing, final wording, summaries, titles."""
    provider = GptOssBedrockProvider(
        settings.aws_region, profile=settings.aws_profile, credentials=settings.aws_credentials(), transport=transport or settings.gpt_oss_transport,
        timeout=settings.llm_timeout_seconds,
    )
    return ModelHandle(provider=provider, model=settings.bedrock_model_response)
