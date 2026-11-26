---
name: vw_balance_sheet_logistics_layout
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Row layout (headers; detail lines; subtotals; Total Assets; Total Liabilities & Equity; balance check) for the logistics
  balance sheet. Join BS_LINE to vw_balance_sheet_logistics.BS_LINE.
grain: one row per balance-sheet display line
primary_key:
- LINE_SORT
entity_column: null
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues: []
proposed_fields: []
reviewed: false
---

# vw_balance_sheet_logistics_layout

Row layout (headers, detail lines, subtotals, Total Assets, Total Liabilities & Equity, balance check) for the logistics balance sheet. Join BS_LINE to vw_balance_sheet_logistics.BS_LINE.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `LINE_SORT` | int |  |  | `LINE_SORT` |
| `LINE_NAME` | string |  |  | `LINE_NAME` |
| `BS_LINE` | string |  |  | `BS_LINE` |
| `LINE_TYPE` | string |  |  | `LINE_TYPE` |
| `SECTION` | string |  |  | `SECTION` |
| `SECTION_SORT` | int |  |  | `SECTION_SORT` |
| `INDENT` | int |  |  | `INDENT` |
| `IS_BOLD` | boolean |  |  | `IS_BOLD` |
| `VARIANCE_SIGN` | int |  |  | `VARIANCE_SIGN` |
| `LINE_DISPLAY` | string |  |  | `LINE_DISPLAY` |
| `ROW_BG_COLOR` | string |  |  | `ROW_BG_COLOR` |
| `ROW_FONT_COLOR` | string |  |  | `ROW_FONT_COLOR` |

## Values

**LINE_SORT**
- `5`
- `10`
- `1`
- `20`
- `49`
- `110`
- `30`
- `40`
- `55`
- `140`
- `130`
- `120`
- `149`
- `205`
- `201`
- `210`
- `199`
- `200`
- `249`
- `220`
- `240`
- `230`
- `255`
- `310`
- `349`
- `400`
- `399`
- `420`
- `405`
- `410`
- `430`
- `500`
- `440`
- `599`
- `499`
- `699`

**LINE_NAME**
- `None`
- `Current Assets`
- `Trade Receivables, net`
- `Assets`
- `Cash & Cash Equivalents`
- `Prepaid Expenses & Other Current Assets`
- `Non-Current Assets`
- `Related Party & Intercompany Receivables`
- `Property & Equipment, net`
- `Total Current Assets`
- `Goodwill & Intangibles, net`
- `Total Non-Current Assets`
- `Operating Lease Right-of-Use Assets`
- `Other Non-Current Assets`
- `Current Liabilities`
- `Total Assets`
- `Liabilities`
- `Accounts Payable`
- `Accrued Expenses`
- `Other Current Liabilities`
- `Related Party & Intercompany Payables`
- `Total Current Liabilities`
- `Non-Current Liabilities`
- `Long-Term Debt`
- `Total Non-Current Liabilities`
- `Total Liabilities`
- `Equity`
- `Members Capital`
- `Current Year Earnings`
- `Retained Earnings`
- `Total Equity`
- `Total Liabilities & Equity`
- `Other Equity`
- `Balance Check (Assets - Liabilities & Equity)`

**BS_LINE**
- `Trade Receivables, net`
- `HDR_CURRENT_ASSETS`
- `Cash & Cash Equivalents`
- `HDR_ASSETS`
- `Prepaid Expenses & Other Current Assets`
- `TOTAL_CURRENT_ASSETS`
- `Related Party & Intercompany Receivables`
- `Property & Equipment, net`
- `HDR_NON_CURRENT_ASSETS`
- `Goodwill & Intangibles, net`
- `Operating Lease Right-of-Use Assets`
- `TOTAL_NON_CURRENT_ASSETS`
- `Other Non-Current Assets`
- `HDR_CURRENT_LIABILITIES`
- `TOTAL_ASSETS`
- `HDR_LIABILITIES`
- `Accounts Payable`
- `SPACER_1`
- `TOTAL_CURRENT_LIABILITIES`
- `Accrued Expenses`
- `Other Current Liabilities`
- `Related Party & Intercompany Payables`
- `HDR_NON_CURRENT_LIABILITIES`
- `Long-Term Debt`
- `SPACER_2`
- `TOTAL_LIABILITIES`
- `TOTAL_NON_CURRENT_LIABILITIES`
- `Members Capital`
- `Current Year Earnings`
- `Retained Earnings`
- `HDR_EQUITY`
- `TOTAL_LIABILITIES_AND_EQUITY`
- `Other Equity`
- `TOTAL_EQUITY`
- `BALANCE_CHECK`
- `SPACER_3`

**LINE_TYPE**
- `Detail`
- `SubHeader`
- `Subtotal`
- `Total`
- `Header`
- `Spacer`
- `Check`

**SECTION**
- `Assets`
- `Liabilities`
- `Equity`
- `Result`

**SECTION_SORT**
- `1`
- `2`
- `3`
- `4`

**INDENT**
- `2`
- `0`
- `1`

**IS_BOLD**
- `False`
- `True`

**VARIANCE_SIGN**
- `1`
- `-1`

**LINE_DISPLAY**
- `Current Assets`
- `Cash & Cash Equivalents`
- `Trade Receivables, net`
- `ASSETS`
- `Property & Equipment, net`
- `Prepaid Expenses & Other Current Assets`
- `Related Party & Intercompany Receivables`
- `Non-Current Assets`
- `Total Current Assets`
- `Goodwill & Intangibles, net`
- `Total Non-Current Assets`
- `Other Non-Current Assets`
- `Operating Lease Right-of-Use Assets`
- `LIABILITIES`
- `Current Liabilities`
- `Accounts Payable`
- `None`
- `Total Assets`
- `Total Current Liabilities`
- `Accrued Expenses`
- `Related Party & Intercompany Payables`
- `Other Current Liabilities`
- `Non-Current Liabilities`
- `Total Non-Current Liabilities`
- `Long-Term Debt`
- `Total Liabilities`
- `EQUITY`
- `Current Year Earnings`
- `Retained Earnings`
- `Members Capital`
- `Other Equity`
- `Total Equity`
- `Total Liabilities & Equity`
- `Balance Check (Assets - Liabilities & Equity)`

**ROW_BG_COLOR**
- `#FFFFFF`
- `#00338D`
- `#E7ECF5`
- `#C9D4EA`

**ROW_FONT_COLOR**
- `#000000`
- `#FFFFFF`
