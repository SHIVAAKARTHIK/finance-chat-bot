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
row_count: 36
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
- `5`: 1 rows
- `10`: 1 rows
- `1`: 1 rows
- `20`: 1 rows
- `49`: 1 rows
- `110`: 1 rows
- `30`: 1 rows
- `40`: 1 rows
- `55`: 1 rows
- `140`: 1 rows
- `130`: 1 rows
- `120`: 1 rows
- `149`: 1 rows
- `205`: 1 rows
- `201`: 1 rows
- `210`: 1 rows
- `199`: 1 rows
- `200`: 1 rows
- `249`: 1 rows
- `220`: 1 rows
- `240`: 1 rows
- `230`: 1 rows
- `255`: 1 rows
- `310`: 1 rows
- `349`: 1 rows
- `400`: 1 rows
- `399`: 1 rows
- `420`: 1 rows
- `405`: 1 rows
- `410`: 1 rows
- `430`: 1 rows
- `500`: 1 rows
- `440`: 1 rows
- `599`: 1 rows
- `499`: 1 rows
- `699`: 1 rows

**LINE_NAME**
- `None`: 3 rows
- `Current Assets`: 1 rows
- `Trade Receivables, net`: 1 rows
- `Assets`: 1 rows
- `Cash & Cash Equivalents`: 1 rows
- `Prepaid Expenses & Other Current Assets`: 1 rows
- `Non-Current Assets`: 1 rows
- `Related Party & Intercompany Receivables`: 1 rows
- `Property & Equipment, net`: 1 rows
- `Total Current Assets`: 1 rows
- `Goodwill & Intangibles, net`: 1 rows
- `Total Non-Current Assets`: 1 rows
- `Operating Lease Right-of-Use Assets`: 1 rows
- `Other Non-Current Assets`: 1 rows
- `Current Liabilities`: 1 rows
- `Total Assets`: 1 rows
- `Liabilities`: 1 rows
- `Accounts Payable`: 1 rows
- `Accrued Expenses`: 1 rows
- `Other Current Liabilities`: 1 rows
- `Related Party & Intercompany Payables`: 1 rows
- `Total Current Liabilities`: 1 rows
- `Non-Current Liabilities`: 1 rows
- `Long-Term Debt`: 1 rows
- `Total Non-Current Liabilities`: 1 rows
- `Total Liabilities`: 1 rows
- `Equity`: 1 rows
- `Members Capital`: 1 rows
- `Current Year Earnings`: 1 rows
- `Retained Earnings`: 1 rows
- `Total Equity`: 1 rows
- `Total Liabilities & Equity`: 1 rows
- `Other Equity`: 1 rows
- `Balance Check (Assets - Liabilities & Equity)`: 1 rows

**BS_LINE**
- `Trade Receivables, net`: 1 rows
- `HDR_CURRENT_ASSETS`: 1 rows
- `Cash & Cash Equivalents`: 1 rows
- `HDR_ASSETS`: 1 rows
- `Prepaid Expenses & Other Current Assets`: 1 rows
- `TOTAL_CURRENT_ASSETS`: 1 rows
- `Related Party & Intercompany Receivables`: 1 rows
- `Property & Equipment, net`: 1 rows
- `HDR_NON_CURRENT_ASSETS`: 1 rows
- `Goodwill & Intangibles, net`: 1 rows
- `Operating Lease Right-of-Use Assets`: 1 rows
- `TOTAL_NON_CURRENT_ASSETS`: 1 rows
- `Other Non-Current Assets`: 1 rows
- `HDR_CURRENT_LIABILITIES`: 1 rows
- `TOTAL_ASSETS`: 1 rows
- `HDR_LIABILITIES`: 1 rows
- `Accounts Payable`: 1 rows
- `SPACER_1`: 1 rows
- `TOTAL_CURRENT_LIABILITIES`: 1 rows
- `Accrued Expenses`: 1 rows
- `Other Current Liabilities`: 1 rows
- `Related Party & Intercompany Payables`: 1 rows
- `HDR_NON_CURRENT_LIABILITIES`: 1 rows
- `Long-Term Debt`: 1 rows
- `SPACER_2`: 1 rows
- `TOTAL_LIABILITIES`: 1 rows
- `TOTAL_NON_CURRENT_LIABILITIES`: 1 rows
- `Members Capital`: 1 rows
- `Current Year Earnings`: 1 rows
- `Retained Earnings`: 1 rows
- `HDR_EQUITY`: 1 rows
- `TOTAL_LIABILITIES_AND_EQUITY`: 1 rows
- `Other Equity`: 1 rows
- `TOTAL_EQUITY`: 1 rows
- `BALANCE_CHECK`: 1 rows
- `SPACER_3`: 1 rows

**LINE_TYPE**
- `Detail`: 17 rows
- `SubHeader`: 4 rows
- `Subtotal`: 4 rows
- `Total`: 4 rows
- `Header`: 3 rows
- `Spacer`: 3 rows
- `Check`: 1 rows

**SECTION**
- `Assets`: 15 rows
- `Liabilities`: 12 rows
- `Equity`: 7 rows
- `Result`: 2 rows

**SECTION_SORT**
- `1`: 15 rows
- `2`: 12 rows
- `3`: 7 rows
- `4`: 2 rows

**INDENT**
- `2`: 17 rows
- `0`: 11 rows
- `1`: 8 rows

**IS_BOLD**
- `False`: 21 rows
- `True`: 15 rows

**VARIANCE_SIGN**
- `1`: 28 rows
- `-1`: 8 rows

**LINE_DISPLAY**
- `Current Assets`: 1 rows
- `Cash & Cash Equivalents`: 1 rows
- `Trade Receivables, net`: 1 rows
- `ASSETS`: 1 rows
- `Property & Equipment, net`: 1 rows
- `Prepaid Expenses & Other Current Assets`: 1 rows
- `Related Party & Intercompany Receivables`: 1 rows
- `Non-Current Assets`: 1 rows
- `Total Current Assets`: 1 rows
- `Goodwill & Intangibles, net`: 1 rows
- `Total Non-Current Assets`: 1 rows
- `Other Non-Current Assets`: 1 rows
- `Operating Lease Right-of-Use Assets`: 1 rows
- `LIABILITIES`: 1 rows
- `Current Liabilities`: 1 rows
- `Accounts Payable`: 1 rows
- `None`: 1 rows
- `Total Assets`: 1 rows
- `Total Current Liabilities`: 1 rows
- `Accrued Expenses`: 1 rows
- `Related Party & Intercompany Payables`: 1 rows
- `Other Current Liabilities`: 1 rows
- `Non-Current Liabilities`: 1 rows
- `Total Non-Current Liabilities`: 1 rows
- `Long-Term Debt`: 1 rows
- `Total Liabilities`: 1 rows
- `EQUITY`: 1 rows
- `Current Year Earnings`: 1 rows
- `Retained Earnings`: 1 rows
- `Members Capital`: 1 rows
- `Other Equity`: 1 rows
- `Total Equity`: 1 rows
- `Total Liabilities & Equity`: 1 rows
- `Balance Check (Assets - Liabilities & Equity)`: 1 rows

**ROW_BG_COLOR**
- `#FFFFFF`: 25 rows
- `#00338D`: 5 rows
- `#E7ECF5`: 4 rows
- `#C9D4EA`: 2 rows

**ROW_FONT_COLOR**
- `#000000`: 31 rows
- `#FFFFFF`: 5 rows

## Profile

Rows in the latest export: 36.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `LINE_SORT` | INT | 36 | 0 | 1 | 699 |
| `LINE_NAME` | STRING | 34 | 0 |  | Trade Receivables, net |
| `BS_LINE` | STRING | 34 | 0 | Accounts Payable | Trade Receivables, net |
| `LINE_TYPE` | STRING | 7 | 0 | Check | Total |
| `SECTION` | STRING | 4 | 0 | Assets | Result |
| `SECTION_SORT` | INT | 4 | 0 | 1 | 4 |
| `INDENT` | INT | 3 | 0 | 0 | 2 |
| `IS_BOLD` | BOOLEAN | 2 | 0 | False | True |
| `VARIANCE_SIGN` | INT | 2 | 0 | -1 | 1 |
| `LINE_DISPLAY` | STRING | 36 | 0 | ASSETS | Trade Receivables, net |
| `ROW_BG_COLOR` | STRING | 4 | 0 | #00338D | #FFFFFF |
| `ROW_FONT_COLOR` | STRING | 2 | 0 | #000000 | #FFFFFF |

## Sample rows

| LINE_SORT | LINE_NAME | BS_LINE | LINE_TYPE | SECTION | SECTION_SORT | INDENT | IS_BOLD | VARIANCE_SIGN | LINE_DISPLAY | ROW_BG_COLOR | ROW_FONT_COLOR |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Assets | HDR_ASSETS | Header | Assets | 1 | 0 | True | 1 | ASSETS | #00338D | #FFFFFF |
| 5 | Current Assets | HDR_CURRENT_ASSETS | SubHeader | Assets | 1 | 1 | True | 1 | Current Assets | #FFFFFF | #000000 |
| 10 | Cash & Cash Equivalents | Cash & Cash Equivalents | Detail | Assets | 1 | 2 | False | 1 | Cash & Cash Equivalents | #FFFFFF | #000000 |
| 20 | Trade Receivables, net | Trade Receivables, net | Detail | Assets | 1 | 2 | False | 1 | Trade Receivables, net | #FFFFFF | #000000 |
| 30 | Related Party & Intercompany Receivables | Related Party & Intercompany Receivables | Detail | Assets | 1 | 2 | False | 1 | Related Party & Intercompany Receivables | #FFFFFF | #000000 |
