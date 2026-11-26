---
name: vw_expense_analysis
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Expense analysis (5-series main accounts) from D365 general journal entries, enriched with Chart of Accounts description
  and expense category; line-level grain for Power BI
grain: one row per D365 GL journal line
primary_key:
- ENTRY_REC_ID
entity_column: LEGAL_ENTITY_CODE
period_columns:
- ACCOUNTING_DATE
- POSTING_YEAR
- POSTING_QUARTER
- POSTING_MONTH
- POSTING_YEAR_MONTH
pii_columns: []
synonyms: []
built_from:
- fact_kpmg_general_journal_account_entries
- dim_main_accounts
known_issues: []
proposed_fields: []
reviewed: false
---

# vw_expense_analysis

Expense analysis (5-series main accounts) from D365 general journal entries, enriched with Chart of Accounts description and expense category; line-level grain for Power BI

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ENTRY_REC_ID` | string |  |  | `ENTRY_REC_ID` |
| `LEGAL_ENTITY_CODE` | string |  |  | `LEGAL_ENTITY_CODE` |
| `LEGAL_ENTITY_NAME` | string |  |  | `LEGAL_ENTITY_NAME` |
| `LEDGER_NAME` | string |  |  | `LEDGER_NAME` |
| `POSTING_LAYER` | string |  |  | `POSTING_LAYER` |
| `ACCOUNTING_DATE` | date |  |  | `ACCOUNTING_DATE` |
| `POSTING_YEAR` | int |  |  | `POSTING_YEAR` |
| `POSTING_QUARTER` | int |  |  | `POSTING_QUARTER` |
| `POSTING_QUARTER_LABEL` | string |  |  | `POSTING_QUARTER_LABEL` |
| `POSTING_MONTH` | int |  |  | `POSTING_MONTH` |
| `POSTING_MONTH_NAME` | string |  |  | `POSTING_MONTH_NAME` |
| `POSTING_YEAR_MONTH` | string |  |  | `POSTING_YEAR_MONTH` |
| `POSTING_MONTH_START` | date |  |  | `POSTING_MONTH_START` |
| `DOCUMENT_DATE` | date |  |  | `DOCUMENT_DATE` |
| `MAIN_ACCOUNT` | string |  |  | `MAIN_ACCOUNT` |
| `ACCOUNT_DESCRIPTION` | string |  |  | `ACCOUNT_DESCRIPTION` |
| `ACCOUNT_LABEL` | string |  |  | `ACCOUNT_LABEL` |
| `EXPENSE_CATEGORY` | string |  |  | `EXPENSE_CATEGORY` |
| `EXPENSE_GROUP` | string |  |  | `EXPENSE_GROUP` |
| `EXPENSE_GROUP_SORT` | int |  |  | `EXPENSE_GROUP_SORT` |
| `BUSINESS_TYPE` | string |  |  | `BUSINESS_TYPE` |
| `MAIN_ACCOUNT_TYPE` | string |  |  | `MAIN_ACCOUNT_TYPE` |
| `DEBIT_CREDIT_DEFAULT` | string |  |  | `DEBIT_CREDIT_DEFAULT` |
| `COST_CENTER` | string |  |  | `COST_CENTER` |
| `PROFIT_CENTER` | string |  |  | `PROFIT_CENTER` |
| `BUSINESS_INDICATOR` | string |  |  | `BUSINESS_INDICATOR` |
| `LINE_OF_BUSINESS` | string |  |  | `LINE_OF_BUSINESS` |
| `LEDGER_ACCOUNT` | string |  |  | `LEDGER_ACCOUNT` |
| `JOURNAL_NUMBER` | string |  |  | `JOURNAL_NUMBER` |
| `VOUCHER` | string |  |  | `VOUCHER` |
| `DOCUMENT_NUMBER` | string |  |  | `DOCUMENT_NUMBER` |
| `LINE_DESCRIPTION` | string |  |  | `LINE_DESCRIPTION` |
| `JOURNAL_CATEGORY` | string |  |  | `JOURNAL_CATEGORY` |
| `POSTING_TYPE` | string |  |  | `POSTING_TYPE` |
| `SOURCE_SYSTEM` | string |  |  | `SOURCE_SYSTEM` |
| `IS_CREDIT` | string |  |  | `IS_CREDIT` |
| `IS_CORRECTION` | string |  |  | `IS_CORRECTION` |
| `TRANSACTION_CURRENCY_CODE` | string |  |  | `TRANSACTION_CURRENCY_CODE` |
| `EXPENSE_AMOUNT` | decimal |  |  | `EXPENSE_AMOUNT` |
| `DEBIT_AMOUNT` | decimal |  |  | `DEBIT_AMOUNT` |
| `CREDIT_AMOUNT` | decimal |  |  | `CREDIT_AMOUNT` |
| `REPORTING_CURRENCY_AMOUNT` | decimal |  |  | `REPORTING_CURRENCY_AMOUNT` |
| `TRANSACTION_CURRENCY_AMOUNT` | decimal |  |  | `TRANSACTION_CURRENCY_AMOUNT` |
| `QUANTITY` | decimal |  |  | `QUANTITY` |
| `LAST_REFRESHED` | timestamp |  |  | `LAST_REFRESHED` |

## Values

**LEDGER_NAME**
- `214`
- `100`
- `228`
- `299`
- `201`
- `236`
- `103`
- `208`
- `UK14`
- `233`
- `UK03`
- `UK17`
- `UK06`
- `UK07`
- `UK13`
- `238`
- `101`

**POSTING_LAYER**
- `Current`
- `Operations`

**POSTING_YEAR**
- `2025`
- `2026`
- `2024`

**POSTING_QUARTER**
- `3`
- `1`
- `2`
- `4`

**POSTING_QUARTER_LABEL**
- `Q3`
- `Q1`
- `Q2`
- `Q4`

**POSTING_MONTH**
- `9`
- `12`
- `6`
- `3`
- `4`
- `1`
- `2`
- `8`
- `7`
- `11`
- `5`
- `10`

**POSTING_MONTH_NAME**
- `Sep`
- `Dec`
- `Jun`
- `Mar`
- `Apr`
- `Jan`
- `Feb`
- `Aug`
- `Jul`
- `Nov`
- `May`
- `Oct`

**POSTING_MONTH_START**
- `2024-12-01 00:00:00`
- `2026-09-01 00:00:00`
- `2025-09-01 00:00:00`
- `2025-03-01 00:00:00`
- `2025-11-01 00:00:00`
- `2025-06-01 00:00:00`
- `2026-08-01 00:00:00`
- `2026-07-01 00:00:00`
- `2026-06-01 00:00:00`
- `2026-05-01 00:00:00`
- `2026-03-01 00:00:00`
- `2026-04-01 00:00:00`
- `2025-01-01 00:00:00`
- `2026-02-01 00:00:00`
- `2026-01-01 00:00:00`
- `2025-02-01 00:00:00`
- `2025-04-01 00:00:00`
- `2025-12-01 00:00:00`
- `2025-07-01 00:00:00`
- `2025-10-01 00:00:00`
- `2025-08-01 00:00:00`
- `2025-05-01 00:00:00`
- `2026-10-01 00:00:00`
- `2026-11-01 00:00:00`

**EXPENSE_CATEGORY**
- `Personnel expenses`
- `Office expenses`
- `Commissions Expense`
- `Premium taxes`
- `Marketing & travel`
- `Loss and loss adjustment expenses`
- `Corporate expenses`
- `Underwriting expenses`
- `Commission and Brokerage - Direct`
- `Salaries expense`
- `Uncategorized`
- `Other underwriting expenses`
- `Computer service expenses`
- `Other taxes, licenses, and fees`
- `Bad Debt Expense`
- `Gain or loss on asset disposal`
- `Consulting Fees`
- `Corporate taxes`
- `Management fees`
- `Interest expense`
- `Commissions - Net`
- `Investment expense`
- `Federal taxes incurred (Current)`
- `Tax Fees`
- `Deferred Compensation Expense`
- `Surplus note interest`
- `Unamortized loan costs`
- `ULAE incurred`
- `Fines & Penalties`
- `UW expense (Pg. 11 STAT Alloc.)`

**EXPENSE_GROUP**
- `Operating & Administrative Expenses`
- `Underwriting & Acquisition Expenses`
- `Losses & Loss Adjustment Expenses`
- `Other Expenses`
- `Income Taxes`
- `Investment & Financing Expenses`
- `Interest Expense`

**EXPENSE_GROUP_SORT**
- `5`
- `2`
- `1`
- `7`
- `6`
- `4`
- `3`

**BUSINESS_TYPE**
- `N/A`
- `Direct`
- `Assumed`
- `Ceded`

**MAIN_ACCOUNT_TYPE**
- `Expense`
- `ProfitAndLoss`

**DEBIT_CREDIT_DEFAULT**
- `Debit`
- `None`

**PROFIT_CENTER**
- `None`
- `Personal`
- `Property & Casualty Insurance`
- `Health Insurance`
- `Life Insurance`
- `Auto Insurance`
- `Specialty`
- `Investment & Wealth Management`
- `Commercial`
- `0`
- `CAI`
- `MAR`

**BUSINESS_INDICATOR**
- `None`
- `DIRECT`
- `New Business`
- `Claims Activity`
- `Customer Retention`
- `Cross-Sell / Up-Sell`
- `Policy Renewal`
- `CONCUR`
- `CEDED`
- `ASSUMED`
- `Up_sell`

**LINE_OF_BUSINESS**
- `None`
- `Direct_Customer`
- `Broker`
- `40`
- `170`
- `10`
- `270`
- `Corporate`
- `90`
- `21`
- `Individual`
- `25`
- `Reinsurance`
- `51`
- `52`

**DOCUMENT_NUMBER**
- `None`

**JOURNAL_CATEGORY**
- `GeneralJournal`
- `FixedAssets`
- `None`
- `Vend`
- `Allocation`

**POSTING_TYPE**
- `LedgerJournal`
- `None`
- `FixedAssetsCredit`
- `FixedAssetsDebit`
- `MSTDiffSecond`
- `MSTDiff`

**SOURCE_SYSTEM**
- `D365`
- `Fynapse`

**IS_CREDIT**
- `No`
- `Yes`

**IS_CORRECTION**
- `No`

**TRANSACTION_CURRENCY_CODE**
- `USD`
- `GBP`
- `EUR`
- `CAD`
- `AUD`
- `SEK`
- `NOK`

**QUANTITY**
- `0`

**LAST_REFRESHED**
- `2026-11-16 11:42:42.223406+00:00`

## Empty columns

Empty in every row: `DOCUMENT_NUMBER`. Do not filter or group on them.
