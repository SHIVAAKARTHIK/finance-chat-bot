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
- `100-000001`

**CUSTOMER**
- `None`

**INVOICE_NUMBER**
- `100-000003`

**AMOUNT**
- `1000`

**INVOICE_DATE**
- `2026-09-26 00:00:00`

**DUE_DATE**
- `2026-10-26 00:00:00`

**AGING**
- `25 days overdue`

**ACTION**
- `Reminder 1`

## Empty columns

Empty in every row: `CUSTOMER`. Do not filter or group on them.
