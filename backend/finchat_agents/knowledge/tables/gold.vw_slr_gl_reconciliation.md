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
row_count: 316
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
- `2026-08-31 00:00:00`: 35 rows
- `2026-09-01 00:00:00`: 33 rows
- `2025-01-31 00:00:00`: 30 rows
- `2025-02-28 00:00:00`: 30 rows
- `2025-04-30 00:00:00`: 30 rows
- `2025-03-31 00:00:00`: 30 rows
- `2026-09-16 00:00:00`: 11 rows
- `2026-09-07 00:00:00`: 10 rows
- `2026-09-21 00:00:00`: 10 rows
- `2026-09-10 00:00:00`: 9 rows
- `2026-09-04 00:00:00`: 9 rows
- `2026-09-08 00:00:00`: 9 rows
- `2026-09-17 00:00:00`: 9 rows
- `2026-09-14 00:00:00`: 6 rows
- `2026-09-15 00:00:00`: 6 rows
- `2026-09-18 00:00:00`: 6 rows
- `2026-09-30 00:00:00`: 6 rows
- `2026-09-09 00:00:00`: 5 rows
- `2026-05-19 00:00:00`: 3 rows
- `2026-08-11 00:00:00`: 3 rows
- `2026-08-01 00:00:00`: 2 rows
- `2026-08-04 00:00:00`: 2 rows
- `2026-03-08 00:00:00`: 2 rows
- `2026-03-07 00:00:00`: 2 rows
- `2026-08-02 00:00:00`: 2 rows
- `2026-09-20 00:00:00`: 2 rows
- `2026-04-16 00:00:00`: 2 rows
- `2026-08-09 00:00:00`: 2 rows
- `2026-05-20 00:00:00`: 2 rows
- `2025-11-01 00:00:00`: 2 rows
- `2026-08-03 00:00:00`: 2 rows
- `2026-03-10 00:00:00`: 2 rows
- `2025-11-02 00:00:00`: 2 rows

**posting_year**
- `2026`: 192 rows
- `2025`: 124 rows

**posting_month_no**
- `9`: 131 rows
- `8`: 48 rows
- `3`: 36 rows
- `4`: 32 rows
- `2`: 30 rows
- `1`: 30 rows
- `5`: 5 rows
- `11`: 4 rows

**posting_month**
- `September`: 131 rows
- `August`: 48 rows
- `March`: 36 rows
- `April`: 32 rows
- `January`: 30 rows
- `February`: 30 rows
- `May`: 5 rows
- `November`: 4 rows

**mdp_slr_amount**
- `0`: 286 rows
- `-116911`: 1 rows
- `151031`: 1 rows
- `-210983`: 1 rows
- `-147650`: 1 rows
- `988931`: 1 rows
- `4751`: 1 rows
- `14148`: 1 rows
- `-72408`: 1 rows
- `-13214`: 1 rows
- `140351`: 1 rows
- `-94184`: 1 rows
- `5701`: 1 rows
- `-14148`: 1 rows
- `376420`: 1 rows
- `301489`: 1 rows
- `94184`: 1 rows
- `-138455`: 1 rows
- `-196614`: 1 rows
- `-15664`: 1 rows
- `210983`: 1 rows
- `-143435`: 1 rows
- `116911`: 1 rows
- `-106760`: 1 rows
- `-4751`: 1 rows
- `-5701`: 1 rows
- `25686`: 1 rows
- `-140351`: 1 rows
- `-988931`: 1 rows
- `-10404`: 1 rows
- `-10022`: 1 rows

**slr_line_count**
- `0`: 286 rows
- `40`: 9 rows
- `8`: 5 rows
- `4`: 4 rows
- `20`: 4 rows
- `48`: 2 rows
- `80`: 2 rows
- `120`: 1 rows
- `88`: 1 rows
- `100`: 1 rows
- `140`: 1 rows

**gl_line_count**
- `2`: 48 rows
- `3`: 44 rows
- `40`: 36 rows
- `4`: 35 rows
- `8`: 23 rows
- `1`: 20 rows
- `20`: 19 rows
- `6`: 16 rows
- `10`: 9 rows
- `48`: 8 rows
- `80`: 8 rows
- `9`: 5 rows
- `140`: 4 rows
- `12`: 4 rows
- `88`: 4 rows
- `120`: 4 rows
- `100`: 4 rows
- `24`: 3 rows
- `17`: 3 rows
- `5`: 3 rows
- `30`: 2 rows
- `194`: 2 rows
- `7`: 2 rows
- `29`: 2 rows
- `32`: 2 rows
- `15`: 2 rows
- `26`: 1 rows
- `38`: 1 rows
- `13`: 1 rows
- `16`: 1 rows

**matching_status**
- `MISSING IN SLR`: 286 rows
- `MATCH`: 30 rows

**last_refreshed**
- `2026-11-20 18:58:54.734151+00:00`: 316 rows

## Profile

Rows in the latest export: 316.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `slr_entity` | STRING | 7 | 0 |  |  |
| `slr_account` | STRING | 60 | 0 | 101413 | 650200 |
| `accounting_date` | DATE | 33 | 0 | 2025-01-31 00:00:00 | 2026-09-30 00:00:00 |
| `posting_year` | INT | 2 | 0 | 2025 | 2026 |
| `posting_month_no` | INT | 8 | 0 | 1 | 11 |
| `posting_month` | STRING | 8 | 0 | April | September |
| `posting_period` | STRING | 10 | 0 |  |  |
| `mdp_slr_amount` | DECIMAL | 32 | 0 | -988931 | 988931 |
| `d365_amount` | DECIMAL | 300 | 0 | -12620732.3 | 7878908.07 |
| `slr_gl_difference` | DECIMAL | 254 | 0 | -7878908.07 | 12620732.3 |
| `slr_line_count` | LONG | 11 | 0 | 0 | 140 |
| `gl_line_count` | LONG | 31 | 0 | 1 | 194 |
| `matching_status` | STRING | 2 | 0 | MATCH | MISSING IN SLR |
| `last_refreshed` | TIMESTAMP | 1 | 0 | 2026-11-20 18:58:44.183000 | 2026-11-20 18:58:44.183000 |

## Sample rows

| slr_account | accounting_date | posting_year | posting_month_no | posting_month | posting_period | mdp_slr_amount | d365_amount | slr_gl_difference | slr_line_count | gl_line_count | matching_status | last_refreshed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 212200 | 2025-02-28 00:00:00 | 2025 | 2 | February | (altered in export) | -116911 | -116911 | 0 | 40 | 40 | MATCH | 2026-11-20 18:58:55.621000 |
| 141121 | 2025-02-28 00:00:00 | 2025 | 2 | February | (altered in export) | -106760 | -106760 | 0 | 120 | 120 | MATCH | 2026-11-20 18:58:55.621000 |
| 412100 | 2025-01-31 00:00:00 | 2025 | 1 | January | (altered in export) | 0 | 143271 | -143271 | 0 | 40 | MISSING IN SLR | 2026-11-20 18:58:55.621000 |
| 512310 | 2025-01-31 00:00:00 | 2025 | 1 | January | (altered in export) | 0 | 8673 | -8673 | 0 | 4 | MISSING IN SLR | 2026-11-20 18:58:55.621000 |
| 511210 | 2025-01-31 00:00:00 | 2025 | 1 | January | (altered in export) | 0 | 12773 | -12773 | 0 | 8 | MISSING IN SLR | 2026-11-20 18:58:55.621000 |
