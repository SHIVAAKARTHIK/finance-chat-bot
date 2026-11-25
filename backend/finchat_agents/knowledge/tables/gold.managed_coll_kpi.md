---
name: managed_coll_kpi
schema: gold
layer: gold
domain: ar
type: view
status: active
purpose: Summarizes receivables; overdue invoices and early-payment discounts by legal entity.
grain: one row per section; KPI and legal entity
primary_key:
- Section
- KPI
- LEGAL_ENTITY
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- fact_cust_trans_opens
- fact_cust_transactions
- fact_cash_discounts
known_issues: []
row_count: 6
proposed_fields: []
reviewed: false
---

# managed_coll_kpi

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Section` | string |  |  | `Section` |
| `KPI` | string |  |  | `KPI` |
| `Amount` | double |  |  | `Amount` |
| `Count` | long |  |  | `Count` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Values

**Section**
- `Receivables overview`: 2 rows
- `Overdue`: 2 rows
- `Early payment discounts`: 2 rows

**KPI**
- `Invoice Count`: 2 rows
- `Overdue`: 1 rows
- `Total receivables`: 1 rows
- `Overdue value`: 1 rows
- `Early payment discounts value`: 1 rows

**Amount**
- `1000`: 4 rows
- `None`: 2 rows

**Count**
- `1`: 6 rows

## Profile

Rows in the latest export: 6.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Section` | STRING | 3 | 0 | Early payment discounts | Receivables overview |
| `KPI` | STRING | 5 | 0 | Early payment discounts value | Total receivables |
| `Amount` | DOUBLE | 1 | 2 | 1000 | 1000 |
| `Count` | LONG | 1 | 0 | 1 | 1 |
| `LEGAL_ENTITY` | STRING | 1 | 0 |  |  |

## Sample rows

| Section | KPI | Amount | Count |
|---|---|---|---|
| Receivables overview | Total receivables | 1000 | 1 |
| Receivables overview | Overdue | 1000 | 1 |
| Overdue | Overdue value | 1000 | 1 |
| Overdue | Invoice Count | NULL | 1 |
| Early payment discounts | Early payment discounts value | 1000 | 1 |
