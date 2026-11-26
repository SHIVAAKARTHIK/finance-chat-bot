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
- `Expense Analysis Report`
- `Identity & Access Control Monitoring`
- `Balance Sheet`
- `Premium Analysis Report`
- `Cash Reconciliation Report`
- `Ultimate Analysis Report`
- `Income Statement`
- `Subledger Summary Report`
- `Anomaly Detection Report`
- `Detailed Subledger Report`

**LIBRARY**
- `Management`
- `Control`
- `Financial Statements`

**FREQUENCY**
- `Daily`
- `Live`

**LINK**
- `https://app.powerbi.com/view?r=eyJrIjoiZDdiZGE1NmItZWQ2ZC00ZjExLWIwMTYtZDNmNTcyNTdhZTE4IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`
- `https://app.powerbi.com/view?r=eyJrIjoiMTU3ZmQ4YjAtMjViYi00YTkzLWFkZTQtZDE3NjVlN2U5MWQ0IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`
- `https://app.powerbi.com/view?r=eyJrIjoiZGY4Mjc2YWEtNWI2Yy00NTZlLThkMWMtOWQ5MGJlZjJmODA2IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`
- `https://app.powerbi.com/view?r=eyJrIjoiODM3N2JiMGYtMWJhOC00YjI3LWFjMGUtYmI5OTc5MjJkNmFhIiwidCI6ImM4N2I4OWJhLTU0ZTItND...`
- `https://app.powerbi.com/view?r=eyJrIjoiMzRjMDU3OTUtOTY0Mi00MjBkLWJmYmItNWI3ZjNhMzBlMjU1IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`
- `https://app.powerbi.com/view?r=eyJrIjoiMzVmYmRhYjktZTE1YS00N2U3LWE2ZDItOWUyMGNmN2IxNjFlIiwidCI6ImM4N2I4OWJhLTU0ZTItND...`
- `https://app.powerbi.com/view?r=eyJrIjoiM2ZhZTdlMDgtYjJkMC00Y2JhLWFmMjEtMWI1YzRkNjhjN2ExIiwidCI6ImM4N2I4OWJhLTU0ZTItND...`
- `https://app.powerbi.com/view?r=eyJrIjoiZmYxMTEzYmEtMTYzOC00ZDJkLTg4ZjUtNmFjNWM2NGZmMzU1IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`
- `https://app.powerbi.com/view?r=eyJrIjoiMDkyZGFjMjctMTQzYi00YzE1LWI2N2YtOWZiNmYwZjY5NDU4IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`
- `https://app.powerbi.com/view?r=eyJrIjoiYjlmODQ0YTQtOWVjOS00OWFjLTk3NjctZmE0Y2IxN2Y1NmU4IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`

**REPORTING_TYPE**
- `Management Reporting`
- `Control Monitoring`
- `Financial Reporting`
