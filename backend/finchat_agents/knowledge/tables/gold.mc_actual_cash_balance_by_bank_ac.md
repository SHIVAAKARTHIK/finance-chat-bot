---
name: mc_actual_cash_balance_by_bank_ac
schema: gold
layer: gold
domain: cash
type: view
status: active
purpose: Shows actual cash balance for each bank account and legal entity.
grain: one row per bank account and legal entity
primary_key:
- LEGAL_ENTITY
- BANK_ACCOUNT_ID
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- dim_bank_account_table_bi_entities
- fact_ledger_journal_lines
known_issues: []
proposed_fields: []
reviewed: false
---

# mc_actual_cash_balance_by_bank_ac

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `BANK` | string |  |  | `BANK` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `CURRENCY` | string |  |  | `CURRENCY` |
| `BALANCE` | string |  |  | `BALANCE` |
| `BANK_ACCOUNT_ID` | string |  |  | `BANK_ACCOUNT_ID` |

## Values

**BANK**
- `IBA Bank Account USD`
- `IBA Bank Account GBP`
- `IBA Bank Account EUR`
- `IBA Bank Account CAD`
- `IBA Bank Account AUD`
- `IBA Bank Account SEK`

**CURRENCY**
- `GBP`

**BALANCE**
- `42.73`
- `1039788.83`
- `528437.11`
- `0`
- `147570.53`
- `108372.15`
- `560905.98`
- `4426082.47`
- `269825.59`
- `15050.74`
- `173305.14`
- `2123.19`
- `511.96`

**BANK_ACCOUNT_ID**
- `IBA E`
- `IBA G`
- `IBA U`
- `IBA C`
- `IBA A`
- `IBA S`
