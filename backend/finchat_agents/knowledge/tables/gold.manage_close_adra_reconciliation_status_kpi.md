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
- `0`
- `5`
- `26.1`
- `36.4`
- `33.3`
- `30`

**EXCEPTIONS_OVER_THRESHOLD**
- `0`
- `13`
- `32.5`
- `20`
- `33.3`
- `27.3`
