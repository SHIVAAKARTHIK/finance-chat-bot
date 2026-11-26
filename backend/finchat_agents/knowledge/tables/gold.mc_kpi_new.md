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
- `Liquidity`
- `Investment Portfolio`
- `Actual Cash Balances By Bank Ac`

**KPI**
- `Actual cash`
- `13-week low`
- `Liquid assets`
- `Current ratio`
- `Quick ratio`
- `Portfolio value`
- `Invested this month`
- `Liquid asset %`

**AMOUNT**
- `0`
- `5821852.77`
- `33490614`
- `1.28`
- `1.15`
- `0.8519082304`

## Empty columns

Empty in every row: `LEGAL_ENTITY`. Do not filter or group on them.
