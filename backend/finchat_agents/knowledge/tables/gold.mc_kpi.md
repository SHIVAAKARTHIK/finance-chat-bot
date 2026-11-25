---
name: mc_kpi
schema: gold
layer: gold
domain: cash
type: view
status: active
purpose: Displays cash; liquidity and investment portfolio KPIs by legal entity.
grain: one row per section; KPI and legal entity
primary_key:
- SECTION
- KPI
- LEGAL_ENTITY
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- fact_ledger_journal_lines
- fact_kpmg_general_journal_account_entries
- dim_bank_account_table_bi_entities
- dim_main_accounts
known_issues: []
row_count: 36
proposed_fields: []
reviewed: false
---

# mc_kpi

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `SECTION` | string |  |  | `SECTION` |
| `KPI` | string |  |  | `KPI` |
| `AMOUNT` | decimal |  |  | `AMOUNT` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Values

**SECTION**
- `Liquidity`: 15 rows
- `Actual Cash Balances By Bank Ac`: 12 rows
- `Investment Portfolio`: 9 rows

**KPI**
- `Current ratio`: 7 rows
- `Liquid asset %`: 7 rows
- `Quick ratio`: 7 rows
- `13-week low`: 4 rows
- `Change today`: 4 rows
- `Actual cash`: 4 rows
- `Liquid assets`: 1 rows
- `Portfolio value`: 1 rows
- `Invested this month`: 1 rows

**AMOUNT**
- `None`: 18 rows
- `0`: 4 rows
- `5821852.77`: 2 rows
- `1800000`: 2 rows
- `5574243.45`: 2 rows
- `561460.67`: 2 rows
- `432446.86`: 2 rows
- `-0.58`: 1 rows
- `-0.48`: 1 rows
- `33490614`: 1 rows
- `3.64`: 1 rows

## Profile

Rows in the latest export: 36.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `SECTION` | STRING | 3 | 0 | Actual Cash Balances By Bank Ac | Liquidity |
| `KPI` | STRING | 9 | 0 | 13-week low | Quick ratio |
| `AMOUNT` | DECIMAL | 10 | 18 | -0.58 | 33490614 |
| `LEGAL_ENTITY` | STRING | 7 | 0 |  |  |

## Sample rows

| SECTION | KPI | AMOUNT |
|---|---|---|
| Actual Cash Balances By Bank Ac | Actual cash | 561460.67 |
| Actual Cash Balances By Bank Ac | Actual cash | 5574243.45 |
| Actual Cash Balances By Bank Ac | Actual cash | 432446.86 |
| Actual Cash Balances By Bank Ac | Change today | 0 |
| Actual Cash Balances By Bank Ac | Change today | 0 |
