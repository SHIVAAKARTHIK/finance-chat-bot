# adra_account_dimensions

**Domain:** ADRA  
**Type:** dimension table  
**Full name:** `lakehouse_mvpai.silver.adra_account_dimensions`  
**Grain:** one row per (ACCOUNT_KEY, ENGAGEMENT_KEY, LEGAL_ENTITY_KEY)  
**Also called:** account, gl account, reconciliation account  

ADRA reconciliation accounts: one row per GL account per legal entity (number, name, class, type, risk, reconciliation type).

> All columns are stored as text (STRING). Cast numbers and dates as shown in *SQL expression*; compare text with `trim()` and `lower()`.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ACCOUNT_KEY` | string | Surrogate account key. |  | `trim(ACCOUNT_KEY)` |
| `ENGAGEMENT_KEY` | string | Engagement key. |  | `trim(ENGAGEMENT_KEY)` |
| `LEGAL_ENTITY_KEY` | string | Legal entity key. |  | `trim(LEGAL_ENTITY_KEY)` |
| `ACCOUNT_NUMBER` | string | GL account number users type, e.g. 103300, 213130. | account number, account | `trim(ACCOUNT_NUMBER)` |
| `ACCOUNT_NAME` | string | Account name, e.g. 'WF - Corp Sweep'. | account name, account description | `trim(ACCOUNT_NAME)` |
| `ACCOUNT_CLASS` | string | Account class. | account class | `trim(ACCOUNT_CLASS)` |
| `ACCOUNT_TYPE` | string | Account type. | account type | `trim(ACCOUNT_TYPE)` |
| `RISK_TYPE` | string | Risk rating of the account. | risk, risk type, risk rating | `trim(RISK_TYPE)` |
| `RECONCILIATION_TYPE` | string | Reconciliation type, e.g. Bank. | reconciliation type, recon type | `trim(RECONCILIATION_TYPE)` |
| `IS_KEY_ACCOUNT` | boolean | Key account flag. | key account | `lower(trim(IS_KEY_ACCOUNT)) = 'true'` |

## Values

**IS_KEY_ACCOUNT**
- `True`: key account
- `False`: not a key account

## Joins (approved, use the full key)

| Join | To table | Cardinality | Condition |
|---|---|---|---|
| `account_fact_to_account` | `adra_account_facts` | many-to-one | `adra_account_facts.ACCOUNT_KEY = adra_account_dimensions.ACCOUNT_KEY AND adra_account_facts.ENGAGEMENT_KEY = adra_account_dimensions.ENGAGEMENT_KEY AND adra_account_facts.LEGAL_ENTITY_KEY = adra_account_dimensions.LEGAL_ENTITY_KEY` |
| `transaction_fact_to_account` | `adra_transaction_facts` | many-to-one | `adra_transaction_facts.ACCOUNT_KEY = adra_account_dimensions.ACCOUNT_KEY AND adra_transaction_facts.ENGAGEMENT_KEY = adra_account_dimensions.ENGAGEMENT_KEY AND adra_transaction_facts.LEGAL_ENTITY_KEY = adra_account_dimensions.LEGAL_ENTITY_KEY` |
