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
row_count: 17
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
- `Manual entries requiring action`: 10 rows
- `Automated entries completed without errors`: 7 rows

**PERCENTAGE**
- `50`: 4 rows
- `100`: 3 rows
- `75`: 2 rows
- `0`: 2 rows
- `66.67`: 2 rows
- `70`: 1 rows
- `40`: 1 rows
- `58.33`: 1 rows
- `14.29`: 1 rows

**KPI_COUNT**
- `2`: 4 rows
- `7`: 3 rows
- `3`: 3 rows
- `1`: 2 rows
- `0`: 2 rows
- `6`: 1 rows
- `5`: 1 rows
- `4`: 1 rows

**TOTAL_COUNT**
- `4`: 4 rows
- `3`: 3 rows
- `5`: 2 rows
- `2`: 2 rows
- `12`: 1 rows
- `10`: 1 rows
- `6`: 1 rows
- `49`: 1 rows
- `8`: 1 rows
- `16`: 1 rows

## Profile

Rows in the latest export: 17.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `KPI` | STRING | 2 | 0 | Automated entries completed without e... | Manual entries requiring action |
| `PERCENTAGE` | DECIMAL | 9 | 0 | 0 | 100 |
| `KPI_COUNT` | LONG | 8 | 0 | 0 | 7 |
| `TOTAL_COUNT` | LONG | 10 | 0 | 2 | 49 |
| `LEGAL_ENTITY` | STRING | 16 | 0 |  |  |

## Sample rows

| KPI | PERCENTAGE | KPI_COUNT | TOTAL_COUNT |
|---|---|---|---|
| Automated entries completed without e... | 58.33 | 7 | 12 |
| Automated entries completed without e... | 100 | 6 | 6 |
| Automated entries completed without e... | 75 | 3 | 4 |
| Automated entries completed without e... | 70 | 7 | 10 |
| Automated entries completed without e... | 100 | 3 | 3 |
