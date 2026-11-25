# fact_fynapse_slr_journals

**Domain:** Fynapse subledger  
**Type:** fact table  
**Full name:** `lakehouse_mvpai.silver.fact_fynapse_slr_journals`  
**Grain:** one row per (JOURNAL_LINE_ID)  
**Also called:** fynapse, subledger, journal lines, slr journals  

Fynapse subledger journal lines: one row per journal line with entity, fiscal period, source system and amounts.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `JOURNAL_LINE_ID` | string | Unique journal line id (grain). |  | `JOURNAL_LINE_ID` |
| `JOURNAL_ID` | string | Journal id; a journal has several lines. 'How many journals' = COUNT(DISTINCT). | journal, journal id | `JOURNAL_ID` |
| `PARENT_ENTITY` | string | Legal entity code (UK03, UK06, UK07, UK13, UK14, UK17). This is THE entity column. | entity, legal entity, parent entity | `PARENT_ENTITY` |
| `CHILD_ENTITY` | string | Sub-unit (BMO, BWE, BWM), often empty. Not the legal entity. | child entity | `CHILD_ENTITY` |
| `FISCAL_YEAR` | integer | Fiscal year, e.g. 2026. | fiscal year | `FISCAL_YEAR` |
| `PERIOD` | integer | Fiscal period number (8 = Aug 2026, 9 = Sep 2026). | fiscal period | `PERIOD` |
| `CORE_DATE` | date | Period month-end date. | date, posting date | `CORE_DATE` |
| `SOURCE_SYSTEM` | string | Upstream source system. | source system, source, integration | `SOURCE_SYSTEM` |
| `JOURNAL_TYPE` | string | Journal type. | journal type | `JOURNAL_TYPE` |
| `ACCOUNT` | string | GL account. | account, gl account | `ACCOUNT` |
| `BUSINESS_EVENT` | string | Business event that created the line. | business event | `BUSINESS_EVENT` |
| `TRANSACTION_CURRENCY` | string | Transaction currency. | transaction currency, currency | `TRANSACTION_CURRENCY` |
| `REPORTING_AMOUNT` | decimal | Amount in reporting currency (signed). 'Net' = SUM; 'gross' = SUM(ABS()). | reporting amount, amount, net amount | `REPORTING_AMOUNT` |
| `TRANSACTION_AMOUNT` | decimal | Amount in transaction currency. | transaction amount | `TRANSACTION_AMOUNT` |

## Values

**SOURCE_SYSTEM**
- `NOVIDEA`: brokerage accounting
- `ACCRUAL`: accrued brokerage
- `Concur`: expenses

## Named metrics

| Metric | Meaning | SQL | Additivity |
|---|---|---|---|
| `journal_line_count` | Number of journal lines. | `COUNT(*)` | additive |
| `journal_count` | Number of distinct journals. | `COUNT(DISTINCT JOURNAL_ID)` | non additive |
| `net_reporting_amount` | Net amount in reporting currency. | `SUM(REPORTING_AMOUNT)` | additive |
| `gross_reporting_amount` | Gross amount in reporting currency. | `SUM(ABS(REPORTING_AMOUNT))` | additive |
