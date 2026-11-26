---
name: vw_managed_coll_overdue_filter
schema: gold
layer: gold
domain: ar
type: view
status: broken
purpose: Lists overdue customer invoices with fiscal-period filter fields.
grain: one row per invoice and selected period
primary_key:
- INVOICE_NUMBER
- PERIOD_TYPE
- PERIOD_YEAR
- PERIOD_MONTH
- PERIOD_QUARTER
entity_column: LEGAL_ENTITY
period_columns:
- INVOICE_DATE
- DUE_DATE
- PERIOD_START_DATE
- PERIOD_END_DATE
pii_columns:
- EMAIL
synonyms: []
built_from:
- fact_cust_trans_opens
- fact_cust_transactions
- fact_cust_table_bi_entities
known_issues: []
proposed_fields: []
reviewed: false
broken_error: the profiling query failed in the catalog export (no row count); the error text is not in the workbook
---

# vw_managed_coll_overdue_filter

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `REFERENCE` | string |  |  | `REFERENCE` |
| `CUSTOMER` | string |  |  | `CUSTOMER` |
| `INVOICE_NUMBER` | string |  |  | `INVOICE_NUMBER` |
| `AMOUNT` | string |  |  | `AMOUNT` |
| `INVOICE_DATE` | string |  |  | `INVOICE_DATE` |
| `DUE_DATE` | string |  |  | `DUE_DATE` |
| `AGING` | string |  |  | `AGING` |
| `ACTION` | string |  |  | `ACTION` |
| `EMAIL` | string |  |  | `EMAIL` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `PERIOD_TYPE` | string |  |  | `PERIOD_TYPE` |
| `PERIOD_YEAR` | int |  |  | `PERIOD_YEAR` |
| `PERIOD_MONTH` | int |  |  | `PERIOD_MONTH` |
| `PERIOD_QUARTER` | int |  |  | `PERIOD_QUARTER` |
| `PERIOD_NAME` | string |  |  | `PERIOD_NAME` |
| `PERIOD_START_DATE` | date |  |  | `PERIOD_START_DATE` |
| `PERIOD_END_DATE` | date |  |  | `PERIOD_END_DATE` |
