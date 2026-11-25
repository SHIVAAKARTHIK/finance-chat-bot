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
row_count: 12
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
- `AUTO-000002`: 1 rows
- `AUTO-000005`: 1 rows
- `BUILD-000002`: 1 rows
- `BUILD-000005`: 1 rows
- `AUTO-000003`: 1 rows
- `AUTO-000001`: 1 rows
- `AUTO-000029`: 1 rows
- `AUTO-000006`: 1 rows
- `AUTO-000004`: 1 rows
- `BUILD-000003`: 1 rows
- `BUILD-000004`: 1 rows
- `BUILD-000001`: 1 rows

**CATEGORY**
- `AUTO`: 7 rows
- `BUILDINGS`: 5 rows

**ASSET_DESCRIPTION**
- `Branch Operations Hatchback`: 1 rows
- `Corporate Office Shuttle Van`: 1 rows
- `New York Records Storage Facility`: 1 rows
- `New York Regional Administration Building`: 1 rows
- `Hyundai Venue car`: 1 rows
- `Regional Manager Touring Vehicle`: 1 rows
- `New York Claims Operations Center`: 1 rows
- `Claims Inspection Utility Vehicle`: 1 rows
- `Office building`: 1 rows
- `Risk Engineering Field Vehicle`: 1 rows
- `Underwriting Field Visit Sedan`: 1 rows
- `New York Training Academy Building`: 1 rows

**DISPOSAL_TYPE**
- `DisposalScrap`: 8 rows
- `DisposalSale`: 4 rows

**BOOK_VALUE**
- `0`: 9 rows
- `15734.51`: 1 rows
- `10627`: 1 rows
- `None`: 1 rows

**SALE_VALUE**
- `0`: 10 rows
- `20000`: 1 rows
- `12000`: 1 rows

**GAIN_LOSS**
- `0`: 5 rows
- `-10727`: 1 rows
- `-10927`: 1 rows
- `-757`: 1 rows
- `-13698.05`: 1 rows
- `-10827`: 1 rows
- `6043.26`: 1 rows
- `-2044.59`: 1 rows

**REQUEST_DATE**
- `2026-10-20 00:00:00`: 6 rows
- `2026-10-22 00:00:00`: 5 rows
- `2026-10-14 00:00:00`: 1 rows

**STATUS**
- `Completed`: 9 rows
- `Not Posted`: 1 rows
- `Scheduled`: 1 rows
- `Pending Approval`: 1 rows

**JOURNAL_ID**
- `100-000123`: 2 rows
- `100-000127`: 2 rows
- `100-000129`: 2 rows
- `100-000216`: 1 rows
- `100-000219`: 1 rows
- `100-000215`: 1 rows
- `100-000217`: 1 rows
- `100-000214`: 1 rows
- `100-000218`: 1 rows

## Profile

Rows in the latest export: 12.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ASSET_ID` | STRING | 12 | 0 | AUTO-000001 | BUILD-000005 |
| `CATEGORY` | STRING | 2 | 0 | AUTO | BUILDINGS |
| `ASSET_DESCRIPTION` | STRING | 12 | 0 | Branch Operations Hatchback | Underwriting Field Visit Sedan |
| `DISPOSAL_TYPE` | STRING | 2 | 0 | DisposalSale | DisposalScrap |
| `BOOK_VALUE` | DECIMAL | 3 | 1 | 0 | 15734.51 |
| `SALE_VALUE` | DECIMAL | 3 | 0 | 0 | 20000 |
| `GAIN_LOSS` | DECIMAL | 8 | 0 | -13698.05 | 6043.26 |
| `REQUEST_DATE` | DATE | 3 | 0 | 2026-10-14 00:00:00 | 2026-10-22 00:00:00 |
| `STATUS` | STRING | 4 | 0 | Completed | Scheduled |
| `LEGAL_ENTITY` | STRING | 1 | 0 |  |  |
| `JOURNAL_ID` | STRING | 9 | 0 | 100-000123 | 100-000219 |

## Sample rows

| ASSET_ID | CATEGORY | ASSET_DESCRIPTION | DISPOSAL_TYPE | BOOK_VALUE | SALE_VALUE | GAIN_LOSS | REQUEST_DATE | STATUS | JOURNAL_ID |
|---|---|---|---|---|---|---|---|---|---|
| BUILD-000005 | BUILDINGS | New York Records Storage Facility | DisposalSale | 0 | 0 | -10927 | 2026-10-22 00:00:00 | Completed | 100-000219 |
| AUTO-000004 | AUTO | Underwriting Field Visit Sedan | DisposalScrap | 0 | 0 | 0 | 2026-10-20 00:00:00 | Completed | 100-000127 |
| AUTO-000005 | AUTO | Regional Manager Touring Vehicle | DisposalSale | 0 | 20000 | 6043.26 | 2026-10-20 00:00:00 | Completed | 100-000129 |
| AUTO-000001 | AUTO | Hyundai Venue car | DisposalScrap | 0 | 0 | -757 | 2026-10-20 00:00:00 | Completed | 100-000123 |
| BUILD-000001 | BUILDINGS | Office building | DisposalScrap | NULL | 0 | 0 | 2026-10-22 00:00:00 | Not Posted | 100-000214 |
