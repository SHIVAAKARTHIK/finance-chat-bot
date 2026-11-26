---
name: capitalization_workbench
schema: gold
layer: gold
domain: fa
type: view
status: active
purpose: Shows fixed assets ready to be capitalized in the fixed-asset workflow.
grain: one row per ASSET_ID (one asset awaiting capitalization)
primary_key:
- ASSET_ID
entity_column: LEGAL_ENTITY
period_columns:
- CAPITALIZATION_DATE
pii_columns: []
synonyms: []
built_from:
- dim_fixed_assets
- dim_fixed_asset_books
- fact_asset_journal
- fact_asset_master_transactions
known_issues: []
proposed_fields:
- grain
- primary_key
reviewed: false
---

# capitalization_workbench

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `JOURNAL_ID` | string |  |  | `JOURNAL_ID` |
| `ASSET_ID` | string |  |  | `ASSET_ID` |
| `ASSET_DESCRIPTION` | string |  |  | `ASSET_DESCRIPTION` |
| `AMOUNT` | decimal |  |  | `AMOUNT` |
| `STATUS` | string |  |  | `STATUS` |
| `CAPITALIZATION_DATE` | date |  |  | `CAPITALIZATION_DATE` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Values

**JOURNAL_ID**
- `None`
- `100-000135`
- `100-000131`
- `100-000224`
- `100-000214`

**AMOUNT**
- `0`

**STATUS**
- `Ready to Capitalize`

**CAPITALIZATION_DATE**
- `2026-10-16 00:00:00`
