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
row_count: 101
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
- `None`: 97 rows
- `100-000135`: 1 rows
- `100-000131`: 1 rows
- `100-000224`: 1 rows
- `100-000214`: 1 rows

**AMOUNT**
- `0`: 101 rows

**STATUS**
- `Ready to Capitalize`: 101 rows

**CAPITALIZATION_DATE**
- `2026-10-16 00:00:00`: 101 rows

## Profile

Rows in the latest export: 101.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `JOURNAL_ID` | STRING | 4 | 97 | 100-000131 | 100-000224 |
| `ASSET_ID` | STRING | 101 | 0 | BUILD-000001 | SOFT-000050 |
| `ASSET_DESCRIPTION` | STRING | 105 | 0 | Accounts Payable Automation Suite | Workflow Automation Suite |
| `AMOUNT` | DECIMAL | 1 | 0 | 0 | 0 |
| `STATUS` | STRING | 1 | 0 | Ready to Capitalize | Ready to Capitalize |
| `CAPITALIZATION_DATE` | DATE | 1 | 0 | 2026-10-16 00:00:00 | 2026-10-16 00:00:00 |
| `LEGAL_ENTITY` | STRING | 1 | 0 |  |  |

## Sample rows

| JOURNAL_ID | ASSET_ID | ASSET_DESCRIPTION | AMOUNT | STATUS | CAPITALIZATION_DATE |
|---|---|---|---|---|---|
| 100-000135 | LHI-000000002 | Corporate Office Conference Room Acou... | 0 | Ready to Capitalize | 2026-10-16 00:00:00 |
| NULL | LHI-000000003 | Corporate Office Office Electrical Re... | 0 | Ready to Capitalize | 2026-10-16 00:00:00 |
| NULL | LHI-000000004 | Corporate Office Central Air Conditio... | 0 | Ready to Capitalize | 2026-10-16 00:00:00 |
| NULL | LHI-000000005 | Corporate Office Fire Detection Syste... | 0 | Ready to Capitalize | 2026-10-16 00:00:00 |
| NULL | LHI-000000006 | Corporate Office Cafeteria Interior R... | 0 | Ready to Capitalize | 2026-10-16 00:00:00 |
