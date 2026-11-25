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
row_count: 189
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
- `2026-01-01 00:00:00`: 187 rows
- `2026-10-01 00:00:00`: 1 rows
- `2026-10-23 00:00:00`: 1 rows

**STATUS**
- `Open`: 189 rows

## Profile

Rows in the latest export: 189.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `FIXED_ASSET_NUMBER` | STRING | 190 | 0 | AUTO-000007 | SOFT-000049 |
| `LEGAL_ENTITY` | STRING | 1 | 0 |  |  |
| `ACQUISITION_DATE` | DATE | 3 | 0 | 2026-01-01 00:00:00 | 2026-10-23 00:00:00 |
| `STATUS` | STRING | 1 | 0 | Open | Open |
| `ACQUISITION_PRICE` | DECIMAL | 189 | 0 | 1100 | 20600 |

## Sample rows

| FIXED_ASSET_NUMBER | ACQUISITION_DATE | STATUS | ACQUISITION_PRICE |
|---|---|---|---|
| SOFT-000048 | 2026-10-01 00:00:00 | Open | 20000 |
| SOFT-000049 | 2026-10-23 00:00:00 | Open | 19000 |
| COMP-000002 | 2026-01-01 00:00:00 | Open | 1100 |
| COMP-000003 | 2026-01-01 00:00:00 | Open | 1200 |
| COMP-000004 | 2026-01-01 00:00:00 | Open | 1300 |
