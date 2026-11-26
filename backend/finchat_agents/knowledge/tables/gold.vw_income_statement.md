---
name: vw_income_statement
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Income statement (P&L) at GL journal-line grain. Revenue (4xxxxx) and Expense (5xxxxx) accounts mapped to the CoA
  MDM hierarchy (lakehouse_hsbc.mdm_ind_pc_insurance.coa_mdm) with standard IS line structure, sort orders, Direct/Assumed/Ceded
  split, KPI components (loss/expense/combined ratio) and sign-normalised amounts. Built for Power BI.
grain: one row per ENTRY_REC_ID (one GL journal line)
primary_key:
- ENTRY_REC_ID
entity_column: LEGAL_ENTITY_CODE
period_columns:
- ACCOUNTING_DATE
- FISCAL_YEAR
- FISCAL_QUARTER
- FISCAL_YEAR_QUARTER
- FISCAL_MONTH
- FISCAL_YEAR_MONTH
- FISCAL_PERIOD_KEY
- PERIOD_START_DATE
- PERIOD_END_DATE
pii_columns: []
synonyms: []
built_from:
- fact_kpmg_general_journal_account_entries
- dim_main_accounts
known_issues: []
proposed_fields:
- grain
- primary_key
reviewed: false
---

# vw_income_statement

Income statement (P&L) at GL journal-line grain. Revenue (4xxxxx) and Expense (5xxxxx) accounts mapped to the CoA MDM hierarchy (lakehouse_hsbc.mdm_ind_pc_insurance.coa_mdm) with standard IS line structure, sort orders, Direct/Assumed/Ceded split, KPI components (loss/expense/combined ratio) and sign-normalised amounts. Built for Power BI.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ENTRY_REC_ID` | string |  |  | `ENTRY_REC_ID` |
| `LEGAL_ENTITY_CODE` | string |  |  | `LEGAL_ENTITY_CODE` |
| `LEGAL_ENTITY_NAME` | string |  |  | `LEGAL_ENTITY_NAME` |
| `LEDGER_NAME` | string |  |  | `LEDGER_NAME` |
| `POSTING_LAYER` | string |  |  | `POSTING_LAYER` |
| `ACCOUNTING_DATE` | date |  |  | `ACCOUNTING_DATE` |
| `FISCAL_YEAR` | int |  |  | `FISCAL_YEAR` |
| `FISCAL_QUARTER` | int |  |  | `FISCAL_QUARTER` |
| `FISCAL_YEAR_QUARTER` | string |  |  | `FISCAL_YEAR_QUARTER` |
| `FISCAL_MONTH` | int |  |  | `FISCAL_MONTH` |
| `FISCAL_MONTH_NAME` | string |  |  | `FISCAL_MONTH_NAME` |
| `FISCAL_YEAR_MONTH` | string |  |  | `FISCAL_YEAR_MONTH` |
| `FISCAL_PERIOD_KEY` | int |  |  | `FISCAL_PERIOD_KEY` |
| `PERIOD_START_DATE` | date |  |  | `PERIOD_START_DATE` |
| `PERIOD_END_DATE` | date |  |  | `PERIOD_END_DATE` |
| `DOCUMENT_DATE` | date |  |  | `DOCUMENT_DATE` |
| `AS_OF_DATE` | date |  |  | `AS_OF_DATE` |
| `RELATIVE_YEAR` | int |  |  | `RELATIVE_YEAR` |
| `YEAR_COMPARISON` | string |  |  | `YEAR_COMPARISON` |
| `IS_YTD_COMPARABLE` | boolean |  |  | `IS_YTD_COMPARABLE` |
| `IS_MTD_COMPARABLE` | boolean |  |  | `IS_MTD_COMPARABLE` |
| `MAIN_ACCOUNT` | string |  |  | `MAIN_ACCOUNT` |
| `ACCOUNT_NAME` | string |  |  | `ACCOUNT_NAME` |
| `ACCOUNT_LABEL` | string |  |  | `ACCOUNT_LABEL` |
| `STAT_OR_MGA` | string |  |  | `STAT_OR_MGA` |
| `REPORTING_BASIS` | string |  |  | `REPORTING_BASIS` |
| `COA_MAPPING_STATUS` | string |  |  | `COA_MAPPING_STATUS` |
| `COA_LEVEL_0` | string |  |  | `COA_LEVEL_0` |
| `COA_LEVEL_1` | string |  |  | `COA_LEVEL_1` |
| `COA_LEVEL_2` | string |  |  | `COA_LEVEL_2` |
| `COA_LEVEL_3` | string |  |  | `COA_LEVEL_3` |
| `COA_LEVEL_4` | string |  |  | `COA_LEVEL_4` |
| `COA_LEVEL_5` | string |  |  | `COA_LEVEL_5` |
| `COA_LEVEL_6` | string |  |  | `COA_LEVEL_6` |
| `IS_SECTION` | string |  |  | `IS_SECTION` |
| `IS_SECTION_SORT` | int |  |  | `IS_SECTION_SORT` |
| `IS_LINE` | string |  |  | `IS_LINE` |
| `IS_LINE_SORT` | int |  |  | `IS_LINE_SORT` |
| `IS_SUB_LINE` | string |  |  | `IS_SUB_LINE` |
| `BUSINESS_TYPE` | string |  |  | `BUSINESS_TYPE` |
| `PREMIUM_COMPONENT` | string |  |  | `PREMIUM_COMPONENT` |
| `KPI_COMPONENT` | string |  |  | `KPI_COMPONENT` |
| `IS_UNDERWRITING_ITEM` | boolean |  |  | `IS_UNDERWRITING_ITEM` |
| `IS_INVESTMENT_ITEM` | boolean |  |  | `IS_INVESTMENT_ITEM` |
| `IS_PRE_TAX_ITEM` | boolean |  |  | `IS_PRE_TAX_ITEM` |
| `COST_CENTER` | string |  |  | `COST_CENTER` |
| `PROFIT_CENTER` | string |  |  | `PROFIT_CENTER` |
| `BUSINESS_INDICATOR` | string |  |  | `BUSINESS_INDICATOR` |
| `LINE_OF_BUSINESS` | string |  |  | `LINE_OF_BUSINESS` |
| `FINANCIAL_DIMENSIONS` | string |  |  | `FINANCIAL_DIMENSIONS` |
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
| `GL_AMOUNT` | decimal |  |  | `GL_AMOUNT` |
| `PL_AMOUNT` | decimal |  |  | `PL_AMOUNT` |
| `REPORT_AMOUNT` | decimal |  |  | `REPORT_AMOUNT` |
| `DEBIT_AMOUNT` | decimal |  |  | `DEBIT_AMOUNT` |
| `CREDIT_AMOUNT` | decimal |  |  | `CREDIT_AMOUNT` |
| `CY_PL_AMOUNT` | decimal |  |  | `CY_PL_AMOUNT` |
| `PY_PL_AMOUNT` | decimal |  |  | `PY_PL_AMOUNT` |
| `CY_REPORT_AMOUNT` | decimal |  |  | `CY_REPORT_AMOUNT` |
| `PY_REPORT_AMOUNT` | decimal |  |  | `PY_REPORT_AMOUNT` |
| `PL_AMOUNT_REPORTING_CCY` | decimal |  |  | `PL_AMOUNT_REPORTING_CCY` |
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
- `UK07`
- `103`
- `208`
- `UK03`
- `233`
- `UK14`
- `UK17`
- `UK06`
- `101`
- `238`
- `UK13`
- `230`

**POSTING_LAYER**
- `Current`
- `Operations`

**FISCAL_YEAR**
- `2026`
- `2025`
- `2024`

**FISCAL_QUARTER**
- `3`
- `1`
- `2`
- `4`

**FISCAL_YEAR_QUARTER**
- `2026-Q3`
- `2025-Q1`
- `2026-Q2`
- `2026-Q1`
- `2025-Q2`
- `2024-Q4`
- `2025-Q4`
- `2025-Q3`
- `2026-Q4`

**FISCAL_MONTH**
- `9`
- `12`
- `6`
- `3`
- `1`
- `8`
- `4`
- `2`
- `7`
- `5`
- `11`
- `10`

**FISCAL_MONTH_NAME**
- `Sep`
- `Dec`
- `Jun`
- `Mar`
- `Jan`
- `Aug`
- `Apr`
- `Feb`
- `Jul`
- `May`
- `Nov`
- `Oct`

**PERIOD_START_DATE**
- `2024-12-01 00:00:00`
- `2026-09-01 00:00:00`
- `2026-08-01 00:00:00`
- `2025-03-01 00:00:00`
- `2025-11-01 00:00:00`
- `2025-09-01 00:00:00`
- `2026-07-01 00:00:00`
- `2026-06-01 00:00:00`
- `2025-06-01 00:00:00`
- `2026-05-01 00:00:00`
- `2025-01-01 00:00:00`
- `2025-02-01 00:00:00`
- `2025-04-01 00:00:00`
- `2026-03-01 00:00:00`
- `2026-04-01 00:00:00`
- `2026-02-01 00:00:00`
- `2026-01-01 00:00:00`
- `2025-12-01 00:00:00`
- `2025-10-01 00:00:00`
- `2025-07-01 00:00:00`
- `2025-08-01 00:00:00`
- `2025-05-01 00:00:00`
- `2026-10-01 00:00:00`
- `2026-11-01 00:00:00`

**PERIOD_END_DATE**
- `2024-12-31 00:00:00`
- `2026-09-30 00:00:00`
- `2026-08-31 00:00:00`
- `2025-03-31 00:00:00`
- `2025-11-30 00:00:00`
- `2025-09-30 00:00:00`
- `2026-07-31 00:00:00`
- `2026-06-30 00:00:00`
- `2025-06-30 00:00:00`
- `2026-05-31 00:00:00`
- `2025-01-31 00:00:00`
- `2025-02-28 00:00:00`
- `2025-04-30 00:00:00`
- `2026-03-31 00:00:00`
- `2026-04-30 00:00:00`
- `2026-02-28 00:00:00`
- `2026-01-31 00:00:00`
- `2025-12-31 00:00:00`
- `2025-10-31 00:00:00`
- `2025-07-31 00:00:00`
- `2025-08-31 00:00:00`
- `2025-05-31 00:00:00`
- `2026-10-31 00:00:00`
- `2026-11-30 00:00:00`

**AS_OF_DATE**
- `2026-11-02 00:00:00`

**RELATIVE_YEAR**
- `0`
- `-1`
- `-2`

**YEAR_COMPARISON**
- `Current Year`
- `Prior Year`
- `Earlier Years`

**IS_YTD_COMPARABLE**
- `True`
- `False`

**IS_MTD_COMPARABLE**
- `False`
- `True`

**STAT_OR_MGA**
- `MGA`
- `STAT`

**REPORTING_BASIS**
- `MGA`
- `Statutory (STAT)`

**COA_MAPPING_STATUS**
- `Mapped`
- `Inferred (account not in CoA MDM)`

**COA_LEVEL_0**
- `Income Statement`

**COA_LEVEL_1**
- `Expense`
- `Revenue`

**COA_LEVEL_2**
- `General and Administrative`
- `Underwriting expenses`
- `Commissions Income`
- `Premiums earned`
- `Service / Fee Income`
- `Loss and loss adjustment expenses`
- `Underwriting expenses (Commissions)`
- `Other Income`
- `Investment Income`
- `Contra Revenue`
- `Other Expenses`
- `Provision for Federal Taxes`
- `Investment expense`
- `Interest expense`
- `Realized investment gains (losses)`
- `Commissions Expense`

**COA_LEVEL_3**
- `Personnel expenses`
- `Office expenses`
- `Commissions Income`
- `Commissions expense`
- `Taxes, licenses, and fees`
- `Marketing and travel expenses`
- `Claim Adjustment Income`
- `Written Premium`
- `Corporate expenses`
- `Change in Unearned Premium Reserve`
- `Loss Adjustment Expense incurred`
- `Losses incurred`
- `Other Underwriting Expenses`
- `Computer service expenses`
- `Regular`
- `Funds held interest`
- `Interest Income Received`
- `Inspection Fee Income`
- `Service / Fee Income`
- `Management fees`
- `Commission Refund Accrual`
- `Contra Revenue`
- `Installment Fee Income`
- `FX Gain/Loss`
- `Due and Accrued`
- `Current`
- `Notes payable`
- `Other Income`
- `Management Fee Income`
- `STAT Exp Allocation`
- `Surplus Note Interest (STAT)`
- `Investment Expense (Excl. Surplus Notes)`
- `Accretion of discount`
- `Investment Income Received`
- `Dividend Income Received`
- `Realized Gains`
- `Amortization of Premium`
- `Retroactive reinsurance gains (losses)`
- `Paid for Accrued Income`
- `Realized Losses`
- `Senior notes`

**COA_LEVEL_6**
- `None`
- `Ground`
- `Travel`
- `Non Travel`
- `Air`
- `Profit`
- `Sliding Scale Commissions`
- `Bank`
- `Mine Subsidence`
- `Brokerage Expense`

**IS_SECTION**
- `Expenses`
- `Revenue`
- `Income Taxes`

**IS_SECTION_SORT**
- `2`
- `1`
- `3`

**IS_LINE**
- `General & Administrative Expenses`
- `Underwriting Expenses`
- `Commission Income`
- `Net Premiums Earned`
- `Service & Fee Income`
- `Losses & Loss Adjustment Expenses`
- `Other Income`
- `Net Investment Income`
- `Contra Revenue`
- `Other Expenses`
- `Provision for Income Taxes`
- `Investment Expenses`
- `Interest Expense`
- `Net Realized Investment Gains (Losses)`

**IS_LINE_SORT**
- `150`
- `120`
- `30`
- `10`
- `20`
- `110`
- `70`
- `50`
- `40`
- `160`
- `210`
- `140`
- `130`
- `60`

**IS_SUB_LINE**
- `Personnel expenses`
- `Office expenses`
- `Commissions Income`
- `Commissions expense`
- `Taxes, licenses, and fees`
- `Marketing and travel expenses`
- `Claim Adjustment Income`
- `Written Premium`
- `Corporate expenses`
- `Change in Unearned Premium Reserve`
- `Loss Adjustment Expense incurred`
- `Losses incurred`
- `Other Underwriting Expenses`
- `Computer service expenses`
- `Regular`
- `Funds held interest`
- `Interest Income Received`
- `Inspection Fee Income`
- `Service / Fee Income`
- `Management fees`
- `Commission Refund Accrual`
- `Contra Revenue`
- `Installment Fee Income`
- `FX Gain/Loss`
- `Due and Accrued`
- `Current`
- `Notes payable`
- `Other Income`
- `Management Fee Income`
- `STAT Exp Allocation`
- `Surplus Note Interest (STAT)`
- `Investment Expense (Excl. Surplus Notes)`
- `Accretion of discount`
- `Investment Income Received`
- `Dividend Income Received`
- `Realized Gains`
- `Amortization of Premium`
- `Retroactive reinsurance gains (losses)`
- `Paid for Accrued Income`
- `Realized Losses`
- `Senior notes`

**BUSINESS_TYPE**
- `N/A`
- `Direct`
- `Assumed`
- `Ceded`

**PREMIUM_COMPONENT**
- `None`
- `Written Premium`
- `Change in UPR`

**KPI_COMPONENT**
- `None`
- `Underwriting Expenses`
- `Net Premiums Earned`
- `Losses & Loss Adjustment Expenses`

**IS_UNDERWRITING_ITEM**
- `False`
- `True`

**IS_INVESTMENT_ITEM**
- `False`
- `True`

**IS_PRE_TAX_ITEM**
- `True`
- `False`

**PROFIT_CENTER**
- `None`
- `Personal`
- `Property & Casualty Insurance`
- `Health Insurance`
- `Life Insurance`
- `Specialty`
- `Auto Insurance`
- `MAR`
- `Investment & Wealth Management`
- `Commercial`
- `0`
- `SLM`
- `CAI`
- `SLA`
- `SLO`
- `FLI`
- `FLM`
- `PRI`
- `PRN`
- `SLP`
- `TRP`
- `FLN`

**BUSINESS_INDICATOR**
- `None`
- `DIRECT`
- `New Business`
- `Claims Activity`
- `Customer Retention`
- `Cross-Sell / Up-Sell`
- `Policy Renewal`
- `CEDED`
- `CONCUR`
- `ASSUMED`
- `Up_sell`

**LINE_OF_BUSINESS**
- `None`
- `Direct_Customer`
- `Broker`
- `40`
- `10`
- `170`
- `270`
- `90`
- `21`
- `25`
- `Corporate`
- `Individual`
- `Reinsurance`
- `51`
- `52`
- `50`

**DOCUMENT_NUMBER**
- `None`

**JOURNAL_CATEGORY**
- `GeneralJournal`
- `None`
- `FixedAssets`
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
- `SEK`
- `AUD`
- `ZAR`
- `NOK`

**QUANTITY**
- `0`

**LAST_REFRESHED**
- `2026-11-16 11:42:42.223406+00:00`

## Empty columns

Empty in every row: `DOCUMENT_NUMBER`. Do not filter or group on them.
