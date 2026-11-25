---
name: vw_managed_coll_kpi_filter
schema: gold
layer: gold
domain: ar
type: view
status: broken
purpose: Summarizes collection KPIs with fiscal-period filter fields.
grain: one row per KPI and selected period
primary_key:
- Section
- KPI
- LEGAL_ENTITY
- PERIOD_TYPE
- PERIOD_YEAR
- PERIOD_MONTH
- PERIOD_QUARTER
entity_column: LEGAL_ENTITY
period_columns:
- PERIOD_YEAR
- PERIOD_MONTH
- PERIOD_QUARTER
- PERIOD_NAME
- PERIOD_START_DATE
- PERIOD_END_DATE
pii_columns: []
synonyms: []
built_from:
- fact_cust_trans_opens
- fact_cust_transactions
- fact_cash_discounts
known_issues: []
row_count: null
proposed_fields: []
reviewed: false
broken_error: the profiling query failed in the catalog export (no row count); the error text is not in the workbook
---

# vw_managed_coll_kpi_filter

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Section` | string |  |  | `Section` |
| `KPI` | string |  |  | `KPI` |
| `Amount` | double |  |  | `Amount` |
| `Count` | long |  |  | `Count` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `PERIOD_TYPE` | string |  |  | `PERIOD_TYPE` |
| `PERIOD_YEAR` | int |  |  | `PERIOD_YEAR` |
| `PERIOD_MONTH` | int |  |  | `PERIOD_MONTH` |
| `PERIOD_QUARTER` | int |  |  | `PERIOD_QUARTER` |
| `PERIOD_NAME` | string |  |  | `PERIOD_NAME` |
| `PERIOD_START_DATE` | date |  |  | `PERIOD_START_DATE` |
| `PERIOD_END_DATE` | date |  |  | `PERIOD_END_DATE` |

## Profile

Rows in the latest export: unknown.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Section` | STRING |  |  |  |  |
| `KPI` | STRING |  |  |  |  |
| `Amount` | DOUBLE |  |  |  |  |
| `Count` | LONG |  |  |  |  |
| `LEGAL_ENTITY` | STRING |  |  |  |  |
| `PERIOD_TYPE` | STRING |  |  |  |  |
| `PERIOD_YEAR` | INT |  |  |  |  |
| `PERIOD_MONTH` | INT |  |  |  |  |
| `PERIOD_QUARTER` | INT |  |  |  |  |
| `PERIOD_NAME` | STRING |  |  |  |  |
| `PERIOD_START_DATE` | DATE |  |  |  |  |
| `PERIOD_END_DATE` | DATE |  |  |  |  |
