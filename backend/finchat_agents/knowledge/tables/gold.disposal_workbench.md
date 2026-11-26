---
name: disposal_workbench
schema: gold
layer: gold
domain: fa
type: view
status: active
purpose: Shows fixed assets with scheduled or completed disposal activity.
grain: one row per ASSET_ID (one asset disposal)
primary_key:
- ASSET_ID
entity_column: LEGAL_ENTITY
period_columns:
- REQUEST_DATE
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

# disposal_workbench

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ASSET_ID` | string |  |  | `ASSET_ID` |
| `CATEGORY` | string |  |  | `CATEGORY` |
| `ASSET_DESCRIPTION` | string |  |  | `ASSET_DESCRIPTION` |
| `DISPOSAL_TYPE` | string |  |  | `DISPOSAL_TYPE` |
| `BOOK_VALUE` | decimal |  |  | `BOOK_VALUE` |
| `SALE_VALUE` | decimal |  |  | `SALE_VALUE` |
| `GAIN_LOSS` | decimal |  |  | `GAIN_LOSS` |
| `REQUEST_DATE` | date |  |  | `REQUEST_DATE` |
| `STATUS` | string |  |  | `STATUS` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `JOURNAL_ID` | string |  |  | `JOURNAL_ID` |

## Values

**ASSET_ID**
- `AUTO-000002`
- `AUTO-000005`
- `BUILD-000002`
- `BUILD-000005`
- `AUTO-000003`
- `AUTO-000001`
- `AUTO-000029`
- `AUTO-000006`
- `AUTO-000004`
- `BUILD-000003`
- `BUILD-000004`
- `BUILD-000001`

**CATEGORY**
- `AUTO`
- `BUILDINGS`

**ASSET_DESCRIPTION**
- `Branch Operations Hatchback`
- `Corporate Office Shuttle Van`
- `New York Records Storage Facility`
- `New York Regional Administration Building`
- `Hyundai Venue car`
- `Regional Manager Touring Vehicle`
- `New York Claims Operations Center`
- `Claims Inspection Utility Vehicle`
- `Office building`
- `Risk Engineering Field Vehicle`
- `Underwriting Field Visit Sedan`
- `New York Training Academy Building`

**DISPOSAL_TYPE**
- `DisposalScrap`
- `DisposalSale`

**BOOK_VALUE**
- `0`
- `15734.51`
- `10627`
- `None`

**SALE_VALUE**
- `0`
- `20000`
- `12000`

**GAIN_LOSS**
- `0`
- `-10727`
- `-10927`
- `-757`
- `-13698.05`
- `-10827`
- `6043.26`
- `-2044.59`

**REQUEST_DATE**
- `2026-10-20 00:00:00`
- `2026-10-22 00:00:00`
- `2026-10-14 00:00:00`

**STATUS**
- `Completed`
- `Not Posted`
- `Scheduled`
- `Pending Approval`

**JOURNAL_ID**
- `100-000123`
- `100-000127`
- `100-000129`
- `100-000216`
- `100-000219`
- `100-000215`
- `100-000217`
- `100-000214`
- `100-000218`
