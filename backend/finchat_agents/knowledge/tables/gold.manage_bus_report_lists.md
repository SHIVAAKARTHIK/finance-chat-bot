---
name: manage_bus_report_lists
schema: gold
layer: gold
domain: null
type: table
status: active
purpose: Catalog of management; control and financial reports with owners and links.
grain: one row per report
primary_key:
- REPORT
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns:
- OWNER
synonyms: []
built_from: []
known_issues: []
row_count: 10
proposed_fields: []
reviewed: false
---

# manage_bus_report_lists

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `REPORT` | string |  |  | `REPORT` |
| `LIBRARY` | string |  |  | `LIBRARY` |
| `OWNER` | string |  |  | `OWNER` |
| `FREQUENCY` | string |  |  | `FREQUENCY` |
| `LINK` | string |  |  | `LINK` |
| `REPORTING_TYPE` | string |  |  | `REPORTING_TYPE` |
| `LEGAL_ENTITY` | long |  |  | `LEGAL_ENTITY` |

## Values

**REPORT**
- `Expense Analysis Report`: 1 rows
- `Identity & Access Control Monitoring`: 1 rows
- `Balance Sheet`: 1 rows
- `Premium Analysis Report`: 1 rows
- `Cash Reconciliation Report`: 1 rows
- `Ultimate Analysis Report`: 1 rows
- `Income Statement`: 1 rows
- `Subledger Summary Report`: 1 rows
- `Anomaly Detection Report`: 1 rows
- `Detailed Subledger Report`: 1 rows

**LIBRARY**
- `Management`: 6 rows
- `Control`: 2 rows
- `Financial Statements`: 2 rows

**FREQUENCY**
- `Daily`: 9 rows
- `Live`: 1 rows

**LINK**
- `https://app.powerbi.com/view?r=eyJrIjoiZDdiZGE1NmItZWQ2ZC00ZjExLWIwMTYtZDNmNTcyNTdhZTE4IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows
- `https://app.powerbi.com/view?r=eyJrIjoiMTU3ZmQ4YjAtMjViYi00YTkzLWFkZTQtZDE3NjVlN2U5MWQ0IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows
- `https://app.powerbi.com/view?r=eyJrIjoiZGY4Mjc2YWEtNWI2Yy00NTZlLThkMWMtOWQ5MGJlZjJmODA2IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows
- `https://app.powerbi.com/view?r=eyJrIjoiODM3N2JiMGYtMWJhOC00YjI3LWFjMGUtYmI5OTc5MjJkNmFhIiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows
- `https://app.powerbi.com/view?r=eyJrIjoiMzRjMDU3OTUtOTY0Mi00MjBkLWJmYmItNWI3ZjNhMzBlMjU1IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows
- `https://app.powerbi.com/view?r=eyJrIjoiMzVmYmRhYjktZTE1YS00N2U3LWE2ZDItOWUyMGNmN2IxNjFlIiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows
- `https://app.powerbi.com/view?r=eyJrIjoiM2ZhZTdlMDgtYjJkMC00Y2JhLWFmMjEtMWI1YzRkNjhjN2ExIiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows
- `https://app.powerbi.com/view?r=eyJrIjoiZmYxMTEzYmEtMTYzOC00ZDJkLTg4ZjUtNmFjNWM2NGZmMzU1IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows
- `https://app.powerbi.com/view?r=eyJrIjoiMDkyZGFjMjctMTQzYi00YzE1LWI2N2YtOWZiNmYwZjY5NDU4IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows
- `https://app.powerbi.com/view?r=eyJrIjoiYjlmODQ0YTQtOWVjOS00OWFjLTk3NjctZmE0Y2IxN2Y1NmU4IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows

**REPORTING_TYPE**
- `Management Reporting`: 6 rows
- `Control Monitoring`: 2 rows
- `Financial Reporting`: 2 rows

## Profile

Rows in the latest export: 10.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `REPORT` | STRING | 10 | 0 | Anomaly Detection Report | Ultimate Analysis Report |
| `LIBRARY` | STRING | 3 | 0 | Control | Management |
| `OWNER` | STRING | 3 | 0 |  |  |
| `FREQUENCY` | STRING | 2 | 0 | Daily | Live |
| `LINK` | STRING | 10 | 0 | https://app.powerbi.com/view?r=eyJrIj... | https://app.powerbi.com/view?r=eyJrIj... |
| `REPORTING_TYPE` | STRING | 3 | 0 | Control Monitoring | Management Reporting |
| `LEGAL_ENTITY` | LONG | 1 | 0 |  |  |

## Sample rows

| REPORT | LIBRARY | OWNER | FREQUENCY | LINK | REPORTING_TYPE |
|---|---|---|---|---|---|
| Expense Analysis Report | Management | <masked> | Daily | https://app.powerbi.com/view?r=eyJrIj... | Management Reporting |
| Premium Analysis Report | Management | <masked> | Daily | https://app.powerbi.com/view?r=eyJrIj... | Management Reporting |
| Ultimate Analysis Report | Management | <masked> | Daily | https://app.powerbi.com/view?r=eyJrIj... | Management Reporting |
| Cash Reconciliation Report | Management | <masked> | Daily | https://app.powerbi.com/view?r=eyJrIj... | Management Reporting |
| Subledger Summary Report | Management | <masked> | Daily | https://app.powerbi.com/view?r=eyJrIj... | Management Reporting |
