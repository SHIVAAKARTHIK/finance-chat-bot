---
name: mc_liquidity
schema: gold
layer: gold
domain: cash
type: view
status: active
purpose: Shows liquid investment balances by asset and account.
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
  note: 41 exact duplicate rows in the latest export (91.1%). Check duplicates at the grain before counting or summing; warn
    the user.
proposed_fields: []
reviewed: false
---

# mc_liquidity

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ASSET` | string |  |  | `ASSET` |
| `MAIN_ACCOUNT_ID` | string |  |  | `MAIN_ACCOUNT_ID` |
| `COMPANY` | string |  |  | `COMPANY` |
| `CATEGORY` | string |  |  | `CATEGORY` |
| `VALUE` | decimal |  |  | `VALUE` |

## Values

**ASSET**
- `Short Term Bonds - FL State Deposits`
- `Bonds - State Acct SET1`

**MAIN_ACCOUNT_ID**
- `121610`
- `131623`

**CATEGORY**
- `Short Term Investments`

**VALUE**
- `830000`
- `41303`
- `77999`
- `52010`
