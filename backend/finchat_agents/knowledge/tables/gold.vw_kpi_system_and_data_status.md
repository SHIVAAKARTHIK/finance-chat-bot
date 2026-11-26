---
name: vw_kpi_system_and_data_status
schema: gold
layer: gold
domain: null
type: view
status: active
purpose: Summarizes pipeline completion and data-quality anomaly counts.
grain: one row per system/data-status KPI
primary_key:
- KPI
entity_column: null
period_columns: []
pii_columns: []
synonyms: []
built_from:
- pipeline_logs
- anomaly_audit
known_issues: []
proposed_fields: []
reviewed: false
---

# vw_kpi_system_and_data_status

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `KPI` | string |  |  | `KPI` |
| `PERCENTAGE` | decimal |  |  | `PERCENTAGE` |
| `KPI_COUNT` | long |  |  | `KPI_COUNT` |
| `TOTAL_COUNT` | long |  |  | `TOTAL_COUNT` |
| `LEGAL_ENTITY` | null |  |  | `LEGAL_ENTITY` |

## Values

**KPI**
- `System processing completed without exception`
- `Count of Anomalies`

**PERCENTAGE**
- `99.54`
- `18`

**KPI_COUNT**
- `866`
- `18`

**TOTAL_COUNT**
- `870`
- `31`

## Empty columns

Empty in every row: `LEGAL_ENTITY`. Do not filter or group on them.
