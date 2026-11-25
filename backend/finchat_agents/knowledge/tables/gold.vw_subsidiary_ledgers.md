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
row_count: 7
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
- `2026-11-11 00:00:00`: 7 rows

**NAME**
- `Period 10`: 7 rows

**STATUS**
- `Open`: 7 rows

**TOTAL_ASSET**
- `None`: 6 rows
- `136088672.4`: 1 rows

**TOTAL_LIABILITIES**
- `None`: 6 rows
- `-103910859.8`: 1 rows

**TOTAL_EQUITY**
- `None`: 6 rows
- `-1880270.17`: 1 rows

**TOTAL_REVENUE**
- `None`: 6 rows
- `-63540340.98`: 1 rows

**TOTAL_EXPENSES**
- `None`: 6 rows
- `64172478.6`: 1 rows

## Profile

Rows in the latest export: 7.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `LEGAL_ENTITY` | STRING | 7 | 0 |  |  |
| `ENTITY_NAME` | STRING | 7 | 0 |  |  |
| `DUE_DATE` | DATE | 1 | 0 | 2026-11-11 00:00:00 | 2026-11-11 00:00:00 |
| `NAME` | STRING | 1 | 0 | Period 10 | Period 10 |
| `STATUS` | STRING | 1 | 0 | Open | Open |
| `TOTAL_ASSET` | DOUBLE | 1 | 6 | 136088672.38 | 136088672.38 |
| `TOTAL_LIABILITIES` | DOUBLE | 1 | 6 | -103910859.83 | -103910859.83 |
| `TOTAL_EQUITY` | DOUBLE | 1 | 6 | -1880270.16999999 | -1880270.16999999 |
| `TOTAL_REVENUE` | DOUBLE | 1 | 6 | -63540340.98 | -63540340.98 |
| `TOTAL_EXPENSES` | DOUBLE | 1 | 6 | 64172478.5999999 | 64172478.5999999 |

## Sample rows

| DUE_DATE | NAME | STATUS | TOTAL_ASSET | TOTAL_LIABILITIES | TOTAL_EQUITY | TOTAL_REVENUE | TOTAL_EXPENSES |
|---|---|---|---|---|---|---|---|
| 2026-11-11 00:00:00 | Period 10 | Open | 136088672.38 | -103910859.83 | -1880270.16999999 | -63540340.98 | 64172478.5999999 |
| 2026-11-11 00:00:00 | Period 10 | Open | NULL | NULL | NULL | NULL | NULL |
| 2026-11-11 00:00:00 | Period 10 | Open | NULL | NULL | NULL | NULL | NULL |
| 2026-11-11 00:00:00 | Period 10 | Open | NULL | NULL | NULL | NULL | NULL |
| 2026-11-11 00:00:00 | Period 10 | Open | NULL | NULL | NULL | NULL | NULL |
