# Task 08 report: full catalog (21 Nov 2026)

Input: `tables.xlsx` (copied to `finchat_v3_starter/data/table_catalog/`, git-ignored there): sheets Tables (143),
keys, Columns (4,665), values, Samples, fill_in, and the Copilot drafts `fill_in_draft_silver` / `fill_in_draft_gold`.
No reviewed CSVs and no Errors sheet were supplied; the draft sheets were used as the review input (they win over
fill_in), and every row's confidence is carried into REVIEW.md.

## Result
- **143 pages** in `knowledge/tables/` (133 new, the 10 hand-written pages updated without touching reviewed fields).
- **102 searchable**; 29 without a domain and 12 broken are excluded from `search_tables` (broken ones also from run_sql).
- `knowledge/REVIEW.md`: grouped lists for quick approval (see below). `knowledge/joins_proposed.yaml`: 242 proposed
  joins (never used until moved to joins.yaml). `INDEX.md` rebuilt. A rerun of the generator changes nothing (idempotent).

Run again after editing pages or with a new export (from `backend`):
```
.venv\Scripts\python -m finchat_agents.knowledge.generator <path>\tables.xlsx --review
```

## Data findings that need you (most important first)
1. **The workbook went through Excel and some values were altered.** Text like "Feb 25" became the date 2026-02-25
   in 12 tables (period-label columns such as `adra_period_dimensions.PERIOD_NAME`). The generator detects this
   (a date inside a STRING column can only come from Excel) and keeps those values out of the pages; REVIEW.md section 8
   lists them. Other Excel effects cannot be detected (leading zeros dropped, long numbers rounded). Please re-export
   and copy the file without opening it in Excel, or import the CSVs as text, before the next run.
2. **Twelve draft rows in `fill_in_draft_gold` were misaligned** (a comma split a cell, so later values sat in the
   wrong columns, e.g. built_from under known_issues). They were rebuilt from what each cell contains and marked
   "repaired" in REVIEW.md section 3: please check their entity, period and PII columns.
3. **Fynapse question bank is stale.** `PARENT_ENTITY` is now `100` on all rows (the entity change is confirmed by the
   export) and the table has 1,200 rows, not the 817 the bank expects. The Fynapse scorecard numbers will not match the
   bank until its expected values are re-run (`ground_truth_adra_fynapse_v1.sql`).
4. **Source of truth for ADRA reconciliations.** `gold.manage_close_adra_reconciliation` holds the same 97 account
   reconciliations as `silver.adra_account_facts`, and search now often ranks the gold copy first (rules say "prefer
   gold"). `close_recon.yaml` says the business uses `adra_*` and that `manage_close_*` are copies "NOT used". Decide:
   (a) gold copy is fine, (b) remove its domain so it is excluded, or (c) add a rule "use adra_* for reconciliations".
5. **Fixed-asset duplicates look fixed.** The export shows 300 rows and 0 exact duplicates for `dim_fixed_asset_books`
   (SPEC said 600 rows). The three hand-written FA pages still warn about duplicate loads; REVIEW.md section 7 flags them.
   If the data team confirms, remove the `duplicates` known issue from those pages.
6. **12 broken objects** (REVIEW.md section 2): the `gold.vw_managed_coll_*` views (their non-`vw_` twins work),
   `gold.vw_commission_analysis_slr_mga`, `gold.vw_expense_analysis_slr`, `silver.dim_vendors`,
   `silver.fact_cust_transactions`. The workbook has no Errors sheet, so the error text is unknown: profiling them
   failed (no row count). Send the list to the data team.
7. **29 tables without a domain** (REVIEW.md section 1): access-screen, audit/SOC, review-controls, pipeline logs,
   portal users, finance_chat_eval_results and similar. Most should probably stay without a domain (the v2 domain file
   excluded audit and access data on purpose).

## What REVIEW.md lists
Summary; 1 missing domains; 2 broken objects; 3 low-confidence and repaired rows (24); 4 proposed keys and grains (62
tables); 5 draft values not used (unknown columns or domains); 6 personal-data columns (234 in 80 tables); 7 duplicate
tables (11); 8 values altered by Excel; 9 page columns missing from the export; 10 proposed joins (242: 5 declared
foreign keys, the rest key-name matches); 11 lineage from built_from (158 links).

## Safety measures in the generator
- **Personal data:** columns are flagged from the drafts and by name (names, usernames, emails, contact people,
  created/modified-by), also on reviewed pages (append only). The ADRA pages gained e.g. `PREPARER_USERNAME`,
  `REVIEWER_NAME`, `ASSIGNED_TO_NAME`, `*_BY_USERNAME`. Flagged columns are masked in results, never listed in Values,
  masked in Sample rows.
- **Entity and key columns:** their values, samples and min/max are not written to pages (entity codes change; agents
  check them live with get_column_values). Generated data sections may still contain codes that appear inside other
  columns (journal numbers, ledger names); those are data, not filters.
- Draft column references are checked against the export (case fixed, unknown names dropped and listed); domains must
  exist in `rbac.v3.yaml`.

## Hand-written page corrections from export evidence
`adra_period_dimensions`: `PERIOD` holds the period end date plus label (e.g. '2025-02-28 Feb 25'), not a period
number; `PERIOD_STATUS` has only `Opened`. New export columns were added to all 10 pages (e.g. 60+ more columns on
`adra_account_facts`, 50+ on the Fynapse table) without changing reviewed fields.

## Files changed
- `knowledge/generator.py` (rewritten: case-insensitive sheets, draft sheets, misaligned-row repair, Excel-date
  detection, column/domain validation, PII auto-flag, broken detection without Errors sheet, hidden entity/key values,
  one-line values), `knowledge/review.py` (new: proposed joins, lineage, REVIEW.md), `knowledge/page.py` (column names
  with spaces in Values), `knowledge/loader.py` (reads joins_proposed.yaml; missing purpose/grain is a warning for
  generated pages).
- `knowledge/tables/*` (143), `INDEX.md`, `REVIEW.md`, `joins_proposed.yaml`.
- `finchat_v3_starter/.gitignore`: catalog xlsx / csv / summary.
- Tests: `test_catalog_full.py` (new), `test_knowledge.py` (20+ gold-domain search cases, exclusion test, scoped
  entity/KPI checks), small updates in `test_agents.py`, `test_data_tools.py`, `tests/fakes.py`.

## Tests
`..\.venv\Scripts\python -m pytest -q`: 242 passed, 30 skipped (live). Includes: every page valid (0 errors); broken and
domain-less tables excluded from search and run_sql; 23 gold-domain questions find the right table in the top 3
(no tuning needed); the 15 question-bank search cases still pass (ADRA reconciliation questions accept the gold copy,
see finding 4); misaligned-row repair; Excel-date detection; PII auto-flag on reviewed pages; hidden entity values;
review files; idempotent reruns.

## Assumptions
- Draft sheets are treated as reviewed input (they were not marked as reviewed by you): domain, purpose, grain and keys
  from them are used, low confidence and repaired rows are flagged. Nothing in them is marked `reviewed`, so the next
  export run can still update them.
- Without an Errors sheet, "no row count" means the profiling query failed (broken).
- Over-flagging personal data is preferred to under-flagging (e.g. `MDP_CREATED_BY`).

## Decision (21 Nov 2026): use adra_* only
The 11 `manage_close_*` tables that copy ADRA data (5 `gold.manage_close_adra_*`, 2 `silver.manage_close_recon_*`,
2 `silver.manage_close_task_*`, `gold.vw_manage_close_task`, `gold.vw_manage_close_task_kpi`) carry
`superseded_by: [<adra_* table>]` on their pages (a reviewed field, so the generator keeps it). They are excluded from
search; run_sql and describe_table refuse them with "is a copy; the source of truth is <adra_* table>". The two GL
journal-entry tables (`gold.manage_close_journal_entries`, `gold.vw_manage_close_journal_entry_kpi`) are not ADRA data
and stay searchable. rules.md has a "Source of truth" note. Searchable tables: 91.

## Open questions
1. Finding 5: are the fixed-asset duplicate loads fixed?
2. Can you re-export without Excel (finding 1) so period labels come back into the pages?
3. Should the layout views (`vw_income_statement_layout`, `vw_balance_sheet_*_layout`) stay searchable? They hold
   row layouts, not figures, and rank high for "income statement" questions.
