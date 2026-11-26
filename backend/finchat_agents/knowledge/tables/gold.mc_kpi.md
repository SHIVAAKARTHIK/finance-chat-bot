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
- `Liquidity`
- `Actual Cash Balances By Bank Ac`
- `Investment Portfolio`

**KPI**
- `Current ratio`
- `Liquid asset %`
- `Quick ratio`
- `13-week low`
- `Change today`
- `Actual cash`
- `Liquid assets`
- `Portfolio value`
- `Invested this month`

**AMOUNT**
- `None`
- `0`
- `5821852.77`
- `1800000`
- `5574243.45`
- `561460.67`
- `432446.86`
- `-0.58`
- `-0.48`
- `33490614`
- `3.64`
