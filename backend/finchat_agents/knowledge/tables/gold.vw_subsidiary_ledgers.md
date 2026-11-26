---
name: vw_subsidiary_ledgers
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Shows entity-level subsidiary ledger totals for assets; liabilities; equity; revenue and expenses.
grain: one row per legal entity and reporting period
primary_key:
- LEGAL_ENTITY
- NAME
entity_column: LEGAL_ENTITY
period_columns:
- DUE_DATE
pii_columns: []
synonyms: []
built_from: []
known_issues: []
proposed_fields: []
reviewed: false
---

# vw_subsidiary_ledgers

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `ENTITY_NAME` | string |  |  | `ENTITY_NAME` |
| `DUE_DATE` | date |  |  | `DUE_DATE` |
| `NAME` | string |  |  | `NAME` |
| `STATUS` | string |  |  | `STATUS` |
| `TOTAL_ASSET` | double |  |  | `TOTAL_ASSET` |
| `TOTAL_LIABILITIES` | double |  |  | `TOTAL_LIABILITIES` |
| `TOTAL_EQUITY` | double |  |  | `TOTAL_EQUITY` |
| `TOTAL_REVENUE` | double |  |  | `TOTAL_REVENUE` |
| `TOTAL_EXPENSES` | double |  |  | `TOTAL_EXPENSES` |

## Values

**DUE_DATE**
- `2026-11-11 00:00:00`

**NAME**
- `Period 10`

**STATUS**
- `Open`

**TOTAL_ASSET**
- `None`
- `136088672.4`

**TOTAL_LIABILITIES**
- `None`
- `-103910859.8`

**TOTAL_EQUITY**
- `None`
- `-1880270.17`

**TOTAL_REVENUE**
- `None`
- `-63540340.98`

**TOTAL_EXPENSES**
- `None`
- `64172478.6`
