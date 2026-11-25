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
row_count: 10
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
- `INS28`: 1 rows
- `INS14`: 1 rows
- `HWKGL`: 1 rows
- `Node`: 1 rows
- `CIBL`: 1 rows
- `Evergreen Solutions`: 1 rows
- `CAN`: 1 rows
- `RBJ`: 1 rows
- `HKEUR`: 1 rows
- `INSHOLDING`: 1 rows

**CURRENCY**
- `GBP`: 6 rows
- `USD`: 4 rows

## Profile

Rows in the latest export: 10.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `LEGAL_ENTITY` | STRING | 10 | 0 |  |  |
| `DESCRIPTION` | STRING | 10 | 0 | CAN | RBJ |
| `CURRENCY` | STRING | 2 | 0 | GBP | USD |

## Sample rows

| DESCRIPTION | CURRENCY |
|---|---|
| Evergreen Solutions | USD |
| CIBL | GBP |
| CAN | GBP |
| HKEUR | GBP |
| RBJ | GBP |
