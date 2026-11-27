# Checking the logs

How to see what happened for a question: which agents ran, how often Databricks was called, what was slow, and what the
guardrails decided. Run the SQL in the Databricks SQL Editor. All queries only read.

The logs hold users' questions, SQL and some result values: share query output only with people allowed to see that data.

## Where the logs are

| Place | One row per | Use it for |
|---|---|---|
| `lakehouse_mvpai.aiops.finance_chat_messages` | Question | Total time, model calls, tokens, final SQL, status |
| `lakehouse_mvpai.aiops.finance_chat_message_events` | Step (model call or tool call) | Timeline, durations, Databricks calls, guardrail decisions |
| `lakehouse_mvpai.aiops.finance_chat_conversations` | Conversation | Memory summary, clear-context point |
| `finchat_agents/traces/events.jsonl` | Every event, on the app server | Same, plus routing and agent start / end |

Logs are saved in the background after the answer: wait a few seconds before querying.

## How to read an event row

| Column | Meaning |
|---|---|
| `step_name` | For a model call: the agent. Otherwise the tool or check (`run_sql`, `databricks_query`, `input_check`) |
| `model_name` | Filled only for model calls |
| `input_payload` | JSON: `agent` (who), and for tools `input` (arguments or SQL) |
| `output_payload` | JSON: tool `output`; model `text` and `tool_calls`; guardrails `decision`, `rule`, `reason` |
| `status` | `ok` or `failed` |
| `duration_ms` | Time of this step. Steps can overlap or contain others (`ask_sql_agent` includes its own steps) |

In the queries below, `:message_id` is a parameter: the SQL Editor shows a box for it. Get the value from query 1.

## 1. Recent questions

```sql
SELECT message_id, conversation_id, created_at, question_text, status, total_latency_ms / 1000 AS seconds,
       llm_call_count, input_tokens, output_tokens
FROM lakehouse_mvpai.aiops.finance_chat_messages
ORDER BY created_at DESC
LIMIT 20;
```

## 2. Timeline of one question (how the agents ran)

```sql
SELECT timestampdiff(MILLISECOND, MIN(started_at) OVER (), started_at) AS starts_at_ms,
       get_json_object(input_payload, '$.agent') AS agent,
       step_name,
       CASE WHEN model_name IS NULL THEN 'tool or check' ELSE 'model call' END AS kind,
       status,
       duration_ms
FROM lakehouse_mvpai.aiops.finance_chat_message_events
WHERE message_id = :message_id
ORDER BY started_at, step_order;
```

The latest question, without copying an id:

```sql
SELECT timestampdiff(MILLISECOND, MIN(started_at) OVER (), started_at) AS starts_at_ms,
       get_json_object(input_payload, '$.agent') AS agent, step_name, status, duration_ms
FROM lakehouse_mvpai.aiops.finance_chat_message_events
WHERE message_id = (SELECT message_id FROM lakehouse_mvpai.aiops.finance_chat_messages ORDER BY created_at DESC LIMIT 1)
ORDER BY started_at, step_order;
```

## 3. Slowest steps of one question

```sql
SELECT get_json_object(input_payload, '$.agent') AS agent, step_name, model_name, duration_ms
FROM lakehouse_mvpai.aiops.finance_chat_message_events
WHERE message_id = :message_id
  AND step_name NOT LIKE 'ask\_%'          -- wrapper steps: their time is the steps inside them
ORDER BY duration_ms DESC NULLS LAST
LIMIT 10;
```

## 4. Databricks calls of one question

Each real query is one `databricks_query` row; `lookup_cache_hit` rows used the cache and made no query.
`run_sql` rows contain a query, so do not add their time to the `databricks_query` time.

```sql
SELECT started_at,
       get_json_object(input_payload, '$.agent')   AS caller,
       step_name,
       status,
       duration_ms,
       get_json_object(output_payload, '$.output') AS outcome,
       get_json_object(input_payload, '$.input')   AS sql_or_lookup
FROM lakehouse_mvpai.aiops.finance_chat_message_events
WHERE message_id = :message_id
  AND step_name IN ('databricks_query', 'lookup_cache_hit')
ORDER BY started_at;
```

Count and total time:

```sql
SELECT COUNT_IF(step_name = 'databricks_query')                               AS databricks_calls,
       SUM(CASE WHEN step_name = 'databricks_query' THEN duration_ms END)     AS databricks_ms,
       MAX(CASE WHEN step_name = 'databricks_query' THEN duration_ms END)     AS slowest_ms,
       COUNT_IF(step_name = 'lookup_cache_hit')                               AS cache_hits,
       COUNT_IF(step_name = 'databricks_query' AND status = 'failed')         AS failed_calls
FROM lakehouse_mvpai.aiops.finance_chat_message_events
WHERE message_id = :message_id;
```

## 5. Databricks calls per question (last 7 days)

```sql
SELECT m.created_at, m.question_text, m.total_latency_ms / 1000 AS total_seconds,
       COUNT(e.event_id)             AS databricks_calls,
       SUM(e.duration_ms) / 1000     AS databricks_seconds
FROM lakehouse_mvpai.aiops.finance_chat_messages m
LEFT JOIN lakehouse_mvpai.aiops.finance_chat_message_events e
       ON e.message_id = m.message_id AND e.step_name = 'databricks_query'
WHERE m.created_at >= current_timestamp() - INTERVAL 7 DAYS
GROUP BY m.message_id, m.created_at, m.question_text, m.total_latency_ms
ORDER BY databricks_calls DESC, total_seconds DESC;
```

Questions asked before call logging was installed show 0 calls.

## 6. Model calls and tokens of one question

```sql
SELECT step_name AS agent, model_name, COUNT(*) AS calls, SUM(duration_ms) AS total_ms, MAX(duration_ms) AS slowest_ms,
       SUM(input_tokens) AS input_tokens, SUM(output_tokens) AS output_tokens, SUM(cache_read_tokens) AS cached_tokens
FROM lakehouse_mvpai.aiops.finance_chat_message_events
WHERE message_id = :message_id AND model_name IS NOT NULL
GROUP BY step_name, model_name
ORDER BY total_ms DESC;
```

## 7. Performance over time

Slow questions:

```sql
SELECT message_id, created_at, question_text, total_latency_ms / 1000 AS seconds, llm_call_count, status
FROM lakehouse_mvpai.aiops.finance_chat_messages
WHERE created_at >= current_timestamp() - INTERVAL 7 DAYS AND total_latency_ms > 30000
ORDER BY total_latency_ms DESC;
```

Per day:

```sql
SELECT CAST(created_at AS DATE) AS day, COUNT(*) AS questions,
       ROUND(percentile_approx(total_latency_ms, 0.5) / 1000, 1) AS typical_seconds,
       ROUND(percentile_approx(total_latency_ms, 0.9) / 1000, 1) AS slow_9_in_10_seconds,
       ROUND(AVG(llm_call_count), 1) AS model_calls_per_question
FROM lakehouse_mvpai.aiops.finance_chat_messages
WHERE created_at >= current_timestamp() - INTERVAL 14 DAYS AND status <> 'processing'
GROUP BY CAST(created_at AS DATE)
ORDER BY day DESC;
```

Which steps take the time:

```sql
SELECT step_name, COUNT(*) AS times_run,
       percentile_approx(duration_ms, 0.5) AS typical_ms,
       percentile_approx(duration_ms, 0.9) AS slow_9_in_10_ms,
       SUM(duration_ms) / 1000 AS total_seconds
FROM lakehouse_mvpai.aiops.finance_chat_message_events
WHERE created_at >= current_timestamp() - INTERVAL 7 DAYS AND duration_ms > 0
GROUP BY step_name
ORDER BY total_seconds DESC;
```

## 8. Errors

```sql
SELECT m.created_at, m.question_text, m.status AS question_status, e.step_name,
       get_json_object(e.input_payload, '$.agent') AS agent,
       COALESCE(e.error_message, get_json_object(e.output_payload, '$.output'), m.error_message) AS error
FROM lakehouse_mvpai.aiops.finance_chat_message_events e
JOIN lakehouse_mvpai.aiops.finance_chat_messages m ON m.message_id = e.message_id
WHERE e.status = 'failed' AND e.created_at >= current_timestamp() - INTERVAL 7 DAYS
ORDER BY m.created_at DESC;
```

Questions that never finished (still `processing` after 10 minutes):

```sql
SELECT message_id, created_at, question_text
FROM lakehouse_mvpai.aiops.finance_chat_messages
WHERE status = 'processing' AND created_at < current_timestamp() - INTERVAL 10 MINUTES
ORDER BY created_at DESC;
```

## 9. Guardrail decisions

All checks of recent questions:

```sql
SELECT m.created_at, m.user_id, m.message_id, m.question_text, e.step_name AS check_name,
       get_json_object(e.output_payload, '$.decision') AS decision,
       get_json_object(e.output_payload, '$.rule')     AS rule,
       get_json_object(e.output_payload, '$.reason')   AS reason
FROM lakehouse_mvpai.aiops.finance_chat_message_events e
JOIN lakehouse_mvpai.aiops.finance_chat_messages m ON m.message_id = e.message_id
WHERE get_json_object(e.output_payload, '$.decision') IS NOT NULL
ORDER BY m.created_at DESC, e.step_order
LIMIT 200;
```

Blocks and changes by rule (last 30 days):

```sql
SELECT e.step_name AS check_name,
       get_json_object(e.output_payload, '$.rule')     AS rule,
       get_json_object(e.output_payload, '$.decision') AS decision,
       COUNT(*) AS times
FROM lakehouse_mvpai.aiops.finance_chat_message_events e
WHERE get_json_object(e.output_payload, '$.decision') IN ('block', 'change', 'error')
  AND e.created_at >= current_timestamp() - INTERVAL 30 DAYS
GROUP BY e.step_name, get_json_object(e.output_payload, '$.rule'), get_json_object(e.output_payload, '$.decision')
ORDER BY times DESC;
```

Refused logins, file downloads and access to another user's conversation are in the application log (logger
`finchat_agents.audit`), not in these tables. What each check means: `GUARDRAILS.md`.

## 10. Conversation memory

How follow-ups were understood:

```sql
SELECT turn_index, question_text, standalone_question, domain, status
FROM lakehouse_mvpai.aiops.finance_chat_messages
WHERE conversation_id = :conversation_id
ORDER BY turn_index;
```

Summary and clear-context point:

```sql
SELECT conversation_id, turn_count, summary_through_turn, context_start_turn, last_message_at, summary
FROM lakehouse_mvpai.aiops.finance_chat_conversations
WHERE conversation_id = :conversation_id;
```

Time spent loading the history:

```sql
SELECT created_at, duration_ms
FROM lakehouse_mvpai.aiops.finance_chat_message_events
WHERE step_name = 'load_context'
ORDER BY created_at DESC
LIMIT 20;
```

## 11. Local trace file (PowerShell, from the `backend` folder)

Load the latest events and pick the last question:

```powershell
$e = Get-Content finchat_agents\traces\events.jsonl -Tail 400 | ConvertFrom-Json
$id = ($e | Where-Object type -eq "answer" | Select-Object -Last 1).message_id
```

Timeline:

```powershell
$e | Where-Object message_id -eq $id | Select-Object started_at, agent, type, name, status, duration_ms | Format-Table -AutoSize
```

Databricks calls:

```powershell
$e | Where-Object { $_.message_id -eq $id -and $_.name -in "databricks_query","lookup_cache_hit" } | Select-Object agent, name, duration_ms | Format-Table -AutoSize
```

The file is not rotated or cleaned automatically.

## Not logged

- Each read and write of chat history, memory and the log tables themselves (history loading is one `load_context` step).
- Warm-up and the summary job's queries.
- Connecting to Databricks separately from running the query: a query's duration includes both.
- A log write that fails is reported in the application log and `/v3/health` (`write_failures`) and is not retried.
