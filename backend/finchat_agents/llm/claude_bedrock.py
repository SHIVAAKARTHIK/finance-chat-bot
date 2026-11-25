"""Claude on AWS Bedrock via the anthropic SDK (AsyncAnthropicBedrock), with tool use and prompt caching.

Prompt caching: the system prompt and the tool definitions are marked `cache_control: ephemeral`, so repeated
calls in one ReAct loop reuse them. SDK retries are off; the runtime retries with backoff (runtime/retry.py).
"""
from __future__ import annotations

from typing import Any

from .types import LLMError, LLMResult, Message, TextBlock, ToolCall, ToolResultBlock, ToolSpec, ToolUseBlock, Usage

_CACHE = {"type": "ephemeral"}


def tools_to_anthropic(tools: list[ToolSpec]) -> list[dict[str, Any]]:
    out = [{"name": t.name, "description": t.description, "input_schema": t.input_schema} for t in tools]
    if out:
        out[-1]["cache_control"] = _CACHE  # caches every tool definition up to and including this one
    return out


def messages_to_anthropic(messages: list[Message]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for m in messages:
        blocks: list[dict[str, Any]] = []
        for b in m.content:
            if isinstance(b, TextBlock):
                if b.text:  # the API rejects empty text blocks
                    blocks.append({"type": "text", "text": b.text})
            elif isinstance(b, ToolUseBlock):
                blocks.append({"type": "tool_use", "id": b.id, "name": b.name, "input": b.input})
            elif isinstance(b, ToolResultBlock):
                blocks.append(
                    {"type": "tool_result", "tool_use_id": b.tool_use_id, "content": b.content, "is_error": b.is_error}
                )
        if blocks:
            out.append({"role": m.role, "content": blocks})
    return out


def with_history_cache(messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Mark the end of the conversation so far as a cache point (third breakpoint, after the tools and the system
    prompt). In an agent loop every step resends the whole conversation; with this, the next step reads it from the
    cache instead of processing it again. Only the last block is marked (the API allows at most 4 breakpoints)."""
    if messages and messages[-1].get("content"):
        last = dict(messages[-1]["content"][-1])
        last["cache_control"] = _CACHE
        messages = [*messages[:-1], {**messages[-1], "content": [*messages[-1]["content"][:-1], last]}]
    return messages


_STOP = {"end_turn": "end_turn", "tool_use": "tool_use", "max_tokens": "max_tokens", "stop_sequence": "end_turn"}


def parse_anthropic_response(resp: Any) -> LLMResult:
    texts: list[str] = []
    calls: list[ToolCall] = []
    for block in resp.content:
        if block.type == "text":
            texts.append(block.text)
        elif block.type == "tool_use":
            calls.append(ToolCall(id=block.id, name=block.name, input=dict(block.input or {})))
    u = resp.usage
    usage = Usage(
        input_tokens=getattr(u, "input_tokens", 0) or 0,
        output_tokens=getattr(u, "output_tokens", 0) or 0,
        cache_read_tokens=getattr(u, "cache_read_input_tokens", 0) or 0,
        cache_write_tokens=getattr(u, "cache_creation_input_tokens", 0) or 0,
    )
    return LLMResult(
        text="\n".join(texts).strip(), tool_calls=calls, usage=usage, stop_reason=_STOP.get(resp.stop_reason, "other")
    )


def map_anthropic_error(exc: Exception) -> LLMError:
    import anthropic

    if isinstance(exc, anthropic.APIStatusError):
        status = exc.status_code
        return LLMError(str(exc)[:500], retryable=status in (408, 429) or status >= 500, status=status, provider="claude")
    if isinstance(exc, anthropic.APIConnectionError):  # includes APITimeoutError
        return LLMError(str(exc)[:500], retryable=True, provider="claude")
    return LLMError(f"{type(exc).__name__}: {str(exc)[:500]}", retryable=False, provider="claude")


class ClaudeBedrockProvider:
    name = "claude-bedrock"

    def __init__(self, region: str | None, *, profile: str | None = None, credentials: Any = None,
                 timeout: float = 120.0, client: Any = None):
        self._region = region
        self._profile = profile
        self._credentials = credentials  # AwsCredentials or None; explicit keys win over the profile
        self._timeout = timeout
        self._client = client

    def _get_client(self) -> Any:
        if self._client is None:
            from anthropic import AsyncAnthropicBedrock

            c = self._credentials
            if c is not None:  # explicit keys (e.g. from backend/.env)
                self._client = AsyncAnthropicBedrock(
                    aws_region=self._region, aws_access_key=c.access_key_id, aws_secret_key=c.secret_access_key,
                    aws_session_token=c.session_token, timeout=self._timeout, max_retries=0)
            else:  # the normal AWS chain: profile, role or exported env keys
                self._client = AsyncAnthropicBedrock(aws_region=self._region, aws_profile=self._profile,
                                                     timeout=self._timeout, max_retries=0)
        return self._client

    def sdk_client(self) -> Any:
        """The underlying Anthropic SDK client (used by the Anthropic SDK ReAct engine)."""
        return self._get_client()

    async def complete(
        self,
        system: str,
        messages: list[Message],
        tools: list[ToolSpec],
        model: str,
        max_tokens: int,
        temperature: float,
    ) -> LLMResult:
        # `temperature` is accepted by the interface but NOT sent: anthropic 2.x `messages.create` has no such parameter
        # (it raised TypeError on a real call). Claude then runs with the model's default sampling.
        kwargs: dict[str, Any] = {
            "model": model,
            "max_tokens": max_tokens,
            "messages": with_history_cache(messages_to_anthropic(messages)),
        }
        if system:
            kwargs["system"] = [{"type": "text", "text": system, "cache_control": _CACHE}]
        if tools:
            kwargs["tools"] = tools_to_anthropic(tools)
        try:
            resp = await self._get_client().messages.create(**kwargs)
        except Exception as exc:  # mapped to LLMError so the runtime can decide on retry
            raise map_anthropic_error(exc) from exc
        return parse_anthropic_response(resp)
