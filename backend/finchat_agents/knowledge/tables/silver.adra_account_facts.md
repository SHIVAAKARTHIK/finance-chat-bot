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
row_count: 97
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
- `None`: 33 rows

**ACCOUNT_STATUS_REASON**
- `None`: 64 rows

**ACCOUNT_CREATED_IN_PERIOD**
- `2026-10-23 10:47:07.0000000 +00:00`: 40 rows
- `None`: 33 rows
- `2026-10-29 05:52:10.0000000 +00:00`: 23 rows
- `2026-10-18 09:40:39.0000000 +00:00`: 1 rows

**NO_OF_DOCUMENTS**
- `0`: 97 rows

**NO_OF_PREPARERS**
- `1`: 63 rows
- `2`: 34 rows

**NO_OF_APPROVERS**
- `1`: 59 rows
- `2`: 38 rows

**NO_OF_REVIEWERS**
- `0`: 96 rows
- `1`: 1 rows

**STATUS_COMMENT**
- `Account Period Created`: 42 rows
- `None`: 39 rows
- `Set to not preapred due to update in balance as a result of import`: 16 rows

**ACCOUNT_PURPOSE**
- `None`: 97 rows

**ACCOUNT_PROCEDURE**
- `None`: 97 rows

**EXTRA_FIELD_01**
- `None`: 97 rows

**EXTRA_FIELD_02**
- `None`: 97 rows

**EXTRA_FIELD_03**
- `None`: 97 rows

**EXTRA_FIELD_04**
- `None`: 97 rows

**EXTRA_FIELD_05**
- `None`: 97 rows

**EXTRA_FIELD_06**
- `None`: 97 rows

**EXTRA_FIELD_07**
- `None`: 97 rows

**EXTRA_FIELD_08**
- `None`: 97 rows

**EXTRA_FIELD_09**
- `None`: 97 rows

**EXTRA_FIELD_10**
- `None`: 97 rows

**NO_OF_REJECTS**
- `0`: 64 rows
- `None`: 33 rows

**PREPARED_DATE**
- `None`: 58 rows
- `2026-10-25 07:34:30.0000000 +00:00`: 1 rows
- `46342.42591`: 1 rows
- `46342.4274`: 1 rows
- `2026-10-29 10:11:12.0000000 +00:00`: 1 rows
- `2026-10-25 04:59:43.0000000 +00:00`: 1 rows
- `2026-10-29 10:10:55.0000000 +00:00`: 1 rows
- `2026-10-25 07:40:02.0000000 +00:00`: 1 rows
- `2026-10-25 05:00:17.0000000 +00:00`: 1 rows
- `46342.42655`: 1 rows
- `2026-10-25 04:58:30.0000000 +00:00`: 1 rows
- `2026-10-25 04:59:14.0000000 +00:00`: 1 rows
- `2026-10-25 04:54:22.0000000 +00:00`: 1 rows
- `2026-10-29 10:08:33.0000000 +00:00`: 1 rows
- `2026-10-25 07:38:05.0000000 +00:00`: 1 rows
- `2026-10-25 05:01:07.0000000 +00:00`: 1 rows
- `2026-10-24 15:56:32.0000000 +00:00`: 1 rows
- `2026-10-29 10:12:29.0000000 +00:00`: 1 rows
- `46342.42753`: 1 rows
- `2026-10-29 10:12:04.0000000 +00:00`: 1 rows
- `46342.42613`: 1 rows
- `2026-10-29 10:07:51.0000000 +00:00`: 1 rows
- `2026-10-24 16:07:17.0000000 +00:00`: 1 rows
- `2026-10-29 10:10:29.0000000 +00:00`: 1 rows
- `2026-10-25 07:31:13.0000000 +00:00`: 1 rows
- `2026-10-25 07:27:36.0000000 +00:00`: 1 rows
- `2026-10-29 10:08:58.0000000 +00:00`: 1 rows
- `2026-10-29 10:11:29.0000000 +00:00`: 1 rows
- `2026-10-24 16:06:16.0000000 +00:00`: 1 rows
- `2026-10-24 16:02:15.0000000 +00:00`: 1 rows
- `2026-10-29 10:11:10.0000000 +00:00`: 1 rows
- `2026-10-29 10:12:40.0000000 +00:00`: 1 rows
- `46342.42553`: 1 rows
- `2026-10-29 10:10:20.0000000 +00:00`: 1 rows
- `46342.42602`: 1 rows
- `46342.42714`: 1 rows
- `46342.42704`: 1 rows
- `2026-10-25 07:33:14.0000000 +00:00`: 1 rows
- `2026-10-29 10:13:17.0000000 +00:00`: 1 rows
- `46342.42726`: 1 rows

**APPROVED_DATE**
- `None`: 74 rows
- `46342.43833`: 6 rows
- `46342.44012`: 4 rows
- `2026-10-25 04:56:41.0000000 +00:00`: 1 rows
- `2026-10-25 07:24:26.0000000 +00:00`: 1 rows
- `2026-10-25 04:57:35.0000000 +00:00`: 1 rows
- `2026-10-25 05:02:34.0000000 +00:00`: 1 rows
- `2026-10-25 07:24:52.0000000 +00:00`: 1 rows
- `2026-10-25 07:24:40.0000000 +00:00`: 1 rows
- `2026-10-25 07:25:02.0000000 +00:00`: 1 rows
- `2026-10-29 10:16:42.0000000 +00:00`: 1 rows
- `2026-10-29 12:33:16.0000000 +00:00`: 1 rows
- `2026-10-29 10:16:31.0000000 +00:00`: 1 rows
- `2026-10-29 12:33:06.0000000 +00:00`: 1 rows
- `2026-10-29 10:10:50.0000000 +00:00`: 1 rows
- `2026-10-29 10:13:32.0000000 +00:00`: 1 rows

**REVIEWED_DATE**
- `None`: 97 rows

**REJECTED_DATE**
- `None`: 97 rows

**BALANCE_UPDATED_DATE**
- `2026-10-23 10:47:28.0000000 +00:00`: 40 rows
- `2026-10-29 05:52:29.0000000 +00:00`: 23 rows
- `46342.41964`: 12 rows
- `46342.40172`: 10 rows
- `46342.41965`: 9 rows
- `46342.4017`: 2 rows
- `2026-10-18 09:40:48.0000000 +00:00`: 1 rows

**ACCOUNT_STATUS_COMMENTS**
- `None`: 97 rows

**ACCOUNT_STATUS_REASON_TEXT**
- `None`: 97 rows

**REVIEW_COMMENT**
- `None`: 97 rows

**SOURCE_FILE_NAME**
- `accountfacts__20261116_094201.csv`: 64 rows
- `adra_account_facts.csv`: 33 rows

**MDP_CREATED_DATE**
- `2026-11-16 09:54:35.180338+00:00`: 64 rows
- `2026-11-16 18:53:24.519208+00:00`: 33 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 09:54:35.180338+00:00`: 64 rows
- `2026-11-16 18:53:24.519208+00:00`: 33 rows

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

## Profile

Rows in the latest export: 97.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ACCOUNT_KEY` | STRING | 93 | 0 |  |  |
| `ENGAGEMENT_KEY` | STRING | 1 | 0 |  |  |
| `LEGAL_ENTITY_KEY` | STRING | 9 | 0 |  |  |
| `PERIOD_KEY` | STRING | 9 | 0 |  |  |
| `FISCAL_YEAR_PERIOD_KEY` | STRING | 3 | 0 |  |  |
| `PREPARER_USERNAME` | STRING | 4 | 0 |  |  |
| `PREPARER_NAME` | STRING | 4 | 0 |  |  |
| `APPROVER_USERNAME` | STRING | 4 | 0 |  |  |
| `APPROVER_NAME` | STRING | 4 | 0 |  |  |
| `REVIEWER_USERNAME` | STRING | 1 | 96 |  |  |
| `REVIEWER_NAME` | STRING | 1 | 96 |  |  |
| `ASSIGNED_TO_USERNAME` | STRING | 5 | 8 |  |  |
| `ASSIGNED_TO_NAME` | STRING | 5 | 8 |  |  |
| `ACCOUNT_STATUS` | STRING | 3 | 0 | Approved | Prepared |
| `ACCOUNT_STATUS_REASON` | STRING | 1 | 33 | None | None |
| `IS_FINALIZED` | STRING | 2 | 0 | False | True |
| `IS_CARRIED_FORWARD` | STRING | 1 | 33 | False | False |
| `BALANCER_ACCOUNT_URL` | STRING | 99 | 0 | https://balancer.adra.com/engagements... | https://balancer.adra.com/engagements... |
| `ACCOUNT_CREATED_IN_PERIOD` | STRING | 3 | 33 | 2026-10-18 09:40:39.0000000 +00:00 | 2026-10-29 05:52:10.0000000 +00:00 |
| `NO_OF_DOCUMENTS` | STRING | 1 | 0 | 0 | 0 |
| `NO_OF_PREPARERS` | STRING | 2 | 0 | 1 | 2 |
| `NO_OF_APPROVERS` | STRING | 2 | 0 | 1 | 2 |
| `NO_OF_REVIEWERS` | STRING | 2 | 0 | 0 | 1 |
| `BALANCE` | STRING | 95 | 0 | -1122 | 98583.59 |
| `BALANCE_ABS` | STRING | 99 | 0 | 0 | 98583.59 |
| `UNIDENTIFIED_BALANCE` | STRING | 58 | 0 | -110908 | 992715 |
| `UNIDENTIFIED_BALANCE_ABS` | STRING | 58 | 0 | 0 | 992715 |
| `BALANCE_ENGAGEMENT` | STRING | 93 | 0 | -10381.98 | 98583.59 |
| `BALANCE_ENGAGEMENT_ABS` | STRING | 95 | 0 | 0 | 98583.59 |
| `UNIDENTIFIED_BALANCE_ENGAGEMENT` | STRING | 57 | 0 | -10381.98 | 992715 |
| `UNIDENTIFIED_BALANCE_ENGAGEMENT_ABS` | STRING | 59 | 0 | 0 | 992715 |
| `STATUS_COMMENT` | STRING | 2 | 39 | Account Period Created | Set to not preapred due to update in ... |
| `ACCOUNT_PURPOSE` | STRING | 0 | 97 |  |  |
| `ACCOUNT_PROCEDURE` | STRING | 0 | 97 |  |  |
| `EXTRA_FIELD_01` | STRING | 0 | 97 |  |  |
| `EXTRA_FIELD_02` | STRING | 0 | 97 |  |  |
| `EXTRA_FIELD_03` | STRING | 0 | 97 |  |  |
| `EXTRA_FIELD_04` | STRING | 0 | 97 |  |  |
| `EXTRA_FIELD_05` | STRING | 0 | 97 |  |  |
| `EXTRA_FIELD_06` | STRING | 0 | 97 |  |  |
| `EXTRA_FIELD_07` | STRING | 0 | 97 |  |  |
| `EXTRA_FIELD_08` | STRING | 0 | 97 |  |  |
| `EXTRA_FIELD_09` | STRING | 0 | 97 |  |  |
| `EXTRA_FIELD_10` | STRING | 0 | 97 |  |  |
| `NO_OF_REJECTS` | STRING | 1 | 33 | 0 | 0 |
| `ACCOUNT_PERIOD_COMMENT_KEY` | STRING | 63 | 33 |  |  |
| `ACCOUNT_PERIOD_TRANSACTION_KEY` | STRING | 63 | 33 |  |  |
| `PREPARED_BY_NAME` | STRING | 3 | 58 |  |  |
| `PREPARED_BY_USERNAME` | STRING | 3 | 58 |  |  |
| `APPROVED_BY_NAME` | STRING | 3 | 74 |  |  |
| `APPROVED_BY_USERNAME` | STRING | 3 | 74 |  |  |
| `REVIEWED_BY_NAME` | STRING | 0 | 97 |  |  |
| `REVIEWED_BY_USERNAME` | STRING | 0 | 97 |  |  |
| `PREPARED_DATE` | STRING | 39 | 58 | 2026-10-24 15:56:32.0000000 +00:00 | 46342.42753 |
| `APPROVED_DATE` | STRING | 14 | 74 | 2026-10-25 04:56:41.0000000 +00:00 | 46342.44012 |
| `REVIEWED_DATE` | STRING | 0 | 97 |  |  |
| `REJECTED_DATE` | STRING | 0 | 97 |  |  |
| `BALANCE_UPDATED_DATE` | STRING | 7 | 0 | 2026-10-18 09:40:48.0000000 +00:00 | 46342.41965 |
| `ACCOUNT_STATUS_COMMENTS` | STRING | 0 | 97 |  |  |
| `ACCOUNT_STATUS_REASON_TEXT` | STRING | 0 | 97 |  |  |
| `REVIEW_COMMENT` | STRING | 0 | 97 |  |  |
| `SOURCE_FILE_NAME` | STRING | 2 | 0 | accountfacts__20261116_094201.csv | adra_account_facts.csv |
| `HASH_KEY` | STRING | 97 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 2 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 2 | 0 | 2026-11-16 09:54:35.180000 | 2026-11-16 18:53:24.519000 |
| `MDP_MODIFIED_BY` | STRING | 2 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 2 | 0 | 2026-11-16 09:54:35.180000 | 2026-11-16 18:53:24.519000 |

## Sample rows

| PREPARER_USERNAME | PREPARER_NAME | APPROVER_USERNAME | APPROVER_NAME | REVIEWER_USERNAME | REVIEWER_NAME | ASSIGNED_TO_USERNAME | ASSIGNED_TO_NAME | ACCOUNT_STATUS | ACCOUNT_STATUS_REASON | IS_FINALIZED | IS_CARRIED_FORWARD | BALANCER_ACCOUNT_URL | ACCOUNT_CREATED_IN_PERIOD | NO_OF_DOCUMENTS | NO_OF_PREPARERS | NO_OF_APPROVERS | NO_OF_REVIEWERS | BALANCE | BALANCE_ABS | UNIDENTIFIED_BALANCE | UNIDENTIFIED_BALANCE_ABS | BALANCE_ENGAGEMENT | BALANCE_ENGAGEMENT_ABS | UNIDENTIFIED_BALANCE_ENGAGEMENT | UNIDENTIFIED_BALANCE_ENGAGEMENT_ABS | STATUS_COMMENT | ACCOUNT_PURPOSE | ACCOUNT_PROCEDURE | EXTRA_FIELD_01 | EXTRA_FIELD_02 | EXTRA_FIELD_03 | EXTRA_FIELD_04 | EXTRA_FIELD_05 | EXTRA_FIELD_06 | EXTRA_FIELD_07 | EXTRA_FIELD_08 | EXTRA_FIELD_09 | EXTRA_FIELD_10 | NO_OF_REJECTS | PREPARED_BY_NAME | PREPARED_BY_USERNAME | APPROVED_BY_NAME | APPROVED_BY_USERNAME | REVIEWED_BY_NAME | REVIEWED_BY_USERNAME | PREPARED_DATE | APPROVED_DATE | REVIEWED_DATE | REJECTED_DATE | BALANCE_UPDATED_DATE | ACCOUNT_STATUS_COMMENTS | ACCOUNT_STATUS_REASON_TEXT | REVIEW_COMMENT | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | Not prepared | NULL | False | NULL | https://balancer.adra.com/engagements... | NULL | 0 | 1 | 1 | 0 | 1254246.64 | 1254246.64 | 104.71 | 104.71 | 1661625.95 | 1661625.95 | 138.72 | 138.72 | Set to not preapred due to update in ... | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | NULL | NULL | NULL | NULL | 46342.41964 | NULL | NULL | NULL | adra_account_facts.csv | <masked> | 2026-11-16 18:53:24.519000 | <masked> | 2026-11-16 18:53:24.519000 |
| <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | Not prepared | NULL | False | NULL | https://balancer.adra.com/engagements... | NULL | 0 | 1 | 1 | 0 | 528437.11 | 528437.11 | 1624.58 | 1624.58 | 700073.48 | 700073.48 | 2152.24 | 2152.24 | Set to not preapred due to update in ... | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | NULL | NULL | NULL | NULL | 46342.41964 | NULL | NULL | NULL | adra_account_facts.csv | <masked> | 2026-11-16 18:53:24.519000 | <masked> | 2026-11-16 18:53:24.519000 |
| <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | Not prepared | NULL | False | NULL | https://balancer.adra.com/engagements... | NULL | 0 | 1 | 1 | 0 | 6531120.01 | 6531120.01 | 1434.19 | 1434.19 | 8652427.79 | 8652427.79 | 1900.01 | 1900.01 | Set to not preapred due to update in ... | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | NULL | NULL | NULL | NULL | 46342.41964 | NULL | NULL | NULL | adra_account_facts.csv | <masked> | 2026-11-16 18:53:24.519000 | <masked> | 2026-11-16 18:53:24.519000 |
| <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | Not prepared | NULL | False | NULL | https://balancer.adra.com/engagements... | NULL | 0 | 1 | 1 | 0 | 116921.92 | 116921.92 | 91.01 | 91.01 | 154898.16 | 154898.16 | 120.57 | 120.57 | Set to not preapred due to update in ... | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | NULL | NULL | NULL | NULL | 46342.41965 | NULL | NULL | NULL | adra_account_facts.csv | <masked> | 2026-11-16 18:53:24.519000 | <masked> | 2026-11-16 18:53:24.519000 |
| <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | Not prepared | NULL | False | NULL | https://balancer.adra.com/engagements... | NULL | 0 | 1 | 1 | 0 | 173305.14 | 173305.14 | 620.2 | 620.2 | 229594.65 | 229594.65 | 821.64 | 821.64 | Set to not preapred due to update in ... | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | NULL | NULL | NULL | NULL | 46342.41965 | NULL | NULL | NULL | adra_account_facts.csv | <masked> | 2026-11-16 18:53:24.519000 | <masked> | 2026-11-16 18:53:24.519000 |
