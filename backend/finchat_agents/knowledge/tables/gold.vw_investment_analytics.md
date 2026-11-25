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
row_count: 489
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
- `103`: 144 rows
- `100`: 98 rows
- `101`: 60 rows
- `236`: 50 rows
- `228`: 39 rows
- `233`: 33 rows
- `299`: 29 rows
- `238`: 19 rows
- `201`: 14 rows
- `230`: 2 rows
- `214`: 1 rows

**POSTING_LAYER**
- `Current`: 442 rows
- `Operations`: 47 rows

**POSTING_YEAR**
- `2025`: 338 rows
- `2024`: 106 rows
- `2026`: 45 rows

**POSTING_QUARTER**
- `1`: 248 rows
- `4`: 154 rows
- `3`: 44 rows
- `2`: 43 rows

**POSTING_QUARTER_LABEL**
- `Q1`: 248 rows
- `Q4`: 154 rows
- `Q3`: 44 rows
- `Q2`: 43 rows

**POSTING_MONTH**
- `1`: 213 rows
- `12`: 117 rows
- `11`: 24 rows
- `3`: 21 rows
- `6`: 19 rows
- `9`: 18 rows
- `4`: 16 rows
- `7`: 14 rows
- `2`: 14 rows
- `10`: 13 rows
- `8`: 12 rows
- `5`: 8 rows

**POSTING_MONTH_NAME**
- `Jan`: 213 rows
- `Dec`: 117 rows
- `Nov`: 24 rows
- `Mar`: 21 rows
- `Jun`: 19 rows
- `Sep`: 18 rows
- `Apr`: 16 rows
- `Feb`: 14 rows
- `Jul`: 14 rows
- `Oct`: 13 rows
- `Aug`: 12 rows
- `May`: 8 rows

**POSTING_MONTH_START**
- `2025-01-01 00:00:00`: 197 rows
- `2024-12-01 00:00:00`: 106 rows
- `2025-11-01 00:00:00`: 24 rows
- `2025-03-01 00:00:00`: 16 rows
- `2026-01-01 00:00:00`: 16 rows
- `2025-09-01 00:00:00`: 16 rows
- `2025-06-01 00:00:00`: 14 rows
- `2025-02-01 00:00:00`: 12 rows
- `2025-10-01 00:00:00`: 12 rows
- `2025-12-01 00:00:00`: 11 rows
- `2025-08-01 00:00:00`: 10 rows
- `2025-07-01 00:00:00`: 10 rows
- `2025-04-01 00:00:00`: 10 rows
- `2026-04-01 00:00:00`: 6 rows
- `2025-05-01 00:00:00`: 6 rows
- `2026-03-01 00:00:00`: 5 rows
- `2026-06-01 00:00:00`: 5 rows
- `2026-07-01 00:00:00`: 4 rows
- `2026-02-01 00:00:00`: 2 rows
- `2026-08-01 00:00:00`: 2 rows
- `2026-05-01 00:00:00`: 2 rows
- `2026-09-01 00:00:00`: 2 rows
- `2026-10-01 00:00:00`: 1 rows

**DOCUMENT_DATE**
- `1900-01-02 00:00:00`: 489 rows

**FINANCIAL_STATEMENT**
- `Balance Sheet`: 326 rows
- `Income Statement`: 163 rows

**ACCOUNT_TYPE**
- `Asset`: 326 rows
- `Revenue`: 146 rows
- `Expense`: 17 rows

**INVESTMENT_CATEGORY**
- `Invested Assets`: 228 rows
- `Investment Income`: 143 rows
- `Short Term Investments`: 98 rows
- `Investment expense`: 9 rows
- `Interest expense`: 8 rows
- `Realized investment gains (losses)`: 3 rows

**ASSET_CLASS**
- `Bonds`: 300 rows
- `Interest Income Received`: 119 rows
- `Investment Income Due and Accrued`: 15 rows
- `Due and Accrued`: 13 rows
- `Notes payable`: 7 rows
- `Surplus Note Interest (STAT)`: 5 rows
- `Investment Expense (Excl. Surplus Notes)`: 4 rows
- `Stocks`: 4 rows
- `Accretion of discount`: 3 rows
- `Other Invested Assets`: 3 rows
- `Investment Income Received`: 3 rows
- `Mortgage`: 3 rows
- `Dividend Income Received`: 2 rows
- `Amortization of Premium`: 2 rows
- `Realized Gains`: 2 rows
- `Unclassified`: 1 rows
- `Paid for Accrued Income`: 1 rows
- `Realized Losses`: 1 rows
- `Senior notes`: 1 rows

**ASSET_SUBCLASS**
- `State Deposits`: 125 rows
- `Cash Equivalents`: 109 rows
- `Premium`: 95 rows
- `Market Val Adj`: 72 rows
- `Interest Income Receivable`: 15 rows
- `Bonds`: 13 rows
- `Mortgage Loans`: 10 rows
- `Internal`: 7 rows
- `External`: 6 rows
- `Short Term`: 4 rows
- `None`: 4 rows
- `Cash`: 4 rows
- `Common`: 4 rows
- `Discount`: 4 rows
- `Receivable for securities`: 3 rows
- `First liens`: 3 rows
- `Other`: 3 rows
- `Investment Management Fees`: 2 rows
- `Other - Than - Temporary Impairment`: 2 rows
- `Cost`: 2 rows
- `Stocks`: 2 rows

**INVESTMENT_DETAIL_1**
- `None`: 314 rows
- `FL`: 95 rows
- `MI`: 29 rows
- `Taxable`: 9 rows
- `Short Term`: 8 rows
- `Non Taxable`: 4 rows
- `Property`: 4 rows
- `Florida State Deposits`: 4 rows
- `Cost`: 3 rows
- `Affiliates`: 3 rows
- `Cash Equivalents`: 3 rows
- `Bank`: 2 rows
- `Common`: 2 rows
- `Mortgage Loans`: 2 rows
- `Commercial`: 2 rows
- `Bonds`: 2 rows
- `NM`: 1 rows
- `Surplus Notes`: 1 rows
- `Market Val Adj`: 1 rows

**INVESTMENT_DETAIL_2**
- `None`: 481 rows
- `Bank`: 4 rows
- `FL State Deposits`: 2 rows
- `Non - affiliate`: 2 rows

**INVESTMENT_DOMAIN**
- `Portfolio Holdings`: 326 rows
- `Investment Returns`: 146 rows
- `Investment Costs`: 17 rows

**INVESTMENT_GROUP**
- `Long-Term Invested Assets`: 228 rows
- `Investment Income`: 143 rows
- `Short-Term Investments`: 98 rows
- `Investment Expenses`: 9 rows
- `Interest Expense`: 8 rows
- `Realized Gains & Losses`: 3 rows

**INVESTMENT_GROUP_SORT**
- `2`: 228 rows
- `3`: 143 rows
- `1`: 98 rows
- `5`: 9 rows
- `6`: 8 rows
- `4`: 3 rows

**INVESTMENT_SUBTYPE**
- `Bonds`: 300 rows
- `Interest Income`: 119 rows
- `Accrued Investment Income`: 15 rows
- `Due & Accrued Income`: 13 rows
- `Interest Expense`: 8 rows
- `Surplus Note Interest`: 5 rows
- `Investment Management Fee`: 4 rows
- `Equities`: 4 rows
- `Mortgage Loans`: 3 rows
- `Investment Income (MGA)`: 3 rows
- `Bond Discount Accretion`: 3 rows
- `Other Invested Assets`: 3 rows
- `Realized Gain`: 2 rows
- `Dividend Income`: 2 rows
- `Bond Premium Amortization`: 2 rows
- `Unclassified`: 1 rows
- `Realized Loss`: 1 rows
- `Paid-for Accrued Income`: 1 rows

**GAIN_LOSS_INDICATOR**
- `None`: 484 rows
- `Loss`: 3 rows
- `Gain`: 2 rows

**TAX_STATUS**
- `None`: 489 rows

**REPORTING_BASIS**
- `STAT`: 390 rows
- `MGA`: 99 rows

**COA_TYPE**
- `Asset`: 326 rows
- `Revenue`: 146 rows
- `Expense`: 17 rows

**D365_ACCOUNT_CATEGORY**
- `Long Term Investments`: 176 rows
- `Investment Income`: 143 rows
- `Short Term Investments`: 127 rows
- `Investment income due and accrued`: 13 rows
- `Investment expense`: 12 rows
- `Surplus note interest`: 5 rows
- `Marketable Securities`: 4 rows
- `Receivable (payables) for securities`: 3 rows
- `Mortgage loans`: 3 rows
- `Realized gain (bonds and stocks)`: 2 rows
- `Realized investment gains (losses)`: 1 rows

**MAIN_ACCOUNT_TYPE**
- `Asset`: 326 rows
- `Revenue`: 146 rows
- `Expense`: 17 rows

**DEBIT_CREDIT_DEFAULT**
- `Debit`: 343 rows
- `Credit`: 146 rows

**COST_CENTER**
- `None`: 279 rows
- `Health Provider Management`: 71 rows
- `Accident Assessment`: 48 rows
- `101`: 45 rows
- `Life Operations`: 14 rows
- `Health Claims Processing`: 11 rows
- `0`: 9 rows
- `Risk Assessment`: 2 rows
- `Portfolio Management`: 2 rows
- `P&C Claims`: 2 rows
- `Underwriting`: 2 rows
- `Wealth Advisory Services`: 2 rows
- `Procurement`: 2 rows

**PROFIT_CENTER**
- `None`: 333 rows
- `Health Insurance`: 86 rows
- `Auto Insurance`: 50 rows
- `Life Insurance`: 16 rows
- `Property & Casualty Insurance`: 2 rows
- `Investment & Wealth Management`: 2 rows

**BUSINESS_INDICATOR**
- `None`: 333 rows
- `Customer Retention`: 75 rows
- `Claims Activity`: 61 rows
- `New Business`: 16 rows
- `Policy Renewal`: 2 rows
- `Cross-Sell / Up-Sell`: 2 rows

**LINE_OF_BUSINESS**
- `None`: 333 rows
- `Corporate`: 75 rows
- `Direct_Customer`: 59 rows
- `Broker`: 18 rows
- `Reinsurance`: 2 rows
- `Individual`: 2 rows

**DOCUMENT_NUMBER**
- `None`: 489 rows

**JOURNAL_CATEGORY**
- `GeneralJournal`: 315 rows
- `None`: 173 rows
- `Payment`: 1 rows

**POSTING_TYPE**
- `LedgerJournal`: 315 rows
- `None`: 173 rows
- `CustBalance`: 1 rows

**SOURCE_SYSTEM**
- `D365`: 489 rows

**IS_CREDIT**
- `No`: 356 rows
- `Yes`: 133 rows

**IS_CORRECTION**
- `No`: 489 rows

**TRANSACTION_CURRENCY_CODE**
- `USD`: 489 rows

**QUANTITY**
- `0`: 489 rows

**LAST_REFRESHED**
- `2026-11-16 11:42:42.223406+00:00`: 489 rows

## Profile

Rows in the latest export: 489.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ENTRY_REC_ID` | STRING | 518 | 0 | 5637220282 | 5637313717 |
| `LEGAL_ENTITY_CODE` | STRING | 11 | 0 |  |  |
| `LEGAL_ENTITY_NAME` | STRING | 11 | 0 |  |  |
| `LEDGER_NAME` | STRING | 11 | 0 | 100 | 299 |
| `POSTING_LAYER` | STRING | 2 | 0 | Current | Operations |
| `ACCOUNTING_DATE` | DATE | 68 | 0 | 2024-12-31 00:00:00 | 2026-10-23 00:00:00 |
| `POSTING_YEAR` | INT | 3 | 0 | 2024 | 2026 |
| `POSTING_QUARTER` | INT | 4 | 0 | 1 | 4 |
| `POSTING_QUARTER_LABEL` | STRING | 4 | 0 | Q1 | Q4 |
| `POSTING_MONTH` | INT | 12 | 0 | 1 | 12 |
| `POSTING_MONTH_NAME` | STRING | 12 | 0 | Apr | Sep |
| `POSTING_YEAR_MONTH` | STRING | 21 | 0 |  |  |
| `POSTING_MONTH_START` | DATE | 24 | 0 | 2024-12-01 00:00:00 | 2026-10-01 00:00:00 |
| `DOCUMENT_DATE` | DATE | 1 | 0 | 1900-01-02 00:00:00 | 1900-01-02 00:00:00 |
| `MAIN_ACCOUNT` | STRING | 56 | 0 | 121200 | 542200 |
| `ACCOUNT_DESCRIPTION` | STRING | 55 | 0 | Accretion of Bond Discounts - Cash Eq... | Surplus Note Interest Expense - External |
| `ACCOUNT_LABEL` | STRING | 56 | 0 | 121200 - Short Term Bonds - Discount | 542200 - Surplus Note Interest Expens... |
| `FINANCIAL_STATEMENT` | STRING | 2 | 0 | Balance Sheet | Income Statement |
| `ACCOUNT_TYPE` | STRING | 3 | 0 | Asset | Revenue |
| `INVESTMENT_CATEGORY` | STRING | 6 | 0 | Interest expense | Short Term Investments |
| `ASSET_CLASS` | STRING | 19 | 0 | Accretion of discount | Unclassified |
| `ASSET_SUBCLASS` | STRING | 19 | 4 | Bonds | Stocks |
| `INVESTMENT_DETAIL_1` | STRING | 18 | 314 | Affiliates | Taxable |
| `INVESTMENT_DETAIL_2` | STRING | 3 | 481 | Bank | Non - affiliate |
| `INVESTMENT_DOMAIN` | STRING | 3 | 0 | Investment Costs | Portfolio Holdings |
| `INVESTMENT_GROUP` | STRING | 5 | 0 | Interest Expense | Short-Term Investments |
| `INVESTMENT_GROUP_SORT` | INT | 6 | 0 | 1 | 6 |
| `INVESTMENT_SUBTYPE` | STRING | 18 | 0 | Accrued Investment Income | Unclassified |
| `GAIN_LOSS_INDICATOR` | STRING | 2 | 484 | Gain | Loss |
| `TAX_STATUS` | STRING | 0 | 489 |  |  |
| `REPORTING_BASIS` | STRING | 2 | 0 | MGA | STAT |
| `COA_TYPE` | STRING | 3 | 0 | Asset | Revenue |
| `D365_ACCOUNT_CATEGORY` | STRING | 11 | 0 | Investment Income | Surplus note interest |
| `MAIN_ACCOUNT_TYPE` | STRING | 3 | 0 | Asset | Revenue |
| `DEBIT_CREDIT_DEFAULT` | STRING | 2 | 0 | Credit | Debit |
| `COST_CENTER` | STRING | 12 | 279 | 0 | Wealth Advisory Services |
| `PROFIT_CENTER` | STRING | 5 | 333 | Auto Insurance | Property & Casualty Insurance |
| `BUSINESS_INDICATOR` | STRING | 5 | 333 | Claims Activity | Policy Renewal |
| `LINE_OF_BUSINESS` | STRING | 5 | 333 | Broker | Reinsurance |
| `LEDGER_ACCOUNT` | STRING | 99 | 0 | 121200---------- | 542200---------- |
| `JOURNAL_NUMBER` | STRING | 298 | 0 | 100-002640 | 299-000366 |
| `VOUCHER` | STRING | 147 | 173 | 201-000000001 | PUQ804216262 |
| `DOCUMENT_NUMBER` | STRING | 0 | 489 |  |  |
| `LINE_DESCRIPTION` | STRING | 101 | 364 | 001009\|ELQ OVGB FLRWXCUF | 998185\|ELQ OVGB FLRWXCUF |
| `JOURNAL_CATEGORY` | STRING | 3 | 0 | GeneralJournal | Payment |
| `POSTING_TYPE` | STRING | 3 | 0 | CustBalance | None |
| `SOURCE_SYSTEM` | STRING | 1 | 0 | D365 | D365 |
| `IS_CREDIT` | STRING | 2 | 0 | No | Yes |
| `IS_CORRECTION` | STRING | 1 | 0 | No | No |
| `TRANSACTION_CURRENCY_CODE` | STRING | 1 | 0 | USD | USD |
| `INVESTMENT_AMOUNT` | DECIMAL | 293 | 0 | -19733559.88 | 107473778.25 |
| `DEBIT_AMOUNT` | DECIMAL | 193 | 0 | 0 | 107473778.25 |
| `CREDIT_AMOUNT` | DECIMAL | 105 | 0 | 0 | 19733559.88 |
| `REPORTING_CURRENCY_AMOUNT` | DECIMAL | 239 | 0 | -19733559.88 | 107473778.25 |
| `TRANSACTION_CURRENCY_AMOUNT` | DECIMAL | 293 | 0 | -19733559.88 | 107473778.25 |
| `QUANTITY` | DECIMAL | 1 | 0 | 0 | 0 |
| `LAST_REFRESHED` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:42.223000 | 2026-11-16 11:42:42.223000 |

## Sample rows

| ENTRY_REC_ID | LEDGER_NAME | POSTING_LAYER | ACCOUNTING_DATE | POSTING_YEAR | POSTING_QUARTER | POSTING_QUARTER_LABEL | POSTING_MONTH | POSTING_MONTH_NAME | POSTING_YEAR_MONTH | POSTING_MONTH_START | DOCUMENT_DATE | MAIN_ACCOUNT | ACCOUNT_DESCRIPTION | ACCOUNT_LABEL | FINANCIAL_STATEMENT | ACCOUNT_TYPE | INVESTMENT_CATEGORY | ASSET_CLASS | ASSET_SUBCLASS | INVESTMENT_DETAIL_1 | INVESTMENT_DETAIL_2 | INVESTMENT_DOMAIN | INVESTMENT_GROUP | INVESTMENT_GROUP_SORT | INVESTMENT_SUBTYPE | GAIN_LOSS_INDICATOR | TAX_STATUS | REPORTING_BASIS | COA_TYPE | D365_ACCOUNT_CATEGORY | MAIN_ACCOUNT_TYPE | DEBIT_CREDIT_DEFAULT | COST_CENTER | PROFIT_CENTER | BUSINESS_INDICATOR | LINE_OF_BUSINESS | LEDGER_ACCOUNT | JOURNAL_NUMBER | VOUCHER | DOCUMENT_NUMBER | LINE_DESCRIPTION | JOURNAL_CATEGORY | POSTING_TYPE | SOURCE_SYSTEM | IS_CREDIT | IS_CORRECTION | TRANSACTION_CURRENCY_CODE | INVESTMENT_AMOUNT | DEBIT_AMOUNT | CREDIT_AMOUNT | REPORTING_CURRENCY_AMOUNT | TRANSACTION_CURRENCY_AMOUNT | QUANTITY | LAST_REFRESHED |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5637272494 | 228 | Current | 2026-06-24 00:00:00 | 2026 | 2 | Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 1900-01-02 00:00:00 | 445000 | Interest Income Received | 445000 - Interest Income Received | Income Statement | Revenue | Investment Income | Interest Income Received | Cash Equivalents | NULL | NULL | Investment Returns | Investment Income | 3 | Interest Income | NULL | NULL | MGA | Revenue | Investment Income | Revenue | Credit | 101 | NULL | NULL | NULL | 445000-101-----0000---- | 228-000055 | GJV-000000001 | NULL | 279081\|ELQ OVGB FLRWXCUF | GeneralJournal | LedgerJournal | D365 | No | No | USD | 24746.7 | 24746.7 | 0 | 24746.7 | 24746.7 | 0 | 2026-11-16 11:42:42.223000 |
| 5637272534 | 228 | Current | 2026-06-30 00:00:00 | 2026 | 2 | Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 1900-01-02 00:00:00 | 445000 | Interest Income Received | 445000 - Interest Income Received | Income Statement | Revenue | Investment Income | Interest Income Received | Cash Equivalents | NULL | NULL | Investment Returns | Investment Income | 3 | Interest Income | NULL | NULL | MGA | Revenue | Investment Income | Revenue | Credit | 0 | NULL | NULL | NULL | 445000-000-----0000---- | 228-000057 | GJV-000000001 | NULL | 481484\|ELQ OVGB FLRWXCUF | GeneralJournal | LedgerJournal | D365 | Yes | No | USD | -14169.75 | 0 | 14169.75 | -14169.75 | -14169.75 | 0 | 2026-11-16 11:42:42.223000 |
| 5637272536 | 228 | Current | 2026-06-30 00:00:00 | 2026 | 2 | Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 1900-01-02 00:00:00 | 445000 | Interest Income Received | 445000 - Interest Income Received | Income Statement | Revenue | Investment Income | Interest Income Received | Cash Equivalents | NULL | NULL | Investment Returns | Investment Income | 3 | Interest Income | NULL | NULL | MGA | Revenue | Investment Income | Revenue | Credit | 101 | NULL | NULL | NULL | 445000-101-----0000---- | 228-000057 | GJV-000000001 | NULL | 548233\|ZKQFYLR XTCIQW EOS DUIOGQ FPZ... | GeneralJournal | LedgerJournal | D365 | Yes | No | USD | -2895 | 0 | 2895 | -2895 | -2895 | 0 | 2026-11-16 11:42:42.223000 |
| 5637273915 | 228 | Current | 2026-07-01 00:00:00 | 2026 | 3 | Q3 | 7 | Jul | (altered in export) | 2026-07-01 00:00:00 | 1900-01-02 00:00:00 | 445000 | Interest Income Received | 445000 - Interest Income Received | Income Statement | Revenue | Investment Income | Interest Income Received | Cash Equivalents | NULL | NULL | Investment Returns | Investment Income | 3 | Interest Income | NULL | NULL | MGA | Revenue | Investment Income | Revenue | Credit | 101 | NULL | NULL | NULL | 445000-101-----0000---- | 228-000058 | GJV-000000001 | NULL | 287844\|ZKQFYLR XTCIQW EOS DUIOGQ FPZ... | GeneralJournal | LedgerJournal | D365 | No | No | USD | 2895 | 2895 | 0 | 2895 | 2895 | 0 | 2026-11-16 11:42:42.223000 |
| 5637274170 | 228 | Current | 2026-07-31 00:00:00 | 2026 | 3 | Q3 | 7 | Jul | (altered in export) | 2026-07-01 00:00:00 | 1900-01-02 00:00:00 | 445000 | Interest Income Received | 445000 - Interest Income Received | Income Statement | Revenue | Investment Income | Interest Income Received | Cash Equivalents | NULL | NULL | Investment Returns | Investment Income | 3 | Interest Income | NULL | NULL | MGA | Revenue | Investment Income | Revenue | Credit | 0 | NULL | NULL | NULL | 445000-000-----0000---- | 228-000064 | GJV-000000001 | NULL | 931542\|ELQ OVGB FLRWXCUF | GeneralJournal | LedgerJournal | D365 | Yes | No | USD | -14777.58 | 0 | 14777.58 | -14777.58 | -14777.58 | 0 | 2026-11-16 11:42:42.223000 |
