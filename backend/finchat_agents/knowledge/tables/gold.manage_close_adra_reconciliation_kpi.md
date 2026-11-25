---
name: manage_close_adra_reconciliation_kpi
schema: gold
layer: gold
domain: recon
type: view
status: active
purpose: Counts prepared; finalized and not-prepared ADRA reconciliations by legal entity.
grain: one row per legal entity KPI summary
primary_key:
- LEGAL_ENTITY
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- adra_account_facts
known_issues: []
row_count: 9
proposed_fields: []
reviewed:
- superseded_by
superseded_by:
- silver.adra_account_facts
---

# manage_close_adra_reconciliation_kpi

> Superseded: this table is a copy of ADRA data. Answers use the source of truth `silver.adra_account_facts` (decision 21 Nov 2026).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `PREPARED` | long |  |  | `PREPARED` |
| `FINALIZED` | long |  |  | `FINALIZED` |
| `NOT_PREPARED` | long |  |  | `NOT_PREPARED` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Values

**PREPARED**
- `0`: 6 rows
- `6`: 1 rows
- `9`: 1 rows
- `1`: 1 rows

**FINALIZED**
- `0`: 4 rows
- `3`: 2 rows
- `6`: 1 rows
- `4`: 1 rows
- `2`: 1 rows

**NOT_PREPARED**
- `1`: 3 rows
- `7`: 2 rows
- `24`: 1 rows
- `6`: 1 rows
- `11`: 1 rows
- `0`: 1 rows

## Profile

Rows in the latest export: 9.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `PREPARED` | LONG | 4 | 0 | 0 | 9 |
| `FINALIZED` | LONG | 5 | 0 | 0 | 6 |
| `NOT_PREPARED` | LONG | 6 | 0 | 0 | 24 |
| `LEGAL_ENTITY` | STRING | 8 | 1 |  |  |

## Sample rows

| PREPARED | FINALIZED | NOT_PREPARED |
|---|---|---|
| 6 | 6 | 11 |
| 1 | 0 | 0 |
| 9 | 2 | 24 |
| 0 | 0 | 1 |
| 0 | 3 | 6 |
