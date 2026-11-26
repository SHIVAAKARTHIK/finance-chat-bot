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
- `Receivables overview`
- `Overdue`
- `Early payment discounts`

**KPI**
- `Invoice Count`
- `Overdue`
- `Total receivables`
- `Overdue value`
- `Early payment discounts value`

**Amount**
- `1000`
- `None`

**Count**
- `1`
