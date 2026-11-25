---
name: managed_coll_early_payment_discounts
schema: gold
layer: gold
domain: ar
type: view
status: active
purpose: Lists customer invoices eligible for early-payment discounts.
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
- fact_cust_transactions
- fact_cust_trans_opens
- fact_cust_table_bi_entities
- fact_cash_discounts
known_issues: []
row_count: 0
proposed_fields: []
reviewed: false
---

# managed_coll_early_payment_discounts

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Reference` | string |  |  | `Reference` |
| `Customer` | string |  |  | `Customer` |
| `invoice_number` | string |  |  | `invoice_number` |
| `Amount` | string |  |  | `Amount` |
| `Invoice_date` | date |  |  | `Invoice_date` |
| `Due_date` | date |  |  | `Due_date` |
| `Discounts` | string |  |  | `Discounts` |
| `Action` | string |  |  | `Action` |
| `email` | string |  |  | `email` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Profile

Rows in the latest export: 0.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Reference` | STRING | 0 | 0 |  |  |
| `Customer` | STRING | 0 | 0 |  |  |
| `invoice_number` | STRING | 0 | 0 |  |  |
| `Amount` | STRING | 0 | 0 |  |  |
| `Invoice_date` | DATE | 0 | 0 |  |  |
| `Due_date` | DATE | 0 | 0 |  |  |
| `Discounts` | STRING | 0 | 0 |  |  |
| `Action` | STRING | 0 | 0 |  |  |
| `email` | STRING | 0 | 0 |  |  |
| `LEGAL_ENTITY` | STRING | 0 | 0 |  |  |
