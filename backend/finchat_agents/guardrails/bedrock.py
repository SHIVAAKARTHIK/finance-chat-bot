"""Optional AWS Bedrock Guardrail (the managed ApplyGuardrail API): harmful content and whatever else your AWS team
configured in it, checked on the user's question and on the answer. Off unless BEDROCK_GUARDRAIL_ID is set."""
from __future__ import annotations

import asyncio
from typing import Any

from pydantic import BaseModel


class ContentFilterError(RuntimeError):
    """The filter could not be asked; callers fail closed."""


class FilterResult(BaseModel):
    blocked: bool = False
    changed: bool = False  # the guardrail masked something and let the rest through
    text: str = ""  # blocked: the guardrail's own message; changed: the masked text; otherwise the original


def _has_blocked(node: Any) -> bool:
    if isinstance(node, dict):
        return node.get("action") == "BLOCKED" or any(_has_blocked(v) for v in node.values())
    if isinstance(node, list):
        return any(_has_blocked(v) for v in node)
    return False


def parse_response(response: dict[str, Any], original: str) -> FilterResult:
    if response.get("action") != "GUARDRAIL_INTERVENED":
        return FilterResult(text=original)
    output = "".join(str(o.get("text") or "") for o in response.get("outputs") or [])
    if _has_blocked(response.get("assessments")) or not output:
        return FilterResult(blocked=True, text=output)
    return FilterResult(changed=True, text=output)


class BedrockContentFilter:
    def __init__(self, region: str, guardrail_id: str, version: str, *, profile: str | None = None,
                 credentials: Any = None, timeout: float = 10.0, client: Any = None):
        self.region, self.guardrail_id, self.version = region, guardrail_id, version
        self._profile, self._credentials, self._timeout, self._client = profile, credentials, timeout, client

    def _get_client(self) -> Any:
        if self._client is None:
            import boto3
            from botocore.config import Config

            config = Config(read_timeout=self._timeout, connect_timeout=5, retries={"max_attempts": 2})
            c = self._credentials
            if c is not None:
                session = boto3.Session(aws_access_key_id=c.access_key_id, aws_secret_access_key=c.secret_access_key,
                                        aws_session_token=c.session_token)
            else:
                session = boto3.Session(profile_name=self._profile) if self._profile else boto3.Session()
            self._client = session.client("bedrock-runtime", region_name=self.region, config=config)
        return self._client

    async def apply(self, text: str, source: str) -> FilterResult:
        """`source` is "INPUT" (the user's question) or "OUTPUT" (text for the user)."""
        try:
            response = await asyncio.wait_for(
                asyncio.to_thread(
                    lambda: self._get_client().apply_guardrail(
                        guardrailIdentifier=self.guardrail_id, guardrailVersion=self.version, source=source,
                        content=[{"text": {"text": text}}])),
                timeout=self._timeout + 5)
        except Exception as exc:  # noqa: BLE001 - network, permission or configuration problem
            raise ContentFilterError(type(exc).__name__) from exc
        return parse_response(response, text)
