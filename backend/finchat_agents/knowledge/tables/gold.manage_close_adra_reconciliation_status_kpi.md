---
name: manage_close_adra_reconciliation_status_kpi
schema: gold
layer: gold
domain: recon
type: view
status: active
purpose: Shows reconciliation completion and exception percentages by legal entity.
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
row_count: 9
proposed_fields: []
reviewed:
- superseded_by
superseded_by:
- silver.adra_account_facts
---

# manage_close_adra_reconciliation_status_kpi

> Superseded: this table is a copy of ADRA data. Answers use the source of truth `silver.adra_account_facts` (decision 21 Nov 2026).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ACCOUNTS_RECONCILED` | decimal |  |  | `ACCOUNTS_RECONCILED` |
| `EXCEPTIONS_OVER_THRESHOLD` | decimal |  |  | `EXCEPTIONS_OVER_THRESHOLD` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Values

**ACCOUNTS_RECONCILED**
- `0`: 4 rows
- `5`: 1 rows
- `26.1`: 1 rows
- `36.4`: 1 rows
- `33.3`: 1 rows
- `30`: 1 rows

**EXCEPTIONS_OVER_THRESHOLD**
- `0`: 4 rows
- `13`: 1 rows
- `32.5`: 1 rows
- `20`: 1 rows
- `33.3`: 1 rows
- `27.3`: 1 rows

## Profile

Rows in the latest export: 9.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ACCOUNTS_RECONCILED` | DECIMAL | 6 | 0 | 0 | 36.4 |
| `EXCEPTIONS_OVER_THRESHOLD` | DECIMAL | 6 | 0 | 0 | 33.3 |
| `LEGAL_ENTITY` | STRING | 8 | 1 |  |  |

## Sample rows

| ACCOUNTS_RECONCILED | EXCEPTIONS_OVER_THRESHOLD |
|---|---|
| 26.1 | 13 |
| 0 | 0 |
| 5 | 32.5 |
| 0 | 0 |
| 33.3 | 33.3 |
