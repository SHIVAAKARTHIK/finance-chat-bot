"""aiops trace sink: buffers one question's LLM and tool events and writes them to finance_chat_message_events in
the background when the orchestrator emits its final `answer` event (or on close)."""
from __future__ import annotations

from ..tracing.events import TraceEvent
from .aiops import AiopsStore
from .records import event_row
from .writer import BackgroundWriter

WRITE_BATCH = 50


class AiopsTraceSink:
    def __init__(self, store: AiopsStore, writer: BackgroundWriter, *, conversation_id: str):
        self.store = store
        self.writer = writer
        self.conversation_id = conversation_id
        self._rows: list[dict] = []
        self._order = 0

    async def write(self, event: TraceEvent) -> None:
        if event.type in ("llm_call", "tool_call") and event.message_id:
            self._order += 1
            self._rows.append(event_row(event, conversation_id=self.conversation_id, step_order=self._order))
        if event.type == "answer":
            self.close()

    def close(self) -> None:
        rows, self._rows = self._rows, []
        for i in range(0, len(rows), WRITE_BATCH):
            batch = rows[i : i + WRITE_BATCH]
            self.writer.submit(
                f"events {batch[0]['message_id']} #{i // WRITE_BATCH + 1}",
                lambda batch=batch: self.store.upsert("finance_chat_message_events", batch),
            )
