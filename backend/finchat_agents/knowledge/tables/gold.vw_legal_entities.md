---
name: vw_legal_entities
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Lists legal entities and their reporting currencies.
grain: one row per legal entity
primary_key:
- LEGAL_ENTITY
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- dim_legal_entities
known_issues: []
proposed_fields: []
reviewed: false
---

# vw_legal_entities

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `DESCRIPTION` | string |  |  | `DESCRIPTION` |
| `CURRENCY` | string |  |  | `CURRENCY` |

## Values

**DESCRIPTION**
- `INS28`
- `INS14`
- `HWKGL`
- `Node`
- `CIBL`
- `Evergreen Solutions`
- `CAN`
- `RBJ`
- `HKEUR`
- `INSHOLDING`

**CURRENCY**
- `GBP`
- `USD`
