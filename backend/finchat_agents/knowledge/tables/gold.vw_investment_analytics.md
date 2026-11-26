---
name: vw_investment_analytics
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Investment analytics from D365 general journal entries, enriched with Chart of Accounts 6-level hierarchy from dim_coa;
  covers portfolio holdings (balance sheet assets), investment returns (revenue), and investment costs (expenses); line-level
  grain for Power BI
grain: one row per ENTRY_REC_ID (one GL journal line)
primary_key:
- ENTRY_REC_ID
entity_column: LEGAL_ENTITY_CODE
period_columns:
- ACCOUNTING_DATE
- POSTING_YEAR
- POSTING_QUARTER
- POSTING_MONTH
- POSTING_YEAR_MONTH
- POSTING_MONTH_START
pii_columns: []
synonyms: []
built_from:
- fact_kpmg_general_journal_account_entries
- dim_main_accounts
- dim_coa
known_issues: []
proposed_fields:
- grain
- primary_key
reviewed: false
---

# vw_investment_analytics

Investment analytics from D365 general journal entries, enriched with Chart of Accounts 6-level hierarchy from dim_coa; covers portfolio holdings (balance sheet assets), investment returns (revenue), and investment costs (expenses); line-level grain for Power BI

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
| `FINANCIAL_STATEMENT` | string |  |  | `FINANCIAL_STATEMENT` |
| `ACCOUNT_TYPE` | string |  |  | `ACCOUNT_TYPE` |
| `INVESTMENT_CATEGORY` | string |  |  | `INVESTMENT_CATEGORY` |
| `ASSET_CLASS` | string |  |  | `ASSET_CLASS` |
| `ASSET_SUBCLASS` | string |  |  | `ASSET_SUBCLASS` |
| `INVESTMENT_DETAIL_1` | string |  |  | `INVESTMENT_DETAIL_1` |
| `INVESTMENT_DETAIL_2` | string |  |  | `INVESTMENT_DETAIL_2` |
| `INVESTMENT_DOMAIN` | string |  |  | `INVESTMENT_DOMAIN` |
| `INVESTMENT_GROUP` | string |  |  | `INVESTMENT_GROUP` |
| `INVESTMENT_GROUP_SORT` | int |  |  | `INVESTMENT_GROUP_SORT` |
| `INVESTMENT_SUBTYPE` | string |  |  | `INVESTMENT_SUBTYPE` |
| `GAIN_LOSS_INDICATOR` | string |  |  | `GAIN_LOSS_INDICATOR` |
| `TAX_STATUS` | string |  |  | `TAX_STATUS` |
| `REPORTING_BASIS` | string |  |  | `REPORTING_BASIS` |
| `COA_TYPE` | string |  |  | `COA_TYPE` |
| `D365_ACCOUNT_CATEGORY` | string |  |  | `D365_ACCOUNT_CATEGORY` |
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
| `INVESTMENT_AMOUNT` | decimal |  |  | `INVESTMENT_AMOUNT` |
| `DEBIT_AMOUNT` | decimal |  |  | `DEBIT_AMOUNT` |
| `CREDIT_AMOUNT` | decimal |  |  | `CREDIT_AMOUNT` |
| `REPORTING_CURRENCY_AMOUNT` | decimal |  |  | `REPORTING_CURRENCY_AMOUNT` |
| `TRANSACTION_CURRENCY_AMOUNT` | decimal |  |  | `TRANSACTION_CURRENCY_AMOUNT` |
| `QUANTITY` | decimal |  |  | `QUANTITY` |
| `LAST_REFRESHED` | timestamp |  |  | `LAST_REFRESHED` |

## Values

**LEDGER_NAME**
- `103`
- `100`
- `101`
- `236`
- `228`
- `233`
- `299`
- `238`
- `201`
- `230`
- `214`

**POSTING_LAYER**
- `Current`
- `Operations`

**POSTING_YEAR**
- `2025`
- `2024`
- `2026`

**POSTING_QUARTER**
- `1`
- `4`
- `3`
- `2`

**POSTING_QUARTER_LABEL**
- `Q1`
- `Q4`
- `Q3`
- `Q2`

**POSTING_MONTH**
- `1`
- `12`
- `11`
- `3`
- `6`
- `9`
- `4`
- `7`
- `2`
- `10`
- `8`
- `5`

**POSTING_MONTH_NAME**
- `Jan`
- `Dec`
- `Nov`
- `Mar`
- `Jun`
- `Sep`
- `Apr`
- `Feb`
- `Jul`
- `Oct`
- `Aug`
- `May`

**POSTING_MONTH_START**
- `2025-01-01 00:00:00`
- `2024-12-01 00:00:00`
- `2025-11-01 00:00:00`
- `2025-03-01 00:00:00`
- `2026-01-01 00:00:00`
- `2025-09-01 00:00:00`
- `2025-06-01 00:00:00`
- `2025-02-01 00:00:00`
- `2025-10-01 00:00:00`
- `2025-12-01 00:00:00`
- `2025-08-01 00:00:00`
- `2025-07-01 00:00:00`
- `2025-04-01 00:00:00`
- `2026-04-01 00:00:00`
- `2025-05-01 00:00:00`
- `2026-03-01 00:00:00`
- `2026-06-01 00:00:00`
- `2026-07-01 00:00:00`
- `2026-02-01 00:00:00`
- `2026-08-01 00:00:00`
- `2026-05-01 00:00:00`
- `2026-09-01 00:00:00`
- `2026-10-01 00:00:00`

**DOCUMENT_DATE**
- `1900-01-02 00:00:00`

**FINANCIAL_STATEMENT**
- `Balance Sheet`
- `Income Statement`

**ACCOUNT_TYPE**
- `Asset`
- `Revenue`
- `Expense`

**INVESTMENT_CATEGORY**
- `Invested Assets`
- `Investment Income`
- `Short Term Investments`
- `Investment expense`
- `Interest expense`
- `Realized investment gains (losses)`

**ASSET_CLASS**
- `Bonds`
- `Interest Income Received`
- `Investment Income Due and Accrued`
- `Due and Accrued`
- `Notes payable`
- `Surplus Note Interest (STAT)`
- `Investment Expense (Excl. Surplus Notes)`
- `Stocks`
- `Accretion of discount`
- `Other Invested Assets`
- `Investment Income Received`
- `Mortgage`
- `Dividend Income Received`
- `Amortization of Premium`
- `Realized Gains`
- `Unclassified`
- `Paid for Accrued Income`
- `Realized Losses`
- `Senior notes`

**ASSET_SUBCLASS**
- `State Deposits`
- `Cash Equivalents`
- `Premium`
- `Market Val Adj`
- `Interest Income Receivable`
- `Bonds`
- `Mortgage Loans`
- `Internal`
- `External`
- `Short Term`
- `None`
- `Cash`
- `Common`
- `Discount`
- `Receivable for securities`
- `First liens`
- `Other`
- `Investment Management Fees`
- `Other - Than - Temporary Impairment`
- `Cost`
- `Stocks`

**INVESTMENT_DETAIL_1**
- `None`
- `FL`
- `MI`
- `Taxable`
- `Short Term`
- `Non Taxable`
- `Property`
- `Florida State Deposits`
- `Cost`
- `Affiliates`
- `Cash Equivalents`
- `Bank`
- `Common`
- `Mortgage Loans`
- `Commercial`
- `Bonds`
- `NM`
- `Surplus Notes`
- `Market Val Adj`

**INVESTMENT_DETAIL_2**
- `None`
- `Bank`
- `FL State Deposits`
- `Non - affiliate`

**INVESTMENT_DOMAIN**
- `Portfolio Holdings`
- `Investment Returns`
- `Investment Costs`

**INVESTMENT_GROUP**
- `Long-Term Invested Assets`
- `Investment Income`
- `Short-Term Investments`
- `Investment Expenses`
- `Interest Expense`
- `Realized Gains & Losses`

**INVESTMENT_GROUP_SORT**
- `2`
- `3`
- `1`
- `5`
- `6`
- `4`

**INVESTMENT_SUBTYPE**
- `Bonds`
- `Interest Income`
- `Accrued Investment Income`
- `Due & Accrued Income`
- `Interest Expense`
- `Surplus Note Interest`
- `Investment Management Fee`
- `Equities`
- `Mortgage Loans`
- `Investment Income (MGA)`
- `Bond Discount Accretion`
- `Other Invested Assets`
- `Realized Gain`
- `Dividend Income`
- `Bond Premium Amortization`
- `Unclassified`
- `Realized Loss`
- `Paid-for Accrued Income`

**GAIN_LOSS_INDICATOR**
- `None`
- `Loss`
- `Gain`

**TAX_STATUS**
- `None`

**REPORTING_BASIS**
- `STAT`
- `MGA`

**COA_TYPE**
- `Asset`
- `Revenue`
- `Expense`

**D365_ACCOUNT_CATEGORY**
- `Long Term Investments`
- `Investment Income`
- `Short Term Investments`
- `Investment income due and accrued`
- `Investment expense`
- `Surplus note interest`
- `Marketable Securities`
- `Receivable (payables) for securities`
- `Mortgage loans`
- `Realized gain (bonds and stocks)`
- `Realized investment gains (losses)`

**MAIN_ACCOUNT_TYPE**
- `Asset`
- `Revenue`
- `Expense`

**DEBIT_CREDIT_DEFAULT**
- `Debit`
- `Credit`

**COST_CENTER**
- `None`
- `Health Provider Management`
- `Accident Assessment`
- `101`
- `Life Operations`
- `Health Claims Processing`
- `0`
- `Risk Assessment`
- `Portfolio Management`
- `P&C Claims`
- `Underwriting`
- `Wealth Advisory Services`
- `Procurement`

**PROFIT_CENTER**
- `None`
- `Health Insurance`
- `Auto Insurance`
- `Life Insurance`
- `Property & Casualty Insurance`
- `Investment & Wealth Management`

**BUSINESS_INDICATOR**
- `None`
- `Customer Retention`
- `Claims Activity`
- `New Business`
- `Policy Renewal`
- `Cross-Sell / Up-Sell`

**LINE_OF_BUSINESS**
- `None`
- `Corporate`
- `Direct_Customer`
- `Broker`
- `Reinsurance`
- `Individual`

**DOCUMENT_NUMBER**
- `None`

**JOURNAL_CATEGORY**
- `GeneralJournal`
- `None`
- `Payment`

**POSTING_TYPE**
- `LedgerJournal`
- `None`
- `CustBalance`

**SOURCE_SYSTEM**
- `D365`

**IS_CREDIT**
- `No`
- `Yes`

**IS_CORRECTION**
- `No`

**TRANSACTION_CURRENCY_CODE**
- `USD`

**QUANTITY**
- `0`

**LAST_REFRESHED**
- `2026-11-16 11:42:42.223406+00:00`

## Empty columns

Empty in every row: `TAX_STATUS`, `DOCUMENT_NUMBER`. Do not filter or group on them.
