---
name: dim_coa_logistics
schema: gold
layer: gold
domain: gl
type: table
status: active
purpose: Logistics chart of accounts with financial-statement classifications.
grain: one row per logistics account
primary_key:
- number
entity_column: null
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues: []
row_count: 133
proposed_fields: []
reviewed: false
---

# dim_coa_logistics

Created by the file upload UI

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `number` | long |  |  | `number` |
| `name` | string |  |  | `name` |
| `financialStatement` | string |  |  | `financialStatement` |
| `type` | string |  |  | `type` |
| `category` | string |  |  | `category` |
| `tag` | string |  |  | `tag` |
| `isActive` | string |  |  | `isActive` |

## Values

**financialStatement**
- `Income Statement`: 90 rows
- `Balance Sheet`: 42 rows
- `Total`: 1 rows

**type**
- `Expense`: 86 rows
- `Asset`: 29 rows
- `Liability`: 10 rows
- `Revenue`: 4 rows
- `Equity`: 3 rows
- `Total`: 1 rows

**category**
- `Other expenses`: 37 rows
- `COGS`: 26 rows
- `Property & Equipment`: 12 rows
- `Other Non-CA`: 8 rows
- `Accrued expenses`: 7 rows
- `Salary -Bonus`: 5 rows
- `Sales Revenue`: 4 rows
- `Utilities`: 4 rows
- `Expenses`: 4 rows
- `Other expense`: 3 rows
- `Related party receiv`: 3 rows
- `Other income (exp)`: 2 rows
- `Members' equity`: 2 rows
- `Cash and Equivalents`: 2 rows
- `None`: 2 rows
- `Base Salaries & Wage`: 2 rows
- `Trade receivables`: 1 rows
- `Operating Lease Righ`: 1 rows
- `Interest income`: 1 rows
- `Prepaids & other CA`: 1 rows
- `Long-term debt`: 1 rows
- `Accounts payable`: 1 rows
- `Related party payabl`: 1 rows
- `Depreciation`: 1 rows
- `Goodwill, net`: 1 rows
- `EmIncome Statementoyee Benefits`: 1 rows

**tag**
- `Cavenders COA`: 133 rows

**isActive**
- `ACTIVE`: 133 rows

## Profile

Rows in the latest export: 133.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `number` | LONG | 133 | 0 | 111100 | 999999 |
| `name` | STRING | 132 | 0 | ACCOUNTS RECEIVABLE ACCRUALS. | Vehicles |
| `financialStatement` | STRING | 3 | 0 | Balance Sheet | Total |
| `type` | STRING | 6 | 0 | Asset | Total |
| `category` | STRING | 26 | 2 | Accounts payable | Utilities |
| `tag` | STRING | 1 | 0 | Cavenders COA | Cavenders COA |
| `isActive` | STRING | 1 | 0 | ACTIVE | ACTIVE |

## Sample rows

| number | name | financialStatement | type | category | tag | isActive |
|---|---|---|---|---|---|---|
| 111100 | BOA CARS DEPOSIT ACCOUNT 8670227524 | Balance Sheet | Asset | Cash and Equivalents | Cavenders COA | ACTIVE |
| 111200 | BOA CARS DISBURSEMENT ACCOUNT 8670227529 | Balance Sheet | Asset | Cash and Equivalents | Cavenders COA | ACTIVE |
| 141110 | PREPAID OPERATIONAL EXPENSES | Balance Sheet | Asset | Prepaids & other CA | Cavenders COA | ACTIVE |
| 122400 | ACCOUNTS RECEIVABLE THIRD PARTY | Balance Sheet | Asset | Related party receiv | Cavenders COA | ACTIVE |
| 122500 | INTERCOMPANY TRADE RECEIVABLES | Balance Sheet | Asset | Related party receiv | Cavenders COA | ACTIVE |
