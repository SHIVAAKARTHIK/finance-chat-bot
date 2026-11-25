---
name: vw_income_statement_logistics_layout
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Row layout (headers; detail lines; subtotals; Gross Profit; Operating Income; Net Income) for the logistics income
  statement. Join IS_LINE to vw_income_statement_logistics.IS_LINE.
grain: one row per logistics income-statement display line
primary_key:
- LINE_SORT
entity_column: null
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues: []
row_count: 29
proposed_fields: []
reviewed: false
---

# vw_income_statement_logistics_layout

Row layout (headers, detail lines, subtotals, Gross Profit, Operating Income, Net Income) for the logistics income statement. Join IS_LINE to vw_income_statement_logistics.IS_LINE.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `LINE_SORT` | int |  |  | `LINE_SORT` |
| `LINE_NAME` | string |  |  | `LINE_NAME` |
| `IS_LINE` | string |  |  | `IS_LINE` |
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
- `20`: 1 rows
- `105`: 1 rows
- `99`: 1 rows
- `100`: 1 rows
- `110`: 1 rows
- `140`: 1 rows
- `130`: 1 rows
- `120`: 1 rows
- `190`: 1 rows
- `195`: 1 rows
- `200`: 1 rows
- `150`: 1 rows
- `205`: 1 rows
- `220`: 1 rows
- `210`: 1 rows
- `230`: 1 rows
- `250`: 1 rows
- `260`: 1 rows
- `240`: 1 rows
- `295`: 1 rows
- `300`: 1 rows
- `290`: 1 rows
- `305`: 1 rows
- `390`: 1 rows
- `320`: 1 rows
- `310`: 1 rows
- `399`: 1 rows

**LINE_NAME**
- `None`: 3 rows
- `Other Income (Expense)`: 2 rows
- `Operating Revenue - Third Party`: 1 rows
- `Revenue`: 1 rows
- `Operating Revenue - Intercompany`: 1 rows
- `Freight & Transportation`: 1 rows
- `Total Revenue`: 1 rows
- `Cost of Sales`: 1 rows
- `Intercompany Direct Costs`: 1 rows
- `Warehousing & Handling`: 1 rows
- `Customs & Brokerage`: 1 rows
- `Gross Profit`: 1 rows
- `Total Cost of Sales`: 1 rows
- `Other Direct Costs`: 1 rows
- `Salaries, Wages & Benefits`: 1 rows
- `Rent, Occupancy & Utilities`: 1 rows
- `Operating Expenses`: 1 rows
- `Sales & Marketing`: 1 rows
- `Travel & Entertainment`: 1 rows
- `General & Administrative`: 1 rows
- `Depreciation & Amortization`: 1 rows
- `Operating Income (EBIT)`: 1 rows
- `Total Operating Expenses`: 1 rows
- `Total Other Income (Expense)`: 1 rows
- `Net Income`: 1 rows
- `Interest Income`: 1 rows

**IS_LINE**
- `HDR_REVENUE`: 1 rows
- `Operating Revenue - Third Party`: 1 rows
- `Operating Revenue - Intercompany`: 1 rows
- `Freight & Transportation`: 1 rows
- `TOTAL_REVENUE`: 1 rows
- `HDR_COST_OF_SALES`: 1 rows
- `SPACER_1`: 1 rows
- `Intercompany Direct Costs`: 1 rows
- `Warehousing & Handling`: 1 rows
- `Customs & Brokerage`: 1 rows
- `GROSS_PROFIT`: 1 rows
- `SPACER_2`: 1 rows
- `TOTAL_COST_OF_SALES`: 1 rows
- `Other Direct Costs`: 1 rows
- `HDR_OPEX`: 1 rows
- `Salaries, Wages & Benefits`: 1 rows
- `Rent, Occupancy & Utilities`: 1 rows
- `Sales & Marketing`: 1 rows
- `Travel & Entertainment`: 1 rows
- `General & Administrative`: 1 rows
- `Depreciation & Amortization`: 1 rows
- `OPERATING_INCOME`: 1 rows
- `TOTAL_OPEX`: 1 rows
- `HDR_OTHER`: 1 rows
- `SPACER_3`: 1 rows
- `TOTAL_OTHER`: 1 rows
- `NET_INCOME`: 1 rows
- `Other Income (Expense)`: 1 rows
- `Interest Income`: 1 rows

**LINE_TYPE**
- `Detail`: 15 rows
- `Header`: 4 rows
- `Subtotal`: 4 rows
- `Spacer`: 3 rows
- `Total`: 3 rows

**SECTION**
- `Operating Expenses`: 10 rows
- `Cost of Sales`: 9 rows
- `Revenue`: 5 rows
- `Other Income (Expense)`: 4 rows
- `Result`: 1 rows

**SECTION_SORT**
- `3`: 10 rows
- `2`: 9 rows
- `1`: 5 rows
- `4`: 4 rows
- `5`: 1 rows

**INDENT**
- `1`: 15 rows
- `0`: 14 rows

**IS_BOLD**
- `False`: 18 rows
- `True`: 11 rows

**VARIANCE_SIGN**
- `1`: 16 rows
- `-1`: 13 rows

**LINE_DISPLAY**
- `Operating Revenue - Third Party`: 1 rows
- `Operating Revenue - Intercompany`: 1 rows
- `REVENUE`: 1 rows
- `None`: 1 rows
- `Total Revenue`: 1 rows
- `Freight & Transportation`: 1 rows
- `COST OF SALES`: 1 rows
- `Intercompany Direct Costs`: 1 rows
- `Customs & Brokerage`: 1 rows
- `Warehousing & Handling`: 1 rows
- `Other Direct Costs`: 1 rows
- `Gross Profit`: 1 rows
- `Total Cost of Sales`: 1 rows
- `Salaries, Wages & Benefits`: 1 rows
- `Rent, Occupancy & Utilities`: 1 rows
- `OPERATING EXPENSES`: 1 rows
- `Sales & Marketing`: 1 rows
- `Depreciation & Amortization`: 1 rows
- `General & Administrative`: 1 rows
- `Travel & Entertainment`: 1 rows
- `Operating Income (EBIT)`: 1 rows
- `Total Operating Expenses`: 1 rows
- `OTHER INCOME (EXPENSE)`: 1 rows
- `Total Other Income (Expense)`: 1 rows
- `Other Income (Expense)`: 1 rows
- `Net Income`: 1 rows
- `Interest Income`: 1 rows

**ROW_BG_COLOR**
- `#FFFFFF`: 18 rows
- `#00338D`: 5 rows
- `#E7ECF5`: 4 rows
- `#C9D4EA`: 2 rows

**ROW_FONT_COLOR**
- `#000000`: 24 rows
- `#FFFFFF`: 5 rows

## Profile

Rows in the latest export: 29.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `LINE_SORT` | INT | 29 | 0 | 5 | 399 |
| `LINE_NAME` | STRING | 26 | 0 |  | Warehousing & Handling |
| `IS_LINE` | STRING | 29 | 0 | Customs & Brokerage | Warehousing & Handling |
| `LINE_TYPE` | STRING | 5 | 0 | Detail | Total |
| `SECTION` | STRING | 5 | 0 | Cost of Sales | Revenue |
| `SECTION_SORT` | INT | 5 | 0 | 1 | 5 |
| `INDENT` | INT | 2 | 0 | 0 | 1 |
| `IS_BOLD` | BOOLEAN | 2 | 0 | False | True |
| `VARIANCE_SIGN` | INT | 2 | 0 | -1 | 1 |
| `LINE_DISPLAY` | STRING | 27 | 0 | COST OF SALES | Warehousing & Handling |
| `ROW_BG_COLOR` | STRING | 4 | 0 | #00338D | #FFFFFF |
| `ROW_FONT_COLOR` | STRING | 2 | 0 | #000000 | #FFFFFF |

## Sample rows

| LINE_SORT | LINE_NAME | IS_LINE | LINE_TYPE | SECTION | SECTION_SORT | INDENT | IS_BOLD | VARIANCE_SIGN | LINE_DISPLAY | ROW_BG_COLOR | ROW_FONT_COLOR |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | Revenue | HDR_REVENUE | Header | Revenue | 1 | 0 | True | 1 | REVENUE | #00338D | #FFFFFF |
| 10 | Operating Revenue - Third Party | Operating Revenue - Third Party | Detail | Revenue | 1 | 1 | False | 1 | Operating Revenue - Third Party | #FFFFFF | #000000 |
| 20 | Operating Revenue - Intercompany | Operating Revenue - Intercompany | Detail | Revenue | 1 | 1 | False | 1 | Operating Revenue - Intercompany | #FFFFFF | #000000 |
| 99 | Total Revenue | TOTAL_REVENUE | Subtotal | Revenue | 1 | 0 | True | 1 | Total Revenue | #E7ECF5 | #000000 |
| 100 | NULL | SPACER_1 | Spacer | Revenue | 1 | 0 | False | 1 | NULL | #FFFFFF | #000000 |
