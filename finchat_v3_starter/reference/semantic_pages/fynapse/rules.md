# Fynapse rules

## Writing queries
Entity = PARENT_ENTITY, filtered to the user's authorized entities. Period = FISCAL_YEAR + PERIOD; map a month mention via CORE_DATE. 'How many lines' = COUNT(*); 'how many journals' = COUNT(DISTINCT JOURNAL_ID). 'Net' = SUM(REPORTING_AMOUNT); 'gross' = SUM(ABS(REPORTING_AMOUNT)). Share of total only for counts or non-negative amounts.

## Questions to refuse
Revenue, P&L and trial-balance questions are not answerable from this subledger; say so instead of substituting journal amounts.
