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
- `208`
- `1612`
- `104`
- `48`
- `972`
- `224`
- `10`
- `526`

**Aged > 60 days**
- `0`
