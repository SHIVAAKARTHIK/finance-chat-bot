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
row_count: 45
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
- `Short Term Bonds - FL State Deposits`: 44 rows
- `Bonds - State Acct SET1`: 1 rows

**MAIN_ACCOUNT_ID**
- `121610`: 44 rows
- `131623`: 1 rows

**CATEGORY**
- `Short Term Investments`: 45 rows

**VALUE**
- `830000`: 40 rows
- `41303`: 2 rows
- `77999`: 2 rows
- `52010`: 1 rows

## Profile

Rows in the latest export: 45.
Exact duplicate rows: 41.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ASSET` | STRING | 2 | 0 | Bonds - State Acct SET1 | Short Term Bonds - FL State Deposits |
| `MAIN_ACCOUNT_ID` | STRING | 2 | 0 | 121610 | 131623 |
| `COMPANY` | STRING | 1 | 0 |  |  |
| `CATEGORY` | STRING | 1 | 0 | Short Term Investments | Short Term Investments |
| `VALUE` | DECIMAL | 4 | 0 | 41303 | 830000 |

## Sample rows

| ASSET | MAIN_ACCOUNT_ID | CATEGORY | VALUE |
|---|---|---|---|
| Short Term Bonds - FL State Deposits | 121610 | Short Term Investments | 77999 |
| Bonds - State Acct SET1 | 131623 | Short Term Investments | 52010 |
| Short Term Bonds - FL State Deposits | 121610 | Short Term Investments | 41303 |
| Short Term Bonds - FL State Deposits | 121610 | Short Term Investments | 830000 |
| Short Term Bonds - FL State Deposits | 121610 | Short Term Investments | 830000 |
