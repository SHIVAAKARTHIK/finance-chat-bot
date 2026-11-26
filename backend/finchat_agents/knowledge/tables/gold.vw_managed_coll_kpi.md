---
name: vw_managed_coll_kpi
schema: gold
layer: gold
domain: ar
type: view
status: broken
purpose: Summarizes receivables; overdue invoices and early-payment discounts.
grain: one row per section and KPI
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
broken_error: the profiling query failed in the catalog export (no row count); the error text is not in the workbook
---

# vw_managed_coll_kpi

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Section` | string |  |  | `Section` |
| `KPI` | string |  |  | `KPI` |
| `Amount` | double |  |  | `Amount` |
| `Count` | long |  |  | `Count` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
