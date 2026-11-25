"""Claude through the Anthropic API directly (API key), as an alternative to Bedrock.

Same request and response handling as `ClaudeBedrockProvider` (tool use, prompt caching); only the client differs
(`AsyncAnthropic`). The key is read from the ANTHROPIC_API_KEY environment variable (Settings.anthropic_api_key); it is
never written to code, logs or traces. Selected with CLAUDE_PROVIDER=anthropic_api (default: bedrock). gpt-oss stays on
Bedrock either way. Model ids differ from Bedrock's (ANTHROPIC_MODEL_SQL, e.g. claude-sonnet-4-5).
"""
from __future__ import annotations

from typing import Any

from .claude_bedrock import ClaudeBedrockProvider


class ClaudeApiProvider(ClaudeBedrockProvider):
    name = "claude-api"

    def __init__(self, api_key: str, *, timeout: float = 120.0, client: Any = None):
        super().__init__(None, timeout=timeout, client=client)
        self._api_key = api_key

    def _get_client(self) -> Any:
        if self._client is None:
            from anthropic import AsyncAnthropic

            self._client = AsyncAnthropic(api_key=self._api_key, timeout=self._timeout, max_retries=0)
        return self._client
