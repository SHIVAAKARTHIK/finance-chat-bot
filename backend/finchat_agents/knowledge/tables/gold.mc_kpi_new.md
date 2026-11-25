---
name: mc_kpi_new
schema: gold
layer: gold
domain: cash
type: view
status: active
purpose: Displays cash and liquidity KPIs in the newer KPI format.
grain: one row per section and KPI
primary_key:
- SECTION
- KPI
entity_column: null
period_columns: []
pii_columns: []
synonyms: []
built_from:
- fact_ledger_journal_lines
- fact_kpmg_general_journal_account_entries
- dim_bank_account_table_bi_entities
- dim_main_accounts
known_issues: []
row_count: 8
proposed_fields: []
reviewed: false
---

# mc_kpi_new

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `SECTION` | string |  |  | `SECTION` |
| `KPI` | string |  |  | `KPI` |
| `AMOUNT` | decimal |  |  | `AMOUNT` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Values

**SECTION**
- `Liquidity`: 3 rows
- `Investment Portfolio`: 3 rows
- `Actual Cash Balances By Bank Ac`: 2 rows

**KPI**
- `Actual cash`: 1 rows
- `13-week low`: 1 rows
- `Liquid assets`: 1 rows
- `Current ratio`: 1 rows
- `Quick ratio`: 1 rows
- `Portfolio value`: 1 rows
- `Invested this month`: 1 rows
- `Liquid asset %`: 1 rows

**AMOUNT**
- `0`: 2 rows
- `5821852.77`: 2 rows
- `33490614`: 1 rows
- `1.28`: 1 rows
- `1.15`: 1 rows
- `0.8519082304`: 1 rows

## Profile

Rows in the latest export: 8.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `SECTION` | STRING | 3 | 0 | Actual Cash Balances By Bank Ac | Liquidity |
| `KPI` | STRING | 8 | 0 | 13-week low | Quick ratio |
| `AMOUNT` | DECIMAL | 6 | 0 | 0 | 33490614 |
| `LEGAL_ENTITY` | STRING | 0 | 8 |  |  |

## Sample rows

| SECTION | KPI | AMOUNT |
|---|---|---|
| Actual Cash Balances By Bank Ac | Actual cash | 0 |
| Actual Cash Balances By Bank Ac | 13-week low | 0 |
| Liquidity | Liquid assets | 33490614 |
| Liquidity | Current ratio | 1.28 |
| Liquidity | Quick ratio | 1.15 |
