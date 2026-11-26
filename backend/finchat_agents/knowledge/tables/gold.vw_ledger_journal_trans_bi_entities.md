---
name: vw_ledger_journal_trans_bi_entities
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Shows intercompany elimination transactions and amounts by legal entity.
grain: one row per elimination transaction
primary_key:
- LEGAL_ENTITY
- Elimination ID
- Transaction Type
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- fact_ledger_journal_trans_bi_entities
known_issues:
- code: duplicates
  note: 5 exact duplicate rows in the latest export (55.6%). Check duplicates at the grain before counting or summing; warn
    the user.
proposed_fields: []
reviewed: false
---

# vw_ledger_journal_trans_bi_entities

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `Elimination ID` | string |  |  | `Elimination ID` |
| `Transaction Type` | string |  |  | `Transaction Type` |
| `Amount` | string |  |  | `Amount` |

## Values

**Elimination ID**
- `ELM-000000001`
- `103-000000001`

**Transaction Type**
- `Intercompany payable - Due to/from`
- `Intercompany payable - Due to / from`
- `Intercompany - Due to/from`
- `Intercompany - Due to / from`

**Amount**
- `576000`
- `341414.82`
