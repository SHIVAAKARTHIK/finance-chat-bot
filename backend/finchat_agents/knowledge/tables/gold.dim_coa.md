---
name: dim_coa
schema: gold
layer: gold
domain: gl
type: table
status: active
purpose: Chart of accounts with statutory/MGA basis and reporting hierarchy.
grain: one row per account and STAT/MGA basis
primary_key:
- Future State CoA
- STAT or MGA
entity_column: null
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues: []
proposed_fields: []
reviewed: false
---

# dim_coa

Created by the file upload UI

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Future State CoA` | long |  |  | `Future State CoA` |
| `Future State CoA Name` | string |  |  | `Future State CoA Name` |
| `STAT or MGA` | string |  |  | `STAT or MGA` |
| `Type` | string |  |  | `Type` |
| `Level 0` | string |  |  | `Level 0` |
| `Level 1` | string |  |  | `Level 1` |
| `Level 2` | string |  |  | `Level 2` |
| `Level 3` | string |  |  | `Level 3` |
| `Level 4` | string |  |  | `Level 4` |
| `Level 5` | string |  |  | `Level 5` |
| `Level 6` | string |  |  | `Level 6` |

## Values

**STAT or MGA**
- `STAT`
- `MGA`

**Type**
- `Asset`
- `Expense`
- `Liability`
- `Revenue`
- `Equity`
- `Reporting`

**Level 0**
- `Balance Sheet`
- `Income Statement`
- `Misc (Reporting Only)`

**Level 1**
- `Asset`
- `Expense`
- `Liability`
- `Revenue`
- `Equity`
- `Reporting`

**Level 2**
- `Cash`
- `General and Administrative`
- `Underwriting expenses`
- `Investment Income`
- `Receivables and Recoverables`
- `Invested Assets`
- `Retained Earnings`
- `Insurance Policy Liabilities`
- `Property and Equipment`
- `Operational Liabilities`
- `Cash Equivalents`
- `Loss and loss adjustment expenses`
- `Financing and Debt`
- `Other assets`
- `Premiums earned`
- `Underwriting Liabilities`
- `Realized investment gains (losses)`
- `Federal Tax Assets`
- `Investment expense`
- `Service / Fee Income`
- `Other Liabilities`
- `Short Term Investments`
- `Capital Assets`
- `Other Income`
- `Commissions Income`
- `Additional paid in capital`
- `Provision for Federal Taxes`
- `Company Stock`
- `Federal Tax Liabilities`
- `Commission and Fees`
- `Written Premium (MGA)`
- `Interest expense`
- `Commissions Expense`
- `Investments`
- `Outstanding loss and loss adjustment expense (Loss Adjustment Expense outstanding)`
- `Underwriting expenses (Commissions)`
- `Contra Revenue`

**Level 6**
- `None`
- `Bank`
- `Non - affiliate`
- `Affiliates`
- `Direct`
- `Ceded`
- `Non - Affiliates`
- `Assumed`
- `Admitted`
- `Taxable`
- `Common`
- `Air`
- `Senior Notes`
- `Non Travel`
- `CD`
- `Affiliate`
- `Corporate Tax`
- `Portfolio Transfer`
- `Step Up for Student`
- `Senior Note`
- `Travel`
- `FL State Deposits`
- `Non Taxable`
- `Profit`
- `AIF Commissions`
- `Brokerage Expense`
- `Mine Subsidence`
- `Sliding Scale Commissions`
- `Salary`
- `Ground`
