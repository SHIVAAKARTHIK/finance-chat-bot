-- Ground truth for question_bank_adra_fynapse_v1.yaml
-- Read-only. Run once in the Databricks SQL editor, then download the result as CSV.
-- Output: one row per (qid, k) with the value as text. Person names are NOT exported
-- (PII questions only check whether a value is populated).
-- Entity keys: 100-Northwind = LEGAL_ENTITY_KEY 14781 (data period Feb 25)
--              561-Cars USA Shipping = LEGAL_ENTITY_KEY 14782 (data period Oct 26)

WITH af AS (
  SELECT f.*,
         d.ACCOUNT_NUMBER, d.ACCOUNT_NAME, d.RISK_TYPE, d.RECONCILIATION_TYPE, d.ACCOUNT_TYPE
  FROM lakehouse_mvpai.silver.adra_account_facts f
  LEFT JOIN lakehouse_mvpai.silver.adra_account_dimensions d
    ON f.ACCOUNT_KEY = d.ACCOUNT_KEY
   AND f.ENGAGEMENT_KEY = d.ENGAGEMENT_KEY
   AND f.LEGAL_ENTITY_KEY = d.LEGAL_ENTITY_KEY
),
tf AS (
  SELECT t.*, d.ACCOUNT_NUMBER
  FROM lakehouse_mvpai.silver.adra_transaction_facts t
  LEFT JOIN lakehouse_mvpai.silver.adra_account_dimensions d
    ON t.ACCOUNT_KEY = d.ACCOUNT_KEY
   AND t.ENGAGEMENT_KEY = d.ENGAGEMENT_KEY
   AND t.LEGAL_ENTITY_KEY = d.LEGAL_ENTITY_KEY
),
fy AS (
  SELECT * FROM lakehouse_mvpai.silver.fact_fynapse_slr_journals
),
answers AS (

-- S0 sanity: which periods each ADRA entity has (confirms Feb 25 / Oct 26 labels)
SELECT 'S0' AS qid,
       concat(CAST(f.LEGAL_ENTITY_KEY AS STRING), ' | ', coalesce(CAST(p.PERIOD_NAME AS STRING), '?'), ' | ', coalesce(CAST(p.PERIOD AS STRING), '?')) AS k,
       CAST(COUNT(*) AS STRING) AS v
FROM lakehouse_mvpai.silver.adra_account_facts f
LEFT JOIN lakehouse_mvpai.silver.adra_period_dimensions p
  ON f.PERIOD_KEY = p.PERIOD_KEY AND f.ENGAGEMENT_KEY = p.ENGAGEMENT_KEY AND f.LEGAL_ENTITY_KEY = p.LEGAL_ENTITY_KEY
GROUP BY f.LEGAL_ENTITY_KEY, p.PERIOD_NAME, p.PERIOD

-- ===================== ADRA =====================
UNION ALL  -- A01 balance of account 141111, Northwind
SELECT 'A01', 'balance', CAST(SUM(TRY_CAST(BALANCE AS DECIMAL(38,2))) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14781' AND trim(ACCOUNT_NUMBER) = '141111'
UNION ALL
SELECT 'A01', 'rows', CAST(COUNT(*) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14781' AND trim(ACCOUNT_NUMBER) = '141111'

UNION ALL  -- A02 status of account 213130, entity 561
SELECT 'A02', concat('status=', trim(ACCOUNT_STATUS)), CAST(COUNT(*) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14782' AND trim(ACCOUNT_NUMBER) = '213130'
GROUP BY trim(ACCOUNT_STATUS)

UNION ALL  -- A03 is account 141111 finalized, Northwind
SELECT 'A03', concat('is_finalized=', trim(IS_FINALIZED)), CAST(COUNT(*) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14781' AND trim(ACCOUNT_NUMBER) = '141111'
GROUP BY trim(IS_FINALIZED)

UNION ALL  -- A04 Northwind accounts by status
SELECT 'A04', coalesce(trim(ACCOUNT_STATUS), '(null)'), CAST(COUNT(*) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14781' GROUP BY trim(ACCOUNT_STATUS)

UNION ALL  -- A05 561 accounts by status
SELECT 'A05', coalesce(trim(ACCOUNT_STATUS), '(null)'), CAST(COUNT(*) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14782' GROUP BY trim(ACCOUNT_STATUS)

UNION ALL  -- A06 561 finalized count
SELECT 'A06', 'finalized', CAST(SUM(CASE WHEN lower(trim(IS_FINALIZED)) = 'true' THEN 1 ELSE 0 END) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14782'

UNION ALL  -- A07 561 % finalized
SELECT 'A07', 'pct_finalized',
       CAST(ROUND(100.0 * SUM(CASE WHEN lower(trim(IS_FINALIZED)) = 'true' THEN 1 ELSE 0 END) / COUNT(*), 1) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14782'
UNION ALL
SELECT 'A07', 'total_accounts', CAST(COUNT(*) AS STRING) FROM af WHERE LEGAL_ENTITY_KEY = '14782'

UNION ALL  -- A08 Northwind total balance
SELECT 'A08', 'total_balance', CAST(SUM(TRY_CAST(BALANCE AS DECIMAL(38,2))) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14781'

UNION ALL  -- A09 Northwind total absolute unidentified balance
SELECT 'A09', 'total_unidentified_abs', CAST(SUM(TRY_CAST(UNIDENTIFIED_BALANCE_ABS AS DECIMAL(38,2))) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14781'

UNION ALL  -- A10 561 top 5 accounts by absolute balance
SELECT * FROM (
  SELECT 'A10', concat(trim(ACCOUNT_NUMBER), ' | ', trim(ACCOUNT_NAME)),
         CAST(TRY_CAST(BALANCE_ABS AS DECIMAL(38,2)) AS STRING)
  FROM af WHERE LEGAL_ENTITY_KEY = '14782'
  ORDER BY TRY_CAST(BALANCE_ABS AS DECIMAL(38,2)) DESC
  LIMIT 5
)

UNION ALL  -- A11 Northwind accounts by risk type
SELECT 'A11', coalesce(trim(RISK_TYPE), '(null)'), CAST(COUNT(*) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14781' GROUP BY trim(RISK_TYPE)

UNION ALL  -- A12 561 absolute unidentified balance by reconciliation type
SELECT 'A12', coalesce(trim(RECONCILIATION_TYPE), '(null)'),
       CAST(SUM(TRY_CAST(UNIDENTIFIED_BALANCE_ABS AS DECIMAL(38,2))) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14782' GROUP BY trim(RECONCILIATION_TYPE)

UNION ALL  -- A13 Northwind accounts with no supporting documents
SELECT 'A13', 'accounts_without_documents',
       CAST(SUM(CASE WHEN coalesce(TRY_CAST(NO_OF_DOCUMENTS AS INT), 0) = 0 THEN 1 ELSE 0 END) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14781'

UNION ALL  -- A14 Northwind total rejections
SELECT 'A14', 'total_rejections', CAST(SUM(coalesce(TRY_CAST(NO_OF_REJECTS AS INT), 0)) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14781'

UNION ALL  -- A15 transactions on account 222120, Northwind
SELECT 'A15', 'transactions', CAST(COUNT(*) AS STRING)
FROM tf WHERE LEGAL_ENTITY_KEY = '14781' AND trim(ACCOUNT_NUMBER) = '222120'

UNION ALL  -- A16 total absolute transaction amount, account 153300, 561
SELECT 'A16', 'total_amount_abs', CAST(SUM(TRY_CAST(AMOUNT_ABS AS DECIMAL(38,2))) AS STRING)
FROM tf WHERE LEGAL_ENTITY_KEY = '14782' AND trim(ACCOUNT_NUMBER) = '153300'

UNION ALL  -- A17 561 transactions by type
SELECT 'A17', coalesce(trim(TRANSACTION_TYPE), '(null)'), CAST(COUNT(*) AS STRING)
FROM tf WHERE LEGAL_ENTITY_KEY = '14782' GROUP BY trim(TRANSACTION_TYPE)

UNION ALL  -- A18 oldest transaction age, Northwind
SELECT 'A18', 'max_age_days', CAST(MAX(TRY_CAST(AGE_DAYS AS INT)) AS STRING)
FROM tf WHERE LEGAL_ENTITY_KEY = '14781'

UNION ALL  -- A19 561 transactions by age group
SELECT 'A19', coalesce(trim(AGE_GROUP), '(null)'), CAST(COUNT(*) AS STRING)
FROM tf WHERE LEGAL_ENTITY_KEY = '14782' GROUP BY trim(AGE_GROUP)

UNION ALL  -- A22 preparer populated for account 141111 (no names exported)
SELECT 'A22', 'preparer_populated',
       CASE WHEN MAX(coalesce(trim(PREPARER_NAME), '')) <> '' THEN 'yes' ELSE 'no' END
FROM af WHERE LEGAL_ENTITY_KEY = '14781' AND trim(ACCOUNT_NUMBER) = '141111'

UNION ALL  -- A23 approver + approved date populated for account 213130 (no names exported)
SELECT 'A23', 'approver_populated',
       CASE WHEN MAX(coalesce(trim(APPROVER_NAME), '')) <> '' THEN 'yes' ELSE 'no' END
FROM af WHERE LEGAL_ENTITY_KEY = '14782' AND trim(ACCOUNT_NUMBER) = '213130'
UNION ALL
SELECT 'A23', 'approved_date', max(trim(APPROVED_DATE))
FROM af WHERE LEGAL_ENTITY_KEY = '14782' AND trim(ACCOUNT_NUMBER) = '213130'

UNION ALL  -- A25 Northwind approved but not finalized
SELECT 'A25', 'approved_not_finalized',
       CAST(SUM(CASE WHEN lower(trim(ACCOUNT_STATUS)) = 'approved' AND lower(trim(IS_FINALIZED)) = 'false' THEN 1 ELSE 0 END) AS STRING)
FROM af WHERE LEGAL_ENTITY_KEY = '14781'

-- ===================== FYNAPSE =====================
UNION ALL  -- F01 lines and net by parent entity
SELECT 'F01', concat(PARENT_ENTITY, ' lines'), CAST(COUNT(*) AS STRING) FROM fy GROUP BY PARENT_ENTITY
UNION ALL
SELECT 'F01', concat(PARENT_ENTITY, ' net'), CAST(SUM(REPORTING_AMOUNT) AS STRING) FROM fy GROUP BY PARENT_ENTITY

UNION ALL  -- F02 lines and net by period (also used by F14)
SELECT 'F02', concat('FY', CAST(FISCAL_YEAR AS STRING), ' P', CAST(PERIOD AS STRING), ' lines (', CAST(min(CORE_DATE) AS STRING), '..', CAST(max(CORE_DATE) AS STRING), ')'),
       CAST(COUNT(*) AS STRING) FROM fy GROUP BY FISCAL_YEAR, PERIOD
UNION ALL
SELECT 'F02', concat('FY', CAST(FISCAL_YEAR AS STRING), ' P', CAST(PERIOD AS STRING), ' net'), CAST(SUM(REPORTING_AMOUNT) AS STRING)
FROM fy GROUP BY FISCAL_YEAR, PERIOD

UNION ALL  -- F03 journal types in Sep 2026 (period 9)
SELECT 'F03', coalesce(JOURNAL_TYPE, '(null)'), CAST(COUNT(*) AS STRING)
FROM fy WHERE FISCAL_YEAR = 2026 AND PERIOD = 9 GROUP BY JOURNAL_TYPE

UNION ALL  -- F04 UK03 top 5 accounts by gross amount
SELECT * FROM (
  SELECT 'F04', ACCOUNT, CAST(SUM(ABS(REPORTING_AMOUNT)) AS STRING)
  FROM fy WHERE PARENT_ENTITY = 'UK03'
  GROUP BY ACCOUNT ORDER BY SUM(ABS(REPORTING_AMOUNT)) DESC LIMIT 5
)

UNION ALL  -- F05 lines and transaction amount by transaction currency
SELECT 'F05', concat(coalesce(TRANSACTION_CURRENCY, '(null)'), ' lines'), CAST(COUNT(*) AS STRING)
FROM fy GROUP BY TRANSACTION_CURRENCY
UNION ALL
SELECT 'F05', concat(coalesce(TRANSACTION_CURRENCY, '(null)'), ' amount'), CAST(SUM(TRANSACTION_AMOUNT) AS STRING)
FROM fy GROUP BY TRANSACTION_CURRENCY

UNION ALL  -- F06 UK07 line count
SELECT 'F06', 'UK07 lines', CAST(COUNT(*) AS STRING) FROM fy WHERE PARENT_ENTITY = 'UK07'

UNION ALL  -- F07 UK17 net reporting amount, Aug 2026 (period 8)
SELECT 'F07', 'UK17 P8 net', CAST(SUM(REPORTING_AMOUNT) AS STRING)
FROM fy WHERE PARENT_ENTITY = 'UK17' AND FISCAL_YEAR = 2026 AND PERIOD = 8

UNION ALL  -- F08 distinct journals in Sep 2026
SELECT 'F08', 'distinct_journals_P9', CAST(COUNT(DISTINCT JOURNAL_ID) AS STRING)
FROM fy WHERE FISCAL_YEAR = 2026 AND PERIOD = 9

UNION ALL  -- F09 reversal lines (REVERSES populated)
SELECT 'F09', 'reversal_lines',
       CAST(SUM(CASE WHEN REVERSES IS NOT NULL AND trim(REVERSES) <> '' THEN 1 ELSE 0 END) AS STRING)
FROM fy

UNION ALL  -- F10 top 5 business events by line count
SELECT * FROM (
  SELECT 'F10', coalesce(BUSINESS_EVENT, '(null)'), CAST(COUNT(*) AS STRING)
  FROM fy GROUP BY BUSINESS_EVENT ORDER BY COUNT(*) DESC LIMIT 5
)

UNION ALL  -- F11 share of lines by parent entity
SELECT 'F11', PARENT_ENTITY,
       CAST(ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM fy), 1) AS STRING)
FROM fy GROUP BY PARENT_ENTITY

UNION ALL  -- F12 lines with no child entity
SELECT 'F12', 'no_child_entity',
       CAST(SUM(CASE WHEN CHILD_ENTITY IS NULL OR trim(CHILD_ENTITY) = '' THEN 1 ELSE 0 END) AS STRING)
FROM fy

UNION ALL  -- F13 top 5 lines of business by line count
SELECT * FROM (
  SELECT 'F13', coalesce(LOB, '(null)'), CAST(COUNT(*) AS STRING)
  FROM fy GROUP BY LOB ORDER BY COUNT(*) DESC LIMIT 5
)

UNION ALL  -- F16 functional amount by functional currency
SELECT 'F16', coalesce(FUNCTIONAL_CURRENCY, '(null)'), CAST(SUM(FUNCTIONAL_AMOUNT) AS STRING)
FROM fy GROUP BY FUNCTIONAL_CURRENCY
)
SELECT qid, k, v FROM answers ORDER BY qid, k;
