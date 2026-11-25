# ADRA named metrics

Use these definitions instead of improvising. Semi-additive metrics may be added across accounts within one period, never across periods.

## adra_account_facts

| Metric | Meaning | SQL | Additivity |
|---|---|---|---|
| `account_count` | Number of account reconciliations. | `COUNT(*)` | additive |
| `finalized_count` | Reconciliations finalized. | `SUM(CASE WHEN lower(trim(IS_FINALIZED)) = 'true' THEN 1 ELSE 0 END)` | additive |
| `not_finalized_count` | Reconciliations pending closure (not finalized). | `SUM(CASE WHEN lower(trim(IS_FINALIZED)) = 'false' THEN 1 ELSE 0 END)` | additive |
| `pct_finalized` | Share of reconciliations finalized, in percent. | `100.0 * SUM(CASE WHEN lower(trim(IS_FINALIZED)) = 'true' THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0)` | non additive |
| `total_balance` | Total GL balance. Semi-additive: add across accounts within ONE period, never across periods. | `SUM(TRY_CAST(BALANCE AS DECIMAL(38,2)))` | semi additive period |
| `total_unidentified_balance_abs` | Total absolute unidentified balance. Semi-additive over periods. | `SUM(TRY_CAST(UNIDENTIFIED_BALANCE_ABS AS DECIMAL(38,2)))` | semi additive period |
| `accounts_without_documents` | Reconciliations with no supporting documents. | `SUM(CASE WHEN coalesce(TRY_CAST(NO_OF_DOCUMENTS AS INT), 0) = 0 THEN 1 ELSE 0 END)` | additive |

## adra_transaction_facts

| Metric | Meaning | SQL | Additivity |
|---|---|---|---|
| `transaction_count` | Number of reconciling items. | `COUNT(*)` | additive |
| `total_amount_abs` | Gross amount of items. | `SUM(TRY_CAST(AMOUNT_ABS AS DECIMAL(38,2)))` | additive |
| `oldest_item_age_days` | Age in days of the oldest item. | `MAX(TRY_CAST(AGE_DAYS AS INT))` | non additive |
