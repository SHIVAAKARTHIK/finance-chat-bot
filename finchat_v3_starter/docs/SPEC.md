# Finance Chat v3: build spec (source of truth)

Last updated: 20 Nov 2026. This file replaces the earlier plan where they differ. If something here is unclear, ask Karthik; do not guess.

## 1. What we are building

A multi-agent ReAct assistant that answers questions over the Databricks catalog `lakehouse_mvpai`
(about 50 tables in `silver`, about 72 in `gold`), answers general questions from model knowledge,
and follows multi-step instructions a user pastes into the chat. Agents choose the tables, write the
SQL, repair it, and explain the result. Latency is accepted in exchange for answering more questions.

v3 **fully replaces v2** (the LangGraph / KPI / JSON-spec pipeline). v3 is built on branch `finance-agentic`,
created from `development`, without the v2 finance code; v2 stays on `feature/finance-kpi` as the fallback.
Reusable v2 knowledge is in `reference/legacy/`; never import from v2.

Out of scope: web search, writing to `silver` or `gold`, KPI layer, row-level entity filters.

## 2. Fixed decisions

| Topic | Decision |
|---|---|
| Location | New package `backend/finchat_agents/`. FastAPI wiring only at the end, as a new endpoint. |
| Orchestration | Our own ReAct loop. **No LangGraph, no LangChain.** |
| Models (both on AWS Bedrock) | `BEDROCK_MODEL_SQL` = Claude Sonnet 4.5 (`us.anthropic.claude-sonnet-4-5-20250929-v1:0`) for supervisor, catalog, SQL, analyst, investigator. `BEDROCK_MODEL_RESPONSE` = gpt-oss-120b (`openai.gpt-oss-120b-1:0`) for routing, final wording, summaries, titles. |
| SDKs | `anthropic` (`AnthropicBedrock`) for Claude. For gpt-oss: `openai` SDK against Bedrock's OpenAI-compatible endpoint **if** tool calling works there in our region, otherwise `boto3` Converse. Check latest versions before pinning. |
| Data access | Databricks **DBSQL MCP server** (`/api/2.0/mcp/sql`). Agents may only use `execute_sql_read_only` and `poll_sql_result`. Never `execute_sql`. See `docs/MCP_NOTES.md`. |
| Auth | Service principal, OAuth client credentials (Entra ID), scope `2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default`. Token lasts about 1 hour: refresh before expiry. No personal access tokens. |
| App storage | `lakehouse_mvpai.aiops` tables from `reference/aiops/finance_chat_memory_delta.sql`, written with `databricks-sql-connector` using the same service principal (MCP is read-only). |
| Access control | Role by Entra object ID or group name (from `config/rbac.v3.yaml`). Role lists domains. Every table has one domain tag. A query touching a table outside the user's domains is refused. Unknown user = no access. |
| Row-level filters | **None.** No engagement key, legal entity, parent entity or data area filters anywhere. |
| KPIs | None: no KPI search, registry or routing. Standard metric definitions, if needed, go in the glossary and examples library. A governed `lookup_metric` tool may be added later as a hint the agent can use or ignore. |
| Modes | One runtime, two modes: fast path for simple single-domain questions, full ReAct loop for complex ones or when the fast path fails (section 3). |
| SQL display | Never shown to users. Every data answer has a business-language `how_calculated`. SQL is kept in traces. |
| Ambiguity | Answer with the most likely reading first, then offer the alternative ("Cars USA also has data for this period; do you want that too?"). Do not block on clarification unless nothing sensible can be assumed. |
| General questions | Any topic, from model knowledge, no web. Labelled as general knowledge. Never used for our numbers. |
| Actions | `export_excel` and `save_report` only, chosen per request. Nothing is sent or shared automatically. |
| Chat history | One continuous chat per user, no question limit (decided 2026-11-25). Context chosen by tokens: the newest turns that fit `HISTORY_TOKEN_BUDGET` (3,000) verbatim, plus a rolling summary written per topic (business area) when the turns not yet in it pass `SUMMARY_TOKEN_THRESHOLD` (3,000), plus a topic list (domains, entities, periods) built in code. Follow-ups use the current topic; when a question fits several earlier topics the user picks from options. A "Clear context" action makes later questions ignore everything before it; the history stays. `CONVERSATION_QUESTION_LIMIT` > 0 brings back the old rollover. |
| Language | English only. |
| UI | Existing UI stays; it renders only the final answer. Produce step events anyway (logged, streamable later). |
| Latency targets | General < 10 s; simple data < 30 s; analysis < 2 min; workflows < 5 min. |
| Users | Internal KPMG only. |

## 3. Architecture

```
user -> API -> Supervisor (Sonnet)
                 |-- ask_catalog_agent   -> search_tables, describe_table, get_join_path, get_column_values, get_glossary
                 |-- ask_sql_agent       -> describe_table, get_column_values, run_sql, resolve_period, resolve_entity
                 |-- ask_analyst_agent   -> ask_sql_agent (per sub-query), calculate
                 |-- ask_knowledge_agent -> model only (+ get_glossary)
                 |-- ask_action_agent    -> export_excel, save_report
                 '-- final answer (gpt-oss wording) + how_calculated + number check
run_sql -> guardrails (code) -> MCP execute_sql_read_only / poll_sql_result -> Databricks
```

Agents are exposed to the supervisor as tools; each call gets a fresh context and returns a structured
result (answer text, rows sample, SQL, notes). Only the supervisor talks to the user.

### Two modes in one runtime (no LangGraph)

Orchestration is plain Python: our ReAct loop (`runtime/loop.py`), `asyncio` for parallel calls and
timeouts, and pydantic models for state. A "node" is a function, an "edge" is an `if`, state is a pydantic object.

1. **Classify** inside the supervisor's first step (no separate router LLM call): `general`, `simple_data`
   (one domain, likely one table or one approved join, no multi-step analysis, no workflow), or `complex`
   (analysis, comparisons across queries, workflows, actions, or unclear).
2. **Fast path** for `simple_data`: a fixed Python sequence using the same tools and guardrails:
   `search_tables` -> SQL agent writes SQL (1 LLM call) -> `run_sql` -> if error or empty, repair once ->
   answer writer (1 LLM call). Target about 3 LLM calls.
3. **Escalate** to the full ReAct loop when the fast path returns nothing usable or the question is
   `complex`. The loop starts with what the fast path already found (tables, SQL tried, error), never from scratch.
4. `general` goes straight to the knowledge agent.

There is **no KPI search, KPI registry or KPI routing** in either mode. Both modes search tables only.
Record per answer which mode ran (`fast` / `react` / `fast->react`) in the trace for latency analysis.

## 4. Guardrails (code inside tools; prompts cannot bypass them)

1. Read-only: sqlglot parses the SQL; exactly one SELECT/WITH statement.
2. Allowed tables: only tables in the catalog index (`lakehouse_mvpai.silver.*`, `lakehouse_mvpai.gold.*`).
3. Role access: every table in the query must be in a domain the user's role allows.
4. PII: columns flagged `pii: true` are masked in returned rows unless the role allows PII
   (default: no role allows PII until Karthik confirms).
5. Limits: row limit (default 1,000 returned, 50 shown to the model), query timeout, max SQL calls per question.
6. Numbers come from data: numbers in the final answer must appear in tool results (allow rounding);
   otherwise rewrite once, then add a caveat.
7. Errors are returned to the agent as plain, fixable messages ("table X is not in the catalog; did you mean Y?").
8. Audit: every LLM call and tool call is an event row in `finance_chat_message_events`.
9. Company guardrails (2026-11-26): packs and values are read from `GUARDRAILS_DIR` (not in the repository); the app does not
   start without them unless `GUARDRAILS_ENABLED=false`. Applied as prompt rules, an input check on the current message only,
   and code checks on query results and answers. Decided: general finance knowledge, calculations and Excel/report files stay
   (project versions of two packs, pending the guardrails owner's approval).

## 5. Knowledge layer

Lives in `backend/finchat_agents/knowledge/` as reviewed Markdown + YAML, generated then edited by people:

- `tables/<schema>.<table>.md`: purpose, layer, domain, grain, keys, columns (type, meaning, synonyms,
  real values, pii flag), joins, known issues, 2-3 verified examples. Format: `reference/semantic_pages/`.
- `INDEX.md` + search index: one line per table (domain, layer, grain, purpose).
- `joins.yaml`: approved join keys (composite keys in full), including gold-to-silver lineage.
- `glossary.md`: business terms -> tables, columns, filters.
- `rules.md`: query conventions (balances are point-in-time, never summed across periods; prefer gold; etc.).
- `examples.yaml`: verified question -> SQL pairs, retrieved by similarity as few-shot examples.

Source for 122 tables: the Excel from `scripts/export_table_catalog.py` (sheets Tables, Keys, Columns, Values,
Samples, Fill_in, Errors) plus the reviewed `fill_in_reviewed_*.csv`, placed in `data/table_catalog/` (never committed).
The generator never overwrites fields a person edited. Objects that fail to query (Errors sheet, e.g. views referencing
dropped columns) get `status: broken` and are excluded from search and run_sql until a later export reads them.

## 6. Known data facts

- ADRA: 6 tables (`adra_account_facts` 97 rows, transaction facts, account / legal entity / period /
  engagement dimensions). Composite keys; see `reference/semantic_pages/adra/joins.md`.
- Fynapse: `fact_fynapse_slr_journals`. **The entity values recently changed from UK03/UK06/UK07/UK13/UK14/UK17
  to 100** (being confirmed with the data team). Table pages must describe current values; no hardcoded entities.
- Fixed assets: source tables are loaded twice (for example 600 rows instead of 300). Not fixed.
  Agents must detect duplicate rows at the grain, warn, and only deduplicate on the business key if they say so.
- Entity key 9819 rows have no matching dimension (orphans).

## 7. API (new, v3)

`POST /v3/chat` request: `{conversation_id?, message, user_id (Entra object id), groups?}`
Response:
```json
{"conversation_id": "", "message_id": "", "status": "answered|partial|clarification|declined|failed",
 "answer": "", "how_calculated": "", "tables": [{"title": "", "columns": [], "rows": []}],
 "files": [{"name": "", "path": ""}], "suggestions": [""], "notices": [""]}
```
`POST /v3/chat/stream` (SSE) emits step events then the final payload; optional until the UI supports it.

## 8. Evaluation

- Question banks in `reference/question_bank/` (ADRA, Fynapse, close/recon) with expected values from Databricks.
- Score by code: numbers compared with tolerance. LLM judge only for wording.
- Categories: correct, partial, could-not-answer, wrong, error. Target: zero wrong.
- Consistency: sample asked 3 times must agree. Safety: out-of-domain table, PII, write attempts must be refused.
- The hold-out set is kept **outside** this repo and never shown to the agent being tuned.
- Fixes are generic: table pages, glossary, examples, prompts. No per-question code.

## 9. Monday (23 Nov) target: about 60%

Prompts 01-05 in `prompts/`: runtime, knowledge layer for ADRA / Fynapse / FA, data tools over MCP,
supervisor + catalog + SQL + knowledge agents, v3 API with aiops storage, and a first scorecard.
Later: analyst and action agents, workflows, summaries and 30-question limit, all 122 tables, summary agent, deploy, v2 removal.

## 10. Open items (do not block; use the default shown)

| Item | Default until confirmed |
|---|---|
| Group-to-role mapping looks shifted (Controller -> ar_reader, AR analyst -> gl_reader, Treasurer -> fa_reader, Fixed asset analyst -> cash_reader) | Keep the file as is; flag it in the report |
| Domains for ADRA and Fynapse | `recon` (ADRA) and `subledger` (Fynapse); only `finance_all` has them |
| PII columns | Person-name / email columns treated as PII; no role sees PII |
| 30-question rollover | Replaced 2026-11-25 by one continuous chat with token-based memory and clear context (rollover only if `CONVERSATION_QUESTION_LIMIT` > 0) |
| Fynapse entity change | Use whatever values are in the table now |
