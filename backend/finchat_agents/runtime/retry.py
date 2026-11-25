"""Retry with exponential backoff and jitter for retryable LLM errors (throttling, timeouts, 5xx)."""
from __future__ import annotations

import asyncio
import random
import time
from typing import Awaitable, Callable, TypeVar

from ..llm.types import LLMError

T = TypeVar("T")


async def call_with_retry(
    fn: Callable[[], Awaitable[T]],
    *,
    attempts: int = 4,
    base_delay: float = 1.0,
    max_delay: float = 20.0,
    deadline: float | None = None,
    sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    clock: Callable[[], float] = time.monotonic,
    on_retry: Callable[[int, LLMError, float], None] | None = None,
) -> T:
    """Call `fn`; on a retryable LLMError wait base*2^n (+-25% jitter, capped) and try again.

    Gives up early when the wait would pass `deadline` (a `clock()` value). Non-retryable errors raise at once.
    """
    for attempt in range(1, attempts + 1):
        try:
            return await fn()
        except LLMError as exc:
            if not exc.retryable or attempt == attempts:
                raise
            delay = min(max_delay, base_delay * (2 ** (attempt - 1)))
            delay *= random.uniform(0.75, 1.25)
            if deadline is not None and clock() + delay >= deadline:
                raise
            if on_retry:
                on_retry(attempt, exc, delay)
            await sleep(delay)
    raise AssertionError("unreachable")  # pragma: no cover
