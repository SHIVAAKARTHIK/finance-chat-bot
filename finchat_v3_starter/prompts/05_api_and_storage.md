Task 05: v3 API endpoint and aiops storage. Read CLAUDE.md, docs/SPEC.md sections 2 and 7, and
reference/aiops/finance_chat_memory_delta.sql first.

1. storage/aiops.py: databricks-sql-connector with the service principal (DATABRICKS_AUTH=azure_spn), writing to
   lakehouse_mvpai.aiops.finance_chat_* using MERGE on the primary key (tables already designed; create them only if
   they do not exist, with the DDL from the reference file, and only in the aiops schema).
   Mapping for v3:
   - conversations: one row per conversation; turn_count; rolling summary columns (filled in task 07).
   - messages: question_text, standalone_question, intent (data | general | mixed | workflow), answer_path = 'adhoc'
     for data, 'declined' when refused (check constraint allows only kpi/adhoc/clarify/declined), sql_text (audit only),
     sql_source = 'generated', result_row_count, result_preview, answer_text (answer + how_calculated), status,
     token and latency columns. kpi_ids and trust_label stay NULL.
   - message_events: one row per LLM call and tool call (step_name = agent or tool name). Implement the aiops trace sink.
   - Writes must never block the answer: queue and write in the background; log failures.
2. Conversation context: load the last 5 visible turns of the conversation for follow-ups.
3. api/router.py (FastAPI APIRouter, mounted by the existing app at /v3): POST /v3/chat (JSON, SPEC section 7) and
   POST /v3/chat/stream (SSE: step events then final). User identity from the existing auth (Entra object id + groups);
   if the existing app has no identity in the request, accept user_id in the body for now and say so in the report.
4. Remove nothing from v2 yet.

Acceptance
- Tests with a fake connector: MERGE statements built correctly, constraint values respected, background write failure
  does not fail the request.
- Live (RUN_LIVE=1): one ADRA question through /v3/chat writes one conversation row, one message row and event rows.
- Report, including the exact steps for the UI team to call /v3/chat.
