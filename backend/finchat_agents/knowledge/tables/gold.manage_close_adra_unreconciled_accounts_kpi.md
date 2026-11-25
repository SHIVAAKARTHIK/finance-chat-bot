---
name: manage_close_adra_unreconciled_accounts_kpi
schema: gold
layer: gold
domain: recon
type: view
status: active
purpose: Counts unreconciled accounts and accounts aged over 60 days by legal entity.
grain: one row per legal entity KPI summary
primary_key:
- LEGAL_ENTITY
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- adra_account_facts
- adra_transaction_facts
known_issues: []
row_count: 8
proposed_fields: []
reviewed:
- superseded_by
superseded_by:
- silver.adra_account_facts
---

# manage_close_adra_unreconciled_accounts_kpi

> Superseded: this table is a copy of ADRA data. Answers use the source of truth `silver.adra_account_facts` (decision 21 Nov 2026).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Accounts` | long |  |  | `Accounts` |
| `Aged > 60 days` | long |  |  | `Aged > 60 days` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Values

**Accounts**
- `208`: 1 rows
- `1612`: 1 rows
- `104`: 1 rows
- `48`: 1 rows
- `972`: 1 rows
- `224`: 1 rows
- `10`: 1 rows
- `526`: 1 rows

**Aged > 60 days**
- `0`: 8 rows

## Profile

Rows in the latest export: 8.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Accounts` | LONG | 8 | 0 | 10 | 1612 |
| `Aged > 60 days` | LONG | 1 | 0 | 0 | 0 |
| `LEGAL_ENTITY` | STRING | 8 | 0 |  |  |

## Sample rows

| Accounts | Aged > 60 days |
|---|---|
| 208 | 0 |
| 526 | 0 |
| 1612 | 0 |
| 48 | 0 |
| 104 | 0 |
