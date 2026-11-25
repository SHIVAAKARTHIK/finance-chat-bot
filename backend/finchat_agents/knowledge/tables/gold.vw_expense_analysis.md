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
row_count: 18167
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
- `214`: 8813 rows
- `100`: 4268 rows
- `228`: 1452 rows
- `299`: 1050 rows
- `201`: 912 rows
- `236`: 653 rows
- `103`: 224 rows
- `208`: 212 rows
- `UK14`: 130 rows
- `233`: 124 rows
- `UK03`: 69 rows
- `UK17`: 65 rows
- `UK06`: 60 rows
- `UK07`: 47 rows
- `UK13`: 40 rows
- `238`: 31 rows
- `101`: 17 rows

**POSTING_LAYER**
- `Current`: 18035 rows
- `Operations`: 132 rows

**POSTING_YEAR**
- `2025`: 8164 rows
- `2026`: 8095 rows
- `2024`: 1908 rows

**POSTING_QUARTER**
- `3`: 5165 rows
- `1`: 4746 rows
- `2`: 4543 rows
- `4`: 3713 rows

**POSTING_QUARTER_LABEL**
- `Q3`: 5165 rows
- `Q1`: 4746 rows
- `Q2`: 4543 rows
- `Q4`: 3713 rows

**POSTING_MONTH**
- `9`: 2516 rows
- `12`: 2232 rows
- `6`: 1996 rows
- `3`: 1944 rows
- `4`: 1416 rows
- `1`: 1406 rows
- `2`: 1396 rows
- `8`: 1387 rows
- `7`: 1262 rows
- `11`: 1166 rows
- `5`: 1131 rows
- `10`: 315 rows

**POSTING_MONTH_NAME**
- `Sep`: 2516 rows
- `Dec`: 2232 rows
- `Jun`: 1996 rows
- `Mar`: 1944 rows
- `Apr`: 1416 rows
- `Jan`: 1406 rows
- `Feb`: 1396 rows
- `Aug`: 1387 rows
- `Jul`: 1262 rows
- `Nov`: 1166 rows
- `May`: 1131 rows
- `Oct`: 315 rows

**POSTING_MONTH_START**
- `2024-12-01 00:00:00`: 1908 rows
- `2026-09-01 00:00:00`: 1288 rows
- `2025-09-01 00:00:00`: 1228 rows
- `2025-03-01 00:00:00`: 1174 rows
- `2025-11-01 00:00:00`: 1158 rows
- `2025-06-01 00:00:00`: 1110 rows
- `2026-08-01 00:00:00`: 1109 rows
- `2026-07-01 00:00:00`: 960 rows
- `2026-06-01 00:00:00`: 886 rows
- `2026-05-01 00:00:00`: 872 rows
- `2026-03-01 00:00:00`: 770 rows
- `2026-04-01 00:00:00`: 768 rows
- `2025-01-01 00:00:00`: 730 rows
- `2026-02-01 00:00:00`: 723 rows
- `2026-01-01 00:00:00`: 676 rows
- `2025-02-01 00:00:00`: 673 rows
- `2025-04-01 00:00:00`: 648 rows
- `2025-12-01 00:00:00`: 324 rows
- `2025-07-01 00:00:00`: 302 rows
- `2025-10-01 00:00:00`: 280 rows
- `2025-08-01 00:00:00`: 278 rows
- `2025-05-01 00:00:00`: 259 rows
- `2026-10-01 00:00:00`: 35 rows
- `2026-11-01 00:00:00`: 8 rows

**EXPENSE_CATEGORY**
- `Personnel expenses`: 10296 rows
- `Office expenses`: 2172 rows
- `Commissions Expense`: 1399 rows
- `Premium taxes`: 871 rows
- `Marketing & travel`: 815 rows
- `Loss and loss adjustment expenses`: 691 rows
- `Corporate expenses`: 317 rows
- `Underwriting expenses`: 298 rows
- `Commission and Brokerage - Direct`: 266 rows
- `Salaries expense`: 264 rows
- `Uncategorized`: 177 rows
- `Other underwriting expenses`: 153 rows
- `Computer service expenses`: 142 rows
- `Other taxes, licenses, and fees`: 41 rows
- `Bad Debt Expense`: 37 rows
- `Gain or loss on asset disposal`: 33 rows
- `Consulting Fees`: 31 rows
- `Corporate taxes`: 28 rows
- `Management fees`: 27 rows
- `Interest expense`: 23 rows
- `Commissions - Net`: 23 rows
- `Investment expense`: 14 rows
- `Federal taxes incurred (Current)`: 12 rows
- `Tax Fees`: 9 rows
- `Deferred Compensation Expense`: 9 rows
- `Surplus note interest`: 5 rows
- `Unamortized loan costs`: 5 rows
- `ULAE incurred`: 4 rows
- `Fines & Penalties`: 3 rows
- `UW expense (Pg. 11 STAT Alloc.)`: 2 rows

**EXPENSE_GROUP**
- `Operating & Administrative Expenses`: 14137 rows
- `Underwriting & Acquisition Expenses`: 3296 rows
- `Losses & Loss Adjustment Expenses`: 691 rows
- `Other Expenses`: 14 rows
- `Income Taxes`: 12 rows
- `Investment & Financing Expenses`: 9 rows
- `Interest Expense`: 8 rows

**EXPENSE_GROUP_SORT**
- `5`: 14137 rows
- `2`: 3296 rows
- `1`: 691 rows
- `7`: 14 rows
- `6`: 12 rows
- `4`: 9 rows
- `3`: 8 rows

**BUSINESS_TYPE**
- `N/A`: 16816 rows
- `Direct`: 932 rows
- `Assumed`: 374 rows
- `Ceded`: 45 rows

**MAIN_ACCOUNT_TYPE**
- `Expense`: 18113 rows
- `ProfitAndLoss`: 54 rows

**DEBIT_CREDIT_DEFAULT**
- `Debit`: 18004 rows
- `None`: 163 rows

**PROFIT_CENTER**
- `None`: 13933 rows
- `Personal`: 1238 rows
- `Property & Casualty Insurance`: 639 rows
- `Health Insurance`: 637 rows
- `Life Insurance`: 520 rows
- `Auto Insurance`: 507 rows
- `Specialty`: 388 rows
- `Investment & Wealth Management`: 180 rows
- `Commercial`: 75 rows
- `0`: 48 rows
- `CAI`: 1 rows
- `MAR`: 1 rows

**BUSINESS_INDICATOR**
- `None`: 13890 rows
- `DIRECT`: 1667 rows
- `New Business`: 897 rows
- `Claims Activity`: 835 rows
- `Customer Retention`: 389 rows
- `Cross-Sell / Up-Sell`: 181 rows
- `Policy Renewal`: 177 rows
- `CONCUR`: 74 rows
- `CEDED`: 26 rows
- `ASSUMED`: 23 rows
- `Up_sell`: 8 rows

**LINE_OF_BUSINESS**
- `None`: 13767 rows
- `Direct_Customer`: 978 rows
- `Broker`: 902 rows
- `40`: 400 rows
- `170`: 282 rows
- `10`: 278 rows
- `270`: 263 rows
- `Corporate`: 257 rows
- `90`: 253 rows
- `21`: 207 rows
- `Individual`: 181 rows
- `25`: 170 rows
- `Reinsurance`: 165 rows
- `51`: 36 rows
- `52`: 28 rows

**DOCUMENT_NUMBER**
- `None`: 18167 rows

**JOURNAL_CATEGORY**
- `GeneralJournal`: 15027 rows
- `FixedAssets`: 1793 rows
- `None`: 1275 rows
- `Vend`: 66 rows
- `Allocation`: 6 rows

**POSTING_TYPE**
- `LedgerJournal`: 16858 rows
- `None`: 1274 rows
- `FixedAssetsCredit`: 15 rows
- `FixedAssetsDebit`: 13 rows
- `MSTDiffSecond`: 4 rows
- `MSTDiff`: 3 rows

**SOURCE_SYSTEM**
- `D365`: 16341 rows
- `Fynapse`: 1826 rows

**IS_CREDIT**
- `No`: 15274 rows
- `Yes`: 2893 rows

**IS_CORRECTION**
- `No`: 18167 rows

**TRANSACTION_CURRENCY_CODE**
- `USD`: 17775 rows
- `GBP`: 322 rows
- `EUR`: 59 rows
- `CAD`: 6 rows
- `AUD`: 3 rows
- `SEK`: 1 rows
- `NOK`: 1 rows

**QUANTITY**
- `0`: 18167 rows

**LAST_REFRESHED**
- `2026-11-16 11:42:42.223406+00:00`: 18167 rows

## Profile

Rows in the latest export: 18167.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ENTRY_REC_ID` | STRING | 17756 | 0 | 5637211377 | 5637313862 |
| `LEGAL_ENTITY_CODE` | STRING | 17 | 0 |  |  |
| `LEGAL_ENTITY_NAME` | STRING | 17 | 0 |  |  |
| `LEDGER_NAME` | STRING | 17 | 0 | 100 | UK17 |
| `POSTING_LAYER` | STRING | 2 | 0 | Current | Operations |
| `ACCOUNTING_DATE` | DATE | 286 | 0 | 2024-12-31 00:00:00 | 2026-11-02 00:00:00 |
| `POSTING_YEAR` | INT | 3 | 0 | 2024 | 2026 |
| `POSTING_QUARTER` | INT | 4 | 0 | 1 | 4 |
| `POSTING_QUARTER_LABEL` | STRING | 4 | 0 | Q1 | Q4 |
| `POSTING_MONTH` | INT | 12 | 0 | 1 | 12 |
| `POSTING_MONTH_NAME` | STRING | 12 | 0 | Apr | Sep |
| `POSTING_YEAR_MONTH` | STRING | 22 | 0 |  |  |
| `POSTING_MONTH_START` | DATE | 25 | 0 | 2024-12-01 00:00:00 | 2026-11-01 00:00:00 |
| `DOCUMENT_DATE` | DATE | 70 | 0 | 1900-01-02 00:00:00 | 2026-01-30 00:00:00 |
| `MAIN_ACCOUNT` | STRING | 106 | 0 | 511110 | 591000 |
| `ACCOUNT_DESCRIPTION` | STRING | 123 | 0 | 401k Contribution | Utilities |
| `ACCOUNT_LABEL` | STRING | 123 | 0 | 511110 - Paid Losses - Direct | 591000 - Provision for Federal Taxes ... |
| `EXPENSE_CATEGORY` | STRING | 31 | 0 | Bad Debt Expense | Underwriting expenses |
| `EXPENSE_GROUP` | STRING | 7 | 0 | Income Taxes | Underwriting & Acquisition Expenses |
| `EXPENSE_GROUP_SORT` | INT | 7 | 0 | 1 | 7 |
| `BUSINESS_TYPE` | STRING | 4 | 0 | Assumed | N/A |
| `MAIN_ACCOUNT_TYPE` | STRING | 2 | 0 | Expense | ProfitAndLoss |
| `DEBIT_CREDIT_DEFAULT` | STRING | 1 | 163 | Debit | Debit |
| `COST_CENTER` | STRING | 91 | 3985 | 0 | Wealth Advisory Services |
| `PROFIT_CENTER` | STRING | 11 | 13933 | 0 | Specialty |
| `BUSINESS_INDICATOR` | STRING | 10 | 13890 | ASSUMED | Up_sell |
| `LINE_OF_BUSINESS` | STRING | 14 | 13767 | 10 | Reinsurance |
| `LEDGER_ACCOUNT` | STRING | 2368 | 0 | 511110 | 591000---------- |
| `JOURNAL_NUMBER` | STRING | 6249 | 0 | 100-000097 | UK17-000066 |
| `VOUCHER` | STRING | 6027 | 1274 | 100-00000001 | YMH957678142 |
| `DOCUMENT_NUMBER` | STRING | 0 | 18167 |  |  |
| `LINE_DESCRIPTION` | STRING | 6747 | 3928 | 000076\|JR OMLZLLN ZHV | soft drink on Monte Carlo business trip |
| `JOURNAL_CATEGORY` | STRING | 5 | 0 | Allocation | Vend |
| `POSTING_TYPE` | STRING | 6 | 0 | FixedAssetsCredit | None |
| `SOURCE_SYSTEM` | STRING | 2 | 0 | D365 | Fynapse |
| `IS_CREDIT` | STRING | 2 | 0 | No | Yes |
| `IS_CORRECTION` | STRING | 1 | 0 | No | No |
| `TRANSACTION_CURRENCY_CODE` | STRING | 7 | 0 | AUD | USD |
| `EXPENSE_AMOUNT` | DECIMAL | 9282 | 0 | -523388273.95 | 523388273.95 |
| `DEBIT_AMOUNT` | DECIMAL | 7291 | 0 | 0 | 523388273.95 |
| `CREDIT_AMOUNT` | DECIMAL | 1843 | 0 | 0 | 523388273.95 |
| `REPORTING_CURRENCY_AMOUNT` | DECIMAL | 9349 | 0 | -523388273.95 | 523388273.95 |
| `TRANSACTION_CURRENCY_AMOUNT` | DECIMAL | 9296 | 0 | -523388273.95 | 523388273.95 |
| `QUANTITY` | DECIMAL | 1 | 0 | 0 | 0 |
| `LAST_REFRESHED` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:42.223000 | 2026-11-16 11:42:42.223000 |

## Sample rows

| ENTRY_REC_ID | LEDGER_NAME | POSTING_LAYER | ACCOUNTING_DATE | POSTING_YEAR | POSTING_QUARTER | POSTING_QUARTER_LABEL | POSTING_MONTH | POSTING_MONTH_NAME | POSTING_YEAR_MONTH | POSTING_MONTH_START | DOCUMENT_DATE | MAIN_ACCOUNT | ACCOUNT_DESCRIPTION | ACCOUNT_LABEL | EXPENSE_CATEGORY | EXPENSE_GROUP | EXPENSE_GROUP_SORT | BUSINESS_TYPE | MAIN_ACCOUNT_TYPE | DEBIT_CREDIT_DEFAULT | COST_CENTER | PROFIT_CENTER | BUSINESS_INDICATOR | LINE_OF_BUSINESS | LEDGER_ACCOUNT | JOURNAL_NUMBER | VOUCHER | DOCUMENT_NUMBER | LINE_DESCRIPTION | JOURNAL_CATEGORY | POSTING_TYPE | SOURCE_SYSTEM | IS_CREDIT | IS_CORRECTION | TRANSACTION_CURRENCY_CODE | EXPENSE_AMOUNT | DEBIT_AMOUNT | CREDIT_AMOUNT | REPORTING_CURRENCY_AMOUNT | TRANSACTION_CURRENCY_AMOUNT | QUANTITY | LAST_REFRESHED |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5637271144 | 228 | Current | 2026-06-01 00:00:00 | 2026 | 2 | Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 1900-01-02 00:00:00 | 521100 | Commissions Expense | 521100 - Commissions Expense | Commissions Expense | Underwriting & Acquisition Expenses | 2 | N/A | Expense | Debit | 0 | Personal | DIRECT | 10 | 521100-000-Personal-DIRECT-010--0000---- | 228-000048 | GJV-000000001 | NULL | 680189\|Tml 7249 Oubf gfigp jyghgpy | GeneralJournal | LedgerJournal | D365 | No | No | USD | 45265.03 | 45265.03 | 0 | 45265.03 | 45265.03 | 0 | 2026-11-16 11:42:42.223000 |
| 5637271145 | 228 | Current | 2026-06-01 00:00:00 | 2026 | 2 | Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 1900-01-02 00:00:00 | 521100 | Commissions Expense | 521100 - Commissions Expense | Commissions Expense | Underwriting & Acquisition Expenses | 2 | N/A | Expense | Debit | 0 | Personal | DIRECT | 21 | 521100-000-Personal-DIRECT-021--0000---- | 228-000048 | GJV-000000001 | NULL | 310832\|Tml 7249 Oubf gfigp jyghgpy | GeneralJournal | LedgerJournal | D365 | No | No | USD | 260425.67 | 260425.67 | 0 | 260425.67 | 260425.67 | 0 | 2026-11-16 11:42:42.223000 |
| 5637271146 | 228 | Current | 2026-06-01 00:00:00 | 2026 | 2 | Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 1900-01-02 00:00:00 | 521100 | Commissions Expense | 521100 - Commissions Expense | Commissions Expense | Underwriting & Acquisition Expenses | 2 | N/A | Expense | Debit | 0 | Personal | DIRECT | 25 | 521100-000-Personal-DIRECT-025--0000---- | 228-000048 | GJV-000000001 | NULL | 993039\|Tml 7249 Oubf gfigp jyghgpy | GeneralJournal | LedgerJournal | D365 | No | No | USD | 866.85 | 866.85 | 0 | 866.85 | 866.85 | 0 | 2026-11-16 11:42:42.223000 |
| 5637271147 | 228 | Current | 2026-06-01 00:00:00 | 2026 | 2 | Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 1900-01-02 00:00:00 | 521100 | Commissions Expense | 521100 - Commissions Expense | Commissions Expense | Underwriting & Acquisition Expenses | 2 | N/A | Expense | Debit | 0 | Personal | DIRECT | 40 | 521100-000-Personal-DIRECT-040--0000---- | 228-000048 | GJV-000000001 | NULL | 226972\|Tml 7249 Oubf gfigp jyghgpy | GeneralJournal | LedgerJournal | D365 | No | No | USD | 798370.6 | 798370.6 | 0 | 798370.6 | 798370.6 | 0 | 2026-11-16 11:42:42.223000 |
| 5637271148 | 228 | Current | 2026-06-01 00:00:00 | 2026 | 2 | Q2 | 6 | Jun | (altered in export) | 2026-06-01 00:00:00 | 1900-01-02 00:00:00 | 521100 | Commissions Expense | 521100 - Commissions Expense | Commissions Expense | Underwriting & Acquisition Expenses | 2 | N/A | Expense | Debit | 0 | Personal | DIRECT | 90 | 521100-000-Personal-DIRECT-090--0000---- | 228-000048 | GJV-000000001 | NULL | 089469\|Tml 7249 Oubf gfigp jyghgpy | GeneralJournal | LedgerJournal | D365 | No | No | USD | 725.13 | 725.13 | 0 | 725.13 | 725.13 | 0 | 2026-11-16 11:42:42.223000 |
