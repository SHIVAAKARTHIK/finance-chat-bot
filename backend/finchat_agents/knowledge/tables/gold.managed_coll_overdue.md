---
name: managed_coll_overdue
schema: gold
layer: gold
domain: ar
type: view
status: active
purpose: Lists overdue customer invoices and collection follow-up details.
grain: one row per INVOICE_NUMBER (one overdue invoice)
primary_key:
- INVOICE_NUMBER
entity_column: LEGAL_ENTITY
period_columns:
- INVOICE_DATE
- DUE_DATE
pii_columns:
- EMAIL
synonyms: []
built_from:
- fact_cust_trans_opens
- fact_cust_transactions
- fact_cust_table_bi_entities
known_issues: []
row_count: 1
proposed_fields:
- grain
- primary_key
reviewed: false
---

# managed_coll_overdue

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `REFERENCE` | string |  |  | `REFERENCE` |
| `CUSTOMER` | string |  |  | `CUSTOMER` |
| `INVOICE_NUMBER` | string |  |  | `INVOICE_NUMBER` |
| `AMOUNT` | string |  |  | `AMOUNT` |
| `INVOICE_DATE` | date |  |  | `INVOICE_DATE` |
| `DUE_DATE` | date |  |  | `DUE_DATE` |
| `AGING` | string |  |  | `AGING` |
| `ACTION` | string |  |  | `ACTION` |
| `EMAIL` | string |  |  | `EMAIL` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Values

**REFERENCE**
- `100-000001`: 1 rows

**CUSTOMER**
- `None`: 1 rows

**INVOICE_NUMBER**
- `100-000003`: 1 rows

**AMOUNT**
- `1000`: 1 rows

**INVOICE_DATE**
- `2026-09-26 00:00:00`: 1 rows

**DUE_DATE**
- `2026-10-26 00:00:00`: 1 rows

**AGING**
- `25 days overdue`: 1 rows

**ACTION**
- `Reminder 1`: 1 rows

## Profile

Rows in the latest export: 1.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `REFERENCE` | STRING | 1 | 0 | 100-000001 | 100-000001 |
| `CUSTOMER` | STRING | 0 | 1 |  |  |
| `INVOICE_NUMBER` | STRING | 1 | 0 | 100-000003 | 100-000003 |
| `AMOUNT` | STRING | 1 | 0 | 1000 | 1000 |
| `INVOICE_DATE` | DATE | 1 | 0 | 2026-09-26 00:00:00 | 2026-09-26 00:00:00 |
| `DUE_DATE` | DATE | 1 | 0 | 2026-10-26 00:00:00 | 2026-10-26 00:00:00 |
| `AGING` | STRING | 1 | 0 | 25 days overdue | 25 days overdue |
| `ACTION` | STRING | 1 | 0 | Reminder 1 | Reminder 1 |
| `EMAIL` | STRING | 1 | 0 |  |  |
| `LEGAL_ENTITY` | STRING | 1 | 0 |  |  |

## Sample rows

| REFERENCE | CUSTOMER | INVOICE_NUMBER | AMOUNT | INVOICE_DATE | DUE_DATE | AGING | ACTION | EMAIL |
|---|---|---|---|---|---|---|---|---|
| 100-000001 | NULL | 100-000003 | 1000 | 2026-09-26 00:00:00 | 2026-10-26 00:00:00 | 25 days overdue | Reminder 1 | <masked> |
