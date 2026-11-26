---
name: adra_account_facts
schema: silver
layer: silver
domain: recon
type: fact
status: active
purpose: 'Account reconciliations: one row per account per legal entity per period, with workflow status, finalized flag,
  balances, unidentified (unreconciled) balances, documents and rejections.'
grain: one row per account reconciliation (ACCOUNT_KEY, ENGAGEMENT_KEY, LEGAL_ENTITY_KEY, PERIOD_KEY)
primary_key:
- ACCOUNT_KEY
- ENGAGEMENT_KEY
- LEGAL_ENTITY_KEY
- PERIOD_KEY
entity_column: LEGAL_ENTITY_KEY
period_columns:
- PERIOD_KEY
pii_columns:
- PREPARER_NAME
- APPROVER_NAME
- PREPARED_BY_NAME
- APPROVED_BY_NAME
- PREPARER_USERNAME
- APPROVER_USERNAME
- REVIEWER_USERNAME
- REVIEWER_NAME
- ASSIGNED_TO_USERNAME
- ASSIGNED_TO_NAME
- PREPARED_BY_USERNAME
- APPROVED_BY_USERNAME
- REVIEWED_BY_NAME
- REVIEWED_BY_USERNAME
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms:
- reconciliations
- account reconciliations
- account balances
- recon
- reconciliation status
- unreconciled
known_issues:
- code: all_string_columns
  note: Every column is stored as STRING. Cast numbers and dates; compare text with trim() and lower().
- code: orphans
  note: Rows with LEGAL_ENTITY_KEY 9819 have no matching legal entity dimension row; an inner join to adra_legal_entity_dimensions
    drops them.
reviewed: true
proposed_fields: []
---

# adra_account_facts

Account reconciliations: one row per account per legal entity per period, with workflow status, finalized flag,
balances, unidentified (unreconciled) balances, documents and rejections.

> All columns are stored as text (STRING). Cast numbers and dates as shown in *SQL expression*; compare text with `trim()` and `lower()`.
> The user names an entity by code or name (e.g. "100-Northwind") and a period by label (e.g. "Feb 25"): join
> `adra_legal_entity_dimensions` (ENTITY_CODE / ENTITY_NAME) and `adra_period_dimensions` (PERIOD_NAME) to filter.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ACCOUNT_KEY` | string | Account key (join to adra_account_dimensions with the full key). |  | `trim(ACCOUNT_KEY)` |
| `ENGAGEMENT_KEY` | string | Engagement key (part of every ADRA join key). |  | `trim(ENGAGEMENT_KEY)` |
| `LEGAL_ENTITY_KEY` | string | Legal entity key (join to adra_legal_entity_dimensions for code and name). |  | `trim(LEGAL_ENTITY_KEY)` |
| `PERIOD_KEY` | string | Period key (join to adra_period_dimensions for the period label). |  | `trim(PERIOD_KEY)` |
| `ACCOUNT_STATUS` | string | Reconciliation workflow status. Values may carry trailing spaces: compare with trim() and case-insensitively. | status, reconciliation status, account status, workflow status | `trim(ACCOUNT_STATUS)` |
| `IS_FINALIZED` | boolean | Reconciliation closed for the period. Independent of ACCOUNT_STATUS. | finalized, finalised, closed, completed, pending closure, unfinished | `lower(trim(IS_FINALIZED)) = 'true'` |
| `IS_CARRIED_FORWARD` | boolean | Carried forward from the previous period. | carried forward | `lower(trim(IS_CARRIED_FORWARD)) = 'true'` |
| `BALANCE` | decimal | GL balance in entity currency. Point-in-time per period: never sum across periods. | balance, account balance, gl balance | `TRY_CAST(BALANCE AS DECIMAL(38,2))` |
| `BALANCE_ABS` | decimal | Absolute GL balance (use for "largest balance"). | absolute balance, largest balance | `TRY_CAST(BALANCE_ABS AS DECIMAL(38,2))` |
| `UNIDENTIFIED_BALANCE` | decimal | Unidentified (unreconciled) difference: GL balance not supported by reconciling items. Point-in-time. | unidentified balance, unreconciled difference, unexplained difference | `TRY_CAST(UNIDENTIFIED_BALANCE AS DECIMAL(38,2))` |
| `UNIDENTIFIED_BALANCE_ABS` | decimal | Absolute unidentified balance; use for totals and "largest difference". | absolute unidentified balance, total unidentified | `TRY_CAST(UNIDENTIFIED_BALANCE_ABS AS DECIMAL(38,2))` |
| `NO_OF_DOCUMENTS` | integer | Number of supporting documents attached (NULL counts as 0). | documents, supporting documents, evidence | `TRY_CAST(NO_OF_DOCUMENTS AS INT)` |
| `NO_OF_REJECTS` | integer | Number of times the reconciliation was rejected (NULL counts as 0). | rejections, rejects, rejected | `TRY_CAST(NO_OF_REJECTS AS INT)` |
| `PREPARER_NAME` | string | Assigned preparer (person). PII: masked unless the role may see personal data; never filter or group by it. | preparer, assigned preparer | `trim(PREPARER_NAME)` |
| `APPROVER_NAME` | string | Assigned approver (person). PII. | approver, assigned approver, reviewer | `trim(APPROVER_NAME)` |
| `PREPARED_BY_NAME` | string | Person who actually prepared it. PII. | prepared by | `trim(PREPARED_BY_NAME)` |
| `APPROVED_BY_NAME` | string | Person who actually approved it. PII. | approved by | `trim(APPROVED_BY_NAME)` |
| `PREPARED_DATE` | timestamp | When it was prepared (NULL = not prepared). | prepared date, prepared on | `TRY_CAST(PREPARED_DATE AS TIMESTAMP)` |
| `APPROVED_DATE` | timestamp | When it was approved (NULL = not approved yet). | approved date, approved on | `TRY_CAST(APPROVED_DATE AS TIMESTAMP)` |
| `FISCAL_YEAR_PERIOD_KEY` | string |  |  | `FISCAL_YEAR_PERIOD_KEY` |
| `PREPARER_USERNAME` | string |  |  | `PREPARER_USERNAME` |
| `APPROVER_USERNAME` | string |  |  | `APPROVER_USERNAME` |
| `REVIEWER_USERNAME` | string |  |  | `REVIEWER_USERNAME` |
| `REVIEWER_NAME` | string |  |  | `REVIEWER_NAME` |
| `ASSIGNED_TO_USERNAME` | string |  |  | `ASSIGNED_TO_USERNAME` |
| `ASSIGNED_TO_NAME` | string |  |  | `ASSIGNED_TO_NAME` |
| `ACCOUNT_STATUS_REASON` | string |  |  | `ACCOUNT_STATUS_REASON` |
| `BALANCER_ACCOUNT_URL` | string |  |  | `BALANCER_ACCOUNT_URL` |
| `ACCOUNT_CREATED_IN_PERIOD` | string |  |  | `ACCOUNT_CREATED_IN_PERIOD` |
| `NO_OF_PREPARERS` | string |  |  | `NO_OF_PREPARERS` |
| `NO_OF_APPROVERS` | string |  |  | `NO_OF_APPROVERS` |
| `NO_OF_REVIEWERS` | string |  |  | `NO_OF_REVIEWERS` |
| `BALANCE_ENGAGEMENT` | string |  |  | `BALANCE_ENGAGEMENT` |
| `BALANCE_ENGAGEMENT_ABS` | string |  |  | `BALANCE_ENGAGEMENT_ABS` |
| `UNIDENTIFIED_BALANCE_ENGAGEMENT` | string |  |  | `UNIDENTIFIED_BALANCE_ENGAGEMENT` |
| `UNIDENTIFIED_BALANCE_ENGAGEMENT_ABS` | string |  |  | `UNIDENTIFIED_BALANCE_ENGAGEMENT_ABS` |
| `STATUS_COMMENT` | string |  |  | `STATUS_COMMENT` |
| `ACCOUNT_PURPOSE` | string |  |  | `ACCOUNT_PURPOSE` |
| `ACCOUNT_PROCEDURE` | string |  |  | `ACCOUNT_PROCEDURE` |
| `EXTRA_FIELD_01` | string |  |  | `EXTRA_FIELD_01` |
| `EXTRA_FIELD_02` | string |  |  | `EXTRA_FIELD_02` |
| `EXTRA_FIELD_03` | string |  |  | `EXTRA_FIELD_03` |
| `EXTRA_FIELD_04` | string |  |  | `EXTRA_FIELD_04` |
| `EXTRA_FIELD_05` | string |  |  | `EXTRA_FIELD_05` |
| `EXTRA_FIELD_06` | string |  |  | `EXTRA_FIELD_06` |
| `EXTRA_FIELD_07` | string |  |  | `EXTRA_FIELD_07` |
| `EXTRA_FIELD_08` | string |  |  | `EXTRA_FIELD_08` |
| `EXTRA_FIELD_09` | string |  |  | `EXTRA_FIELD_09` |
| `EXTRA_FIELD_10` | string |  |  | `EXTRA_FIELD_10` |
| `ACCOUNT_PERIOD_COMMENT_KEY` | string |  |  | `ACCOUNT_PERIOD_COMMENT_KEY` |
| `ACCOUNT_PERIOD_TRANSACTION_KEY` | string |  |  | `ACCOUNT_PERIOD_TRANSACTION_KEY` |
| `PREPARED_BY_USERNAME` | string |  |  | `PREPARED_BY_USERNAME` |
| `APPROVED_BY_USERNAME` | string |  |  | `APPROVED_BY_USERNAME` |
| `REVIEWED_BY_NAME` | string |  |  | `REVIEWED_BY_NAME` |
| `REVIEWED_BY_USERNAME` | string |  |  | `REVIEWED_BY_USERNAME` |
| `REVIEWED_DATE` | string |  |  | `REVIEWED_DATE` |
| `REJECTED_DATE` | string |  |  | `REJECTED_DATE` |
| `BALANCE_UPDATED_DATE` | string |  |  | `BALANCE_UPDATED_DATE` |
| `ACCOUNT_STATUS_COMMENTS` | string |  |  | `ACCOUNT_STATUS_COMMENTS` |
| `ACCOUNT_STATUS_REASON_TEXT` | string |  |  | `ACCOUNT_STATUS_REASON_TEXT` |
| `REVIEW_COMMENT` | string |  |  | `REVIEW_COMMENT` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**ACCOUNT_STATUS**
- `Not prepared`: preparer has not prepared it yet
- `Prepared`: prepared, awaiting approval
- `Approved`: approved by the approver
- `Approval not needed`: no approval step required

**IS_FINALIZED**
- `True`: finalized (closed for the period)
- `False`: not finalized (pending closure, unfinished, open)

**IS_CARRIED_FORWARD**
- `True`: carried forward
- `False`: not carried forward
- `None`

**ACCOUNT_STATUS_REASON**
- `None`

**ACCOUNT_CREATED_IN_PERIOD**
- `2026-10-23 10:47:07.0000000 +00:00`
- `None`
- `2026-10-29 05:52:10.0000000 +00:00`
- `2026-10-18 09:40:39.0000000 +00:00`

**NO_OF_DOCUMENTS**
- `0`

**NO_OF_PREPARERS**
- `1`
- `2`

**NO_OF_APPROVERS**
- `1`
- `2`

**NO_OF_REVIEWERS**
- `0`
- `1`

**STATUS_COMMENT**
- `Account Period Created`
- `None`
- `Set to not preapred due to update in balance as a result of import`

**ACCOUNT_PURPOSE**
- `None`

**ACCOUNT_PROCEDURE**
- `None`

**EXTRA_FIELD_01**
- `None`

**EXTRA_FIELD_02**
- `None`

**EXTRA_FIELD_03**
- `None`

**EXTRA_FIELD_04**
- `None`

**EXTRA_FIELD_05**
- `None`

**EXTRA_FIELD_06**
- `None`

**EXTRA_FIELD_07**
- `None`

**EXTRA_FIELD_08**
- `None`

**EXTRA_FIELD_09**
- `None`

**EXTRA_FIELD_10**
- `None`

**NO_OF_REJECTS**
- `0`
- `None`

**PREPARED_DATE**
- `None`
- `2026-10-25 07:34:30.0000000 +00:00`
- `46342.42591`
- `46342.4274`
- `2026-10-29 10:11:12.0000000 +00:00`
- `2026-10-25 04:59:43.0000000 +00:00`
- `2026-10-29 10:10:55.0000000 +00:00`
- `2026-10-25 07:40:02.0000000 +00:00`
- `2026-10-25 05:00:17.0000000 +00:00`
- `46342.42655`
- `2026-10-25 04:58:30.0000000 +00:00`
- `2026-10-25 04:59:14.0000000 +00:00`
- `2026-10-25 04:54:22.0000000 +00:00`
- `2026-10-29 10:08:33.0000000 +00:00`
- `2026-10-25 07:38:05.0000000 +00:00`
- `2026-10-25 05:01:07.0000000 +00:00`
- `2026-10-24 15:56:32.0000000 +00:00`
- `2026-10-29 10:12:29.0000000 +00:00`
- `46342.42753`
- `2026-10-29 10:12:04.0000000 +00:00`
- `46342.42613`
- `2026-10-29 10:07:51.0000000 +00:00`
- `2026-10-24 16:07:17.0000000 +00:00`
- `2026-10-29 10:10:29.0000000 +00:00`
- `2026-10-25 07:31:13.0000000 +00:00`
- `2026-10-25 07:27:36.0000000 +00:00`
- `2026-10-29 10:08:58.0000000 +00:00`
- `2026-10-29 10:11:29.0000000 +00:00`
- `2026-10-24 16:06:16.0000000 +00:00`
- `2026-10-24 16:02:15.0000000 +00:00`
- `2026-10-29 10:11:10.0000000 +00:00`
- `2026-10-29 10:12:40.0000000 +00:00`
- `46342.42553`
- `2026-10-29 10:10:20.0000000 +00:00`
- `46342.42602`
- `46342.42714`
- `46342.42704`
- `2026-10-25 07:33:14.0000000 +00:00`
- `2026-10-29 10:13:17.0000000 +00:00`
- `46342.42726`

**APPROVED_DATE**
- `None`
- `46342.43833`
- `46342.44012`
- `2026-10-25 04:56:41.0000000 +00:00`
- `2026-10-25 07:24:26.0000000 +00:00`
- `2026-10-25 04:57:35.0000000 +00:00`
- `2026-10-25 05:02:34.0000000 +00:00`
- `2026-10-25 07:24:52.0000000 +00:00`
- `2026-10-25 07:24:40.0000000 +00:00`
- `2026-10-25 07:25:02.0000000 +00:00`
- `2026-10-29 10:16:42.0000000 +00:00`
- `2026-10-29 12:33:16.0000000 +00:00`
- `2026-10-29 10:16:31.0000000 +00:00`
- `2026-10-29 12:33:06.0000000 +00:00`
- `2026-10-29 10:10:50.0000000 +00:00`
- `2026-10-29 10:13:32.0000000 +00:00`

**REVIEWED_DATE**
- `None`

**REJECTED_DATE**
- `None`

**BALANCE_UPDATED_DATE**
- `2026-10-23 10:47:28.0000000 +00:00`
- `2026-10-29 05:52:29.0000000 +00:00`
- `46342.41964`
- `46342.40172`
- `46342.41965`
- `46342.4017`
- `2026-10-18 09:40:48.0000000 +00:00`

**ACCOUNT_STATUS_COMMENTS**
- `None`

**ACCOUNT_STATUS_REASON_TEXT**
- `None`

**REVIEW_COMMENT**
- `None`

**SOURCE_FILE_NAME**
- `accountfacts__20261116_094201.csv`
- `adra_account_facts.csv`

**MDP_CREATED_DATE**
- `2026-11-16 09:54:35.180338+00:00`
- `2026-11-16 18:53:24.519208+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 09:54:35.180338+00:00`
- `2026-11-16 18:53:24.519208+00:00`

## Empty columns

Empty in every row: `ACCOUNT_PURPOSE`, `ACCOUNT_PROCEDURE`, `EXTRA_FIELD_01`, `EXTRA_FIELD_02`, `EXTRA_FIELD_03`, `EXTRA_FIELD_04`, `EXTRA_FIELD_05`, `EXTRA_FIELD_06`, `EXTRA_FIELD_07`, `EXTRA_FIELD_08`, `EXTRA_FIELD_09`, `EXTRA_FIELD_10`, `REVIEWED_BY_NAME`, `REVIEWED_BY_USERNAME`, `REVIEWED_DATE`, `REJECTED_DATE`, `ACCOUNT_STATUS_COMMENTS`, `ACCOUNT_STATUS_REASON_TEXT`, `REVIEW_COMMENT`. Do not filter or group on them.

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `account_fact_to_account` | `adra_account_dimensions` | many-to-one |
| `account_fact_to_period` | `adra_period_dimensions` | many-to-one |
| `account_fact_to_legal_entity` | `adra_legal_entity_dimensions` | many-to-one |

Join conditions are in `joins.yaml`.

## Named metrics

| Metric | Meaning | SQL | Additivity |
|---|---|---|---|
| `account_count` | Number of account reconciliations. | `COUNT(*)` | additive |
| `finalized_count` | Reconciliations finalized. | `SUM(CASE WHEN lower(trim(IS_FINALIZED)) = 'true' THEN 1 ELSE 0 END)` | additive |
| `not_finalized_count` | Reconciliations pending closure. | `SUM(CASE WHEN lower(trim(IS_FINALIZED)) = 'false' THEN 1 ELSE 0 END)` | additive |
| `pct_finalized` | Share finalized, in percent. | `100.0 * SUM(CASE WHEN lower(trim(IS_FINALIZED)) = 'true' THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0)` | non additive |
| `total_balance` | Total GL balance. Add across accounts within ONE period, never across periods. | `SUM(TRY_CAST(BALANCE AS DECIMAL(38,2)))` | semi additive (period) |
| `total_unidentified_balance_abs` | Total absolute unidentified balance. | `SUM(TRY_CAST(UNIDENTIFIED_BALANCE_ABS AS DECIMAL(38,2)))` | semi additive (period) |
| `accounts_without_documents` | Reconciliations with no supporting documents. | `SUM(CASE WHEN coalesce(TRY_CAST(NO_OF_DOCUMENTS AS INT), 0) = 0 THEN 1 ELSE 0 END)` | additive |

## Notes

- Status and finalized are different questions: an account can be Approved and still not finalized.
- "Who approved" = APPROVED_BY_NAME with APPROVED_DATE; if APPROVED_DATE is NULL nobody has approved it yet
  (APPROVER_NAME is only the assigned approver).
- Verified examples for this table are in `examples.yaml`.
