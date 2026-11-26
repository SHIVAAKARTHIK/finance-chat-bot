---
name: manage_close_adra_reconciliation
schema: gold
layer: gold
domain: recon
type: view
status: active
purpose: Shows ADRA account reconciliations with legal entity; preparer/reviewer; due date and status.
grain: one row per account reconciliation
primary_key:
- ACCOUNT
- LEGAL_ENTITY
- PERIOD_NAME
entity_column: LEGAL_ENTITY
period_columns:
- DUE
- PERIOD_NAME
pii_columns:
- PREPARER
- REVIEWER
synonyms: []
built_from:
- adra_account_dimensions
- adra_account_facts
- adra_transaction_facts
known_issues: []
proposed_fields: []
reviewed:
- superseded_by
superseded_by:
- silver.adra_account_facts
---

# manage_close_adra_reconciliation

> Superseded: this table is a copy of ADRA data. Answers use the source of truth `silver.adra_account_facts` (decision 21 Nov 2026).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ACCOUNT` | string |  |  | `ACCOUNT` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `ENTITY_NAME` | string |  |  | `ENTITY_NAME` |
| `PREPARER` | string |  |  | `PREPARER` |
| `REVIEWER` | string |  |  | `REVIEWER` |
| `DUE` | date |  |  | `DUE` |
| `STATUS` | string |  |  | `STATUS` |
| `ACTION` | string |  |  | `ACTION` |
| `PERIOD_NAME` | string |  |  | `PERIOD_NAME` |

## Values

**DUE**
- `2026-11-10 00:00:00`

**STATUS**
- `Not prepared`
- `Approved`
- `Prepared`
