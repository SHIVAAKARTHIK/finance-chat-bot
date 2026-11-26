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
- `0`
- `6`
- `9`
- `1`

**FINALIZED**
- `0`
- `3`
- `6`
- `4`
- `2`

**NOT_PREPARED**
- `1`
- `7`
- `24`
- `6`
- `11`
- `0`
