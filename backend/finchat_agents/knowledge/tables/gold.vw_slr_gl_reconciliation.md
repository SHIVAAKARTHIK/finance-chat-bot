---
name: vw_slr_gl_reconciliation
schema: gold
layer: gold
domain: subledger
type: view
status: active
purpose: SLR (Fynapse) vs GL (D365) reconciliation by entity, main account and accounting date
grain: one row per entity; account and accounting date
primary_key:
- slr_entity
- slr_account
- accounting_date
entity_column: slr_entity
period_columns:
- accounting_date
- posting_year
- posting_month
- posting_period
pii_columns: []
synonyms: []
built_from:
- fact_fynapse_slr_journals
- fact_kpmg_general_journal_account_entries
known_issues: []
proposed_fields: []
reviewed: false
---

# vw_slr_gl_reconciliation

SLR (Fynapse) vs GL (D365) reconciliation by entity, main account and accounting date

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `slr_entity` | string |  |  | `slr_entity` |
| `slr_account` | string |  |  | `slr_account` |
| `accounting_date` | date |  |  | `accounting_date` |
| `posting_year` | int |  |  | `posting_year` |
| `posting_month_no` | int |  |  | `posting_month_no` |
| `posting_month` | string |  |  | `posting_month` |
| `posting_period` | string |  |  | `posting_period` |
| `mdp_slr_amount` | decimal |  |  | `mdp_slr_amount` |
| `d365_amount` | decimal |  |  | `d365_amount` |
| `slr_gl_difference` | decimal |  |  | `slr_gl_difference` |
| `slr_line_count` | long |  |  | `slr_line_count` |
| `gl_line_count` | long |  |  | `gl_line_count` |
| `matching_status` | string |  |  | `matching_status` |
| `last_refreshed` | timestamp |  |  | `last_refreshed` |

## Values

**accounting_date**
- `2026-08-31 00:00:00`
- `2026-09-01 00:00:00`
- `2025-01-31 00:00:00`
- `2025-02-28 00:00:00`
- `2025-04-30 00:00:00`
- `2025-03-31 00:00:00`
- `2026-09-16 00:00:00`
- `2026-09-07 00:00:00`
- `2026-09-21 00:00:00`
- `2026-09-10 00:00:00`
- `2026-09-04 00:00:00`
- `2026-09-08 00:00:00`
- `2026-09-17 00:00:00`
- `2026-09-14 00:00:00`
- `2026-09-15 00:00:00`
- `2026-09-18 00:00:00`
- `2026-09-30 00:00:00`
- `2026-09-09 00:00:00`
- `2026-05-19 00:00:00`
- `2026-08-11 00:00:00`
- `2026-08-01 00:00:00`
- `2026-08-04 00:00:00`
- `2026-03-08 00:00:00`
- `2026-03-07 00:00:00`
- `2026-08-02 00:00:00`
- `2026-09-20 00:00:00`
- `2026-04-16 00:00:00`
- `2026-08-09 00:00:00`
- `2026-05-20 00:00:00`
- `2025-11-01 00:00:00`
- `2026-08-03 00:00:00`
- `2026-03-10 00:00:00`
- `2025-11-02 00:00:00`

**posting_year**
- `2026`
- `2025`

**posting_month_no**
- `9`
- `8`
- `3`
- `4`
- `2`
- `1`
- `5`
- `11`

**posting_month**
- `September`
- `August`
- `March`
- `April`
- `January`
- `February`
- `May`
- `November`

**mdp_slr_amount**
- `0`
- `-116911`
- `151031`
- `-210983`
- `-147650`
- `988931`
- `4751`
- `14148`
- `-72408`
- `-13214`
- `140351`
- `-94184`
- `5701`
- `-14148`
- `376420`
- `301489`
- `94184`
- `-138455`
- `-196614`
- `-15664`
- `210983`
- `-143435`
- `116911`
- `-106760`
- `-4751`
- `-5701`
- `25686`
- `-140351`
- `-988931`
- `-10404`
- `-10022`

**slr_line_count**
- `0`
- `40`
- `8`
- `4`
- `20`
- `48`
- `80`
- `120`
- `88`
- `100`
- `140`

**gl_line_count**
- `2`
- `3`
- `40`
- `4`
- `8`
- `1`
- `20`
- `6`
- `10`
- `48`
- `80`
- `9`
- `140`
- `12`
- `88`
- `120`
- `100`
- `24`
- `17`
- `5`
- `30`
- `194`
- `7`
- `29`
- `32`
- `15`
- `26`
- `38`
- `13`
- `16`

**matching_status**
- `MISSING IN SLR`
- `MATCH`

**last_refreshed**
- `2026-11-20 18:58:54.734151+00:00`
