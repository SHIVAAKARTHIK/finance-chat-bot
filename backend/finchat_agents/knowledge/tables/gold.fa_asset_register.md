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
row_count: 189
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
- `FURNITURE`: 49 rows
- `COMPUTER`: 49 rows
- `BUILDINGS`: 46 rows
- `AUTO`: 43 rows
- `SOFTWARE`: 2 rows

**AGE_DAYS**
- `323`: 187 rows
- `50`: 1 rows
- `28`: 1 rows

**LOCATION**
- `HQ`: 187 rows
- `None`: 2 rows

**DEPRECIATION_LAST_RUN**
- `2026-09-30 12:00:00.0000000 +00:00`: 176 rows
- `2026-08-31 12:00:00.0000000 +00:00`: 8 rows
- `2026-10-31 12:00:00.0000000 +00:00`: 3 rows
- `1900-01-01 12:00:00.0000000 +00:00`: 2 rows

**CAPITALIZATION_DATE**
- `2026-01-01 12:00:00.0000000 +00:00`: 187 rows
- `2026-10-23 12:00:00.0000000 +00:00`: 1 rows
- `2026-10-01 12:00:00.0000000 +00:00`: 1 rows

**USEFUL_LIFE**
- `5`: 94 rows
- `10`: 49 rows
- `39`: 46 rows

**REMAINING_LIFE**
- `1553`: 81 rows
- `3380`: 49 rows
- `13972`: 46 rows
- `1583`: 4 rows
- `1522`: 3 rows
- `1826`: 2 rows
- `10`: 1 rows
- `310`: 1 rows
- `100`: 1 rows
- `330`: 1 rows

## Profile

Rows in the latest export: 189.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ASSET_ID` | STRING | 190 | 0 | AUTO-000007 | SOFT-000049 |
| `DESCRIPTION` | STRING | 190 | 0 | Accounts Payable Mobile Pedestal | Wellness Room Recliner |
| `CATEGORY` | STRING | 5 | 0 | AUTO | SOFTWARE |
| `COST` | DECIMAL | 189 | 0 | 1100 | 20600 |
| `NBV` | DECIMAL | 176 | 0 | 827 | 20000 |
| `AGE_DAYS` | INT | 3 | 0 | 28 | 323 |
| `LOCATION` | STRING | 1 | 2 | HQ | HQ |
| `DEPRECIATION_LAST_RUN` | STRING | 4 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 2026-10-31 12:00:00.0000000 +00:00 |
| `CAPITALIZATION_DATE` | STRING | 3 | 0 | 2026-01-01 12:00:00.0000000 +00:00 | 2026-10-23 12:00:00.0000000 +00:00 |
| `CUMULATIVE_DEPRECIATION` | DECIMAL | 118 | 0 | -3079.44 | 0 |
| `LEGAL_ENTITY` | STRING | 1 | 0 |  |  |
| `USEFUL_LIFE` | STRING | 3 | 0 | 10 | 5 |
| `REMAINING_LIFE` | STRING | 10 | 0 | 10 | 3380 |

## Sample rows

| ASSET_ID | DESCRIPTION | CATEGORY | COST | NBV | AGE_DAYS | LOCATION | DEPRECIATION_LAST_RUN | CAPITALIZATION_DATE | CUMULATIVE_DEPRECIATION | USEFUL_LIFE | REMAINING_LIFE |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SOFT-000049 | Data Quality Management Suite | SOFTWARE | 19000 | 19000 | 28 | HQ | 1900-01-01 12:00:00.0000000 +00:00 | 2026-10-23 12:00:00.0000000 +00:00 | 0 | 5 | 1826 |
| COMP-000007 | HP Elite Dragonfly G4 | COMPUTER | 1600 | 1327 | 323 | HQ | 2026-09-30 12:00:00.0000000 +00:00 | 2026-01-01 12:00:00.0000000 +00:00 | -273 | 5 | 1553 |
| COMP-000024 | Dell Precision 3480 | COMPUTER | 3300 | 2805.87 | 323 | HQ | 2026-09-30 12:00:00.0000000 +00:00 | 2026-01-01 12:00:00.0000000 +00:00 | -494.13 | 5 | 1553 |
| FUR-000025 | Breakout Lounge Ottoman | FURNITURE | 8300 | 7680.29 | 323 | HQ | 2026-09-30 12:00:00.0000000 +00:00 | 2026-01-01 12:00:00.0000000 +00:00 | -619.71 | 10 | 3380 |
| FUR-000041 | Fraud Investigation Secure Cabinet | FURNITURE | 9900 | 9160.17 | 323 | HQ | 2026-09-30 12:00:00.0000000 +00:00 | 2026-01-01 12:00:00.0000000 +00:00 | -739.83 | 10 | 3380 |
