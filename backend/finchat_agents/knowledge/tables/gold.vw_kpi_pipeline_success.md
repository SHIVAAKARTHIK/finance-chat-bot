---
name: vw_kpi_pipeline_success
schema: gold
layer: gold
domain: null
type: view
status: active
purpose: Summarizes successful pipeline runs as a success rate by source system.
grain: one row per source system KPI
primary_key:
- LEGAL_ENTITY
entity_column: null
period_columns: []
pii_columns: []
synonyms: []
built_from:
- pipeline_logs
known_issues: []
row_count: 4
proposed_fields: []
reviewed: false
---

# vw_kpi_pipeline_success

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
- `Pipeline Success Rate`: 4 rows

**PERCENTAGE**
- `100`: 1 rows
- `99.68`: 1 rows
- `99.43`: 1 rows
- `99.03`: 1 rows

**KPI_COUNT**
- `173`: 1 rows
- `174`: 1 rows
- `205`: 1 rows
- `314`: 1 rows

**TOTAL_COUNT**
- `174`: 2 rows
- `315`: 1 rows
- `207`: 1 rows

## Profile

Rows in the latest export: 4.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `KPI` | STRING | 1 | 0 | Pipeline Success Rate | Pipeline Success Rate |
| `PERCENTAGE` | DECIMAL | 4 | 0 | 99.03 | 100 |
| `KPI_COUNT` | LONG | 4 | 0 | 173 | 314 |
| `TOTAL_COUNT` | LONG | 3 | 0 | 174 | 315 |
| `LEGAL_ENTITY` | STRING | 4 | 0 |  |  |

## Sample rows

| KPI | PERCENTAGE | KPI_COUNT | TOTAL_COUNT |
|---|---|---|---|
| Pipeline Success Rate | 100 | 174 | 174 |
| Pipeline Success Rate | 99.43 | 173 | 174 |
| Pipeline Success Rate | 99.68 | 314 | 315 |
| Pipeline Success Rate | 99.03 | 205 | 207 |
