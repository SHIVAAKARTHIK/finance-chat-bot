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
row_count: 92
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
- `Mutual Funds (Long Term)`: 22 rows
- `Equity (Investment)`: 22 rows
- `Bonds - Premium`: 22 rows
- `Bonds - Market Val Adj`: 22 rows
- `Bonds - State Account MI`: 1 rows
- `WF - Corp Sweep`: 1 rows
- `Intercompany - Investments in affiliates`: 1 rows
- `Fixed Deposit (Long Term)`: 1 rows

**MAIN_ACCOUNT_CATEGORY**
- `Long Term Investments`: 92 rows

**VALUE**
- `41147`: 22 rows
- `45563`: 21 rows
- `32230`: 21 rows
- `160552`: 20 rows
- `39599`: 2 rows
- `20`: 1 rows
- `46265`: 1 rows
- `-207242.23`: 1 rows
- `63746`: 1 rows
- `37929`: 1 rows
- `52010`: 1 rows

**MAIN_ACCOUNT_ID**
- `103803`: 22 rows
- `103703`: 22 rows
- `131300`: 22 rows
- `131400`: 22 rows
- `103303`: 1 rows
- `131623`: 1 rows
- `146200`: 1 rows
- `103300`: 1 rows

## Profile

Rows in the latest export: 92.
Exact duplicate rows: 81.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `HOLDING` | STRING | 8 | 0 | Bonds - Market Val Adj | WF - Corp Sweep |
| `COMPANY` | STRING | 1 | 0 |  |  |
| `MAIN_ACCOUNT_CATEGORY` | STRING | 1 | 0 | Long Term Investments | Long Term Investments |
| `VALUE` | DECIMAL | 11 | 0 | -207242.23 | 160552 |
| `MAIN_ACCOUNT_ID` | STRING | 8 | 0 | 103300 | 146200 |

## Sample rows

| HOLDING | MAIN_ACCOUNT_CATEGORY | VALUE | MAIN_ACCOUNT_ID |
|---|---|---|---|
| WF - Corp Sweep | Long Term Investments | 37929 | 103300 |
| Fixed Deposit (Long Term) | Long Term Investments | 46265 | 103303 |
| Mutual Funds (Long Term) | Long Term Investments | -207242.23 | 103703 |
| Equity (Investment) | Long Term Investments | 39599 | 103803 |
| Bonds - Premium | Long Term Investments | 63746 | 131300 |
