---
name: fa_asset_register
schema: gold
layer: gold
domain: fa
type: view
status: active
purpose: Fixed-asset register showing cost; net book value; age and depreciation status.
grain: one row per ASSET_ID (one fixed asset)
primary_key:
- ASSET_ID
entity_column: LEGAL_ENTITY
period_columns:
- CAPITALIZATION_DATE
- DEPRECIATION_LAST_RUN
pii_columns: []
synonyms: []
built_from:
- dim_fixed_assets
- dim_fixed_asset_books
- fact_asset_master_transactions
known_issues: []
proposed_fields:
- grain
- primary_key
reviewed: false
---

# fa_asset_register

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ASSET_ID` | string |  |  | `ASSET_ID` |
| `DESCRIPTION` | string |  |  | `DESCRIPTION` |
| `CATEGORY` | string |  |  | `CATEGORY` |
| `COST` | decimal |  |  | `COST` |
| `NBV` | decimal |  |  | `NBV` |
| `AGE_DAYS` | int |  |  | `AGE_DAYS` |
| `LOCATION` | string |  |  | `LOCATION` |
| `DEPRECIATION_LAST_RUN` | string |  |  | `DEPRECIATION_LAST_RUN` |
| `CAPITALIZATION_DATE` | string |  |  | `CAPITALIZATION_DATE` |
| `CUMULATIVE_DEPRECIATION` | decimal |  |  | `CUMULATIVE_DEPRECIATION` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `USEFUL_LIFE` | string |  |  | `USEFUL_LIFE` |
| `REMAINING_LIFE` | string |  |  | `REMAINING_LIFE` |

## Values

**CATEGORY**
- `FURNITURE`
- `COMPUTER`
- `BUILDINGS`
- `AUTO`
- `SOFTWARE`

**AGE_DAYS**
- `323`
- `50`
- `28`

**LOCATION**
- `HQ`
- `None`

**DEPRECIATION_LAST_RUN**
- `2026-09-30 12:00:00.0000000 +00:00`
- `2026-08-31 12:00:00.0000000 +00:00`
- `2026-10-31 12:00:00.0000000 +00:00`
- `1900-01-01 12:00:00.0000000 +00:00`

**CAPITALIZATION_DATE**
- `2026-01-01 12:00:00.0000000 +00:00`
- `2026-10-23 12:00:00.0000000 +00:00`
- `2026-10-01 12:00:00.0000000 +00:00`

**USEFUL_LIFE**
- `5`
- `10`
- `39`

**REMAINING_LIFE**
- `1553`
- `3380`
- `13972`
- `1583`
- `1522`
- `1826`
- `10`
- `310`
- `100`
- `330`
