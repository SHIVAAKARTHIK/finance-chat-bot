# Task 02 report: knowledge layer for ADRA, Fynapse and fixed assets (21 Nov 2026)

## Files
- `knowledge/tables/` (10 pages, all `reviewed: true`):
  - recon: `silver.adra_account_facts`, `silver.adra_transaction_facts`, `silver.adra_account_dimensions`,
    `silver.adra_legal_entity_dimensions`, `silver.adra_period_dimensions`, `silver.adra_engagement_dimensions`
  - subledger: `silver.fact_fynapse_slr_journals` (added REVERSES, LOB, COST_CENTER, functional/reporting currency columns
    that the ground-truth SQL uses but the old page lacked)
  - fa: `silver.dim_fixed_asset_books`, `silver.dim_fixed_assets`, `silver.fact_asset_master_transactions`
- `knowledge/INDEX.md` (generated), `joins.yaml` (9 approved + 1 blocked), `glossary.md` (28 terms), `rules.md`,
  `examples.yaml` (27 examples).
- `knowledge/page.py` (front matter + sections, `<!-- reviewed -->` marker), `models.py`, `search.py` (BM25),
  `loader.py` (load, validate, search, join path, glossary lookup, similar examples, INDEX.md writer),
  `generator.py` (catalog Excel + reviewed CSVs -> pages).
- `reference/` (copies of semantic_pages, legacy, question_bank), `config/rbac.v3.yaml` (copy of the template).
- `requirements.txt`: added `openpyxl==3.1.5`.

## What changed versus the reference pages
- Entity scopes removed: no 581 / 14781 / 14782 / UK03..UK17 / DATA_AREA_ID filters anywhere (a test scans every file).
- ADRA examples: the RBAC key filters were replaced by the filter the question asks for, through the dimensions
  (`ENTITY_CODE` / `ENTITY_NAME` and `PERIOD_NAME`). Marked `verified: false` until re-run live.
- Fynapse: page says entity values changed and must be checked with get_column_values. Examples that filter a
  specific entity (old UK codes) were left out.
- Fixed assets: `duplicates` known issue on all three tables, with the check to run; a dedup pattern example.
- KPI content dropped (no KPI ids in glossary).

## Tests
`..\.venv\Scripts\python -m pytest -q` from `backend/finchat_agents`: 102 passed, 2 skipped (live Bedrock).
- Loader: every page valid, domains in the access file, key/entity/period/PII columns exist, PII flagged.
- Joins reference known tables and columns; ADRA joins keep the full composite key; join path works.
- Every example SQL parses, reads exactly its listed tables, and every JOIN uses an approved join with its full key.
- No hardcoded entity values and no KPI text in any knowledge file (checked against the original pages: the test catches them).
- Search: 15 question-bank questions return the right table in the top 3 (14 at rank 1). Domain filter and broken /
  domain-less exclusion tested.
- Generator (fake Excel): creates pages, CSV wins over Fill_in, reviewed fields and sections kept, Columns/Values merged
  without overwriting, PII masked in samples and values, Errors -> `status: broken`, re-enabled on a clean export,
  idempotent second run.
- `INDEX.md` must match the pages (test fails if stale).

## Assumptions
- Page file name is `<schema>.<table>.md`; catalog is `lakehouse_mvpai` unless the page says otherwise.
- `joins.yaml` uses `keys:` for the column pairs (YAML reads a bare `on:` key as boolean true).
- `known_issues` is a list of `{code, note}`; codes: duplicates, orphans, all_string_columns, entity_values_changing,
  empty_column, broken, other. run_sql (task 03) can key off `duplicates`.
- `entity_column` on ADRA facts is LEGAL_ENTITY_KEY; users' entity names resolve through adra_legal_entity_dimensions.
- Generator: values starting with "proposed:" are stored without the prefix and listed in `proposed_fields`;
  status, broken_error and row_count are generator-owned; sample rows mask PII columns.

## Questions for Karthik
1. `fact_asset_journal` is in the old FA domain but no column information exists in the pack; left for task 08.
2. FA physical column types and the business key of `fact_asset_master_transactions` are not confirmed.
3. ADRA `adra_period_dimensions.PERIOD`: the ground-truth SQL uses it, but its meaning is not documented.
4. Current Fynapse `PARENT_ENTITY` values (the "100" change): once confirmed, entity examples can be added back.
5. Do `ENTITY_CODE` values really read '100' and '561'? The rewritten ADRA examples rely on it (task 03 live check).
6. Close-task tables (`adra_tasks_*`) are not modelled, so the close/recon task questions cannot be answered yet.
   Which domain should they get: recon or gl?
7. Draft glossary terms need Finance sign-off: capitalized, in service, reversal, pending with a person.
8. Shared tables (`dim_legal_entities`, `dim_companies`, fiscal periods, FX) have no domain in the access file.
