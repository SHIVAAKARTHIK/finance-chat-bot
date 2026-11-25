# Query rules

These rules apply to every query. Table pages add table-specific notes.

## Writing SQL
- One read-only statement: a single SELECT or WITH ... SELECT. Databricks SQL dialect.
- Always use fully qualified names: `lakehouse_mvpai.<schema>.<table>`. Only tables from the catalog.
- Prefer gold tables over silver when both hold the answer; use silver when gold does not have it.
- Join only through approved joins (`get_join_path`), always with the FULL composite key. A partial key multiplies rows.
- Select only the columns you need. Add ORDER BY for "top", "largest", "oldest"; LIMIT for top-N.
- Some tables store every column as STRING (see the page): cast numbers with `TRY_CAST(x AS DECIMAL(38,2))` or
  `TRY_CAST(x AS INT)`, dates with `TRY_CAST(x AS DATE)`, and compare text with `trim()` and `lower()`.
  Codes and keys (currency, *_KEY, account numbers) are identifiers, never numbers.
- Never filter on a value you have not seen. Check values with `get_column_values` (status words, entity codes,
  period labels) and use the stored spelling.

## Entities and periods
- There are no row-level entity restrictions: do not add entity filters the question does not ask for.
- When the question names an entity, find its stored code or name first (`resolve_entity` / `get_column_values`)
  and filter on that. Entity values can change; never rely on remembered values.
- When the question names a period, resolve it to the table's period values (`resolve_period`).
- If no period is given: balances (point-in-time) use the latest period with data and say "as of <period>";
  activity (counts, amounts of transactions) covers all available data and says so.
- If the requested period or entity has no rows, say so and list what does exist. Never fall back silently.
- Comparing periods needs data for both. If one is missing, say the comparison cannot be made.

## Measures
- Balances are point-in-time: add across accounts within ONE period; never across periods.
- "How many X" counts rows at the table's grain unless the question says distinct something.
- Percentages: compute in SQL with `100.0 * part / NULLIF(total, 0)` and round to one decimal in the answer.
- Use the named metrics on the table pages instead of improvising definitions.

## Data quality
- Tables with a `duplicates` known issue: check duplicates at the grain first. If they exist, warn the user; remove
  them only if the answer says it did and how.
- Tables with an `orphans` known issue: inner joins drop orphan rows; mention it if it changes the answer.
- Empty columns: say the column is not populated; never invent categories.

## People and personal data
- Person-name columns are PII. They are masked unless the user's role allows personal data.
- Never filter, group or sort by a person-name column unless the role allows PII.

## Answers
- Every number in an answer comes from a query result. Never estimate or invent numbers.
- Ambiguous question: answer the most likely reading first, then offer the alternative.
- Never show SQL to the user; explain the calculation in business words (filters, grouping, period).

## Domain notes
### ADRA (recon)
- Status (ACCOUNT_STATUS) and finalized (IS_FINALIZED) are independent.
- Entity filter: join adra_legal_entity_dimensions (ENTITY_CODE / ENTITY_NAME). Period filter: join
  adra_period_dimensions (PERIOD_NAME, labels like 'Feb 25').
- Open question for the user, do not guess: "pending with <person>" (preparer, approver or assignee?).
- Close-task questions (task lists, due dates) need the ADRA task tables, which are not modelled yet.

### Fynapse (subledger)
- Entity = PARENT_ENTITY (values recently changed; check them). Period = FISCAL_YEAR + PERIOD, mapped from CORE_DATE.
- Lines = COUNT(*); journals = COUNT(DISTINCT JOURNAL_ID); net = SUM(REPORTING_AMOUNT); gross = SUM(ABS(REPORTING_AMOUNT)).
- Revenue, P&L and trial-balance questions are not answerable from this subledger.

### Source of truth
- ADRA reconciliations and close tasks: use the `adra_*` tables. The `manage_close_*` tables that copy ADRA data are
  marked superseded on their pages; they are not searchable and queries against them are refused.

### Fixed assets (fa)
- Sources are loaded twice: always run the duplicate check first and state what you did.
- Asset counts and invested capital come from dim_fixed_asset_books; workload by type from fact_asset_master_transactions.
