---
name: vw_manage_close_journal_entry_kpi
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Shows automated versus manual journal-entry processing outcomes by legal entity.
grain: one row per KPI and legal entity
primary_key:
- KPI
- LEGAL_ENTITY
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- fact_ledger_journal_headers
- fact_ledger_journal_lines
known_issues: []
proposed_fields: []
reviewed: false
---

# vw_manage_close_journal_entry_kpi

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `KPI` | string |  |  | `KPI` |
| `PERCENTAGE` | decimal |  |  | `PERCENTAGE` |
| `KPI_COUNT` | long |  |  | `KPI_COUNT` |
| `TOTAL_COUNT` | long |  |  | `TOTAL_COUNT` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Values

**KPI**
- `Manual entries requiring action`
- `Automated entries completed without errors`

**PERCENTAGE**
- `50`
- `100`
- `75`
- `0`
- `66.67`
- `70`
- `40`
- `58.33`
- `14.29`

**KPI_COUNT**
- `2`
- `7`
- `3`
- `1`
- `0`
- `6`
- `5`
- `4`

**TOTAL_COUNT**
- `4`
- `3`
- `5`
- `2`
- `12`
- `10`
- `6`
- `49`
- `8`
- `16`
