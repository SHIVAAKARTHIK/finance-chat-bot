---
name: mc_actual_cash_balance_by_bank_ac_new
schema: gold
layer: gold
domain: cash
type: view
status: active
purpose: Provides actual cash balances by bank account and entity in local and USD currencies.
grain: one row per bank account and entity
primary_key:
- ENTITY
- BANK_ACCOUNT_ID
entity_column: ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- dim_bank_account_table_bi_entities
known_issues: []
row_count: 0
proposed_fields: []
reviewed: false
---

# mc_actual_cash_balance_by_bank_ac_new

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `BANK` | string |  |  | `BANK` |
| `ENTITY` | string |  |  | `ENTITY` |
| `CURRENCY` | string |  |  | `CURRENCY` |
| `BALANCE_LOCAL_CURRENCY` | string |  |  | `BALANCE_LOCAL_CURRENCY` |
| `BALANCE_USD` | string |  |  | `BALANCE_USD` |
| `BANK_ACCOUNT_ID` | string |  |  | `BANK_ACCOUNT_ID` |

## Profile

Rows in the latest export: 0.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `BANK` | STRING | 0 | 0 |  |  |
| `ENTITY` | STRING | 0 | 0 |  |  |
| `CURRENCY` | STRING | 0 | 0 |  |  |
| `BALANCE_LOCAL_CURRENCY` | STRING | 0 | 0 |  |  |
| `BALANCE_USD` | STRING | 0 | 0 |  |  |
| `BANK_ACCOUNT_ID` | STRING | 0 | 0 |  |  |
