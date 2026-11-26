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
- `Income Statement`
- `Balance Sheet`
- `Total`

**type**
- `Expense`
- `Asset`
- `Liability`
- `Revenue`
- `Equity`
- `Total`

**category**
- `Other expenses`
- `COGS`
- `Property & Equipment`
- `Other Non-CA`
- `Accrued expenses`
- `Salary -Bonus`
- `Sales Revenue`
- `Utilities`
- `Expenses`
- `Other expense`
- `Related party receiv`
- `Other income (exp)`
- `Members' equity`
- `Cash and Equivalents`
- `None`
- `Base Salaries & Wage`
- `Trade receivables`
- `Operating Lease Righ`
- `Interest income`
- `Prepaids & other CA`
- `Long-term debt`
- `Accounts payable`
- `Related party payabl`
- `Depreciation`
- `Goodwill, net`
- `EmIncome Statementoyee Benefits`

**tag**
- `Cavenders COA`

**isActive**
- `ACTIVE`
