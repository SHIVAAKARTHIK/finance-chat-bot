"""Provider-neutral LLM types: tool specs, messages, results, errors and the provider interface.

Tools are defined once as JSON Schema (`ToolSpec`); each provider converts them to its own format.
Messages use a small neutral block format; each provider converts them too.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Annotated, Any, Literal, Protocol, Union

from pydantic import BaseModel, Field


class ToolSpec(BaseModel):
    name: str
    description: str
    input_schema: dict[str, Any] = Field(default_factory=lambda: {"type": "object", "properties": {}})


class TextBlock(BaseModel):
    type: Literal["text"] = "text"
    text: str


class ToolUseBlock(BaseModel):
    type: Literal["tool_use"] = "tool_use"
    id: str
    name: str
    input: dict[str, Any] = Field(default_factory=dict)


class ToolResultBlock(BaseModel):
    type: Literal["tool_result"] = "tool_result"
    tool_use_id: str
    content: str
    is_error: bool = False


Block = Annotated[Union[TextBlock, ToolUseBlock, ToolResultBlock], Field(discriminator="type")]


class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: list[Block]

    @classmethod
    def user(cls, text: str) -> "Message":
        return cls(role="user", content=[TextBlock(text=text)])

    @property
    def text(self) -> str:
        return "\n".join(b.text for b in self.content if isinstance(b, TextBlock)).strip()


class ToolCall(BaseModel):
    id: str
    name: str
    input: dict[str, Any] = Field(default_factory=dict)


class Usage(BaseModel):
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0

    def __add__(self, other: "Usage") -> "Usage":
        return Usage(
            input_tokens=self.input_tokens + other.input_tokens,
            output_tokens=self.output_tokens + other.output_tokens,
            cache_read_tokens=self.cache_read_tokens + other.cache_read_tokens,
            cache_write_tokens=self.cache_write_tokens + other.cache_write_tokens,
        )


StopReason = Literal["end_turn", "tool_use", "max_tokens", "other"]


class LLMResult(BaseModel):
    text: str = ""
    tool_calls: list[ToolCall] = Field(default_factory=list)
    usage: Usage = Field(default_factory=Usage)
    stop_reason: StopReason = "end_turn"

    def to_message(self) -> Message:
        blocks: list[Any] = []
        if self.text:
            blocks.append(TextBlock(text=self.text))
        blocks.extend(ToolUseBlock(id=c.id, name=c.name, input=c.input) for c in self.tool_calls)
        if not blocks:
            blocks.append(TextBlock(text="(no output)"))
        return Message(role="assistant", content=blocks)


class LLMError(Exception):
    """Provider failure mapped to one type. `retryable` covers throttling, timeouts and 5xx."""

    def __init__(self, message: str, *, retryable: bool, status: int | None = None, provider: str = ""):
        super().__init__(message)
        self.retryable = retryable
        self.status = status
        self.provider = provider


class LLMProvider(Protocol):
    name: str

    async def complete(
        self,
        system: str,
        messages: list[Message],
        tools: list[ToolSpec],
        model: str,
        max_tokens: int,
        temperature: float,
    ) -> LLMResult: ...


@dataclass(frozen=True)
class ModelHandle:
    """A provider plus the model id to call on it."""

    provider: LLMProvider
    model: str

    async def complete(
        self, system: str, messages: list[Message], tools: list[ToolSpec], max_tokens: int, temperature: float
    ) -> LLMResult:
        return await self.provider.complete(system, messages, tools, self.model, max_tokens, temperature)
