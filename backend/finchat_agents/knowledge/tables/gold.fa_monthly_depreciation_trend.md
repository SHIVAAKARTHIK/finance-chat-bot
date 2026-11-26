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
- `Depreciation`

**DEPRECIATION**
- `23170.95`
- `22423.5`
- `29479.76`
- `20928.6`
- `18609.6`
