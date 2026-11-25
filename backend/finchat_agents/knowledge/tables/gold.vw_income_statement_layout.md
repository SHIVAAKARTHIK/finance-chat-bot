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
row_count: 22
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
- `5`: 1 rows
- `10`: 1 rows
- `20`: 1 rows
- `30`: 1 rows
- `40`: 1 rows
- `70`: 1 rows
- `50`: 1 rows
- `60`: 1 rows
- `105`: 1 rows
- `99`: 1 rows
- `100`: 1 rows
- `110`: 1 rows
- `120`: 1 rows
- `140`: 1 rows
- `130`: 1 rows
- `150`: 1 rows
- `190`: 1 rows
- `195`: 1 rows
- `160`: 1 rows
- `210`: 1 rows
- `299`: 1 rows
- `200`: 1 rows

**LINE_NAME**
- `None`: 2 rows
- `Net Premiums Earned`: 1 rows
- `Revenue`: 1 rows
- `Service & Fee Income`: 1 rows
- `Commission Income`: 1 rows
- `Contra Revenue`: 1 rows
- `Net Investment Income`: 1 rows
- `Net Realized Investment Gains (Losses)`: 1 rows
- `Other Income`: 1 rows
- `Expenses`: 1 rows
- `Total Revenue`: 1 rows
- `Losses & Loss Adjustment Expenses`: 1 rows
- `Underwriting Expenses`: 1 rows
- `Investment Expenses`: 1 rows
- `Interest Expense`: 1 rows
- `General & Administrative Expenses`: 1 rows
- `Other Expenses`: 1 rows
- `Total Expenses`: 1 rows
- `Provision for Income Taxes`: 1 rows
- `Income Before Income Taxes`: 1 rows
- `Net Income`: 1 rows

**IS_LINE**
- `HDR_REVENUE`: 1 rows
- `Net Premiums Earned`: 1 rows
- `Service & Fee Income`: 1 rows
- `Commission Income`: 1 rows
- `Contra Revenue`: 1 rows
- `Net Investment Income`: 1 rows
- `Net Realized Investment Gains (Losses)`: 1 rows
- `Other Income`: 1 rows
- `HDR_EXPENSES`: 1 rows
- `TOTAL_REVENUE`: 1 rows
- `SPACER_1`: 1 rows
- `Losses & Loss Adjustment Expenses`: 1 rows
- `Underwriting Expenses`: 1 rows
- `Investment Expenses`: 1 rows
- `Interest Expense`: 1 rows
- `General & Administrative Expenses`: 1 rows
- `SPACER_2`: 1 rows
- `TOTAL_EXPENSES`: 1 rows
- `Other Expenses`: 1 rows
- `NET_INCOME`: 1 rows
- `PRE_TAX_INCOME`: 1 rows
- `Provision for Income Taxes`: 1 rows

**LINE_TYPE**
- `Detail`: 14 rows
- `Header`: 2 rows
- `Subtotal`: 2 rows
- `Spacer`: 2 rows
- `Total`: 2 rows

**SECTION**
- `Revenue`: 10 rows
- `Expenses`: 9 rows
- `Income Taxes`: 2 rows
- `Result`: 1 rows

**SECTION_SORT**
- `1`: 10 rows
- `2`: 9 rows
- `3`: 2 rows
- `4`: 1 rows

**INDENT**
- `1`: 14 rows
- `0`: 8 rows

**IS_BOLD**
- `False`: 16 rows
- `True`: 6 rows

**VARIANCE_SIGN**
- `1`: 14 rows
- `-1`: 8 rows

**LINE_DISPLAY**
- `Net Premiums Earned`: 1 rows
- `REVENUE`: 1 rows
- `Contra Revenue`: 1 rows
- `Commission Income`: 1 rows
- `Service & Fee Income`: 1 rows
- `Other Income`: 1 rows
- `Net Investment Income`: 1 rows
- `Net Realized Investment Gains (Losses)`: 1 rows
- `None`: 1 rows
- `Total Revenue`: 1 rows
- `EXPENSES`: 1 rows
- `Underwriting Expenses`: 1 rows
- `Losses & Loss Adjustment Expenses`: 1 rows
- `Interest Expense`: 1 rows
- `General & Administrative Expenses`: 1 rows
- `Investment Expenses`: 1 rows
- `Other Expenses`: 1 rows
- `Total Expenses`: 1 rows
- `Provision for Income Taxes`: 1 rows
- `Income Before Income Taxes`: 1 rows
- `Net Income`: 1 rows

**ROW_BG_COLOR**
- `#FFFFFF`: 16 rows
- `#00338D`: 3 rows
- `#E7ECF5`: 2 rows
- `#C9D4EA`: 1 rows

**ROW_FONT_COLOR**
- `#000000`: 19 rows
- `#FFFFFF`: 3 rows

## Profile

Rows in the latest export: 22.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `LINE_SORT` | INT | 22 | 0 | 5 | 299 |
| `LINE_NAME` | STRING | 20 | 0 |  | Underwriting Expenses |
| `IS_LINE` | STRING | 21 | 0 | Commission Income | Underwriting Expenses |
| `LINE_TYPE` | STRING | 5 | 0 | Detail | Total |
| `SECTION` | STRING | 4 | 0 | Expenses | Revenue |
| `SECTION_SORT` | INT | 4 | 0 | 1 | 4 |
| `INDENT` | INT | 2 | 0 | 0 | 1 |
| `IS_BOLD` | BOOLEAN | 2 | 0 | False | True |
| `VARIANCE_SIGN` | INT | 2 | 0 | -1 | 1 |
| `LINE_DISPLAY` | STRING | 20 | 0 | EXPENSES | Underwriting Expenses |
| `ROW_BG_COLOR` | STRING | 4 | 0 | #00338D | #FFFFFF |
| `ROW_FONT_COLOR` | STRING | 2 | 0 | #000000 | #FFFFFF |

## Sample rows

| LINE_SORT | LINE_NAME | IS_LINE | LINE_TYPE | SECTION | SECTION_SORT | INDENT | IS_BOLD | VARIANCE_SIGN | LINE_DISPLAY | ROW_BG_COLOR | ROW_FONT_COLOR |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | Revenue | HDR_REVENUE | Header | Revenue | 1 | 0 | True | 1 | REVENUE | #00338D | #FFFFFF |
| 10 | Net Premiums Earned | Net Premiums Earned | Detail | Revenue | 1 | 1 | False | 1 | Net Premiums Earned | #FFFFFF | #000000 |
| 20 | Service & Fee Income | Service & Fee Income | Detail | Revenue | 1 | 1 | False | 1 | Service & Fee Income | #FFFFFF | #000000 |
| 30 | Commission Income | Commission Income | Detail | Revenue | 1 | 1 | False | 1 | Commission Income | #FFFFFF | #000000 |
| 40 | Contra Revenue | Contra Revenue | Detail | Revenue | 1 | 1 | False | 1 | Contra Revenue | #FFFFFF | #000000 |
