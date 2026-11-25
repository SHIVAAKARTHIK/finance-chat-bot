# Finance Chat v3: starter pack for Claude Code

Everything needed to start building v3 in Claude Code. Read in this order: this file, `CLAUDE.md`, `docs/SPEC.md`.

## Contents

| Path | What it is |
|---|---|
| `CLAUDE.md` | Rules Claude Code must follow (no commits, no secrets, no LangGraph, read-only data, no entity filters, no KPI code) |
| `docs/SPEC.md` | The build spec: all decisions, architecture, guardrails, API, evaluation, open items with defaults |
| `docs/MCP_NOTES.md` | Tested facts about the Databricks DBSQL MCP server: auth, tools, response format |
| `prompts/01..10` | One prompt per Claude Code task, in order. 01-05 are the Monday target |
| `prompts/catalog_fill_copilot.md` | Low-credit Copilot prompt to draft domain, purpose, grain and lineage for the 122 tables |
| `config/.env.example` | Environment variable names (no values) |
| `config/rbac.v3.yaml` | Access file template: role -> domains, no row-level scopes. Has TODOs for you |
| `reference/semantic_pages/` | Reviewed ADRA and Fynapse table pages, joins, metrics, rules, verified queries |
| `reference/question_bank/` | ADRA, Fynapse and close/recon questions with expected answers, plus the ground-truth SQL |
| `reference/aiops/` | DDL for the `lakehouse_mvpai.aiops.finance_chat_*` tables (memory, events, feedback) |
| `reference/legacy/` | v2 knowledge worth reusing: silver query skill, glossary, domains, calendar |
| `reference/code/` | fincore (guard, resolvers, executor, DuckDB fixture) and the ReAct agent package, to copy from |
| `scripts/export_table_catalog.py` | Read-only catalog export: all columns with stats and values, sample rows, declared and proposed keys, proposed grain, duplicate rows, broken objects |
| `data/table_catalog/` | Put the catalog Excel, summary and reviewed CSVs here (task 08). Never commit them |

Not included on purpose: the hold-out question set (keep it outside the repo), any secrets.

## How to start

Before Claude Code:
1. Create `finance-agentic` from `development` (Claude Code never changes branches or commits). Copy the v2 files listed below into `reference/legacy/v2_config/` first.
2. Unzip at the repo root as `finchat_v3_starter/`.
3. Fill in the TODOs in `config/rbac.v3.yaml` (at least the users block; role mapping before task 03).
4. Check `backend/.env` has the names in `config/.env.example` (service principal, rotated secret, `DATABRICKS_MCP_URL`)
   and that `.env` is git-ignored. Check AWS Bedrock access works on this machine.

Two tracks, in parallel:

**Track 1: build (Claude Code), start now.** Prompts 01-05 need only what is in this pack.
Send: *"Read finchat_v3_starter/README.md, CLAUDE.md and docs/SPEC.md. Then do the task in prompts/01_setup_and_runtime.md only. Stop and report when done."*
After each task: read the report, run the tests yourself (`pytest`; `RUN_LIVE=1` for live checks), commit, then the next prompt.

**Track 2: the 122-table catalog.**
1. Run `scripts/export_table_catalog.py --env <path to .env>` (read-only). Output: `output/table_catalog.xlsx`,
   `output/fill_in.csv`, `output/catalog_summary.md`.
2. Run `prompts/catalog_fill_copilot.md` in Copilot, once for silver and once for gold.
3. Review the drafts (domain and grain first), save as `fill_in_reviewed_silver.csv` / `fill_in_reviewed_gold.csv`.
4. Copy the files into `data/table_catalog/` and, once tasks 01-03 are done, run prompt 08 in Claude Code.
5. Send the broken objects (Errors sheet) to the data team.

## Copy from v2 before starting (v2 stays on feature/finance-kpi)

PowerShell (the `| Set-Content -Encoding utf8` part matters: a plain `>` in Windows PowerShell 5.1 writes UTF-16 and breaks YAML):

```powershell
mkdir finchat_v3_starter\reference\legacy\v2_config
git show feature/finance-kpi:backend/finance_intelligence/config/rbac.silver.yaml | Set-Content -Encoding utf8 finchat_v3_starter\reference\legacy\v2_config\rbac.silver.yaml
git show feature/finance-kpi:backend/finance_intelligence/config/tables.yaml | Set-Content -Encoding utf8 finchat_v3_starter\reference\legacy\v2_config\tables.yaml
```

## Monday (23 Nov) plan: everything, in this order

- [ ] 01 runtime: tests pass; both Bedrock models answer the smoke test
- [ ] 02 knowledge: ADRA, Fynapse, FA pages load; search finds the right table
- [ ] 03 data tools: guardrail tests pass; live count of adra_account_facts = 97
- [ ] 04 agents: ADRA and Fynapse question bank scorecard, zero wrong
- [ ] 05 API: /v3/chat answers and writes to aiops
- [ ] 08 full catalog: all 122 tables loaded; REVIEW.md approved (needs the reviewed CSVs)
- [ ] 06 analyst, actions, workflows: Excel export and saved reports work
- [ ] 07 memory: summaries, follow-ups, 30-question rollover
- [ ] 09 summary agent: create the two tables from reference/aiops/finance_chat_summary_cards.sql first; dry run, then real run
- [ ] 10 deploy: VM runs finance-agentic; /v3/health green; rollback steps written

## Things only you can do

- Commit after each task (Claude Code never commits).
- Fill in `rbac.v3.yaml` TODOs and the catalog Excel `Fill_in` sheet.
- Confirm the Fynapse entity change with the data team.
- Review `knowledge/REVIEW.md` after task 08, and the v2 deletion list in task 10.
