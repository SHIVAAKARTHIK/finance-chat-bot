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
- `Pipeline Success Rate`

**PERCENTAGE**
- `100`
- `99.68`
- `99.43`
- `99.03`

**KPI_COUNT**
- `173`
- `174`
- `205`
- `314`

**TOTAL_COUNT**
- `174`
- `315`
- `207`
