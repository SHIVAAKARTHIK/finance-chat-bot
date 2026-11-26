---
name: dim_main_accounts
schema: silver
layer: silver
domain: gl
type: table
status: active
purpose: 'Chart of accounts: main accounts with type and name.'
grain: one row per MAIN_ACCOUNT_REC_ID (one main account in a chart)
primary_key:
- MAIN_ACCOUNT_REC_ID
entity_column: null
period_columns: []
pii_columns:
- USER_NAME
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: SRU_CODE all null
proposed_fields:
- grain
- primary_key
reviewed: false
---

# dim_main_accounts

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `CHART_OF_ACCOUNTS` | string |  |  | `CHART_OF_ACCOUNTS` |
| `MAIN_ACCOUNT_ID` | string |  |  | `MAIN_ACCOUNT_ID` |
| `MAIN_ACCOUNT_REC_ID` | string |  |  | `MAIN_ACCOUNT_REC_ID` |
| `SRU_CODE` | string |  |  | `SRU_CODE` |
| `MAIN_ACCOUNT_TYPE` | string |  |  | `MAIN_ACCOUNT_TYPE` |
| `NAME` | string |  |  | `NAME` |
| `REPORTING_EXCHANGE_ADJUSTMENT_RATE_TYPE` | string |  |  | `REPORTING_EXCHANGE_ADJUSTMENT_RATE_TYPE` |
| `USER_NAME` | string |  |  | `USER_NAME` |
| `CLOSING` | string |  |  | `CLOSING` |
| `ACCOUNT_CATEGORY_DESCRIPTION` | string |  |  | `ACCOUNT_CATEGORY_DESCRIPTION` |
| `FOREIGN_CURRENCY_REVALUATION` | string |  |  | `FOREIGN_CURRENCY_REVALUATION` |
| `INFLATION_ADJUSTMENT` | string |  |  | `INFLATION_ADJUSTMENT` |
| `OFFSET_ACCOUNT_DISPLAY_VALUE` | string |  |  | `OFFSET_ACCOUNT_DISPLAY_VALUE` |
| `PARENT_MAIN_ACCOUNT_ID` | string |  |  | `PARENT_MAIN_ACCOUNT_ID` |
| `FINANCIAL_REPORTING_CURRENCY_TRANSLATION_TYPE` | string |  |  | `FINANCIAL_REPORTING_CURRENCY_TRANSLATION_TYPE` |
| `DEFAULT_CURRENCY` | string |  |  | `DEFAULT_CURRENCY` |
| `DEBIT_CREDIT_DEFAULT` | string |  |  | `DEBIT_CREDIT_DEFAULT` |
| `ACTIVE_TO` | string |  |  | `ACTIVE_TO` |
| `MANDATORY_PAYMENT_REFERENCE` | string |  |  | `MANDATORY_PAYMENT_REFERENCE` |
| `MONETARY` | string |  |  | `MONETARY` |
| `BALANCE_CONTROL` | string |  |  | `BALANCE_CONTROL` |
| `OPENING_ACCOUNT_ID` | string |  |  | `OPENING_ACCOUNT_ID` |
| `VALIDATE_POSTING_TYPE` | string |  |  | `VALIDATE_POSTING_TYPE` |
| `REPOMO_TYPE` | string |  |  | `REPOMO_TYPE` |
| `EXCHANGE_ADJUSTMENT_RATE_TYPE` | string |  |  | `EXCHANGE_ADJUSTMENT_RATE_TYPE` |
| `IS_SUSPENDED` | string |  |  | `IS_SUSPENDED` |
| `ADJUSTMENT_METHOD` | string |  |  | `ADJUSTMENT_METHOD` |
| `POSTING_TYPE` | string |  |  | `POSTING_TYPE` |
| `CHART_OF_ACCOUNTS_REC_ID` | string |  |  | `CHART_OF_ACCOUNTS_REC_ID` |
| `VALIDATE_CURRENCY` | string |  |  | `VALIDATE_CURRENCY` |
| `MAIN_ACCOUNT_CATEGORY` | string |  |  | `MAIN_ACCOUNT_CATEGORY` |
| `REPORTING_ACCOUNT_TYPE` | string |  |  | `REPORTING_ACCOUNT_TYPE` |
| `FINANCIAL_REPORTING_EXCHANGE_RATE_TYPE` | string |  |  | `FINANCIAL_REPORTING_EXCHANGE_RATE_TYPE` |
| `DEFAULT_CONSOLIDATION_ACCOUNT` | string |  |  | `DEFAULT_CONSOLIDATION_ACCOUNT` |
| `DO_NOT_ALLOW_MANUAL_ENTRY` | string |  |  | `DO_NOT_ALLOW_MANUAL_ENTRY` |
| `DEBIT_CREDIT_REQUIREMENT` | string |  |  | `DEBIT_CREDIT_REQUIREMENT` |
| `VALIDATE_USER` | string |  |  | `VALIDATE_USER` |
| `ACTIVE_FROM` | string |  |  | `ACTIVE_FROM` |
| `NATURE_CODE_BR` | string |  |  | `NATURE_CODE_BR` |
| `INCOME_STATEMENT_CATEGORY` | string |  |  | `INCOME_STATEMENT_CATEGORY` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**CHART_OF_ACCOUNTS**
- `INSCOA`
- `Shared`
- `COA`
- `Rock_It`
- `HCOA`

**SRU_CODE**
- `None`

**MAIN_ACCOUNT_TYPE**
- `Asset`
- `Expense`
- `Liability`
- `Revenue`
- `Equity`
- `ProfitAndLoss`
- `BalanceSheet`
- `Total`

**REPORTING_EXCHANGE_ADJUSTMENT_RATE_TYPE**
- `None`

**CLOSING**
- `None`

**FOREIGN_CURRENCY_REVALUATION**
- `No`

**INFLATION_ADJUSTMENT**
- `No`

**OFFSET_ACCOUNT_DISPLAY_VALUE**
- `None`

**PARENT_MAIN_ACCOUNT_ID**
- `None`

**FINANCIAL_REPORTING_CURRENCY_TRANSLATION_TYPE**
- `WeightedAverage`

**DEFAULT_CURRENCY**
- `USD`
- `None`

**DEBIT_CREDIT_DEFAULT**
- `None`
- `Debit`
- `Credit`

**ACTIVE_TO**
- `1900-01-01 12:00:00.0000000 +00:00`

**MANDATORY_PAYMENT_REFERENCE**
- `No`

**MONETARY**
- `No`

**BALANCE_CONTROL**
- `None`

**OPENING_ACCOUNT_ID**
- `None`

**VALIDATE_POSTING_TYPE**
- `Optional`

**REPOMO_TYPE**
- `NotApplicable`

**EXCHANGE_ADJUSTMENT_RATE_TYPE**
- `None`

**IS_SUSPENDED**
- `No`

**ADJUSTMENT_METHOD**
- `None`

**POSTING_TYPE**
- `None`

**CHART_OF_ACCOUNTS_REC_ID**
- `5637147576`
- `5637144577`
- `5637145326`
- `5637146076`
- `5637146826`

**VALIDATE_CURRENCY**
- `Optional`

**REPORTING_ACCOUNT_TYPE**
- `None`

**FINANCIAL_REPORTING_EXCHANGE_RATE_TYPE**
- `None`

**DEFAULT_CONSOLIDATION_ACCOUNT**
- `None`

**DO_NOT_ALLOW_MANUAL_ENTRY**
- `No`
- `Yes`

**DEBIT_CREDIT_REQUIREMENT**
- `None`

**VALIDATE_USER**
- `Optional`

**ACTIVE_FROM**
- `1900-01-01 12:00:00.0000000 +00:00`

**NATURE_CODE_BR**
- `None`
- `4`
- `1`
- `2`
- `3`

**INCOME_STATEMENT_CATEGORY**
- `None`

**SOURCE_FILE_NAME**
- `mainaccounts__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:41:35.174303+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:41:35.174303+00:00`

## Empty columns

Empty in every row: `SRU_CODE`, `REPORTING_EXCHANGE_ADJUSTMENT_RATE_TYPE`, `USER_NAME`, `OFFSET_ACCOUNT_DISPLAY_VALUE`, `PARENT_MAIN_ACCOUNT_ID`, `OPENING_ACCOUNT_ID`, `EXCHANGE_ADJUSTMENT_RATE_TYPE`, `FINANCIAL_REPORTING_EXCHANGE_RATE_TYPE`, `DEFAULT_CONSOLIDATION_ACCOUNT`, `INCOME_STATEMENT_CATEGORY`. Do not filter or group on them.
