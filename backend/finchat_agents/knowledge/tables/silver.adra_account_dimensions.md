---
name: adra_account_dimensions
schema: silver
layer: silver
domain: recon
type: dim
status: active
purpose: 'ADRA reconciliation accounts: one row per GL account per legal entity (number, name, class, type, risk rating, reconciliation
  type, key-account flag).'
grain: one row per account per legal entity (ACCOUNT_KEY, ENGAGEMENT_KEY, LEGAL_ENTITY_KEY)
primary_key:
- ACCOUNT_KEY
- ENGAGEMENT_KEY
- LEGAL_ENTITY_KEY
entity_column: LEGAL_ENTITY_KEY
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms:
- account
- accounts
- gl account
- reconciliation account
- account master
- chart of accounts
- risk type
- key account
known_issues:
- code: all_string_columns
  note: Every column is stored as STRING. Compare text with trim() and lower().
reviewed: true
proposed_fields: []
---

# adra_account_dimensions

ADRA reconciliation accounts: one row per GL account per legal entity (number, name, class, type, risk rating,
reconciliation type, key-account flag).

> All columns are stored as text (STRING). Compare text with `trim()` and `lower()`. Users name accounts by
> ACCOUNT_NUMBER (e.g. 103300) or ACCOUNT_NAME.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ACCOUNT_KEY` | string | Surrogate account key. |  | `trim(ACCOUNT_KEY)` |
| `ENGAGEMENT_KEY` | string | Engagement key. |  | `trim(ENGAGEMENT_KEY)` |
| `LEGAL_ENTITY_KEY` | string | Legal entity key. |  | `trim(LEGAL_ENTITY_KEY)` |
| `ACCOUNT_NUMBER` | string | GL account number users type, e.g. 103300. | account number, account no, account | `trim(ACCOUNT_NUMBER)` |
| `ACCOUNT_NAME` | string | Account name, e.g. 'WF - Corp Sweep'. | account name, account description | `trim(ACCOUNT_NAME)` |
| `ACCOUNT_CLASS` | string | Account class. | account class | `trim(ACCOUNT_CLASS)` |
| `ACCOUNT_TYPE` | string | Account type. | account type | `trim(ACCOUNT_TYPE)` |
| `RISK_TYPE` | string | Risk rating of the account. | risk, risk type, risk rating | `trim(RISK_TYPE)` |
| `RECONCILIATION_TYPE` | string | Reconciliation type, e.g. Bank. | reconciliation type, recon type | `trim(RECONCILIATION_TYPE)` |
| `IS_KEY_ACCOUNT` | boolean | Key account flag. | key account | `lower(trim(IS_KEY_ACCOUNT)) = 'true'` |
| `BASE_CLASS` | string |  |  | `BASE_CLASS` |
| `PARENT_ACCOUNT_KEY` | string |  |  | `PARENT_ACCOUNT_KEY` |
| `PREPARE_FREQUENCY` | string |  |  | `PREPARE_FREQUENCY` |
| `APPROVE_FREQUENCY` | string |  |  | `APPROVE_FREQUENCY` |
| `REVIEW_FREQUENCY` | string |  |  | `REVIEW_FREQUENCY` |
| `ACCOUNT_ID` | string |  |  | `ACCOUNT_ID` |
| `PARENT_ACCOUNT_ID` | string |  |  | `PARENT_ACCOUNT_ID` |
| `ACCOUNT` | string |  |  | `ACCOUNT` |
| `ACCOUNT_SUB_CLASS` | string |  |  | `ACCOUNT_SUB_CLASS` |
| `SYSTEM_CERTIFY` | string |  |  | `SYSTEM_CERTIFY` |
| `CARRY_FORWARD` | string |  |  | `CARRY_FORWARD` |
| `ACCOUNT_PROCEDURE` | string |  |  | `ACCOUNT_PROCEDURE` |
| `ACCOUNT_PURPOSE` | string |  |  | `ACCOUNT_PURPOSE` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**IS_KEY_ACCOUNT**
- `True`: key account
- `False`: not a key account

**BASE_CLASS**
- `Not set`
- `Balance`

**ACCOUNT_CLASS**
- `Asset`
- `Liability`
- `Equity`
- `Not set`

**ACCOUNT_TYPE**
- `Normal`

**RECONCILIATION_TYPE**
- `Basic`
- `Bank`

**RISK_TYPE**
- `Not set`
- `High`

**PREPARE_FREQUENCY**
- `Month end`

**APPROVE_FREQUENCY**
- `Month end`

**REVIEW_FREQUENCY**
- `Never`
- `Month end`

**PARENT_ACCOUNT_ID**
- `0`

**ACCOUNT_SUB_CLASS**
- `None`

**SYSTEM_CERTIFY**
- `Not allowed`
- `Allow all`

**CARRY_FORWARD**
- `Never`

**ACCOUNT_PROCEDURE**
- `None`

**ACCOUNT_PURPOSE**
- `None`

**SOURCE_FILE_NAME**
- `accountdimensions__20261116_194202.csv`

**MDP_CREATED_DATE**
- `2026-11-16 19:45:18.857373+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 19:45:18.857373+00:00`

## Empty columns

Empty in every row: `ACCOUNT_SUB_CLASS`, `ACCOUNT_PROCEDURE`, `ACCOUNT_PURPOSE`. Do not filter or group on them.

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `account_fact_to_account` | `adra_account_facts` | many-to-one (from the fact) |
| `transaction_fact_to_account` | `adra_transaction_facts` | many-to-one (from the fact) |

## Notes

- Account attributes (risk type, reconciliation type) are per account and entity, not per period. To count
  accounts "for a period", count rows of adra_account_facts for that period joined to this table.
