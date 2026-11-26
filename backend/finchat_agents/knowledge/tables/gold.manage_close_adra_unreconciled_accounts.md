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
- `176100 Credit Card - Expenses Control`
- `109023 CMC control account`
- `239001 IBA Liabilities`
- `199001 IBA Debtor`
- `144000 Accrued Brokerage`
- `109036 IBA Bank Account CAD`
- `109051 JPMC Bank`
- `142000 Fixed Asset Control Account`
- `211211 Direct LAE Reserves`
- `191100 Prepaid expenses`
- `191110 Prepaid expenses - admitted`
- `239210 Use Tax Payable`
- `212200 Assumed Unearned Premiums`
- `141111 Premium Receivable - Current - Direct`
- `103803 Equity (Investment)`
- `131623 Bonds - State Acct SET1`
- `109045 IBA Bank Account NOK`
- `221400 INTERCOMPANY TRADE PAYABLES`
- `109053 CITI Bank`
- `333420 Non Admitted Assets - Prepaid Expense`
- `109033 IBA Bank Account GBP`
- `222200 Corporate taxes payable`
- `213440 Accounts Payable`
- `213130 ACCOUNTS RECEIVABLE CREDIT BALANCES`
- `141121 Premium Receivable - Current - Assumed`
- `213230 COST OF SALES ACCRUAL`
- `211111 Direct Loss Reserves`
- `145100 Deferred policy acquisition costs- Direct`
- `213210 DEPOSITS AND UNEARNED REVENUE`
- `211220 Accounts Payable`
- `123100 INTERCOMPANY RECEIVABLE ACCRUAL`
- `231000 Accounts payable - insurance companies`
- `192200 Salvage and subrogation recoverable`
- `122500 INTERCOMPANY TRADE RECEIVABLES`
- `131300 Bonds - Premium`
- `239200 Taxes Payable`
- `222110 Premium taxes payable`
- `123200 ACCOUNTS RECEIVABLE ACCRUALS.`
- `212100 Direct Unearned Premiums`
- `142200 Funds held by on deposit`
- `213110 ACCRUED BONUSES & COMMISSION`
- `109521 FHLB - Deposit`

**SUPPORTING_BALANCE**
- `0`
- `2754368.12`
- `526812.53`
- `376420`
- `-210983`
- `-14148`
- `988931`
- `-72408`
- `6529685.82`
- `-140351`
- `1254141.93`
- `-15651157.75`
- `2531890.55`
- `-106760`
- `-3182019.99`
- `10496.08`
- `-2929121.74`
- `-232.96`
- `-116911`
- `116830.91`
- `172684.94`
- `301489`
- `17617.63`
