---
name: vw_managed_coll_due_soon_accounts_filter
schema: gold
layer: gold
domain: ar
type: view
status: broken
purpose: Lists due-soon customer invoices with fiscal-period filter fields.
grain: one row per customer invoice and selected period
primary_key:
- invoice_number
- PERIOD_TYPE
- PERIOD_YEAR
- PERIOD_MONTH
- PERIOD_QUARTER
entity_column: LEGAL_ENTITY
period_columns:
- Invoice_date
- Due_date
- PERIOD_START_DATE
- PERIOD_END_DATE
pii_columns:
- email
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

# vw_managed_coll_due_soon_accounts_filter

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Reference` | string |  |  | `Reference` |
| `Customer` | string |  |  | `Customer` |
| `invoice_number` | string |  |  | `invoice_number` |
| `Amount` | string |  |  | `Amount` |
| `Invoice_date` | string |  |  | `Invoice_date` |
| `Due_date` | string |  |  | `Due_date` |
| `Aging` | string |  |  | `Aging` |
| `Action` | string |  |  | `Action` |
| `email` | string |  |  | `email` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `PERIOD_TYPE` | string |  |  | `PERIOD_TYPE` |
| `PERIOD_YEAR` | int |  |  | `PERIOD_YEAR` |
| `PERIOD_MONTH` | int |  |  | `PERIOD_MONTH` |
| `PERIOD_QUARTER` | int |  |  | `PERIOD_QUARTER` |
| `PERIOD_NAME` | string |  |  | `PERIOD_NAME` |
| `PERIOD_START_DATE` | date |  |  | `PERIOD_START_DATE` |
| `PERIOD_END_DATE` | date |  |  | `PERIOD_END_DATE` |
