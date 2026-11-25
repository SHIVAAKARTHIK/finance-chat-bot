# adra_account_facts

**Domain:** ADRA  
**Type:** fact table  
**Full name:** `lakehouse_mvpai.silver.adra_account_facts`  
**Grain:** one row per (ACCOUNT_KEY, ENGAGEMENT_KEY, LEGAL_ENTITY_KEY, PERIOD_KEY)  
**Also called:** reconciliations, account reconciliations, account balances  

Account reconciliations: one row per account per legal entity per period, with workflow status, finalized flag, balances, unidentified (unreconciled) balances, documents and rejections.

> All columns are stored as text (STRING). Cast numbers and dates as shown in *SQL expression*; compare text with `trim()` and `lower()`.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ACCOUNT_KEY` | string | Account key (FK to adra_account_dimensions). |  | `trim(ACCOUNT_KEY)` |
| `ENGAGEMENT_KEY` | string | Engagement key. |  | `trim(ENGAGEMENT_KEY)` |
| `LEGAL_ENTITY_KEY` | string | Legal entity key (FK to adra_legal_entity_dimensions). |  | `trim(LEGAL_ENTITY_KEY)` |
| `PERIOD_KEY` | string | Period key (FK to adra_period_dimensions). |  | `trim(PERIOD_KEY)` |
| `ACCOUNT_STATUS` | string | Reconciliation workflow status. Values may carry trailing spaces: compare with TRIM and case-insensitively. | status, reconciliation status, account status | `trim(ACCOUNT_STATUS)` |
| `IS_FINALIZED` | boolean | Reconciliation closed for the period. 'Pending closure' or 'unfinished' = not finalized. Independent of ACCOUNT_STATUS. | finalized, finalised, closed, pending closure | `lower(trim(IS_FINALIZED)) = 'true'` |
| `IS_CARRIED_FORWARD` | boolean | Carried forward from the previous period. | carried forward | `lower(trim(IS_CARRIED_FORWARD)) = 'true'` |
| `BALANCE` | decimal | GL balance in entity currency. Point-in-time per period: never sum across periods. | balance, account balance, gl balance | `TRY_CAST(BALANCE AS DECIMAL(38,2))` |
| `BALANCE_ABS` | decimal | Absolute GL balance (for 'largest balance'). | absolute balance | `TRY_CAST(BALANCE_ABS AS DECIMAL(38,2))` |
| `UNIDENTIFIED_BALANCE` | decimal | Unidentified (unreconciled) difference: GL balance not supported by reconciling items. Point-in-time. | unidentified balance, unreconciled difference, unexplained difference | `TRY_CAST(UNIDENTIFIED_BALANCE AS DECIMAL(38,2))` |
| `UNIDENTIFIED_BALANCE_ABS` | decimal | Absolute unidentified balance; use for totals and 'largest difference'. | absolute unidentified balance, total unidentified | `TRY_CAST(UNIDENTIFIED_BALANCE_ABS AS DECIMAL(38,2))` |
| `NO_OF_DOCUMENTS` | integer | Number of supporting documents attached. | documents, supporting documents | `TRY_CAST(NO_OF_DOCUMENTS AS INT)` |
| `NO_OF_REJECTS` | integer | Number of times the reconciliation was rejected. | rejections, rejects | `TRY_CAST(NO_OF_REJECTS AS INT)` |
| `PREPARER_NAME` | string | Assigned preparer (person). **PII: mask unless the user may view personal data; never filter or group by it.** | preparer, assigned preparer | `trim(PREPARER_NAME)` |
| `APPROVER_NAME` | string | Assigned approver (person). **PII: mask unless the user may view personal data; never filter or group by it.** | approver, assigned approver | `trim(APPROVER_NAME)` |
| `PREPARED_BY_NAME` | string | Person who actually prepared it. **PII: mask unless the user may view personal data; never filter or group by it.** | prepared by | `trim(PREPARED_BY_NAME)` |
| `APPROVED_BY_NAME` | string | Person who actually approved it. **PII: mask unless the user may view personal data; never filter or group by it.** | approved by | `trim(APPROVED_BY_NAME)` |
| `PREPARED_DATE` | timestamp | When it was prepared. | prepared date, prepared on | `TRY_CAST(PREPARED_DATE AS TIMESTAMP)` |
| `APPROVED_DATE` | timestamp | When it was approved (NULL = not approved). | approved date, approved on | `TRY_CAST(APPROVED_DATE AS TIMESTAMP)` |

## Values

**ACCOUNT_STATUS**
- `Not prepared`: preparer has not prepared it yet
- `Prepared`: prepared, awaiting approval
- `Approved`: approved by the approver
- `Approval not needed`: no approval step required

**IS_FINALIZED**
- `True`: finalized
- `False`: not finalized

**IS_CARRIED_FORWARD**
- `True`: carried forward
- `False`: not carried forward

## Joins (approved, use the full key)

| Join | To table | Cardinality | Condition |
|---|---|---|---|
| `account_fact_to_account` | `adra_account_dimensions` | many-to-one | `adra_account_facts.ACCOUNT_KEY = adra_account_dimensions.ACCOUNT_KEY AND adra_account_facts.ENGAGEMENT_KEY = adra_account_dimensions.ENGAGEMENT_KEY AND adra_account_facts.LEGAL_ENTITY_KEY = adra_account_dimensions.LEGAL_ENTITY_KEY` |
| `account_fact_to_period` | `adra_period_dimensions` | many-to-one | `adra_account_facts.PERIOD_KEY = adra_period_dimensions.PERIOD_KEY AND adra_account_facts.ENGAGEMENT_KEY = adra_period_dimensions.ENGAGEMENT_KEY AND adra_account_facts.LEGAL_ENTITY_KEY = adra_period_dimensions.LEGAL_ENTITY_KEY` |
| `account_fact_to_legal_entity` | `adra_legal_entity_dimensions` | many-to-one | `adra_account_facts.LEGAL_ENTITY_KEY = adra_legal_entity_dimensions.LEGAL_ENTITY_KEY AND adra_account_facts.ENGAGEMENT_KEY = adra_legal_entity_dimensions.ENGAGEMENT_KEY` |

## Named metrics

| Metric | Meaning | SQL | Additivity |
|---|---|---|---|
| `account_count` | Number of account reconciliations. | `COUNT(*)` | additive |
| `finalized_count` | Reconciliations finalized. | `SUM(CASE WHEN lower(trim(IS_FINALIZED)) = 'true' THEN 1 ELSE 0 END)` | additive |
| `not_finalized_count` | Reconciliations pending closure (not finalized). | `SUM(CASE WHEN lower(trim(IS_FINALIZED)) = 'false' THEN 1 ELSE 0 END)` | additive |
| `pct_finalized` | Share of reconciliations finalized, in percent. | `100.0 * SUM(CASE WHEN lower(trim(IS_FINALIZED)) = 'true' THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0)` | non additive |
| `total_balance` | Total GL balance. Semi-additive: add across accounts within ONE period, never across periods. | `SUM(TRY_CAST(BALANCE AS DECIMAL(38,2)))` | semi additive period |
| `total_unidentified_balance_abs` | Total absolute unidentified balance. Semi-additive over periods. | `SUM(TRY_CAST(UNIDENTIFIED_BALANCE_ABS AS DECIMAL(38,2)))` | semi additive period |
| `accounts_without_documents` | Reconciliations with no supporting documents. | `SUM(CASE WHEN coalesce(TRY_CAST(NO_OF_DOCUMENTS AS INT), 0) = 0 THEN 1 ELSE 0 END)` | additive |
