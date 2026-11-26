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
- `2026`

**MONTH**
- `May`
- `April`
- `August`
- `July`
- `June`
- `September`
- `October`

**DISPOSAL_COUNT**
- `85`
- `92`
- `34`
- `45`
- `68`
- `80`
- `57`

**POSTING_SCHEMA**
- `GAAP`
