---
name: manage_close_adra_unreconciled_accounts
schema: gold
layer: gold
domain: recon
type: view
status: active
purpose: Lists unreconciled ADRA accounts with GL/supporting balances and their difference.
grain: one row per account; entity and period
primary_key:
- ACCOUNT
- LEGAL_ENTITY
- PERIOD_NAME
entity_column: LEGAL_ENTITY
period_columns:
- PERIOD_NAME
pii_columns: []
synonyms: []
built_from:
- adra_account_dimensions
- adra_account_facts
- adra_transaction_facts
known_issues: []
row_count: 56
proposed_fields: []
reviewed:
- superseded_by
superseded_by:
- silver.adra_account_facts
- silver.adra_account_dimensions
---

# manage_close_adra_unreconciled_accounts

> Superseded: this table is a copy of ADRA data. Answers use the source of truth `silver.adra_account_facts`, `silver.adra_account_dimensions` (decision 21 Nov 2026).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ACCOUNT` | string |  |  | `ACCOUNT` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `ENTITY_NAME` | string |  |  | `ENTITY_NAME` |
| `GL_BALANCE` | decimal |  |  | `GL_BALANCE` |
| `SUPPORTING_BALANCE` | decimal |  |  | `SUPPORTING_BALANCE` |
| `DIFFERENCE` | decimal |  |  | `DIFFERENCE` |
| `ACTION` | string |  |  | `ACTION` |
| `PERIOD_NAME` | string |  |  | `PERIOD_NAME` |

## Values

**ACCOUNT**
- `176100 Credit Card - Expenses Control`: 6 rows
- `109023 CMC control account`: 3 rows
- `239001 IBA Liabilities`: 3 rows
- `199001 IBA Debtor`: 3 rows
- `144000 Accrued Brokerage`: 3 rows
- `109036 IBA Bank Account CAD`: 2 rows
- `109051 JPMC Bank`: 1 rows
- `142000 Fixed Asset Control Account`: 1 rows
- `211211 Direct LAE Reserves`: 1 rows
- `191100 Prepaid expenses`: 1 rows
- `191110 Prepaid expenses - admitted`: 1 rows
- `239210 Use Tax Payable`: 1 rows
- `212200 Assumed Unearned Premiums`: 1 rows
- `141111 Premium Receivable - Current - Direct`: 1 rows
- `103803 Equity (Investment)`: 1 rows
- `131623 Bonds - State Acct SET1`: 1 rows
- `109045 IBA Bank Account NOK`: 1 rows
- `221400 INTERCOMPANY TRADE PAYABLES`: 1 rows
- `109053 CITI Bank`: 1 rows
- `333420 Non Admitted Assets - Prepaid Expense`: 1 rows
- `109033 IBA Bank Account GBP`: 1 rows
- `222200 Corporate taxes payable`: 1 rows
- `213440 Accounts Payable`: 1 rows
- `213130 ACCOUNTS RECEIVABLE CREDIT BALANCES`: 1 rows
- `141121 Premium Receivable - Current - Assumed`: 1 rows
- `213230 COST OF SALES ACCRUAL`: 1 rows
- `211111 Direct Loss Reserves`: 1 rows
- `145100 Deferred policy acquisition costs- Direct`: 1 rows
- `213210 DEPOSITS AND UNEARNED REVENUE`: 1 rows
- `211220 Accounts Payable`: 1 rows
- `123100 INTERCOMPANY RECEIVABLE ACCRUAL`: 1 rows
- `231000 Accounts payable - insurance companies`: 1 rows
- `192200 Salvage and subrogation recoverable`: 1 rows
- `122500 INTERCOMPANY TRADE RECEIVABLES`: 1 rows
- `131300 Bonds - Premium`: 1 rows
- `239200 Taxes Payable`: 1 rows
- `222110 Premium taxes payable`: 1 rows
- `123200 ACCOUNTS RECEIVABLE ACCRUALS.`: 1 rows
- `212100 Direct Unearned Premiums`: 1 rows
- `142200 Funds held by on deposit`: 1 rows
- `213110 ACCRUED BONUSES & COMMISSION`: 1 rows
- `109521 FHLB - Deposit`: 1 rows

**SUPPORTING_BALANCE**
- `0`: 34 rows
- `2754368.12`: 1 rows
- `526812.53`: 1 rows
- `376420`: 1 rows
- `-210983`: 1 rows
- `-14148`: 1 rows
- `988931`: 1 rows
- `-72408`: 1 rows
- `6529685.82`: 1 rows
- `-140351`: 1 rows
- `1254141.93`: 1 rows
- `-15651157.75`: 1 rows
- `2531890.55`: 1 rows
- `-106760`: 1 rows
- `-3182019.99`: 1 rows
- `10496.08`: 1 rows
- `-2929121.74`: 1 rows
- `-232.96`: 1 rows
- `-116911`: 1 rows
- `116830.91`: 1 rows
- `172684.94`: 1 rows
- `301489`: 1 rows
- `17617.63`: 1 rows

## Profile

Rows in the latest export: 56.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ACCOUNT` | STRING | 43 | 0 | 103803 Equity (Investment) | 333420 Non Admitted Assets - Prepaid ... |
| `LEGAL_ENTITY` | STRING | 8 | 0 |  |  |
| `ENTITY_NAME` | STRING | 8 | 0 |  |  |
| `GL_BALANCE` | DECIMAL | 57 | 0 | -19697737.46 | 6531120.01 |
| `SUPPORTING_BALANCE` | DECIMAL | 24 | 0 | -15651157.75 | 6529685.82 |
| `DIFFERENCE` | DECIMAL | 59 | 0 | -19697737.46 | 1193073.56 |
| `ACTION` | STRING | 57 | 0 | https://balancer.adra.com/engagements... | https://balancer.adra.com/engagements... |
| `PERIOD_NAME` | STRING | 3 | 0 |  |  |

## Sample rows

| ACCOUNT | GL_BALANCE | SUPPORTING_BALANCE | DIFFERENCE | ACTION | PERIOD_NAME |
|---|---|---|---|---|---|
| 103803 Equity (Investment) | 39599 | 0 | 39599 | https://balancer.adra.com/engagements... | (altered in export) |
| 109051 JPMC Bank | 154878 | 0 | 154878 | https://balancer.adra.com/engagements... | (altered in export) |
| 109053 CITI Bank | 205407 | 0 | 205407 | https://balancer.adra.com/engagements... | (altered in export) |
| 109521 FHLB - Deposit | 45867 | 0 | 45867 | https://balancer.adra.com/engagements... | (altered in export) |
| 131300 Bonds - Premium | 35066 | 0 | 35066 | https://balancer.adra.com/engagements... | (altered in export) |
