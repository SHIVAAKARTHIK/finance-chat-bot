"""Background writes: the answer never waits for storage. Jobs run in order on one worker; failures are logged."""
from __future__ import annotations

import asyncio
import logging
from typing import Awaitable, Callable

log = logging.getLogger(__name__)

Job = Callable[[], Awaitable[None]]


class BackgroundWriter:
    def __init__(self, *, max_queue: int = 10_000):
        self._queue: asyncio.Queue[tuple[str, Job]] = asyncio.Queue(maxsize=max_queue)
        self._task: asyncio.Task | None = None
        self.failures: list[str] = []  # last errors, for health checks and tests

    def start(self) -> None:
        if self._task is None or self._task.done():
            self._task = asyncio.get_running_loop().create_task(self._run(), name="aiops-writer")

    def submit(self, name: str, job: Job) -> None:
        """Queue a write and return immediately. A full queue drops the write (logged), never blocks."""
        self.start()
        try:
            self._queue.put_nowait((name, job))
        except asyncio.QueueFull:
            log.error("aiops write queue full; dropped %s", name)
            self._remember(f"{name}: queue full")

    async def _run(self) -> None:
        while True:
            name, job = await self._queue.get()
            try:
                await job()
            except Exception as exc:  # storage problems must not affect answers
                log.exception("aiops write %s failed", name)
                self._remember(f"{name}: {type(exc).__name__}: {str(exc)[:300]}")
            finally:
                self._queue.task_done()

    def _remember(self, msg: str) -> None:
        self.failures.append(msg)
        del self.failures[:-50]

    async def flush(self, timeout: float = 30.0) -> None:
        """Wait until queued writes are done (tests, shutdown)."""
        if self._task is None:
            return
        await asyncio.wait_for(self._queue.join(), timeout)

    async def stop(self, timeout: float = 30.0) -> None:
        try:
            await self.flush(timeout)
        finally:
            if self._task is not None:
                self._task.cancel()
                self._task = None
