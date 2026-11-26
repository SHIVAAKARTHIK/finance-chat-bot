---
name: fact_ap_invoices
schema: gold
layer: gold
domain: ap
type: view
status: active
purpose: Combines vendor invoices from invoice headers and journals with due dates; status and amounts.
grain: one row per invoice source record
primary_key:
- LEGAL_ENTITY
- INVOICE
- SOURCE_TYPE
entity_column: LEGAL_ENTITY
period_columns:
- INVOICE_DATE
- DUE_DATE
- PAYMENT_DATE
pii_columns: []
synonyms: []
built_from:
- fact_vendor_invoice_headers
- fact_vendor_invoice_lines
- fact_vendor_invoice_journal_headers
- fact_vendor_invoice_journal_lines
- fact_kpmg_vend_payment_bi_vend_trans_open
known_issues: []
proposed_fields: []
reviewed: false
---

# fact_ap_invoices

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `INVOICE` | string |  |  | `INVOICE` |
| `SUPPLIER` | string |  |  | `SUPPLIER` |
| `AMOUNT` | string |  |  | `AMOUNT` |
| `JOURNAL_ID` | string |  |  | `JOURNAL_ID` |
| `SOURCE_TYPE` | string |  |  | `SOURCE_TYPE` |
| `STATUS` | string |  |  | `STATUS` |
| `INVOICE_DATE` | date |  |  | `INVOICE_DATE` |
| `DUE_DATE` | string |  |  | `DUE_DATE` |
| `PAYMENT_DATE` | date |  |  | `PAYMENT_DATE` |
| `AGE` | int |  |  | `AGE` |
| `CATEGORY` | string |  |  | `CATEGORY` |
| `PO_NUMBER` | string |  |  | `PO_NUMBER` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Values

**SOURCE_TYPE**
- `JOURNAL`
- `HEADER`

**STATUS**
- `Ready For Payment`
- `Awaiting Processing`
- `Pending Approval`
- `Approved`
- `MATCHED`
- `Paid`

**PAYMENT_DATE**
- `None`

**CATEGORY**
- `NA`
- `Office Rent`
- `Building`
- `Computer/Laptop`
- `Furniture`

**PO_NUMBER**
- `NA`
- `None`
- `100-000059`
- `100-000057`
- `100-000058`

## Empty columns

Empty in every row: `PAYMENT_DATE`. Do not filter or group on them.
