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
row_count: 569
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
- `STAT`: 350 rows
- `MGA`: 219 rows

**Type**
- `Asset`: 213 rows
- `Expense`: 143 rows
- `Liability`: 89 rows
- `Revenue`: 88 rows
- `Equity`: 32 rows
- `Reporting`: 4 rows

**Level 0**
- `Balance Sheet`: 334 rows
- `Income Statement`: 231 rows
- `Misc (Reporting Only)`: 4 rows

**Level 1**
- `Asset`: 213 rows
- `Expense`: 143 rows
- `Liability`: 89 rows
- `Revenue`: 88 rows
- `Equity`: 32 rows
- `Reporting`: 4 rows

**Level 2**
- `Cash`: 78 rows
- `General and Administrative`: 60 rows
- `Underwriting expenses`: 52 rows
- `Investment Income`: 49 rows
- `Receivables and Recoverables`: 28 rows
- `Invested Assets`: 28 rows
- `Retained Earnings`: 26 rows
- `Insurance Policy Liabilities`: 26 rows
- `Property and Equipment`: 24 rows
- `Operational Liabilities`: 23 rows
- `Cash Equivalents`: 20 rows
- `Loss and loss adjustment expenses`: 18 rows
- `Financing and Debt`: 18 rows
- `Other assets`: 16 rows
- `Premiums earned`: 14 rows
- `Underwriting Liabilities`: 13 rows
- `Realized investment gains (losses)`: 12 rows
- `Federal Tax Assets`: 9 rows
- `Investment expense`: 6 rows
- `Service / Fee Income`: 5 rows
- `Other Liabilities`: 5 rows
- `Short Term Investments`: 5 rows
- `Capital Assets`: 4 rows
- `Other Income`: 4 rows
- `Commissions Income`: 3 rows
- `Additional paid in capital`: 3 rows
- `Provision for Federal Taxes`: 3 rows
- `Company Stock`: 3 rows
- `Federal Tax Liabilities`: 3 rows
- `Commission and Fees`: 2 rows
- `Written Premium (MGA)`: 2 rows
- `Interest expense`: 2 rows
- `Commissions Expense`: 1 rows
- `Investments`: 1 rows
- `Outstanding loss and loss adjustment expense (Loss Adjustment Expense outstanding)`: 1 rows
- `Underwriting expenses (Commissions)`: 1 rows
- `Contra Revenue`: 1 rows

**Level 6**
- `None`: 514 rows
- `Bank`: 6 rows
- `Non - affiliate`: 5 rows
- `Affiliates`: 5 rows
- `Direct`: 4 rows
- `Ceded`: 4 rows
- `Non - Affiliates`: 4 rows
- `Assumed`: 3 rows
- `Admitted`: 2 rows
- `Taxable`: 2 rows
- `Common`: 1 rows
- `Air`: 1 rows
- `Senior Notes`: 1 rows
- `Non Travel`: 1 rows
- `CD`: 1 rows
- `Affiliate`: 1 rows
- `Corporate Tax`: 1 rows
- `Portfolio Transfer`: 1 rows
- `Step Up for Student`: 1 rows
- `Senior Note`: 1 rows
- `Travel`: 1 rows
- `FL State Deposits`: 1 rows
- `Non Taxable`: 1 rows
- `Profit`: 1 rows
- `AIF Commissions`: 1 rows
- `Brokerage Expense`: 1 rows
- `Mine Subsidence`: 1 rows
- `Sliding Scale Commissions`: 1 rows
- `Salary`: 1 rows
- `Ground`: 1 rows

## Profile

Rows in the latest export: 569.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Future State CoA` | LONG | 577 | 0 | 100004 | 921000 |
| `Future State CoA Name` | STRING | 492 | 0 | 401k Contribution | Written Premium Offset |
| `STAT or MGA` | STRING | 2 | 0 | MGA | STAT |
| `Type` | STRING | 6 | 0 | Asset | Revenue |
| `Level 0` | STRING | 3 | 0 | Balance Sheet | Misc (Reporting Only) |
| `Level 1` | STRING | 6 | 0 | Asset | Revenue |
| `Level 2` | STRING | 37 | 0 | Additional paid in capital | Written Premium (MGA) |
| `Level 3` | STRING | 105 | 12 | Accounts payable - insurance companies | Written Premium |
| `Level 4` | STRING | 182 | 61 | Accounts Payable - Liability | Valuation Allowance |
| `Level 5` | STRING | 141 | 253 | 401k Contribution | Workers Comp |
| `Level 6` | STRING | 30 | 514 | AIF Commissions | Travel |

## Sample rows

| Future State CoA | Future State CoA Name | STAT or MGA | Type | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 | Level 6 |
|---|---|---|---|---|---|---|---|---|---|---|
| 100004 | Money Market - Insurance Carrier | MGA | Asset | Balance Sheet | Asset | Cash Equivalents | Bank - Fiduciary | Money Market | Insurance Carrier | NULL |
| 100007 | Money Market - Insurance Carrier | MGA | Asset | Balance Sheet | Asset | Cash Equivalents | Bank - Fiduciary | Money Market | Insurance Carrier | NULL |
| 101000 | Bank - Corporate | MGA | Asset | Balance Sheet | Asset | Cash | Bank - Corporate | Refunds - Zero - Balance Account | NULL | NULL |
| 101031 | Bank Corporate | MGA | Asset | Balance Sheet | Asset | Cash | Bank - Corporate | Refunds - Zero - Balance Account | Insurance Carrier | NULL |
| 101100 | Bank Corporate - Operating | MGA | Asset | Balance Sheet | Asset | Cash | Bank - Corporate | Operating | NULL | NULL |
