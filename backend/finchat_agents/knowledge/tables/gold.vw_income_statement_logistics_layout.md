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
- `5`
- `10`
- `20`
- `105`
- `99`
- `100`
- `110`
- `140`
- `130`
- `120`
- `190`
- `195`
- `200`
- `150`
- `205`
- `220`
- `210`
- `230`
- `250`
- `260`
- `240`
- `295`
- `300`
- `290`
- `305`
- `390`
- `320`
- `310`
- `399`

**LINE_NAME**
- `None`
- `Other Income (Expense)`
- `Operating Revenue - Third Party`
- `Revenue`
- `Operating Revenue - Intercompany`
- `Freight & Transportation`
- `Total Revenue`
- `Cost of Sales`
- `Intercompany Direct Costs`
- `Warehousing & Handling`
- `Customs & Brokerage`
- `Gross Profit`
- `Total Cost of Sales`
- `Other Direct Costs`
- `Salaries, Wages & Benefits`
- `Rent, Occupancy & Utilities`
- `Operating Expenses`
- `Sales & Marketing`
- `Travel & Entertainment`
- `General & Administrative`
- `Depreciation & Amortization`
- `Operating Income (EBIT)`
- `Total Operating Expenses`
- `Total Other Income (Expense)`
- `Net Income`
- `Interest Income`

**IS_LINE**
- `HDR_REVENUE`
- `Operating Revenue - Third Party`
- `Operating Revenue - Intercompany`
- `Freight & Transportation`
- `TOTAL_REVENUE`
- `HDR_COST_OF_SALES`
- `SPACER_1`
- `Intercompany Direct Costs`
- `Warehousing & Handling`
- `Customs & Brokerage`
- `GROSS_PROFIT`
- `SPACER_2`
- `TOTAL_COST_OF_SALES`
- `Other Direct Costs`
- `HDR_OPEX`
- `Salaries, Wages & Benefits`
- `Rent, Occupancy & Utilities`
- `Sales & Marketing`
- `Travel & Entertainment`
- `General & Administrative`
- `Depreciation & Amortization`
- `OPERATING_INCOME`
- `TOTAL_OPEX`
- `HDR_OTHER`
- `SPACER_3`
- `TOTAL_OTHER`
- `NET_INCOME`
- `Other Income (Expense)`
- `Interest Income`

**LINE_TYPE**
- `Detail`
- `Header`
- `Subtotal`
- `Spacer`
- `Total`

**SECTION**
- `Operating Expenses`
- `Cost of Sales`
- `Revenue`
- `Other Income (Expense)`
- `Result`

**SECTION_SORT**
- `3`
- `2`
- `1`
- `4`
- `5`

**INDENT**
- `1`
- `0`

**IS_BOLD**
- `False`
- `True`

**VARIANCE_SIGN**
- `1`
- `-1`

**LINE_DISPLAY**
- `Operating Revenue - Third Party`
- `Operating Revenue - Intercompany`
- `REVENUE`
- `None`
- `Total Revenue`
- `Freight & Transportation`
- `COST OF SALES`
- `Intercompany Direct Costs`
- `Customs & Brokerage`
- `Warehousing & Handling`
- `Other Direct Costs`
- `Gross Profit`
- `Total Cost of Sales`
- `Salaries, Wages & Benefits`
- `Rent, Occupancy & Utilities`
- `OPERATING EXPENSES`
- `Sales & Marketing`
- `Depreciation & Amortization`
- `General & Administrative`
- `Travel & Entertainment`
- `Operating Income (EBIT)`
- `Total Operating Expenses`
- `OTHER INCOME (EXPENSE)`
- `Total Other Income (Expense)`
- `Other Income (Expense)`
- `Net Income`
- `Interest Income`

**ROW_BG_COLOR**
- `#FFFFFF`
- `#00338D`
- `#E7ECF5`
- `#C9D4EA`

**ROW_FONT_COLOR**
- `#000000`
- `#FFFFFF`
