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

## Empty columns

Empty in every row: `Reference`, `Customer`, `invoice_number`, `Amount`, `Invoice_date`, `Due_date`, `Discounts`, `Action`, `email`, `LEGAL_ENTITY`. Do not filter or group on them.
