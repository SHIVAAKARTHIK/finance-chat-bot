---
name: depreciation_workbench
schema: gold
layer: gold
domain: fa
type: view
status: active
purpose: Shows fixed-asset depreciation journal lines and their posting status.
grain: one row per JOURNAL_ID + ASSET_ID (one asset in a depreciation journal)
primary_key:
- JOURNAL_ID
- ASSET_ID
entity_column: LEGAL_ENTITY
period_columns: []
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

# depreciation_workbench

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `JOURNAL_ID` | string |  |  | `JOURNAL_ID` |
| `ASSET_ID` | string |  |  | `ASSET_ID` |
| `ASSET_CATEGORY` | string |  |  | `ASSET_CATEGORY` |
| `DEPRECIATION_METHOD` | string |  |  | `DEPRECIATION_METHOD` |
| `USEFUL_LIFE` | string |  |  | `USEFUL_LIFE` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `MONTHLY_DEPRECIATION` | decimal |  |  | `MONTHLY_DEPRECIATION` |
| `STATUS` | string |  |  | `STATUS` |

## Values

**JOURNAL_ID**
- `100-000004`
- `100-000006`
- `100-000010`
- `100-000009`
- `100-000011`
- `100-000012`
- `100-000008`
- `100-000007`
- `100-000205`
- `100-000204`
- `100-000203`
- `100-000013`
- `100-000128`
- `100-000206`
- `100-000213`
- `100-000211`
- `100-000212`
- `100-000132`
- `100-000210`

**ASSET_CATEGORY**
- `AUTO`
- `COMPUTER`
- `FURNITURE`
- `BUILDINGS`

**DEPRECIATION_METHOD**
- `SLM`

**USEFUL_LIFE**
- `5`
- `10`
- `39`

**STATUS**
- `Posted`
- `Scheduled`
- `Not Posted`
- `Pending Approval`
