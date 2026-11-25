# ADRA verified queries

Verified question → SQL pairs (DEV business ground truth only; never add hold-out questions).

## What is the reconciliation status of account 103300 for 100-Northwind in Feb 25?

**Expected answer:** Approved (account 103300, WF - Corp Sweep)

```sql
SELECT a.ACCOUNT_NUMBER, a.ACCOUNT_NAME, trim(f.ACCOUNT_STATUS) AS account_status
FROM lakehouse_mvpai.silver.adra_account_facts f
JOIN lakehouse_mvpai.silver.adra_account_dimensions a ON f.ACCOUNT_KEY = a.ACCOUNT_KEY AND f.ENGAGEMENT_KEY = a.ENGAGEMENT_KEY AND f.LEGAL_ENTITY_KEY = a.LEGAL_ENTITY_KEY
JOIN lakehouse_mvpai.silver.adra_period_dimensions p ON f.PERIOD_KEY = p.PERIOD_KEY AND f.ENGAGEMENT_KEY = p.ENGAGEMENT_KEY AND f.LEGAL_ENTITY_KEY = p.LEGAL_ENTITY_KEY
WHERE f.ENGAGEMENT_KEY = '581' AND f.LEGAL_ENTITY_KEY = '14781'
  AND p.PERIOD_NAME = 'Feb 25' AND trim(a.ACCOUNT_NUMBER) = '103300'
```

## Has account 103300 been finalized for 100-Northwind in Feb 25?

**Expected answer:** No, not finalized (status is Approved, IS_FINALIZED is False)

```sql
SELECT a.ACCOUNT_NUMBER, lower(trim(f.IS_FINALIZED)) = 'true' AS is_finalized
FROM lakehouse_mvpai.silver.adra_account_facts f
JOIN lakehouse_mvpai.silver.adra_account_dimensions a ON f.ACCOUNT_KEY = a.ACCOUNT_KEY AND f.ENGAGEMENT_KEY = a.ENGAGEMENT_KEY AND f.LEGAL_ENTITY_KEY = a.LEGAL_ENTITY_KEY
JOIN lakehouse_mvpai.silver.adra_period_dimensions p ON f.PERIOD_KEY = p.PERIOD_KEY AND f.ENGAGEMENT_KEY = p.ENGAGEMENT_KEY AND f.LEGAL_ENTITY_KEY = p.LEGAL_ENTITY_KEY
WHERE f.ENGAGEMENT_KEY = '581' AND f.LEGAL_ENTITY_KEY = '14781'
  AND p.PERIOD_NAME = 'Feb 25' AND trim(a.ACCOUNT_NUMBER) = '103300'
```

## How many Northwind accounts are pending closure for Feb 2025?

**Expected answer:** 38 accounts not finalized

```sql
SELECT SUM(CASE WHEN lower(trim(f.IS_FINALIZED)) = 'false' THEN 1 ELSE 0 END) AS not_finalized
FROM lakehouse_mvpai.silver.adra_account_facts f
JOIN lakehouse_mvpai.silver.adra_period_dimensions p ON f.PERIOD_KEY = p.PERIOD_KEY AND f.ENGAGEMENT_KEY = p.ENGAGEMENT_KEY AND f.LEGAL_ENTITY_KEY = p.LEGAL_ENTITY_KEY
WHERE f.ENGAGEMENT_KEY = '581' AND f.LEGAL_ENTITY_KEY = '14781' AND p.PERIOD_NAME = 'Feb 25'
```

## What is the unidentified balance on account 213130 for 561 - Cars USA Shipping, LLC in Oct 26?

**Expected answer:** -455,376.16

```sql
SELECT a.ACCOUNT_NUMBER, a.ACCOUNT_NAME, TRY_CAST(f.UNIDENTIFIED_BALANCE AS DECIMAL(38,2)) AS unidentified_balance
FROM lakehouse_mvpai.silver.adra_account_facts f
JOIN lakehouse_mvpai.silver.adra_account_dimensions a ON f.ACCOUNT_KEY = a.ACCOUNT_KEY AND f.ENGAGEMENT_KEY = a.ENGAGEMENT_KEY AND f.LEGAL_ENTITY_KEY = a.LEGAL_ENTITY_KEY
JOIN lakehouse_mvpai.silver.adra_period_dimensions p ON f.PERIOD_KEY = p.PERIOD_KEY AND f.ENGAGEMENT_KEY = p.ENGAGEMENT_KEY AND f.LEGAL_ENTITY_KEY = p.LEGAL_ENTITY_KEY
WHERE f.ENGAGEMENT_KEY = '581' AND f.LEGAL_ENTITY_KEY = '14782'
  AND p.PERIOD_NAME = 'Oct 26' AND trim(a.ACCOUNT_NUMBER) = '213130'
```

## What is the total absolute unidentified balance for 561 - Cars USA Shipping, LLC in Oct 26?

**Expected answer:** 22,831,252.26

```sql
SELECT SUM(TRY_CAST(f.UNIDENTIFIED_BALANCE_ABS AS DECIMAL(38,2))) AS total_unidentified_abs
FROM lakehouse_mvpai.silver.adra_account_facts f
JOIN lakehouse_mvpai.silver.adra_period_dimensions p ON f.PERIOD_KEY = p.PERIOD_KEY AND f.ENGAGEMENT_KEY = p.ENGAGEMENT_KEY AND f.LEGAL_ENTITY_KEY = p.LEGAL_ENTITY_KEY
WHERE f.ENGAGEMENT_KEY = '581' AND f.LEGAL_ENTITY_KEY = '14782' AND p.PERIOD_NAME = 'Oct 26'
```

## How many transactions are in each status for account 153300 in Oct 26?

**Expected answer:** Required adjustment: 2

```sql
SELECT trim(f.TRANSACTION_STATUS) AS transaction_status, COUNT(*) AS transactions
FROM lakehouse_mvpai.silver.adra_transaction_facts f
JOIN lakehouse_mvpai.silver.adra_account_dimensions a ON f.ACCOUNT_KEY = a.ACCOUNT_KEY AND f.ENGAGEMENT_KEY = a.ENGAGEMENT_KEY AND f.LEGAL_ENTITY_KEY = a.LEGAL_ENTITY_KEY
JOIN lakehouse_mvpai.silver.adra_period_dimensions p ON f.PERIOD_KEY = p.PERIOD_KEY AND f.ENGAGEMENT_KEY = p.ENGAGEMENT_KEY AND f.LEGAL_ENTITY_KEY = p.LEGAL_ENTITY_KEY
WHERE f.ENGAGEMENT_KEY = '581' AND f.LEGAL_ENTITY_KEY = '14782'
  AND p.PERIOD_NAME = 'Oct 26' AND trim(a.ACCOUNT_NUMBER) = '153300'
GROUP BY trim(f.TRANSACTION_STATUS)
```
