"""gpt-oss-120b on AWS Bedrock, with two transports:

- "converse" (default): boto3 bedrock-runtime Converse API with toolConfig. Uses the normal AWS credential chain.
- "openai": the openai SDK against Bedrock's OpenAI-compatible Chat Completions endpoint
  (`openai.providers.bedrock(endpoint="runtime")`, SigV4 from the normal AWS chain).

Pick with GPT_OSS_TRANSPORT. The live smoke test (tests/live) checks tool calling on both, so the choice can be
confirmed per region. SDK retries are off; the runtime retries with backoff.
"""
from __future__ import annotations

import asyncio
import json
import re
from typing import Any, Literal

from .types import LLMError, LLMResult, Message, TextBlock, ToolCall, ToolResultBlock, ToolSpec, ToolUseBlock, Usage

_REASONING = re.compile(r"<reasoning>.*?</reasoning>", re.DOTALL)


def _clean(text: str) -> str:
    """gpt-oss can inline its chain of thought in <reasoning> tags; it never goes to users or other agents."""
    return _REASONING.sub("", text or "").strip()


# ---------------------------------------------------------------- Converse transport

def tools_to_converse(tools: list[ToolSpec]) -> list[dict[str, Any]]:
    return [
        {"toolSpec": {"name": t.name, "description": t.description, "inputSchema": {"json": t.input_schema}}}
        for t in tools
    ]


def messages_to_converse(messages: list[Message]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for m in messages:
        blocks: list[dict[str, Any]] = []
        for b in m.content:
            if isinstance(b, TextBlock):
                if b.text:
                    blocks.append({"text": b.text})
            elif isinstance(b, ToolUseBlock):
                blocks.append({"toolUse": {"toolUseId": b.id, "name": b.name, "input": b.input}})
            elif isinstance(b, ToolResultBlock):
                blocks.append(
                    {
                        "toolResult": {
                            "toolUseId": b.tool_use_id,
                            "content": [{"text": b.content}],
                            "status": "error" if b.is_error else "success",
                        }
                    }
                )
        if blocks:
            out.append({"role": m.role, "content": blocks})
    return out


_CONVERSE_STOP = {"end_turn": "end_turn", "tool_use": "tool_use", "max_tokens": "max_tokens", "stop_sequence": "end_turn"}


def parse_converse_response(resp: dict[str, Any]) -> LLMResult:
    content = (resp.get("output") or {}).get("message", {}).get("content", []) or []
    texts: list[str] = []
    calls: list[ToolCall] = []
    for block in content:
        if "text" in block:
            texts.append(block["text"])
        elif "toolUse" in block:
            tu = block["toolUse"]
            calls.append(ToolCall(id=tu["toolUseId"], name=tu["name"], input=tu.get("input") or {}))
        # reasoningContent blocks are dropped on purpose
    usage = resp.get("usage") or {}
    return LLMResult(
        text=_clean("\n".join(texts)),
        tool_calls=calls,
        usage=Usage(input_tokens=int(usage.get("inputTokens", 0) or 0), output_tokens=int(usage.get("outputTokens", 0) or 0)),
        stop_reason=_CONVERSE_STOP.get(resp.get("stopReason", ""), "other"),
    )


_RETRYABLE_AWS_CODES = {
    "ThrottlingException",
    "TooManyRequestsException",
    "ServiceUnavailableException",
    "InternalServerException",
    "ModelNotReadyException",
    "ModelTimeoutException",
    "RequestTimeout",
}


def map_boto_error(exc: Exception) -> LLMError:
    try:
        from botocore.exceptions import ClientError, ConnectionError as BotoConnectionError, ReadTimeoutError
    except ImportError:  # pragma: no cover
        return LLMError(str(exc)[:500], retryable=False, provider="gpt-oss")
    if isinstance(exc, ClientError):
        code = exc.response.get("Error", {}).get("Code", "")
        status = exc.response.get("ResponseMetadata", {}).get("HTTPStatusCode")
        retryable = code in _RETRYABLE_AWS_CODES or (status is not None and (status == 429 or status >= 500))
        return LLMError(f"{code}: {str(exc)[:500]}", retryable=retryable, status=status, provider="gpt-oss")
    if isinstance(exc, (BotoConnectionError, ReadTimeoutError)):
        return LLMError(str(exc)[:500], retryable=True, provider="gpt-oss")
    return LLMError(f"{type(exc).__name__}: {str(exc)[:500]}", retryable=False, provider="gpt-oss")


# ---------------------------------------------------------------- OpenAI-compatible transport

def tools_to_openai(tools: list[ToolSpec]) -> list[dict[str, Any]]:
    return [
        {"type": "function", "function": {"name": t.name, "description": t.description, "parameters": t.input_schema}}
        for t in tools
    ]


def messages_to_openai(system: str, messages: list[Message]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = [{"role": "system", "content": system}] if system else []
    for m in messages:
        if m.role == "assistant":
            text = "\n".join(b.text for b in m.content if isinstance(b, TextBlock) and b.text)
            calls = [
                {"id": b.id, "type": "function", "function": {"name": b.name, "arguments": json.dumps(b.input)}}
                for b in m.content
                if isinstance(b, ToolUseBlock)
            ]
            msg: dict[str, Any] = {"role": "assistant", "content": text or None}
            if calls:
                msg["tool_calls"] = calls
            out.append(msg)
        else:
            for b in m.content:  # tool results first (they answer the previous assistant turn), then user text
                if isinstance(b, ToolResultBlock):
                    out.append({"role": "tool", "tool_call_id": b.tool_use_id, "content": b.content})
            text = "\n".join(b.text for b in m.content if isinstance(b, TextBlock) and b.text)
            if text:
                out.append({"role": "user", "content": text})
    return out


_OPENAI_STOP = {"stop": "end_turn", "tool_calls": "tool_use", "length": "max_tokens"}


def parse_openai_response(resp: Any) -> LLMResult:
    choice = resp.choices[0]
    msg = choice.message
    calls: list[ToolCall] = []
    for tc in msg.tool_calls or []:
        try:
            args = json.loads(tc.function.arguments or "{}")
        except json.JSONDecodeError:
            args = {"_unparsed_arguments": tc.function.arguments}
        calls.append(ToolCall(id=tc.id, name=tc.function.name, input=args if isinstance(args, dict) else {"value": args}))
    u = getattr(resp, "usage", None)
    return LLMResult(
        text=_clean(msg.content or ""),
        tool_calls=calls,
        usage=Usage(
            input_tokens=getattr(u, "prompt_tokens", 0) or 0, output_tokens=getattr(u, "completion_tokens", 0) or 0
        ),
        stop_reason="tool_use" if calls else _OPENAI_STOP.get(choice.finish_reason or "", "other"),
    )


def map_openai_error(exc: Exception) -> LLMError:
    import openai

    if isinstance(exc, openai.APIStatusError):
        status = exc.status_code
        return LLMError(str(exc)[:500], retryable=status in (408, 429) or status >= 500, status=status, provider="gpt-oss")
    if isinstance(exc, openai.APIConnectionError):
        return LLMError(str(exc)[:500], retryable=True, provider="gpt-oss")
    return LLMError(f"{type(exc).__name__}: {str(exc)[:500]}", retryable=False, provider="gpt-oss")


# ---------------------------------------------------------------- provider

class GptOssBedrockProvider:
    name = "gpt-oss-bedrock"

    def __init__(
        self,
        region: str | None,
        *,
        profile: str | None = None,
        credentials: Any = None,
        transport: Literal["converse", "openai"] = "converse",
        timeout: float = 120.0,
        boto_client: Any = None,
        openai_client: Any = None,
    ):
        if transport not in ("converse", "openai"):
            raise ValueError(f"unknown gpt-oss transport: {transport}")
        self.transport = transport
        self._region = region
        self._profile = profile
        self._credentials = credentials  # AwsCredentials or None; explicit keys win over the profile
        self._timeout = timeout
        self._boto = boto_client
        self._openai = openai_client

    def _boto_client(self) -> Any:
        if self._boto is None:
            import boto3
            from botocore.config import Config

            cfg = Config(read_timeout=self._timeout, connect_timeout=10, retries={"max_attempts": 1})
            c = self._credentials
            if c is not None:
                session = boto3.Session(aws_access_key_id=c.access_key_id, aws_secret_access_key=c.secret_access_key,
                                        aws_session_token=c.session_token)
            else:
                session = boto3.Session(profile_name=self._profile) if self._profile else boto3.Session()
            self._boto = session.client("bedrock-runtime", region_name=self._region, config=cfg)
        return self._boto

    def _openai_client(self) -> Any:
        if self._openai is None:
            from openai import AsyncOpenAI
            from openai.providers import bedrock

            c = self._credentials
            if c is not None:
                provider = bedrock(endpoint="runtime", region=self._region, access_key_id=c.access_key_id,
                                   secret_access_key=c.secret_access_key, session_token=c.session_token)
            else:
                provider = bedrock(endpoint="runtime", region=self._region, profile=self._profile)
            self._openai = AsyncOpenAI(provider=provider, timeout=self._timeout, max_retries=0)
        return self._openai

    async def complete(
        self,
        system: str,
        messages: list[Message],
        tools: list[ToolSpec],
        model: str,
        max_tokens: int,
        temperature: float,
    ) -> LLMResult:
        if self.transport == "openai":
            return await self._complete_openai(system, messages, tools, model, max_tokens, temperature)
        return await self._complete_converse(system, messages, tools, model, max_tokens, temperature)

    async def _complete_converse(self, system, messages, tools, model, max_tokens, temperature) -> LLMResult:
        kwargs: dict[str, Any] = {
            "modelId": model,
            "messages": messages_to_converse(messages),
            "inferenceConfig": {"maxTokens": max_tokens, "temperature": temperature},
        }
        if system:
            kwargs["system"] = [{"text": system}]
        if tools:  # Converse rejects an empty tools list
            kwargs["toolConfig"] = {"tools": tools_to_converse(tools)}
        client = self._boto_client()
        try:
            resp = await asyncio.to_thread(client.converse, **kwargs)
        except Exception as exc:
            raise map_boto_error(exc) from exc
        return parse_converse_response(resp)

    async def _complete_openai(self, system, messages, tools, model, max_tokens, temperature) -> LLMResult:
        kwargs: dict[str, Any] = {
            "model": model,
            "messages": messages_to_openai(system, messages),
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        if tools:
            kwargs["tools"] = tools_to_openai(tools)
        try:
            resp = await self._openai_client().chat.completions.create(**kwargs)
        except Exception as exc:
            raise map_openai_error(exc) from exc
        return parse_openai_response(resp)
