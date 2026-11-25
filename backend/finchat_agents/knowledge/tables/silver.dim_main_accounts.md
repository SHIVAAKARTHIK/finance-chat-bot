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
row_count: 1867
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
- `INSCOA`: 574 rows
- `Shared`: 555 rows
- `COA`: 541 rows
- `Rock_It`: 163 rows
- `HCOA`: 34 rows

**SRU_CODE**
- `None`: 1867 rows

**MAIN_ACCOUNT_TYPE**
- `Asset`: 657 rows
- `Expense`: 553 rows
- `Liability`: 284 rows
- `Revenue`: 263 rows
- `Equity`: 99 rows
- `ProfitAndLoss`: 9 rows
- `BalanceSheet`: 1 rows
- `Total`: 1 rows

**REPORTING_EXCHANGE_ADJUSTMENT_RATE_TYPE**
- `None`: 1867 rows

**CLOSING**
- `None`: 1867 rows

**FOREIGN_CURRENCY_REVALUATION**
- `No`: 1867 rows

**INFLATION_ADJUSTMENT**
- `No`: 1867 rows

**OFFSET_ACCOUNT_DISPLAY_VALUE**
- `None`: 1867 rows

**PARENT_MAIN_ACCOUNT_ID**
- `None`: 1867 rows

**FINANCIAL_REPORTING_CURRENCY_TRANSLATION_TYPE**
- `WeightedAverage`: 1867 rows

**DEFAULT_CURRENCY**
- `USD`: 1806 rows
- `None`: 61 rows

**DEBIT_CREDIT_DEFAULT**
- `None`: 1262 rows
- `Debit`: 397 rows
- `Credit`: 208 rows

**ACTIVE_TO**
- `1900-01-01 12:00:00.0000000 +00:00`: 1867 rows

**MANDATORY_PAYMENT_REFERENCE**
- `No`: 1867 rows

**MONETARY**
- `No`: 1867 rows

**BALANCE_CONTROL**
- `None`: 1867 rows

**OPENING_ACCOUNT_ID**
- `None`: 1867 rows

**VALIDATE_POSTING_TYPE**
- `Optional`: 1867 rows

**REPOMO_TYPE**
- `NotApplicable`: 1867 rows

**EXCHANGE_ADJUSTMENT_RATE_TYPE**
- `None`: 1867 rows

**IS_SUSPENDED**
- `No`: 1867 rows

**ADJUSTMENT_METHOD**
- `None`: 1867 rows

**POSTING_TYPE**
- `None`: 1867 rows

**CHART_OF_ACCOUNTS_REC_ID**
- `5637147576`: 574 rows
- `5637144577`: 555 rows
- `5637145326`: 541 rows
- `5637146076`: 163 rows
- `5637146826`: 34 rows

**VALIDATE_CURRENCY**
- `Optional`: 1867 rows

**REPORTING_ACCOUNT_TYPE**
- `None`: 1867 rows

**FINANCIAL_REPORTING_EXCHANGE_RATE_TYPE**
- `None`: 1867 rows

**DEFAULT_CONSOLIDATION_ACCOUNT**
- `None`: 1867 rows

**DO_NOT_ALLOW_MANUAL_ENTRY**
- `No`: 1865 rows
- `Yes`: 2 rows

**DEBIT_CREDIT_REQUIREMENT**
- `None`: 1867 rows

**VALIDATE_USER**
- `Optional`: 1867 rows

**ACTIVE_FROM**
- `1900-01-01 12:00:00.0000000 +00:00`: 1867 rows

**NATURE_CODE_BR**
- `None`: 1337 rows
- `4`: 222 rows
- `1`: 198 rows
- `2`: 108 rows
- `3`: 2 rows

**INCOME_STATEMENT_CATEGORY**
- `None`: 1867 rows

**SOURCE_FILE_NAME**
- `mainaccounts__20261116_105417.csv`: 1867 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:41:35.174303+00:00`: 1867 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:41:35.174303+00:00`: 1867 rows

## Profile

Rows in the latest export: 1867.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `CHART_OF_ACCOUNTS` | STRING | 5 | 0 | COA | Shared |
| `MAIN_ACCOUNT_ID` | STRING | 710 | 0 | 100004 | 999999 |
| `MAIN_ACCOUNT_REC_ID` | STRING | 1764 | 0 | 5637144576 | 5637160331 |
| `SRU_CODE` | STRING | 0 | 1867 |  |  |
| `MAIN_ACCOUNT_TYPE` | STRING | 8 | 0 | Asset | Total |
| `NAME` | STRING | 983 | 0 | (Loss)/Gain on Fixed Asset | WrittenPremiumOffset |
| `REPORTING_EXCHANGE_ADJUSTMENT_RATE_TYPE` | STRING | 0 | 1867 |  |  |
| `USER_NAME` | STRING | 0 | 1867 |  |  |
| `CLOSING` | STRING | 1 | 0 | None | None |
| `ACCOUNT_CATEGORY_DESCRIPTION` | STRING | 173 | 723 | AIF Commissions | Written premium |
| `FOREIGN_CURRENCY_REVALUATION` | STRING | 1 | 0 | No | No |
| `INFLATION_ADJUSTMENT` | STRING | 1 | 0 | No | No |
| `OFFSET_ACCOUNT_DISPLAY_VALUE` | STRING | 0 | 1867 |  |  |
| `PARENT_MAIN_ACCOUNT_ID` | STRING | 0 | 1867 |  |  |
| `FINANCIAL_REPORTING_CURRENCY_TRANSLATION_TYPE` | STRING | 1 | 0 | WeightedAverage | WeightedAverage |
| `DEFAULT_CURRENCY` | STRING | 1 | 61 | USD | USD |
| `DEBIT_CREDIT_DEFAULT` | STRING | 3 | 0 | Credit | None |
| `ACTIVE_TO` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `MANDATORY_PAYMENT_REFERENCE` | STRING | 1 | 0 | No | No |
| `MONETARY` | STRING | 1 | 0 | No | No |
| `BALANCE_CONTROL` | STRING | 1 | 0 | None | None |
| `OPENING_ACCOUNT_ID` | STRING | 0 | 1867 |  |  |
| `VALIDATE_POSTING_TYPE` | STRING | 1 | 0 | Optional | Optional |
| `REPOMO_TYPE` | STRING | 1 | 0 | NotApplicable | NotApplicable |
| `EXCHANGE_ADJUSTMENT_RATE_TYPE` | STRING | 0 | 1867 |  |  |
| `IS_SUSPENDED` | STRING | 1 | 0 | No | No |
| `ADJUSTMENT_METHOD` | STRING | 1 | 0 | None | None |
| `POSTING_TYPE` | STRING | 1 | 0 | None | None |
| `CHART_OF_ACCOUNTS_REC_ID` | STRING | 5 | 0 | 5637144577 | 5637147576 |
| `VALIDATE_CURRENCY` | STRING | 1 | 0 | Optional | Optional |
| `MAIN_ACCOUNT_CATEGORY` | STRING | 159 | 723 | AALOAN | WRIPREMGAOF |
| `REPORTING_ACCOUNT_TYPE` | STRING | 1 | 0 | None | None |
| `FINANCIAL_REPORTING_EXCHANGE_RATE_TYPE` | STRING | 0 | 1867 |  |  |
| `DEFAULT_CONSOLIDATION_ACCOUNT` | STRING | 0 | 1867 |  |  |
| `DO_NOT_ALLOW_MANUAL_ENTRY` | STRING | 2 | 0 | No | Yes |
| `DEBIT_CREDIT_REQUIREMENT` | STRING | 1 | 0 | None | None |
| `VALIDATE_USER` | STRING | 1 | 0 | Optional | Optional |
| `ACTIVE_FROM` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `NATURE_CODE_BR` | STRING | 4 | 1337 | 1 | 4 |
| `INCOME_STATEMENT_CATEGORY` | STRING | 0 | 1867 |  |  |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | mainaccounts__20261116_105417.csv | mainaccounts__20261116_105417.csv |
| `HASH_KEY` | STRING | 1907 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:41:35.174000 | 2026-11-16 11:41:35.174000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:41:35.174000 | 2026-11-16 11:41:35.174000 |

## Sample rows

| CHART_OF_ACCOUNTS | MAIN_ACCOUNT_ID | MAIN_ACCOUNT_REC_ID | SRU_CODE | MAIN_ACCOUNT_TYPE | NAME | REPORTING_EXCHANGE_ADJUSTMENT_RATE_TYPE | USER_NAME | CLOSING | ACCOUNT_CATEGORY_DESCRIPTION | FOREIGN_CURRENCY_REVALUATION | INFLATION_ADJUSTMENT | OFFSET_ACCOUNT_DISPLAY_VALUE | PARENT_MAIN_ACCOUNT_ID | FINANCIAL_REPORTING_CURRENCY_TRANSLATION_TYPE | DEFAULT_CURRENCY | DEBIT_CREDIT_DEFAULT | ACTIVE_TO | MANDATORY_PAYMENT_REFERENCE | MONETARY | BALANCE_CONTROL | OPENING_ACCOUNT_ID | VALIDATE_POSTING_TYPE | REPOMO_TYPE | EXCHANGE_ADJUSTMENT_RATE_TYPE | IS_SUSPENDED | ADJUSTMENT_METHOD | POSTING_TYPE | CHART_OF_ACCOUNTS_REC_ID | VALIDATE_CURRENCY | MAIN_ACCOUNT_CATEGORY | REPORTING_ACCOUNT_TYPE | FINANCIAL_REPORTING_EXCHANGE_RATE_TYPE | DEFAULT_CONSOLIDATION_ACCOUNT | DO_NOT_ALLOW_MANUAL_ENTRY | DEBIT_CREDIT_REQUIREMENT | VALIDATE_USER | ACTIVE_FROM | NATURE_CODE_BR | INCOME_STATEMENT_CATEGORY | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shared | 101106 | 5637144576 | NULL | Asset | BMO - Operating - TH Risk Management | NULL | <masked> | None | Cash and equivalents - fiduciary | No | No | NULL | NULL | WeightedAverage | USD | Debit | 1900-01-01 12:00:00.0000000 +00:00 | No | No | None | NULL | Optional | NotApplicable | NULL | No | None | None | 5637144577 | Optional | Cash - Fiduciary | None | NULL | NULL | No | None | Optional | 1900-01-01 12:00:00.0000000 +00:00 | 1 | NULL | mainaccounts__20261116_105417.csv | <masked> | 2026-11-16 11:41:35.174000 | <masked> | 2026-11-16 11:41:35.174000 |
| Shared | 101113 | 5637144577 | NULL | Asset | BMO - Operating | NULL | <masked> | None | Cash and short term investments | No | No | NULL | NULL | WeightedAverage | USD | Debit | 1900-01-01 12:00:00.0000000 +00:00 | No | No | None | NULL | Optional | NotApplicable | NULL | No | None | None | 5637144577 | Optional | CSTINV | None | NULL | NULL | No | None | Optional | 1900-01-01 12:00:00.0000000 +00:00 | 1 | NULL | mainaccounts__20261116_105417.csv | <masked> | 2026-11-16 11:41:35.174000 | <masked> | 2026-11-16 11:41:35.174000 |
| Shared | 101413 | 5637144578 | NULL | Asset | BMO - Claims ZBA - Omega | NULL | <masked> | None | Cash and short term investments | No | No | NULL | NULL | WeightedAverage | USD | Debit | 1900-01-01 12:00:00.0000000 +00:00 | No | No | None | NULL | Optional | NotApplicable | NULL | No | None | None | 5637144577 | Optional | CSTINV | None | NULL | NULL | No | None | Optional | 1900-01-01 12:00:00.0000000 +00:00 | 1 | NULL | mainaccounts__20261116_105417.csv | <masked> | 2026-11-16 11:41:35.174000 | <masked> | 2026-11-16 11:41:35.174000 |
| Shared | 101602 | 5637144579 | NULL | Asset | BMO - Trust - Exchange | NULL | <masked> | None | Cash and short term investments | No | No | NULL | NULL | WeightedAverage | USD | Debit | 1900-01-01 12:00:00.0000000 +00:00 | No | No | None | NULL | Optional | NotApplicable | NULL | No | None | None | 5637144577 | Optional | CSTINV | None | NULL | NULL | No | None | Optional | 1900-01-01 12:00:00.0000000 +00:00 | 1 | NULL | mainaccounts__20261116_105417.csv | <masked> | 2026-11-16 11:41:35.174000 | <masked> | 2026-11-16 11:41:35.174000 |
| Shared | 101604 | 5637144580 | NULL | Asset | BMO - Trust - TH Preferred | NULL | <masked> | None | Cash and short term investments | No | No | NULL | NULL | WeightedAverage | USD | Debit | 1900-01-01 12:00:00.0000000 +00:00 | No | No | None | NULL | Optional | NotApplicable | NULL | No | None | None | 5637144577 | Optional | CSTINV | None | NULL | NULL | No | None | Optional | 1900-01-01 12:00:00.0000000 +00:00 | 1 | NULL | mainaccounts__20261116_105417.csv | <masked> | 2026-11-16 11:41:35.174000 | <masked> | 2026-11-16 11:41:35.174000 |
