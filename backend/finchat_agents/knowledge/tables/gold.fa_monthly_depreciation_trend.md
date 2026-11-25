---
name: fa_monthly_depreciation_trend
schema: gold
layer: gold
domain: fa
type: view
status: active
purpose: Shows monthly depreciation transaction totals.
grain: one row per transaction month
primary_key:
- TRANSACTION_YEAR_MONTH
entity_column: LEGAL_ENTITY
period_columns:
- TRANSACTION_YEAR_MONTH
pii_columns: []
synonyms: []
built_from:
- fact_asset_journal
- fact_asset_master_transactions
known_issues: []
row_count: 10
proposed_fields: []
reviewed: false
---

# fa_monthly_depreciation_trend

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `TRANSACTION_TYPE` | string |  |  | `TRANSACTION_TYPE` |
| `TRANSACTION_YEAR_MONTH` | string |  |  | `TRANSACTION_YEAR_MONTH` |
| `DEPRECIATION` | decimal |  |  | `DEPRECIATION` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Values

**TRANSACTION_TYPE**
- `Depreciation`: 10 rows

**DEPRECIATION**
- `23170.95`: 5 rows
- `22423.5`: 2 rows
- `29479.76`: 1 rows
- `20928.6`: 1 rows
- `18609.6`: 1 rows

## Profile

Rows in the latest export: 10.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `TRANSACTION_TYPE` | STRING | 1 | 0 | Depreciation | Depreciation |
| `TRANSACTION_YEAR_MONTH` | STRING | 10 | 0 |  |  |
| `DEPRECIATION` | DECIMAL | 5 | 0 | 18609.6 | 29479.76 |
| `LEGAL_ENTITY` | STRING | 1 | 0 |  |  |

## Sample rows

| TRANSACTION_TYPE | TRANSACTION_YEAR_MONTH | DEPRECIATION |
|---|---|---|
| Depreciation | (altered in export) | 29479.76 |
| Depreciation | (altered in export) | 23170.95 |
| Depreciation | (altered in export) | 18609.6 |
| Depreciation | (altered in export) | 22423.5 |
| Depreciation | (altered in export) | 23170.95 |
