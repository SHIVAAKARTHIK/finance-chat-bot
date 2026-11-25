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
row_count: 2
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
- `System processing completed without exception`: 1 rows
- `Count of Anomalies`: 1 rows

**PERCENTAGE**
- `99.54`: 1 rows
- `18`: 1 rows

**KPI_COUNT**
- `866`: 1 rows
- `18`: 1 rows

**TOTAL_COUNT**
- `870`: 1 rows
- `31`: 1 rows

## Profile

Rows in the latest export: 2.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `KPI` | STRING | 2 | 0 | Count of Anomalies | System processing completed without e... |
| `PERCENTAGE` | DECIMAL | 2 | 0 | 18 | 99.54 |
| `KPI_COUNT` | LONG | 2 | 0 | 18 | 866 |
| `TOTAL_COUNT` | LONG | 2 | 0 | 31 | 870 |
| `LEGAL_ENTITY` | NULL | 0 | 2 |  |  |

## Sample rows

| KPI | PERCENTAGE | KPI_COUNT | TOTAL_COUNT |
|---|---|---|---|
| System processing completed without e... | 99.54 | 866 | 870 |
| Count of Anomalies | 18 | 18 | 31 |
