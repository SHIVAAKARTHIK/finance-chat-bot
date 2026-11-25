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
row_count: 97
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
- `Not set`: 74 rows
- `Balance`: 23 rows

**ACCOUNT_CLASS**
- `Asset`: 72 rows
- `Liability`: 23 rows
- `Equity`: 1 rows
- `Not set`: 1 rows

**ACCOUNT_TYPE**
- `Normal`: 97 rows

**RECONCILIATION_TYPE**
- `Basic`: 74 rows
- `Bank`: 23 rows

**RISK_TYPE**
- `Not set`: 83 rows
- `High`: 14 rows

**PREPARE_FREQUENCY**
- `Month end`: 97 rows

**APPROVE_FREQUENCY**
- `Month end`: 97 rows

**REVIEW_FREQUENCY**
- `Never`: 60 rows
- `Month end`: 37 rows

**PARENT_ACCOUNT_ID**
- `0`: 97 rows

**ACCOUNT_SUB_CLASS**
- `None`: 97 rows

**SYSTEM_CERTIFY**
- `Not allowed`: 64 rows
- `Allow all`: 33 rows

**CARRY_FORWARD**
- `Never`: 97 rows

**ACCOUNT_PROCEDURE**
- `None`: 97 rows

**ACCOUNT_PURPOSE**
- `None`: 97 rows

**SOURCE_FILE_NAME**
- `accountdimensions__20261116_194202.csv`: 97 rows

**MDP_CREATED_DATE**
- `2026-11-16 19:45:18.857373+00:00`: 97 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 19:45:18.857373+00:00`: 97 rows

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `account_fact_to_account` | `adra_account_facts` | many-to-one (from the fact) |
| `transaction_fact_to_account` | `adra_transaction_facts` | many-to-one (from the fact) |

## Notes

- Account attributes (risk type, reconciliation type) are per account and entity, not per period. To count
  accounts "for a period", count rows of adra_account_facts for that period joined to this table.

## Profile

Rows in the latest export: 97.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ACCOUNT_KEY` | STRING | 93 | 0 |  |  |
| `BASE_CLASS` | STRING | 2 | 0 | Balance | Not set |
| `ENGAGEMENT_KEY` | STRING | 1 | 0 |  |  |
| `PARENT_ACCOUNT_KEY` | STRING | 1 | 0 |  |  |
| `ACCOUNT_CLASS` | STRING | 4 | 0 | Asset | Not set |
| `ACCOUNT_TYPE` | STRING | 1 | 0 | Normal | Normal |
| `IS_KEY_ACCOUNT` | STRING | 2 | 0 | False | True |
| `RECONCILIATION_TYPE` | STRING | 2 | 0 | Bank | Basic |
| `RISK_TYPE` | STRING | 2 | 0 | High | Not set |
| `PREPARE_FREQUENCY` | STRING | 1 | 0 | Month end | Month end |
| `APPROVE_FREQUENCY` | STRING | 1 | 0 | Month end | Month end |
| `REVIEW_FREQUENCY` | STRING | 2 | 0 | Month end | Never |
| `ACCOUNT_ID` | STRING | 98 | 0 | 2267785 | 2283977 |
| `PARENT_ACCOUNT_ID` | STRING | 1 | 0 | 0 | 0 |
| `ACCOUNT_NUMBER` | STRING | 80 | 0 | 101101 | 333420 |
| `ACCOUNT_NAME` | STRING | 76 | 0 | ABC Test Account | Wells Fargo Bank |
| `ACCOUNT` | STRING | 79 | 0 | 101101 ABC Test Account | 333420 Non Admitted Assets - Prepaid ... |
| `ACCOUNT_SUB_CLASS` | STRING | 0 | 97 |  |  |
| `SYSTEM_CERTIFY` | STRING | 2 | 0 | Allow all | Not allowed |
| `CARRY_FORWARD` | STRING | 1 | 0 | Never | Never |
| `ACCOUNT_PROCEDURE` | STRING | 0 | 97 |  |  |
| `ACCOUNT_PURPOSE` | STRING | 0 | 97 |  |  |
| `LEGAL_ENTITY_KEY` | STRING | 9 | 0 |  |  |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | accountdimensions__20261116_194202.csv | accountdimensions__20261116_194202.csv |
| `HASH_KEY` | STRING | 94 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 19:45:18.857000 | 2026-11-16 19:45:18.857000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 19:45:18.857000 | 2026-11-16 19:45:18.857000 |

## Sample rows

| BASE_CLASS | ACCOUNT_CLASS | ACCOUNT_TYPE | IS_KEY_ACCOUNT | RECONCILIATION_TYPE | RISK_TYPE | PREPARE_FREQUENCY | APPROVE_FREQUENCY | REVIEW_FREQUENCY | ACCOUNT_ID | PARENT_ACCOUNT_ID | ACCOUNT_NUMBER | ACCOUNT_NAME | ACCOUNT | ACCOUNT_SUB_CLASS | SYSTEM_CERTIFY | CARRY_FORWARD | ACCOUNT_PROCEDURE | ACCOUNT_PURPOSE | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Not set | Not set | Normal | False | Basic | Not set | Month end | Month end | Month end | 2267785 | 0 | 101101 | ABC Test Account | 101101 ABC Test Account | NULL | Not allowed | Never | NULL | NULL | accountdimensions__20261116_194202.csv | <masked> | 2026-11-16 19:45:18.857000 | <masked> | 2026-11-16 19:45:18.857000 |
| Not set | Asset | Normal | False | Basic | Not set | Month end | Month end | Month end | 2273672 | 0 | 102100 | Regions - Operating | 102100 Regions - Operating | NULL | Not allowed | Never | NULL | NULL | accountdimensions__20261116_194202.csv | <masked> | 2026-11-16 19:45:18.857000 | <masked> | 2026-11-16 19:45:18.857000 |
| Not set | Asset | Normal | False | Basic | Not set | Month end | Month end | Month end | 2273673 | 0 | 102403 | Regions - Claims DEF - InsuranceD | 102403 Regions - Claims DEF - InsuranceD | NULL | Not allowed | Never | NULL | NULL | accountdimensions__20261116_194202.csv | <masked> | 2026-11-16 19:45:18.857000 | <masked> | 2026-11-16 19:45:18.857000 |
| Not set | Asset | Normal | False | Basic | Not set | Month end | Month end | Month end | 2273674 | 0 | 103300 | WF - Corp Sweep | 103300 WF - Corp Sweep | NULL | Not allowed | Never | NULL | NULL | accountdimensions__20261116_194202.csv | <masked> | 2026-11-16 19:45:18.857000 | <masked> | 2026-11-16 19:45:18.857000 |
| Not set | Asset | Normal | False | Basic | Not set | Month end | Month end | Month end | 2273675 | 0 | 103303 | Fixed Deposit (Long Term) | 103303 Fixed Deposit (Long Term) | NULL | Not allowed | Never | NULL | NULL | accountdimensions__20261116_194202.csv | <masked> | 2026-11-16 19:45:18.857000 | <masked> | 2026-11-16 19:45:18.857000 |
