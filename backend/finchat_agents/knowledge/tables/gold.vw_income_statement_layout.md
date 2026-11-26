---
name: vw_income_statement_layout
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: 'Income statement presentation layout: ordered rows (headers, detail lines, subtotals, spacers, net income) for the
  Power BI P&L matrix, with indented display labels and row colours. Join IS_LINE to vw_income_statement.IS_LINE.'
grain: one row per income-statement display line
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

# vw_income_statement_layout

Income statement presentation layout: ordered rows (headers, detail lines, subtotals, spacers, net income) for the Power BI P&L matrix, with indented display labels and row colours. Join IS_LINE to vw_income_statement.IS_LINE.

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
- `30`
- `40`
- `70`
- `50`
- `60`
- `105`
- `99`
- `100`
- `110`
- `120`
- `140`
- `130`
- `150`
- `190`
- `195`
- `160`
- `210`
- `299`
- `200`

**LINE_NAME**
- `None`
- `Net Premiums Earned`
- `Revenue`
- `Service & Fee Income`
- `Commission Income`
- `Contra Revenue`
- `Net Investment Income`
- `Net Realized Investment Gains (Losses)`
- `Other Income`
- `Expenses`
- `Total Revenue`
- `Losses & Loss Adjustment Expenses`
- `Underwriting Expenses`
- `Investment Expenses`
- `Interest Expense`
- `General & Administrative Expenses`
- `Other Expenses`
- `Total Expenses`
- `Provision for Income Taxes`
- `Income Before Income Taxes`
- `Net Income`

**IS_LINE**
- `HDR_REVENUE`
- `Net Premiums Earned`
- `Service & Fee Income`
- `Commission Income`
- `Contra Revenue`
- `Net Investment Income`
- `Net Realized Investment Gains (Losses)`
- `Other Income`
- `HDR_EXPENSES`
- `TOTAL_REVENUE`
- `SPACER_1`
- `Losses & Loss Adjustment Expenses`
- `Underwriting Expenses`
- `Investment Expenses`
- `Interest Expense`
- `General & Administrative Expenses`
- `SPACER_2`
- `TOTAL_EXPENSES`
- `Other Expenses`
- `NET_INCOME`
- `PRE_TAX_INCOME`
- `Provision for Income Taxes`

**LINE_TYPE**
- `Detail`
- `Header`
- `Subtotal`
- `Spacer`
- `Total`

**SECTION**
- `Revenue`
- `Expenses`
- `Income Taxes`
- `Result`

**SECTION_SORT**
- `1`
- `2`
- `3`
- `4`

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
- `Net Premiums Earned`
- `REVENUE`
- `Contra Revenue`
- `Commission Income`
- `Service & Fee Income`
- `Other Income`
- `Net Investment Income`
- `Net Realized Investment Gains (Losses)`
- `None`
- `Total Revenue`
- `EXPENSES`
- `Underwriting Expenses`
- `Losses & Loss Adjustment Expenses`
- `Interest Expense`
- `General & Administrative Expenses`
- `Investment Expenses`
- `Other Expenses`
- `Total Expenses`
- `Provision for Income Taxes`
- `Income Before Income Taxes`
- `Net Income`

**ROW_BG_COLOR**
- `#FFFFFF`
- `#00338D`
- `#E7ECF5`
- `#C9D4EA`

**ROW_FONT_COLOR**
- `#000000`
- `#FFFFFF`
