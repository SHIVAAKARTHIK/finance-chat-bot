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
row_count: 22226
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
- `214`: 9407 rows
- `100`: 5161 rows
- `228`: 2603 rows
- `299`: 1557 rows
- `201`: 1038 rows
- `236`: 840 rows
- `UK07`: 347 rows
- `103`: 319 rows
- `208`: 213 rows
- `UK03`: 173 rows
- `233`: 142 rows
- `UK14`: 130 rows
- `UK17`: 104 rows
- `UK06`: 60 rows
- `101`: 49 rows
- `238`: 41 rows
- `UK13`: 40 rows
- `230`: 2 rows

**POSTING_LAYER**
- `Current`: 22070 rows
- `Operations`: 156 rows

**FISCAL_YEAR**
- `2026`: 10265 rows
- `2025`: 9800 rows
- `2024`: 2161 rows

**FISCAL_QUARTER**
- `3`: 6576 rows
- `1`: 5833 rows
- `2`: 5469 rows
- `4`: 4348 rows

**FISCAL_YEAR_QUARTER**
- `2026-Q3`: 4631 rows
- `2025-Q1`: 3391 rows
- `2026-Q2`: 3149 rows
- `2026-Q1`: 2442 rows
- `2025-Q2`: 2320 rows
- `2024-Q4`: 2161 rows
- `2025-Q4`: 2144 rows
- `2025-Q3`: 1945 rows
- `2026-Q4`: 43 rows

**FISCAL_MONTH**
- `9`: 3229 rows
- `12`: 2604 rows
- `6`: 2334 rows
- `3`: 2285 rows
- `1`: 1838 rows
- `8`: 1780 rows
- `4`: 1730 rows
- `2`: 1710 rows
- `7`: 1567 rows
- `5`: 1405 rows
- `11`: 1315 rows
- `10`: 429 rows

**FISCAL_MONTH_NAME**
- `Sep`: 3229 rows
- `Dec`: 2604 rows
- `Jun`: 2334 rows
- `Mar`: 2285 rows
- `Jan`: 1838 rows
- `Aug`: 1780 rows
- `Apr`: 1730 rows
- `Feb`: 1710 rows
- `Jul`: 1567 rows
- `May`: 1405 rows
- `Nov`: 1315 rows
- `Oct`: 429 rows

**PERIOD_START_DATE**
- `2024-12-01 00:00:00`: 2161 rows
- `2026-09-01 00:00:00`: 1936 rows
- `2026-08-01 00:00:00`: 1457 rows
- `2025-03-01 00:00:00`: 1412 rows
- `2025-11-01 00:00:00`: 1307 rows
- `2025-09-01 00:00:00`: 1293 rows
- `2026-07-01 00:00:00`: 1238 rows
- `2026-06-01 00:00:00`: 1179 rows
- `2025-06-01 00:00:00`: 1155 rows
- `2026-05-01 00:00:00`: 1113 rows
- `2025-01-01 00:00:00`: 1079 rows
- `2025-02-01 00:00:00`: 900 rows
- `2025-04-01 00:00:00`: 873 rows
- `2026-03-01 00:00:00`: 873 rows
- `2026-04-01 00:00:00`: 857 rows
- `2026-02-01 00:00:00`: 810 rows
- `2026-01-01 00:00:00`: 759 rows
- `2025-12-01 00:00:00`: 443 rows
- `2025-10-01 00:00:00`: 394 rows
- `2025-07-01 00:00:00`: 329 rows
- `2025-08-01 00:00:00`: 323 rows
- `2025-05-01 00:00:00`: 292 rows
- `2026-10-01 00:00:00`: 35 rows
- `2026-11-01 00:00:00`: 8 rows

**PERIOD_END_DATE**
- `2024-12-31 00:00:00`: 2161 rows
- `2026-09-30 00:00:00`: 1936 rows
- `2026-08-31 00:00:00`: 1457 rows
- `2025-03-31 00:00:00`: 1412 rows
- `2025-11-30 00:00:00`: 1307 rows
- `2025-09-30 00:00:00`: 1293 rows
- `2026-07-31 00:00:00`: 1238 rows
- `2026-06-30 00:00:00`: 1179 rows
- `2025-06-30 00:00:00`: 1155 rows
- `2026-05-31 00:00:00`: 1113 rows
- `2025-01-31 00:00:00`: 1079 rows
- `2025-02-28 00:00:00`: 900 rows
- `2025-04-30 00:00:00`: 873 rows
- `2026-03-31 00:00:00`: 873 rows
- `2026-04-30 00:00:00`: 857 rows
- `2026-02-28 00:00:00`: 810 rows
- `2026-01-31 00:00:00`: 759 rows
- `2025-12-31 00:00:00`: 443 rows
- `2025-10-31 00:00:00`: 394 rows
- `2025-07-31 00:00:00`: 329 rows
- `2025-08-31 00:00:00`: 323 rows
- `2025-05-31 00:00:00`: 292 rows
- `2026-10-31 00:00:00`: 35 rows
- `2026-11-30 00:00:00`: 8 rows

**AS_OF_DATE**
- `2026-11-02 00:00:00`: 22226 rows

**RELATIVE_YEAR**
- `0`: 10265 rows
- `-1`: 9800 rows
- `-2`: 2161 rows

**YEAR_COMPARISON**
- `Current Year`: 10265 rows
- `Prior Year`: 9800 rows
- `Earlier Years`: 2161 rows

**IS_YTD_COMPARABLE**
- `True`: 19325 rows
- `False`: 2901 rows

**IS_MTD_COMPARABLE**
- `False`: 21208 rows
- `True`: 1018 rows

**STAT_OR_MGA**
- `MGA`: 18600 rows
- `STAT`: 3626 rows

**REPORTING_BASIS**
- `MGA`: 18600 rows
- `Statutory (STAT)`: 3626 rows

**COA_MAPPING_STATUS**
- `Mapped`: 22063 rows
- `Inferred (account not in CoA MDM)`: 163 rows

**COA_LEVEL_0**
- `Income Statement`: 22226 rows

**COA_LEVEL_1**
- `Expense`: 18167 rows
- `Revenue`: 4059 rows

**COA_LEVEL_2**
- `General and Administrative`: 14137 rows
- `Underwriting expenses`: 3124 rows
- `Commissions Income`: 1822 rows
- `Premiums earned`: 985 rows
- `Service / Fee Income`: 934 rows
- `Loss and loss adjustment expenses`: 691 rows
- `Underwriting expenses (Commissions)`: 169 rows
- `Other Income`: 156 rows
- `Investment Income`: 143 rows
- `Contra Revenue`: 16 rows
- `Other Expenses`: 14 rows
- `Provision for Federal Taxes`: 12 rows
- `Investment expense`: 9 rows
- `Interest expense`: 8 rows
- `Realized investment gains (losses)`: 3 rows
- `Commissions Expense`: 3 rows

**COA_LEVEL_3**
- `Personnel expenses`: 10441 rows
- `Office expenses`: 2172 rows
- `Commissions Income`: 1802 rows
- `Commissions expense`: 1758 rows
- `Taxes, licenses, and fees`: 1006 rows
- `Marketing and travel expenses`: 940 rows
- `Claim Adjustment Income`: 855 rows
- `Written Premium`: 591 rows
- `Corporate expenses`: 411 rows
- `Change in Unearned Premium Reserve`: 394 rows
- `Loss Adjustment Expense incurred`: 346 rows
- `Losses incurred`: 345 rows
- `Other Underwriting Expenses`: 330 rows
- `Computer service expenses`: 173 rows
- `Regular`: 169 rows
- `Funds held interest`: 147 rows
- `Interest Income Received`: 119 rows
- `Inspection Fee Income`: 30 rows
- `Service / Fee Income`: 28 rows
- `Management fees`: 27 rows
- `Commission Refund Accrual`: 20 rows
- `Contra Revenue`: 16 rows
- `Installment Fee Income`: 15 rows
- `FX Gain/Loss`: 14 rows
- `Due and Accrued`: 13 rows
- `Current`: 12 rows
- `Notes payable`: 7 rows
- `Other Income`: 7 rows
- `Management Fee Income`: 7 rows
- `STAT Exp Allocation`: 6 rows
- `Surplus Note Interest (STAT)`: 5 rows
- `Investment Expense (Excl. Surplus Notes)`: 4 rows
- `Accretion of discount`: 3 rows
- `Investment Income Received`: 3 rows
- `Dividend Income Received`: 2 rows
- `Realized Gains`: 2 rows
- `Amortization of Premium`: 2 rows
- `Retroactive reinsurance gains (losses)`: 1 rows
- `Paid for Accrued Income`: 1 rows
- `Realized Losses`: 1 rows
- `Senior notes`: 1 rows

**COA_LEVEL_6**
- `None`: 21615 rows
- `Ground`: 255 rows
- `Travel`: 142 rows
- `Non Travel`: 125 rows
- `Air`: 80 rows
- `Profit`: 3 rows
- `Sliding Scale Commissions`: 2 rows
- `Bank`: 2 rows
- `Mine Subsidence`: 1 rows
- `Brokerage Expense`: 1 rows

**IS_SECTION**
- `Expenses`: 18155 rows
- `Revenue`: 4059 rows
- `Income Taxes`: 12 rows

**IS_SECTION_SORT**
- `2`: 18155 rows
- `1`: 4059 rows
- `3`: 12 rows

**IS_LINE**
- `General & Administrative Expenses`: 14137 rows
- `Underwriting Expenses`: 3296 rows
- `Commission Income`: 1822 rows
- `Net Premiums Earned`: 985 rows
- `Service & Fee Income`: 934 rows
- `Losses & Loss Adjustment Expenses`: 691 rows
- `Other Income`: 156 rows
- `Net Investment Income`: 143 rows
- `Contra Revenue`: 16 rows
- `Other Expenses`: 14 rows
- `Provision for Income Taxes`: 12 rows
- `Investment Expenses`: 9 rows
- `Interest Expense`: 8 rows
- `Net Realized Investment Gains (Losses)`: 3 rows

**IS_LINE_SORT**
- `150`: 14137 rows
- `120`: 3296 rows
- `30`: 1822 rows
- `10`: 985 rows
- `20`: 934 rows
- `110`: 691 rows
- `70`: 156 rows
- `50`: 143 rows
- `40`: 16 rows
- `160`: 14 rows
- `210`: 12 rows
- `140`: 9 rows
- `130`: 8 rows
- `60`: 3 rows

**IS_SUB_LINE**
- `Personnel expenses`: 10441 rows
- `Office expenses`: 2172 rows
- `Commissions Income`: 1802 rows
- `Commissions expense`: 1758 rows
- `Taxes, licenses, and fees`: 1006 rows
- `Marketing and travel expenses`: 940 rows
- `Claim Adjustment Income`: 855 rows
- `Written Premium`: 591 rows
- `Corporate expenses`: 411 rows
- `Change in Unearned Premium Reserve`: 394 rows
- `Loss Adjustment Expense incurred`: 346 rows
- `Losses incurred`: 345 rows
- `Other Underwriting Expenses`: 330 rows
- `Computer service expenses`: 173 rows
- `Regular`: 169 rows
- `Funds held interest`: 147 rows
- `Interest Income Received`: 119 rows
- `Inspection Fee Income`: 30 rows
- `Service / Fee Income`: 28 rows
- `Management fees`: 27 rows
- `Commission Refund Accrual`: 20 rows
- `Contra Revenue`: 16 rows
- `Installment Fee Income`: 15 rows
- `FX Gain/Loss`: 14 rows
- `Due and Accrued`: 13 rows
- `Current`: 12 rows
- `Notes payable`: 7 rows
- `Other Income`: 7 rows
- `Management Fee Income`: 7 rows
- `STAT Exp Allocation`: 6 rows
- `Surplus Note Interest (STAT)`: 5 rows
- `Investment Expense (Excl. Surplus Notes)`: 4 rows
- `Accretion of discount`: 3 rows
- `Investment Income Received`: 3 rows
- `Dividend Income Received`: 2 rows
- `Realized Gains`: 2 rows
- `Amortization of Premium`: 2 rows
- `Retroactive reinsurance gains (losses)`: 1 rows
- `Paid for Accrued Income`: 1 rows
- `Realized Losses`: 1 rows
- `Senior notes`: 1 rows

**BUSINESS_TYPE**
- `N/A`: 19889 rows
- `Direct`: 1463 rows
- `Assumed`: 712 rows
- `Ceded`: 162 rows

**PREMIUM_COMPONENT**
- `None`: 21241 rows
- `Written Premium`: 591 rows
- `Change in UPR`: 394 rows

**KPI_COMPONENT**
- `None`: 17254 rows
- `Underwriting Expenses`: 3296 rows
- `Net Premiums Earned`: 985 rows
- `Losses & Loss Adjustment Expenses`: 691 rows

**IS_UNDERWRITING_ITEM**
- `False`: 17254 rows
- `True`: 4972 rows

**IS_INVESTMENT_ITEM**
- `False`: 22071 rows
- `True`: 155 rows

**IS_PRE_TAX_ITEM**
- `True`: 22214 rows
- `False`: 12 rows

**PROFIT_CENTER**
- `None`: 14785 rows
- `Personal`: 2716 rows
- `Property & Casualty Insurance`: 925 rows
- `Health Insurance`: 917 rows
- `Life Insurance`: 710 rows
- `Specialty`: 699 rows
- `Auto Insurance`: 664 rows
- `MAR`: 308 rows
- `Investment & Wealth Management`: 192 rows
- `Commercial`: 125 rows
- `0`: 52 rows
- `SLM`: 26 rows
- `CAI`: 25 rows
- `SLA`: 23 rows
- `SLO`: 17 rows
- `FLI`: 14 rows
- `FLM`: 9 rows
- `PRI`: 7 rows
- `PRN`: 5 rows
- `SLP`: 3 rows
- `TRP`: 3 rows
- `FLN`: 1 rows

**BUSINESS_INDICATOR**
- `None`: 15188 rows
- `DIRECT`: 3385 rows
- `New Business`: 1281 rows
- `Claims Activity`: 1204 rows
- `Customer Retention`: 540 rows
- `Cross-Sell / Up-Sell`: 191 rows
- `Policy Renewal`: 188 rows
- `CEDED`: 138 rows
- `CONCUR`: 74 rows
- `ASSUMED`: 29 rows
- `Up_sell`: 8 rows

**LINE_OF_BUSINESS**
- `None`: 15394 rows
- `Direct_Customer`: 1434 rows
- `Broker`: 1286 rows
- `40`: 691 rows
- `10`: 484 rows
- `170`: 477 rows
- `270`: 464 rows
- `90`: 442 rows
- `21`: 416 rows
- `25`: 343 rows
- `Corporate`: 321 rows
- `Individual`: 192 rows
- `Reinsurance`: 175 rows
- `51`: 69 rows
- `52`: 37 rows
- `50`: 1 rows

**DOCUMENT_NUMBER**
- `None`: 22226 rows

**JOURNAL_CATEGORY**
- `GeneralJournal`: 18484 rows
- `None`: 1877 rows
- `FixedAssets`: 1793 rows
- `Vend`: 66 rows
- `Allocation`: 6 rows

**POSTING_TYPE**
- `LedgerJournal`: 20315 rows
- `None`: 1876 rows
- `FixedAssetsCredit`: 15 rows
- `FixedAssetsDebit`: 13 rows
- `MSTDiffSecond`: 4 rows
- `MSTDiff`: 3 rows

**SOURCE_SYSTEM**
- `D365`: 19250 rows
- `Fynapse`: 2976 rows

**IS_CREDIT**
- `No`: 16107 rows
- `Yes`: 6119 rows

**IS_CORRECTION**
- `No`: 22226 rows

**TRANSACTION_CURRENCY_CODE**
- `USD`: 21732 rows
- `GBP`: 355 rows
- `EUR`: 105 rows
- `CAD`: 18 rows
- `SEK`: 9 rows
- `AUD`: 4 rows
- `ZAR`: 2 rows
- `NOK`: 1 rows

**QUANTITY**
- `0`: 22226 rows

**LAST_REFRESHED**
- `2026-11-16 11:42:42.223406+00:00`: 22226 rows

## Profile

Rows in the latest export: 22226.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ENTRY_REC_ID` | STRING | 22948 | 0 | 5637211377 | 5637313862 |
| `LEGAL_ENTITY_CODE` | STRING | 18 | 0 |  |  |
| `LEGAL_ENTITY_NAME` | STRING | 18 | 0 |  |  |
| `LEDGER_NAME` | STRING | 18 | 0 | 100 | UK17 |
| `POSTING_LAYER` | STRING | 2 | 0 | Current | Operations |
| `ACCOUNTING_DATE` | DATE | 367 | 0 | 2024-12-31 00:00:00 | 2026-11-02 00:00:00 |
| `FISCAL_YEAR` | INT | 3 | 0 | 2024 | 2026 |
| `FISCAL_QUARTER` | INT | 4 | 0 | 1 | 4 |
| `FISCAL_YEAR_QUARTER` | STRING | 9 | 0 | 2024-Q4 | 2026-Q4 |
| `FISCAL_MONTH` | INT | 12 | 0 | 1 | 12 |
| `FISCAL_MONTH_NAME` | STRING | 12 | 0 | Apr | Sep |
| `FISCAL_YEAR_MONTH` | STRING | 22 | 0 |  |  |
| `FISCAL_PERIOD_KEY` | INT | 24 | 0 |  |  |
| `PERIOD_START_DATE` | DATE | 25 | 0 | 2024-12-01 00:00:00 | 2026-11-01 00:00:00 |
| `PERIOD_END_DATE` | DATE | 24 | 0 | 2024-12-31 00:00:00 | 2026-11-30 00:00:00 |
| `DOCUMENT_DATE` | DATE | 70 | 0 | 1900-01-02 00:00:00 | 2026-01-30 00:00:00 |
| `AS_OF_DATE` | DATE | 1 | 0 | 2026-11-02 00:00:00 | 2026-11-02 00:00:00 |
| `RELATIVE_YEAR` | INT | 3 | 0 | -2 | 0 |
| `YEAR_COMPARISON` | STRING | 3 | 0 | Current Year | Prior Year |
| `IS_YTD_COMPARABLE` | BOOLEAN | 2 | 0 | False | True |
| `IS_MTD_COMPARABLE` | BOOLEAN | 2 | 0 | False | True |
| `MAIN_ACCOUNT` | STRING | 154 | 0 | 411100 | 591000 |
| `ACCOUNT_NAME` | STRING | 165 | 0 | 401k Contribution | Written Premium - Direct |
| `ACCOUNT_LABEL` | STRING | 170 | 0 | 411100 - Written Premium - Direct | 591000 - Provision for Federal Taxes ... |
| `STAT_OR_MGA` | STRING | 2 | 0 | MGA | STAT |
| `REPORTING_BASIS` | STRING | 2 | 0 | MGA | Statutory (STAT) |
| `COA_MAPPING_STATUS` | STRING | 2 | 0 | Inferred (account not in CoA MDM) | Mapped |
| `COA_LEVEL_0` | STRING | 1 | 0 | Income Statement | Income Statement |
| `COA_LEVEL_1` | STRING | 2 | 0 | Expense | Revenue |
| `COA_LEVEL_2` | STRING | 16 | 0 | Commissions Expense | Underwriting expenses (Commissions) |
| `COA_LEVEL_3` | STRING | 42 | 0 | Accretion of discount | Written Premium |
| `COA_LEVEL_4` | STRING | 80 | 177 | Accumulated depreciation | Underwriting Expense |
| `COA_LEVEL_5` | STRING | 64 | 17403 | 401k Contribution | Workers Comp |
| `COA_LEVEL_6` | STRING | 9 | 21615 | Air | Travel |
| `IS_SECTION` | STRING | 3 | 0 | Expenses | Revenue |
| `IS_SECTION_SORT` | INT | 3 | 0 | 1 | 3 |
| `IS_LINE` | STRING | 13 | 0 | Commission Income | Underwriting Expenses |
| `IS_LINE_SORT` | INT | 14 | 0 | 10 | 210 |
| `IS_SUB_LINE` | STRING | 42 | 0 | Accretion of discount | Written Premium |
| `BUSINESS_TYPE` | STRING | 4 | 0 | Assumed | N/A |
| `PREMIUM_COMPONENT` | STRING | 2 | 21241 | Change in UPR | Written Premium |
| `KPI_COMPONENT` | STRING | 3 | 17254 | Losses & Loss Adjustment Expenses | Underwriting Expenses |
| `IS_UNDERWRITING_ITEM` | BOOLEAN | 2 | 0 | False | True |
| `IS_INVESTMENT_ITEM` | BOOLEAN | 2 | 0 | False | True |
| `IS_PRE_TAX_ITEM` | BOOLEAN | 2 | 0 | False | True |
| `COST_CENTER` | STRING | 91 | 5247 | 0 | Wealth Advisory Services |
| `PROFIT_CENTER` | STRING | 21 | 14785 | 0 | TRP |
| `BUSINESS_INDICATOR` | STRING | 10 | 15188 | ASSUMED | Up_sell |
| `LINE_OF_BUSINESS` | STRING | 15 | 15394 | 10 | Reinsurance |
| `FINANCIAL_DIMENSIONS` | STRING | 530 | 319 | ---- | Wealth Advisory Services-Property & C... |
| `LEDGER_ACCOUNT` | STRING | 2667 | 0 | 411100 | 591000---------- |
| `JOURNAL_NUMBER` | STRING | 7687 | 0 | 100-000097 | UK17-000066 |
| `VOUCHER` | STRING | 7050 | 1876 | 100-00000001 | YMH957678142 |
| `DOCUMENT_NUMBER` | STRING | 0 | 22226 |  |  |
| `LINE_DESCRIPTION` | STRING | 8963 | 5473 | 000076\|JR OMLZLLN ZHV | soft drink on Monte Carlo business trip |
| `JOURNAL_CATEGORY` | STRING | 5 | 0 | Allocation | Vend |
| `POSTING_TYPE` | STRING | 6 | 0 | FixedAssetsCredit | None |
| `SOURCE_SYSTEM` | STRING | 2 | 0 | D365 | Fynapse |
| `IS_CREDIT` | STRING | 2 | 0 | No | Yes |
| `IS_CORRECTION` | STRING | 1 | 0 | No | No |
| `TRANSACTION_CURRENCY_CODE` | STRING | 7 | 0 | AUD | ZAR |
| `GL_AMOUNT` | DECIMAL | 12624 | 0 | -523388273.95 | 523388273.95 |
| `PL_AMOUNT` | DECIMAL | 12449 | 0 | -523388273.95 | 523388273.95 |
| `REPORT_AMOUNT` | DECIMAL | 12526 | 0 | -523388273.95 | 523388273.95 |
| `DEBIT_AMOUNT` | DECIMAL | 7841 | 0 | 0 | 523388273.95 |
| `CREDIT_AMOUNT` | DECIMAL | 4569 | 0 | 0 | 523388273.95 |
| `CY_PL_AMOUNT` | DECIMAL | 5220 | 11961 | -26885967.71 | 39744184.4 |
| `PY_PL_AMOUNT` | DECIMAL | 5509 | 12426 | -26422374.9 | 39058895.38 |
| `CY_REPORT_AMOUNT` | DECIMAL | 5118 | 11961 | -6109343.75 | 39744184.4 |
| `PY_REPORT_AMOUNT` | DECIMAL | 5738 | 12426 | -14671934.43 | 39058895.38 |
| `PL_AMOUNT_REPORTING_CCY` | DECIMAL | 12436 | 0 | -523388273.95 | 523388273.95 |
| `REPORTING_CURRENCY_AMOUNT` | DECIMAL | 12857 | 0 | -523388273.95 | 523388273.95 |
| `TRANSACTION_CURRENCY_AMOUNT` | DECIMAL | 12604 | 0 | -523388273.95 | 523388273.95 |
| `QUANTITY` | DECIMAL | 1 | 0 | 0 | 0 |
| `LAST_REFRESHED` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:42.223000 | 2026-11-16 11:42:42.223000 |

## Sample rows

| ENTRY_REC_ID | LEDGER_NAME | POSTING_LAYER | ACCOUNTING_DATE | FISCAL_YEAR | FISCAL_QUARTER | FISCAL_YEAR_QUARTER | FISCAL_MONTH | FISCAL_MONTH_NAME | FISCAL_YEAR_MONTH | PERIOD_START_DATE | PERIOD_END_DATE | DOCUMENT_DATE | AS_OF_DATE | RELATIVE_YEAR | YEAR_COMPARISON | IS_YTD_COMPARABLE | IS_MTD_COMPARABLE | MAIN_ACCOUNT | ACCOUNT_NAME | ACCOUNT_LABEL | STAT_OR_MGA | REPORTING_BASIS | COA_MAPPING_STATUS | COA_LEVEL_0 | COA_LEVEL_1 | COA_LEVEL_2 | COA_LEVEL_3 | COA_LEVEL_4 | COA_LEVEL_5 | COA_LEVEL_6 | IS_SECTION | IS_SECTION_SORT | IS_LINE | IS_LINE_SORT | IS_SUB_LINE | BUSINESS_TYPE | PREMIUM_COMPONENT | KPI_COMPONENT | IS_UNDERWRITING_ITEM | IS_INVESTMENT_ITEM | IS_PRE_TAX_ITEM | COST_CENTER | PROFIT_CENTER | BUSINESS_INDICATOR | LINE_OF_BUSINESS | FINANCIAL_DIMENSIONS | LEDGER_ACCOUNT | JOURNAL_NUMBER | VOUCHER | DOCUMENT_NUMBER | LINE_DESCRIPTION | JOURNAL_CATEGORY | POSTING_TYPE | SOURCE_SYSTEM | IS_CREDIT | IS_CORRECTION | TRANSACTION_CURRENCY_CODE | GL_AMOUNT | PL_AMOUNT | REPORT_AMOUNT | DEBIT_AMOUNT | CREDIT_AMOUNT | CY_PL_AMOUNT | PY_PL_AMOUNT | CY_REPORT_AMOUNT | PY_REPORT_AMOUNT | PL_AMOUNT_REPORTING_CCY | REPORTING_CURRENCY_AMOUNT | TRANSACTION_CURRENCY_AMOUNT | QUANTITY | LAST_REFRESHED |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5637271137 | 228 | Current | 2026-06-01 00:00:00 | 2026 | 2 | 2026-Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 2026-06-30 00:00:00 | 1900-01-02 00:00:00 | 2026-11-02 00:00:00 | 0 | Current Year | True | False | 430000 | Commissions Income | 430000 - Commissions Income | MGA | MGA | Mapped | Income Statement | Revenue | Commissions Income | Commissions Income | Commissions Income | NULL | NULL | Revenue | 1 | Commission Income | 30 | Commissions Income | N/A | NULL | NULL | False | False | True | 0 | Personal | DIRECT | 10 | 000-Personal-DIRECT-010--0000---- | 430000-000-Personal-DIRECT-010--0000---- | 228-000048 | GJV-000000001 | NULL | 682269\|Lzz 7708 Wqxl tfxvgk | GeneralJournal | LedgerJournal | D365 | Yes | No | USD | -66908.18 | 66908.18 | 66908.18 | 0 | 66908.18 | 66908.18 | NULL | 66908.18 | NULL | 66908.18 | -66908.18 | -66908.18 | 0 | 2026-11-16 11:42:42.223000 |
| 5637271138 | 228 | Current | 2026-06-01 00:00:00 | 2026 | 2 | 2026-Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 2026-06-30 00:00:00 | 1900-01-02 00:00:00 | 2026-11-02 00:00:00 | 0 | Current Year | True | False | 430000 | Commissions Income | 430000 - Commissions Income | MGA | MGA | Mapped | Income Statement | Revenue | Commissions Income | Commissions Income | Commissions Income | NULL | NULL | Revenue | 1 | Commission Income | 30 | Commissions Income | N/A | NULL | NULL | False | False | True | 0 | Personal | DIRECT | 21 | 000-Personal-DIRECT-021--0000---- | 430000-000-Personal-DIRECT-021--0000---- | 228-000048 | GJV-000000001 | NULL | 379345\|Lzz 7708 Wqxl tfxvgk | GeneralJournal | LedgerJournal | D365 | Yes | No | USD | -384970.53 | 384970.53 | 384970.53 | 0 | 384970.53 | 384970.53 | NULL | 384970.53 | NULL | 384970.53 | -384970.53 | -384970.53 | 0 | 2026-11-16 11:42:42.223000 |
| 5637271139 | 228 | Current | 2026-06-01 00:00:00 | 2026 | 2 | 2026-Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 2026-06-30 00:00:00 | 1900-01-02 00:00:00 | 2026-11-02 00:00:00 | 0 | Current Year | True | False | 430000 | Commissions Income | 430000 - Commissions Income | MGA | MGA | Mapped | Income Statement | Revenue | Commissions Income | Commissions Income | Commissions Income | NULL | NULL | Revenue | 1 | Commission Income | 30 | Commissions Income | N/A | NULL | NULL | False | False | True | 0 | Personal | DIRECT | 25 | 000-Personal-DIRECT-025--0000---- | 430000-000-Personal-DIRECT-025--0000---- | 228-000048 | GJV-000000001 | NULL | 225844\|Lzz 7708 Wqxl tfxvgk | GeneralJournal | LedgerJournal | D365 | Yes | No | USD | -1281.38 | 1281.38 | 1281.38 | 0 | 1281.38 | 1281.38 | NULL | 1281.38 | NULL | 1281.38 | -1281.38 | -1281.38 | 0 | 2026-11-16 11:42:42.223000 |
| 5637271140 | 228 | Current | 2026-06-01 00:00:00 | 2026 | 2 | 2026-Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 2026-06-30 00:00:00 | 1900-01-02 00:00:00 | 2026-11-02 00:00:00 | 0 | Current Year | True | False | 430000 | Commissions Income | 430000 - Commissions Income | MGA | MGA | Mapped | Income Statement | Revenue | Commissions Income | Commissions Income | Commissions Income | NULL | NULL | Revenue | 1 | Commission Income | 30 | Commissions Income | N/A | NULL | NULL | False | False | True | 0 | Personal | DIRECT | 40 | 000-Personal-DIRECT-040--0000---- | 430000-000-Personal-DIRECT-040--0000---- | 228-000048 | GJV-000000001 | NULL | 611951\|Lzz 7708 Wqxl tfxvgk | GeneralJournal | LedgerJournal | D365 | Yes | No | USD | -1180191.85 | 1180191.85 | 1180191.85 | 0 | 1180191.85 | 1180191.85 | NULL | 1180191.85 | NULL | 1180191.85 | -1180191.85 | -1180191.85 | 0 | 2026-11-16 11:42:42.223000 |
| 5637271141 | 228 | Current | 2026-06-01 00:00:00 | 2026 | 2 | 2026-Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 2026-06-30 00:00:00 | 1900-01-02 00:00:00 | 2026-11-02 00:00:00 | 0 | Current Year | True | False | 430000 | Commissions Income | 430000 - Commissions Income | MGA | MGA | Mapped | Income Statement | Revenue | Commissions Income | Commissions Income | Commissions Income | NULL | NULL | Revenue | 1 | Commission Income | 30 | Commissions Income | N/A | NULL | NULL | False | False | True | 0 | Personal | DIRECT | 90 | 000-Personal-DIRECT-090--0000---- | 430000-000-Personal-DIRECT-090--0000---- | 228-000048 | GJV-000000001 | NULL | 052683\|Lzz 7708 Wqxl tfxvgk | GeneralJournal | LedgerJournal | D365 | Yes | No | USD | -1071.85 | 1071.85 | 1071.85 | 0 | 1071.85 | 1071.85 | NULL | 1071.85 | NULL | 1071.85 | -1071.85 | -1071.85 | 0 | 2026-11-16 11:42:42.223000 |
