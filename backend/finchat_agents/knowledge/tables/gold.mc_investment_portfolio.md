---
name: mc_investment_portfolio
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Shows investment portfolio holdings and their recorded value.
grain: one row per company and main account
primary_key:
- COMPANY
- MAIN_ACCOUNT_ID
entity_column: COMPANY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- fact_kpmg_general_journal_account_entries
- dim_main_accounts
known_issues:
- code: duplicates
  note: 81 exact duplicate rows in the latest export (88.0%). Check duplicates at the grain before counting or summing; warn
    the user.
proposed_fields: []
reviewed: false
---

# mc_investment_portfolio

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `HOLDING` | string |  |  | `HOLDING` |
| `COMPANY` | string |  |  | `COMPANY` |
| `MAIN_ACCOUNT_CATEGORY` | string |  |  | `MAIN_ACCOUNT_CATEGORY` |
| `VALUE` | decimal |  |  | `VALUE` |
| `MAIN_ACCOUNT_ID` | string |  |  | `MAIN_ACCOUNT_ID` |

## Values

**HOLDING**
- `Mutual Funds (Long Term)`
- `Equity (Investment)`
- `Bonds - Premium`
- `Bonds - Market Val Adj`
- `Bonds - State Account MI`
- `WF - Corp Sweep`
- `Intercompany - Investments in affiliates`
- `Fixed Deposit (Long Term)`

**MAIN_ACCOUNT_CATEGORY**
- `Long Term Investments`

**VALUE**
- `41147`
- `45563`
- `32230`
- `160552`
- `39599`
- `20`
- `46265`
- `-207242.23`
- `63746`
- `37929`
- `52010`

**MAIN_ACCOUNT_ID**
- `103803`
- `103703`
- `131300`
- `131400`
- `103303`
- `131623`
- `146200`
- `103300`
