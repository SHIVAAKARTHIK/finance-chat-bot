# Glossary

Business terms users type, and what they mean in the data. One `##` entry per term; `Aliases:` lists other words
for the same thing. `Status: draft` entries are working definitions not yet confirmed by Finance: use them, and say
in the answer which definition was used.

## reconciliation status
Aliases: status, workflow status, account status, recon status
Tables: silver.adra_account_facts
The workflow step of an account reconciliation: column ACCOUNT_STATUS (Not prepared, Prepared, Approved,
Approval not needed). Compare with trim() and lower(). It is not the same as finalized.

## finalized
Aliases: finalised, closed, completed, closed reconciliation
Tables: silver.adra_account_facts
Reconciliation closed for the period: IS_FINALIZED is true (`lower(trim(IS_FINALIZED)) = 'true'`).
Independent of ACCOUNT_STATUS: an account can be Approved and still not finalized.

## pending closure
Aliases: unfinished, open reconciliation, not finalized, not closed, remaining
Tables: silver.adra_account_facts
Reconciliations not yet finalized: `lower(trim(IS_FINALIZED)) = 'false'`.

## unreconciled difference
Aliases: unidentified balance, unexplained difference, unidentified difference, unreconciled balance
Tables: silver.adra_account_facts
UNIDENTIFIED_BALANCE (signed). For "total" or "largest" use UNIDENTIFIED_BALANCE_ABS, even when the user only says
"total". Point-in-time per period: add across accounts within one period only.

## balance
Aliases: account balance, gl balance
Tables: silver.adra_account_facts
BALANCE in entity currency, point-in-time per period. Never add balances across periods; for a trend show one value
per period. "Largest balance" = BALANCE_ABS.

## who approved
Aliases: approved by, approver
Tables: silver.adra_account_facts
The person who actually approved = APPROVED_BY_NAME with APPROVED_DATE. If APPROVED_DATE is NULL it has not been
approved yet; APPROVER_NAME is only the assigned approver. Person names are PII (masked unless the role allows).

## who prepared
Aliases: prepared by, preparer
Tables: silver.adra_account_facts
PREPARED_BY_NAME with PREPARED_DATE is who actually prepared it; PREPARER_NAME is the assigned preparer. PII.

## pending with a person
Aliases: pending with, assigned to, waiting on
Status: draft
Ambiguous: preparer, approver or assignee? Answer with the most likely reading (assigned preparer for not-prepared
items, assigned approver for prepared items), say which, and offer the other. Person filters need PII permission.

## reconciling items
Aliases: transactions, open items, items
Tables: silver.adra_transaction_facts
Rows of adra_transaction_facts. TRANSACTION_TYPE (Ledger / Subledger transaction) is not TRANSACTION_STATUS
(Required adjustment / Not Set). "Oldest" item = MAX(AGE_DAYS). Ageing buckets = AGE_GROUP.

## supporting documents
Aliases: documents, evidence, attachments
Tables: silver.adra_account_facts
NO_OF_DOCUMENTS; NULL counts as zero (`coalesce(TRY_CAST(NO_OF_DOCUMENTS AS INT), 0)`).

## rejections
Aliases: rejects, rejected
Tables: silver.adra_account_facts
NO_OF_REJECTS; NULL counts as zero.

## latest period
Aliases: latest, current period, most recent period
The period with the greatest end date that has data for the entity (ADRA: PERIOD_END in adra_period_dimensions;
Fynapse: max CORE_DATE). Say which period was used.

## journal lines
Aliases: lines, subledger lines, fynapse lines
Tables: silver.fact_fynapse_slr_journals
"How many lines" = COUNT(*). "How many journals" = COUNT(DISTINCT JOURNAL_ID).

## net amount
Aliases: net, net reporting amount, balanced
Tables: silver.fact_fynapse_slr_journals
SUM(REPORTING_AMOUNT). A balanced subledger nets to (almost) zero.

## gross amount
Aliases: gross, gross reporting amount, absolute amount
Tables: silver.fact_fynapse_slr_journals
SUM(ABS(REPORTING_AMOUNT)).

## fynapse entity
Aliases: parent entity, subledger entity
Tables: silver.fact_fynapse_slr_journals
PARENT_ENTITY. CHILD_ENTITY is a sub-unit, often empty. Entity values changed recently: check current values with
get_column_values before filtering.

## reversal
Aliases: reversals, reversed lines
Status: draft
Tables: silver.fact_fynapse_slr_journals
Working definition: a line whose REVERSES column is populated. Not confirmed by Finance; say so.

## line of business
Aliases: lob
Tables: silver.fact_fynapse_slr_journals
Column LOB. It is currently empty on all lines: say it is not populated instead of inventing categories.

## revenue
Aliases: p&l, profit and loss, trial balance, income
Fynapse journal amounts are not revenue, P&L or a trial balance; do not substitute them. Look for a general ledger
or gold table instead, or say the data is not available.

## invested capital
Aliases: acquisition price, acquisition value, cost of assets
Tables: silver.dim_fixed_asset_books
SUM(ACQUISITION_PRICE) from dim_fixed_asset_books, after checking duplicate loads.

## capitalized
Aliases: capitalised
Status: draft
Tables: silver.dim_fixed_asset_books
Fixed assets whose asset book STATUS is Open.

## in service
Status: draft
Tables: silver.fact_asset_master_transactions
Fixed asset transactions with status Open that count as actively in service (column to be confirmed).

## inactive assets
Aliases: retired assets, disposed assets
Tables: silver.dim_fixed_asset_books
STATUS Sold, Scrapped or Closed.

## not financially activated
Aliases: not activated, no acquisition
Tables: silver.dim_fixed_asset_books
STATUS NoAcquisition (acquisition price 0).

## asset category
Aliases: asset group, category
Tables: silver.dim_fixed_asset_books, silver.dim_fixed_assets
FIXED_ASSET_GROUP_ID.

## NBV
Aliases: net book value
Abbreviation: net book value (acquisition cost less accumulated depreciation).

## WIP
Aliases: work in progress
Abbreviation: work in progress.

## performance
Ambiguous. Ask, or answer the most likely reading and offer the others: revenue, profit margin, or depreciation?
