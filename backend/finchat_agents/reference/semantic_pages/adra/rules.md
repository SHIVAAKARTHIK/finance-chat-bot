# ADRA business definitions

These are the agreed definitions. When a question uses one of these terms, use exactly this definition.

## Reconciliation status vs finalized
- `ACCOUNT_STATUS` is the workflow step: Not prepared, Prepared, Approved, Approval not needed.
- `IS_FINALIZED` says whether the reconciliation is closed for the period. It is independent of the status:
  an account can be Approved and still not finalized.
- "Pending closure", "unfinished", "open" reconciliation = `IS_FINALIZED` is false.
- "Finalized", "closed", "completed" reconciliation = `IS_FINALIZED` is true.

## Balances
- `BALANCE` and `UNIDENTIFIED_BALANCE` are point-in-time values per period. Add them across accounts within one
  period only. Never add them across periods; for a trend, show one value per period.
- "Unreconciled difference" = `UNIDENTIFIED_BALANCE`. For "largest" or "total" use `UNIDENTIFIED_BALANCE_ABS`.

## People
- `PREPARER_NAME` / `APPROVER_NAME` are the assigned people. `PREPARED_BY_NAME` / `APPROVED_BY_NAME` are the people
  who actually did it. "Who approved" = `APPROVED_BY_NAME` with `APPROVED_DATE`; if `APPROVED_DATE` is NULL it is not
  approved yet.

## Transactions
- `TRANSACTION_TYPE` (Ledger / Subledger transaction) is not `TRANSACTION_STATUS` (Required adjustment / Not Set).
- "Oldest" item = MAX(`AGE_DAYS`).

## Open questions (do not guess; ask the user)
- "Pending with <person>": preparer, approver or assignee?
- "Unfinished tasks" and how close tasks link to a period (task tables are not modelled here).

# Query conventions (ADRA)

- All ADRA columns are stored as STRING. Cast numbers with TRY_CAST(x AS DECIMAL(38,2)) / INT, and compare text with
  trim() and lower(). `CURRENCY` and all *_KEY columns are identifiers, never numbers.
- Every query must filter to the user's authorized entities: (ENGAGEMENT_KEY, LEGAL_ENTITY_KEY) pairs.
- Join only through the relationships in relationships.yml, always with the FULL composite key.
- Period: join adra_period_dimensions and filter `PERIOD_NAME` ('Feb 25'). "Latest" = the period with the greatest
  `PERIOD_END` that has data for the entity. If the requested period has no rows, say so; do not fall back silently.
- Person columns (*_NAME of people) are PII: mask them for users without PII permission and never filter or group by them.
- One known data issue: a fact row with LEGAL_ENTITY_KEY 9819 has no matching legal entity; entity filters exclude it.
