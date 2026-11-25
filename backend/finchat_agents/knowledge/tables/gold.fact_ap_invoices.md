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
row_count: 107
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
- `JOURNAL`: 102 rows
- `HEADER`: 5 rows

**STATUS**
- `Ready For Payment`: 63 rows
- `Awaiting Processing`: 29 rows
- `Pending Approval`: 6 rows
- `Approved`: 3 rows
- `MATCHED`: 3 rows
- `Paid`: 3 rows

**PAYMENT_DATE**
- `None`: 107 rows

**CATEGORY**
- `NA`: 102 rows
- `Office Rent`: 2 rows
- `Building`: 1 rows
- `Computer/Laptop`: 1 rows
- `Furniture`: 1 rows

**PO_NUMBER**
- `NA`: 102 rows
- `None`: 2 rows
- `100-000059`: 1 rows
- `100-000057`: 1 rows
- `100-000058`: 1 rows

## Profile

Rows in the latest export: 107.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `INVOICE` | STRING | 113 | 0 | INV-090 | Inv-059 |
| `SUPPLIER` | STRING | 63 | 0 | Accord Field Services | Workday Inc. |
| `AMOUNT` | STRING | 108 | 0 | 10050 | 9950 |
| `JOURNAL_ID` | STRING | 104 | 0 |  | 100-000119 |
| `SOURCE_TYPE` | STRING | 2 | 0 | HEADER | JOURNAL |
| `STATUS` | STRING | 6 | 0 | Approved | Ready For Payment |
| `INVOICE_DATE` | DATE | 109 | 0 | 2025-01-26 00:00:00 | 2026-11-09 00:00:00 |
| `DUE_DATE` | STRING | 109 | 0 | 2025-02-05 12:00:00.0000000 +00:00 | 2026-11-19 12:00:00.0000000 +00:00 |
| `PAYMENT_DATE` | DATE | 0 | 107 |  |  |
| `AGE` | INT | 99 | 0 | 11 | 663 |
| `CATEGORY` | STRING | 5 | 0 | Building | Office Rent |
| `PO_NUMBER` | STRING | 4 | 2 | 100-000057 | NA |
| `LEGAL_ENTITY` | STRING | 1 | 0 |  |  |

## Sample rows

| INVOICE | SUPPLIER | AMOUNT | JOURNAL_ID | SOURCE_TYPE | STATUS | INVOICE_DATE | DUE_DATE | PAYMENT_DATE | AGE | CATEGORY | PO_NUMBER |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Inv-057 | Workday Inc. | 7500 | NULL | HEADER | Pending Approval | 2026-01-01 00:00:00 | 2026-01-11 12:00:00.0000000 +00:00 | NULL | 323 | Building | 100-000057 |
| Inv-058 | ServiceNow Inc. | 7600 | NULL | HEADER | Pending Approval | 2026-01-02 00:00:00 | 2026-01-12 12:00:00.0000000 +00:00 | NULL | 322 | Computer/Laptop | 100-000058 |
| Inv-059 | VMware LLC | 7700 | NULL | HEADER | Pending Approval | 2026-01-06 00:00:00 | 2026-01-16 12:00:00.0000000 +00:00 | NULL | 318 | Furniture | 100-000059 |
| INV-090 | Evergreen Adjusting Services | 200 | NULL | HEADER | Pending Approval | 2026-11-09 00:00:00 | 2026-11-19 12:00:00.0000000 +00:00 | NULL | 11 | Office Rent | NULL |
| INV-091 | ShieldPro Claims Agency | 1200 | NULL | HEADER | Pending Approval | 2026-11-09 00:00:00 | 2026-11-19 12:00:00.0000000 +00:00 | NULL | 11 | Office Rent | NULL |
