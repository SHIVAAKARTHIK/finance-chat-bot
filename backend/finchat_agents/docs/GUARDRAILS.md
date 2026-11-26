# Guardrail index

Last updated 2026-11-28. Paths are relative to `finchat_agents/`. Setup: `docs/reports/guardrails_report.md`.

**Source:** Company = company pack; App = built into this application. **How:** Code = enforced in code; Model = a
model judges it; Prompt = an instruction to the model (weakest).

## Input (before anything runs)

| ID | Guardrail | Source | How | Where |
|---|---|---|---|---|
| I1 | Message length limit | App | Code | `api/router.py`, `integration/backend.py` |
| I2 | Passwords, keys, emails, phone, card and social security numbers removed from the question | App | Code | `guardrails/input_checks/redact.py` |
| I3 | Instruction attacks (`prompt_injection_shield`) | Company | Model | `guardrails/input_checks/intent.py` |
| I4 | Questions about the assistant (`system_prompt_confidentiality`) | Company | Model | same |
| I5 | Only the approved domain (`scope_enforcement`); follow-ups are also checked with the history | Company | Model | same, `agents/orchestrator.py` |
| I6 | Disallowed capabilities (`disallowed_capabilities`, project version) | Company, changed | Model | same |
| I7 | Security judged on the current message only (`history_isolation`) | Company | Code | `guardrails/input_checks/intent.py` |
| I8 | Abusive, hateful, sexual, violent or unlawful requests | App | Model | same |
| I9 | Reply with help resources when someone may be at risk | App | Model | same |
| I10 | AWS Bedrock Guardrail on the question (**off until configured**) | App | AWS service | `guardrails/bedrock.py` |

## Data and actions (while answering)

| ID | Guardrail | Source | How | Where |
|---|---|---|---|---|
| D1 | Read-only: one `SELECT` / `WITH` statement | App | Code | `tools/sql_guard.py` |
| D2 | Approved catalog tables only | App | Code | `tools/sql_guard.py` |
| D3 | Role may use only its business areas | App | Code | `access/rbac.py`, `tools/sql_guard.py` |
| D4 | Personal-data columns masked; no filtering or grouping on them | App | Code | `tools/sql_guard.py`, `tools/run_sql.py` |
| D5 | Contact details, keys and storage paths removed from results (`content_safety`) | Company | Code | `tools/run_sql.py` |
| D6 | Row, time, step and query limits per question | App | Code | `runtime/tools.py`, `tools/run_sql.py` |
| D7 | Data is never an instruction | App | Prompt | `agents/prompts/data_rule.md` |
| D8 | Only Excel and report files; nothing is sent; text stays text in Excel | App | Code | `tools/actions.py` |

## Output (before the user sees it)

| ID | Guardrail | Source | How | Where |
|---|---|---|---|---|
| O1 | Fixed refusal replies are exact | Company | Code | `guardrails/output_checks/answer.py` |
| O2 | Answers only from approved data (`grounded_answering`, project version) | Company, changed | Prompt, Code (marker) | agent prompts, `output_checks/answer.py` |
| O3 | Every number must come from a query result | App | Code | `agents/number_check.py` |
| O4 | Contact details, keys, paths, model and table names removed | Company | Code | `guardrails/output_checks/filters.py` |
| O5 | Same treatment for all demographics (`demographic_neutrality`) | Company | Prompt | agent prompts |
| O6 | No agent or tool names in progress events | Company | Code | `api/router.py`, `integration/stream.py` |
| O7 | AWS Bedrock Guardrail on the answer text (**off until configured**) | App | AWS service | `guardrails/bedrock.py` |

## Access and audit

| ID | Guardrail | Source | How | Where |
|---|---|---|---|---|
| A1 | Verified login required; users see only their own conversations and files | App | Code | `api/router.py`, `api/service.py`, `api/files.py` |
| A2 | Request rate limit (10 per minute) | Company backend | Code | backend `slowapi` decorator |
| A3 | Model calls, tool calls and every guardrail decision logged (see Audit log) | App | Code | `tracing/`, `guardrails/audit.py` |

## Audit log

Every check records a decision (`allow`, `block`, `change` or `error`) with its rule and reason. Removed content itself is
never recorded.

| Check (`step_name`) | Records |
|---|---|
| `input_redaction` | Sensitive data removed from the question, or nothing |
| `access_check` | Whether the user has a role |
| `input_check` | The input check verdict; a switched-off rule is recorded as allowed |
| `scope_check` | The routing step's in-scope or refusal decision |
| `data_check` | Each user query: allowed (tables, masked values) or refused |
| `number_check` | Numbers compared with the data |
| `answer_check` | The assistant declined while answering |
| `output_check` | Answer unchanged, changed or replaced |
| `content_filter_input`, `content_filter_output` | AWS content filter, when configured |

Stored in `lakehouse_mvpai.aiops.finance_chat_message_events` (also in `traces/events.jsonl`):

```sql
SELECT m.created_at, m.user_id, m.conversation_id, m.message_id, m.question_text, e.step_name AS check_name,
       get_json_object(e.output_payload, '$.decision') AS decision,
       get_json_object(e.output_payload, '$.rule')     AS rule,
       get_json_object(e.output_payload, '$.reason')   AS reason
FROM lakehouse_mvpai.aiops.finance_chat_message_events e
JOIN lakehouse_mvpai.aiops.finance_chat_messages m ON m.message_id = e.message_id
WHERE get_json_object(e.output_payload, '$.decision') IS NOT NULL
ORDER BY m.created_at DESC, e.step_order;
```

Add `AND get_json_object(e.output_payload, '$.decision') = 'block'` for refusals only.

Requests with no chat message (missing login, file download, another user's conversation) are written to the application
log, logger `finchat_agents.audit` (`guardrail decision=... check=... rule=... user=... reason=...`). Keeping that log
is a platform setting. The request rate limit is the backend's and is not logged here.

**Limits:** audit rows are written in the background; a failed write is reported in the application log and
`/v3/health` (`write_failures`), and that entry is not retried. Without aiops storage only the trace file is written.

## Switches

| Setting | Default | Effect |
|---|---|---|
| `GUARDRAILS_ENABLED` | true | false turns off I2-I10, D5, O1, O2 marker, O4-O7 |
| `GUARDRAILS_DIR` | guardrails | Folder with `guardrail.yaml`, `packs/` (added by hand), `overrides/`, notes |
| `BEDROCK_GUARDRAIL_ID`, `BEDROCK_GUARDRAIL_VERSION` | empty | Turn on I10 and O7 |
| `ALLOW_REQUEST_IDENTITY` | false | true weakens A1: local testing only |

## Testing

- Offline: `pytest finchat_agents/tests` (fake models; proves the wiring, not model judgement).
- Live attack tests for the input checks: `RUN_LIVE=1`, then `python -m finchat_agents.guardrails.evaluate`.

## Not covered

- Per-user daily question limit.
- Pack rules for the summary card writer (its data is cleaned by D5).
- Checking statements other than numbers against the data.
- Personal names in free text (only flagged columns are masked).
- Bedrock masking is applied to answers; on questions it only blocks.
- Alerts on repeated blocked requests, and a chat retention rule.
- The `/v3` clear-context route can return internal error text.

## Pending approval

The project versions of `disallowed_capabilities` and `grounded_answering`, and `application_notes.md`.
