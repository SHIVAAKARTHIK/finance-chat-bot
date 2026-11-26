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

## Empty columns

Empty in every row: `BANK`, `ENTITY`, `CURRENCY`, `BALANCE_LOCAL_CURRENCY`, `BALANCE_USD`, `BANK_ACCOUNT_ID`. Do not filter or group on them.
