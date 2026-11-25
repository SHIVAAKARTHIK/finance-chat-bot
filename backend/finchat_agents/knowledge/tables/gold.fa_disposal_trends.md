---
name: fa_disposal_trends
schema: gold
layer: gold
domain: fa
type: table
status: active
purpose: Monthly count of fixed-asset disposals.
grain: one row per MONTH (one monthly disposal count)
primary_key:
- MONTH
entity_column: LEGAL_ENTITY
period_columns:
- YEAR
- MONTH
pii_columns: []
synonyms: []
built_from:
- fact_asset_journal
- fact_asset_master_transactions
known_issues: []
row_count: 7
proposed_fields:
- grain
- primary_key
reviewed: false
---

# fa_disposal_trends

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `YEAR` | long |  |  | `YEAR` |
| `MONTH` | string |  |  | `MONTH` |
| `DISPOSAL_COUNT` | long |  |  | `DISPOSAL_COUNT` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `POSTING_SCHEMA` | string |  |  | `POSTING_SCHEMA` |

## Values

**YEAR**
- `2026`: 7 rows

**MONTH**
- `May`: 1 rows
- `April`: 1 rows
- `August`: 1 rows
- `July`: 1 rows
- `June`: 1 rows
- `September`: 1 rows
- `October`: 1 rows

**DISPOSAL_COUNT**
- `85`: 1 rows
- `92`: 1 rows
- `34`: 1 rows
- `45`: 1 rows
- `68`: 1 rows
- `80`: 1 rows
- `57`: 1 rows

**POSTING_SCHEMA**
- `GAAP`: 7 rows

## Profile

Rows in the latest export: 7.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `YEAR` | LONG | 1 | 0 | 2026 | 2026 |
| `MONTH` | STRING | 7 | 0 | April | September |
| `DISPOSAL_COUNT` | LONG | 7 | 0 | 34 | 92 |
| `LEGAL_ENTITY` | STRING | 1 | 0 |  |  |
| `POSTING_SCHEMA` | STRING | 1 | 0 | GAAP | GAAP |

## Sample rows

| YEAR | MONTH | DISPOSAL_COUNT | POSTING_SCHEMA |
|---|---|---|---|
| 2026 | April | 45 | GAAP |
| 2026 | May | 68 | GAAP |
| 2026 | June | 34 | GAAP |
| 2026 | July | 92 | GAAP |
| 2026 | August | 57 | GAAP |
