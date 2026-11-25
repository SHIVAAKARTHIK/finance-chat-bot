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
row_count: 13
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
- `IBA Bank Account USD`: 3 rows
- `IBA Bank Account GBP`: 3 rows
- `IBA Bank Account EUR`: 3 rows
- `IBA Bank Account CAD`: 2 rows
- `IBA Bank Account AUD`: 1 rows
- `IBA Bank Account SEK`: 1 rows

**CURRENCY**
- `GBP`: 13 rows

**BALANCE**
- `42.73`: 1 rows
- `1039788.83`: 1 rows
- `528437.11`: 1 rows
- `0`: 1 rows
- `147570.53`: 1 rows
- `108372.15`: 1 rows
- `560905.98`: 1 rows
- `4426082.47`: 1 rows
- `269825.59`: 1 rows
- `15050.74`: 1 rows
- `173305.14`: 1 rows
- `2123.19`: 1 rows
- `511.96`: 1 rows

**BANK_ACCOUNT_ID**
- `IBA E`: 3 rows
- `IBA G`: 3 rows
- `IBA U`: 3 rows
- `IBA C`: 2 rows
- `IBA A`: 1 rows
- `IBA S`: 1 rows

## Profile

Rows in the latest export: 13.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `BANK` | STRING | 6 | 0 | IBA Bank Account AUD | IBA Bank Account USD |
| `LEGAL_ENTITY` | STRING | 3 | 0 |  |  |
| `CURRENCY` | STRING | 1 | 0 | GBP | GBP |
| `BALANCE` | STRING | 13 | 0 | 0 | 560905.98 |
| `BANK_ACCOUNT_ID` | STRING | 6 | 0 | IBA A | IBA U |

## Sample rows

| BANK | CURRENCY | BALANCE | BANK_ACCOUNT_ID |
|---|---|---|---|
| IBA Bank Account EUR | GBP | 0 | IBA E |
| IBA Bank Account GBP | GBP | 1039788.83 | IBA G |
| IBA Bank Account USD | GBP | 4426082.47 | IBA U |
| IBA Bank Account CAD | GBP | 528437.11 | IBA C |
| IBA Bank Account AUD | GBP | 108372.15 | IBA A |
