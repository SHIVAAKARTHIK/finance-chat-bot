---
name: fa_capitalized_value_trend
schema: gold
layer: gold
domain: fa
type: view
status: active
purpose: Shows capitalized acquisition value by fixed asset.
grain: one row per FIXED_ASSET_NUMBER (one asset acquisition)
primary_key:
- FIXED_ASSET_NUMBER
entity_column: LEGAL_ENTITY
period_columns:
- ACQUISITION_DATE
pii_columns: []
synonyms: []
built_from:
- dim_fixed_asset_books
- fact_asset_master_transactions
known_issues: []
proposed_fields:
- grain
- primary_key
reviewed: false
---

# fa_capitalized_value_trend

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `FIXED_ASSET_NUMBER` | string |  |  | `FIXED_ASSET_NUMBER` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `ACQUISITION_DATE` | date |  |  | `ACQUISITION_DATE` |
| `STATUS` | string |  |  | `STATUS` |
| `ACQUISITION_PRICE` | decimal |  |  | `ACQUISITION_PRICE` |

## Values

**ACQUISITION_DATE**
- `2026-01-01 00:00:00`
- `2026-10-01 00:00:00`
- `2026-10-23 00:00:00`

**STATUS**
- `Open`
