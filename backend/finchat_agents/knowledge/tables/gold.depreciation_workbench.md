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
row_count: 1766
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
- `100-000004`: 197 rows
- `100-000006`: 197 rows
- `100-000010`: 197 rows
- `100-000009`: 197 rows
- `100-000011`: 197 rows
- `100-000012`: 197 rows
- `100-000008`: 197 rows
- `100-000007`: 197 rows
- `100-000205`: 49 rows
- `100-000204`: 49 rows
- `100-000203`: 49 rows
- `100-000013`: 35 rows
- `100-000128`: 2 rows
- `100-000206`: 1 rows
- `100-000213`: 1 rows
- `100-000211`: 1 rows
- `100-000212`: 1 rows
- `100-000132`: 1 rows
- `100-000210`: 1 rows

**ASSET_CATEGORY**
- `AUTO`: 443 rows
- `COMPUTER`: 441 rows
- `FURNITURE`: 441 rows
- `BUILDINGS`: 441 rows

**DEPRECIATION_METHOD**
- `SLM`: 1766 rows

**USEFUL_LIFE**
- `5`: 884 rows
- `10`: 441 rows
- `39`: 441 rows

**STATUS**
- `Posted`: 1763 rows
- `Scheduled`: 1 rows
- `Not Posted`: 1 rows
- `Pending Approval`: 1 rows

## Profile

Rows in the latest export: 1766.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `JOURNAL_ID` | STRING | 18 | 0 | 100-000004 | 100-000213 |
| `ASSET_ID` | STRING | 199 | 0 | AUTO-000001 | FUR-000050 |
| `ASSET_CATEGORY` | STRING | 4 | 0 | AUTO | FURNITURE |
| `DEPRECIATION_METHOD` | STRING | 1 | 0 | SLM | SLM |
| `USEFUL_LIFE` | STRING | 3 | 0 | 10 | 5 |
| `LEGAL_ENTITY` | STRING | 1 | 0 |  |  |
| `MONTHLY_DEPRECIATION` | DECIMAL | 375 | 0 | 280 | 180327.16 |
| `STATUS` | STRING | 4 | 0 | Not Posted | Scheduled |

## Sample rows

| JOURNAL_ID | ASSET_ID | ASSET_CATEGORY | DEPRECIATION_METHOD | USEFUL_LIFE | MONTHLY_DEPRECIATION | STATUS |
|---|---|---|---|---|---|---|
| 100-000204 | COMP-000005 | COMPUTER | SLM | 5 | 300 | Posted |
| 100-000204 | COMP-000021 | COMPUTER | SLM | 5 | 492 | Posted |
| 100-000204 | COMP-000030 | COMPUTER | SLM | 5 | 642 | Posted |
| 100-000205 | FUR-000008 | FURNITURE | SLM | 10 | 543 | Posted |
| 100-000205 | FUR-000032 | FURNITURE | SLM | 10 | 738 | Posted |
