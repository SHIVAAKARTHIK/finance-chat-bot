# Conversation memory: token-based context, topics, clear context

Date: 2026-11-25. Defaults change behaviour (no question limit, token budget). No new tables. One new nullable
column (below). Nothing was run against Databricks or Bedrock.

## What changed

1. **One continuous chat, no question limit.** `CONVERSATION_QUESTION_LIMIT` now defaults to 0, meaning no limit.
   Setting it above 0 brings back the old rollover.
2. **Context is chosen by tokens, not by question count.** Each question gets:
   - the newest turns that fit `HISTORY_TOKEN_BUDGET` (3,000 tokens) word for word. Answers are cut to 1,200
     characters first, and the newest turn is always kept;
   - the rolling summary;
   - "Earlier questions": questions that are neither in the recent turns nor in the summary yet, so nothing falls
     through the gap;
   - the topic list (below) and the user-memory hint, as before.
3. **Summary trigger.** The summary is rewritten (gpt-oss, in the background) when the turns not yet in it pass
   `SUMMARY_TOKEN_THRESHOLD` (now 3,000). The size of the old summary no longer counts, so a long summary doesn't
   trigger a rewrite on every question.
4. **Summary per topic.** One section per business area (`Topic: Fixed assets (turns 1-3)` with entities, periods,
   key numbers and open threads), most recent first. An earlier topic is shortened, never dropped.
5. **Topic state, built in code.** Each turn's domain (from the tables it used) and its entity/period filters are
   already stored on the message row (`domain`, `plan`). They are grouped into "Topics in this conversation", most
   recent first, and the most recent is marked "current topic". Each recent turn shows `[topic: …]`. Business names
   come from the access file (`domains:`), so nothing is hardcoded and it costs no model call.
6. **Which topic does a question belong to?** Supervisor prompt rules, in order:
   1. the question names a topic, entity or metric: use that;
   2. it's a follow-up: use the current topic;
   3. it points back to an earlier topic: use that one;
   4. it fits several topics equally well: the `route` call returns `options`, and the user picks one.
   With options, v3 answers with status `clarification` straight away, without running SQL. Each option is a complete
   question ("Fixed assets: total additions in Oct 2026"), so the UI sends the chosen one as the next question.
7. **"Answering for".** Every data answer carries `answer_context`: topics (business names), entities, periods, and
   `other_topics` from this conversation that the user can switch to. Built in code from the tables used and the SQL
   filters.
8. **Clear context.** `POST /api/invoke/finance-chat/clear-context {conversation_id}` (and
   `POST /v3/conversations/{id}/clear-context`), or typing `/clear` or `/new` in the chat. Later questions ignore the
   summary, turns and topics from before that point. The history stays stored and visible. Only the owner can clear.
   User memory (usual entity) is kept.

## New column (Karthik / Databricks admin, once)

```sql
ALTER TABLE lakehouse_mvpai.aiops.finance_chat_conversations
  ADD COLUMNS (context_start_turn INT COMMENT 'Turns up to this index are ignored as context (clear context)');
```

Until the column exists, answering and history keep working: the read falls back to the old columns and logs the
fix once. Only "clear context" fails, with a clear 503 ("could not be cleared"), and the log names the ALTER statement.

## Settings (.env, all optional)

| Setting | Default | Meaning |
|---|---|---|
| `HISTORY_TOKEN_BUDGET` | 3000 | Tokens of recent turns shown word for word |
| `SUMMARY_TOKEN_THRESHOLD` | 3000 | Unsummarised tokens that trigger a summary rewrite |
| `CONVERSATION_QUESTION_LIMIT` | 0 | 0 = no limit; > 0 = old rollover |

If your laptop `.env` still has `SUMMARY_TOKEN_THRESHOLD=6000` or `CONVERSATION_QUESTION_LIMIT=30`, remove those lines
to get the new defaults.

## Response changes (UI)

- `answer_context`: `{topics, entities, periods, other_topics}` or null. This is new.
- `clarification_options`: a list of strings. This is new. For a clarification, `follow_up_questions` holds the same
  options, so a UI that already renders follow-ups as buttons works without changes.
- The new route `POST /api/invoke/finance-chat/clear-context` returns `{status, conversation_id, cleared,
  context_start_turn, message}`. It's rate-limited like the other routes.
- The v3 JSON envelope gains `options` and `answer_context`.

## Files changed

- New: `memory/context.py`, `tests/test_conversation_context.py` (14 tests).
- Changed: `config.py`, `memory/summary.py`, `agents/prompts/summary.md`, `agents/orchestrator.py`,
  `agents/supervisor.py`, `agents/prompts/supervisor.md`, `api/service.py`, `api/router.py`, `integration/backend.py`,
  `integration/ui_contract.py`, `storage/aiops.py`, `storage/aiops_ddl.sql`, `tests/test_memory.py`,
  `tests/test_storage_api.py`, `tests/test_integration_backend.py`.
- Docs (starter folder): `docs/SPEC.md` (chat-history decision), `reference/aiops/finance_chat_memory_delta.sql`.

## Tests

`pytest finchat_agents/tests`: 375 passed, 30 skipped (live tests). Covered: budget selection, topic state from stored
rows, topic tags in the summary input, topics and turn tags reaching the supervisor, earlier questions listed (no gap),
summary trigger ignoring summary size, no limit by default, topic options leading to a clarification without SQL,
`answer_context`, clear context (saved turn, later questions ignore earlier ones, turns after a clear are used again),
the `/clear` command, other users refused, the missing-column fallback, and the backend route (200 / 403 / 503).

## Assumptions

- A topic = the domain of the tables an answer used (the access-file domains). General-knowledge turns have no topic.
- A clear keeps user memory (it's a habit, not chat context) and keeps the conversation id (one chat per user).
- Clarification options come only from the route call (no extra model call). The supervisor's own `clarification`
  status also passes its `alternatives` as options.

## Open questions / to check on the laptop

- Run the FA → Fynapse scenario: 3 FA questions, 3 Fynapse questions, then "what about last month?" (should use
  Fynapse), "compare with the fixed assets number" (should use FA), and something like "what is the total?" (should
  offer options). Check `standalone_question` and the `route` event in the trace.
- **Heads-up:** the Anthropic SDK warns that `claude-sonnet-4-5` reaches end of life on **30 Nov 2026**, which is the
  Anthropic API model id. Please check Bedrock's date for `us.anthropic.claude-sonnet-4-5-20250929-v1:0` with your
  AWS admin, and plan the switch to a newer Sonnet (`BEDROCK_MODEL_SQL` in `.env`).
