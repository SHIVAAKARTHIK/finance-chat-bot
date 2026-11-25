# Fynapse verified queries

Verified question → SQL pairs (DEV business ground truth only; never add hold-out questions).

## How concentrated is the journal integration workload across source systems, and does the subledger remain balanced?

**Expected answer:** 817 lines: NOVIDEA 433 (53.0%), ACCRUAL 214 (26.2%), Concur 170 (20.8%); net -0.08

```sql
SELECT SOURCE_SYSTEM, COUNT(*) AS journal_lines,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS share_pct,
       SUM(REPORTING_AMOUNT) AS net_reporting_amount
FROM lakehouse_mvpai.silver.fact_fynapse_slr_journals
GROUP BY SOURCE_SYSTEM
ORDER BY journal_lines DESC
```
