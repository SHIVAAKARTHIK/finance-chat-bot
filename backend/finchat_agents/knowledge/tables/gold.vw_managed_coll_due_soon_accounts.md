---
name: vw_managed_coll_due_soon_accounts
schema: gold
layer: gold
domain: ar
type: view
status: broken
purpose: Lists customer invoices approaching their due date for collection follow-up.
grain: one row per customer invoice
primary_key:
- invoice_number
entity_column: LEGAL_ENTITY
period_columns:
- Invoice_date
- Due_date
pii_columns:
- email
synonyms: []
built_from:
- fact_cust_trans_opens
- fact_cust_transactions
- fact_cust_table_bi_entities
known_issues: []
row_count: null
proposed_fields: []
reviewed: false
broken_error: the profiling query failed in the catalog export (no row count); the error text is not in the workbook
---

# vw_managed_coll_due_soon_accounts

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

## Profile

Rows in the latest export: unknown.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Reference` | STRING |  |  |  |  |
| `Customer` | STRING |  |  |  |  |
| `invoice_number` | STRING |  |  |  |  |
| `Amount` | STRING |  |  |  |  |
| `Invoice_date` | STRING |  |  |  |  |
| `Due_date` | STRING |  |  |  |  |
| `Aging` | STRING |  |  |  |  |
| `Action` | STRING |  |  |  |  |
| `email` | STRING |  |  |  |  |
| `LEGAL_ENTITY` | STRING |  |  |  |  |
