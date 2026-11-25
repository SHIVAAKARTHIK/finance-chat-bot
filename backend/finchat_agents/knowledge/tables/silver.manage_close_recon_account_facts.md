---
name: manage_close_recon_account_facts
schema: silver
layer: silver
domain: recon
type: table
status: active
purpose: Reconciliation status of accounts used by the Manage the Close screen.
grain: one row per Account_Key (one account reconciliation)
primary_key:
- Account_Key
entity_column: LegalEntity_Key
period_columns:
- Period_Key
- FiscalYearPeriod_Key
- AccountCreatedInPeriod
pii_columns:
- PreparerUsername
- PreparerName
- ApproverUsername
- ApproverName
- ReviewerUsername
- ReviewerName
- AssignedToUsername
- AssignedToName
- PreparedByUsername
- ApprovedByUsername
- ReviewedByUsername
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from:
- adra_account_facts (likely)
known_issues: []
row_count: 1
proposed_fields:
- grain
- primary_key
reviewed:
- superseded_by
superseded_by:
- silver.adra_account_facts
---

# manage_close_recon_account_facts

> Superseded: this table is a copy of ADRA data. Answers use the source of truth `silver.adra_account_facts` (decision 21 Nov 2026).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Account_Key` | long |  |  | `Account_Key` |
| `Engagement_Key` | int |  |  | `Engagement_Key` |
| `LegalEntity_Key` | int |  |  | `LegalEntity_Key` |
| `Period_Key` | long |  |  | `Period_Key` |
| `FiscalYearPeriod_Key` | int |  |  | `FiscalYearPeriod_Key` |
| `PreparerUsername` | string |  |  | `PreparerUsername` |
| `PreparerName` | string |  |  | `PreparerName` |
| `ApproverUsername` | string |  |  | `ApproverUsername` |
| `ApproverName` | string |  |  | `ApproverName` |
| `ReviewerUsername` | string |  |  | `ReviewerUsername` |
| `ReviewerName` | string |  |  | `ReviewerName` |
| `AssignedToUsername` | string |  |  | `AssignedToUsername` |
| `AssignedToName` | string |  |  | `AssignedToName` |
| `AccountStatus` | string |  |  | `AccountStatus` |
| `AccountStatusReason` | string |  |  | `AccountStatusReason` |
| `IsFinalized` | boolean |  |  | `IsFinalized` |
| `IsCarriedForward` | boolean |  |  | `IsCarriedForward` |
| `BalancerAccountUrl` | string |  |  | `BalancerAccountUrl` |
| `AccountCreatedInPeriod` | timestamp |  |  | `AccountCreatedInPeriod` |
| `NoOfDocuments` | int |  |  | `NoOfDocuments` |
| `NoOfPreparers` | int |  |  | `NoOfPreparers` |
| `NoOfApprovers` | int |  |  | `NoOfApprovers` |
| `NoOfReviewers` | int |  |  | `NoOfReviewers` |
| `Balance` | decimal |  |  | `Balance` |
| `BalanceAbs` | decimal |  |  | `BalanceAbs` |
| `UnidentifiedBalance` | decimal |  |  | `UnidentifiedBalance` |
| `UnIdentifiedBalanceAbs` | decimal |  |  | `UnIdentifiedBalanceAbs` |
| `BalanceEngagement` | decimal |  |  | `BalanceEngagement` |
| `BalanceEngagementAbs` | decimal |  |  | `BalanceEngagementAbs` |
| `UnidentifiedBalanceEngagement` | decimal |  |  | `UnidentifiedBalanceEngagement` |
| `UnIdentifiedBalanceEngagementAbs` | decimal |  |  | `UnIdentifiedBalanceEngagementAbs` |
| `StatusComment` | string |  |  | `StatusComment` |
| `AccountPurpose` | string |  |  | `AccountPurpose` |
| `AccountProcedure` | string |  |  | `AccountProcedure` |
| `ExtraField01` | string |  |  | `ExtraField01` |
| `ExtraField02` | string |  |  | `ExtraField02` |
| `ExtraField03` | string |  |  | `ExtraField03` |
| `ExtraField04` | string |  |  | `ExtraField04` |
| `ExtraField05` | string |  |  | `ExtraField05` |
| `ExtraField06` | string |  |  | `ExtraField06` |
| `ExtraField07` | string |  |  | `ExtraField07` |
| `ExtraField08` | string |  |  | `ExtraField08` |
| `ExtraField09` | string |  |  | `ExtraField09` |
| `ExtraField10` | string |  |  | `ExtraField10` |
| `NoOfRejects` | int |  |  | `NoOfRejects` |
| `AccountPeriodComment_Key` | long |  |  | `AccountPeriodComment_Key` |
| `AccountPeriodTransaction_Key` | long |  |  | `AccountPeriodTransaction_Key` |
| `PreparedByName` | string |  |  | `PreparedByName` |
| `PreparedByUsername` | string |  |  | `PreparedByUsername` |
| `ApprovedByName` | string |  |  | `ApprovedByName` |
| `ApprovedByUsername` | string |  |  | `ApprovedByUsername` |
| `ReviewedByName` | string |  |  | `ReviewedByName` |
| `ReviewedByUsername` | string |  |  | `ReviewedByUsername` |
| `PreparedDate` | timestamp |  |  | `PreparedDate` |
| `ApprovedDate` | timestamp |  |  | `ApprovedDate` |
| `ReviewedDate` | timestamp |  |  | `ReviewedDate` |
| `RejectedDate` | timestamp |  |  | `RejectedDate` |
| `BalanceUpdatedDate` | timestamp |  |  | `BalanceUpdatedDate` |
| `AccountStatusComments` | string |  |  | `AccountStatusComments` |
| `AccountStatusReasonText` | string |  |  | `AccountStatusReasonText` |
| `ReviewComment` | string |  |  | `ReviewComment` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**AccountStatus**
- `Not prepared`: 1 rows

**AccountStatusReason**
- `None`: 1 rows

**IsFinalized**
- `False`: 1 rows

**IsCarriedForward**
- `False`: 1 rows

**BalancerAccountUrl**
- `https://balancer.adra.com/engagements/y2WelBZytUyYQEvBOKGSGw/accountperiods/16481111`: 1 rows

**AccountCreatedInPeriod**
- `2026-10-18 09:40:39.816853+00:00`: 1 rows

**NoOfDocuments**
- `0`: 1 rows

**NoOfPreparers**
- `1`: 1 rows

**NoOfApprovers**
- `1`: 1 rows

**NoOfReviewers**
- `1`: 1 rows

**Balance**
- `30890`: 1 rows

**BalanceAbs**
- `30890`: 1 rows

**UnidentifiedBalance**
- `0`: 1 rows

**UnIdentifiedBalanceAbs**
- `0`: 1 rows

**BalanceEngagement**
- `30890`: 1 rows

**BalanceEngagementAbs**
- `30890`: 1 rows

**UnidentifiedBalanceEngagement**
- `0`: 1 rows

**UnIdentifiedBalanceEngagementAbs**
- `0`: 1 rows

**StatusComment**
- `Account Period Created`: 1 rows

**AccountPurpose**
- `None`: 1 rows

**AccountProcedure**
- `None`: 1 rows

**ExtraField01**
- `None`: 1 rows

**ExtraField02**
- `None`: 1 rows

**ExtraField03**
- `None`: 1 rows

**ExtraField04**
- `None`: 1 rows

**ExtraField05**
- `None`: 1 rows

**ExtraField06**
- `None`: 1 rows

**ExtraField07**
- `None`: 1 rows

**ExtraField08**
- `None`: 1 rows

**ExtraField09**
- `None`: 1 rows

**ExtraField10**
- `None`: 1 rows

**NoOfRejects**
- `0`: 1 rows

**PreparedByName**
- `None`: 1 rows

**ApprovedByName**
- `None`: 1 rows

**ReviewedByName**
- `None`: 1 rows

**PreparedDate**
- `None`: 1 rows

**ApprovedDate**
- `None`: 1 rows

**ReviewedDate**
- `None`: 1 rows

**RejectedDate**
- `None`: 1 rows

**BalanceUpdatedDate**
- `2026-10-18 09:40:48.373333+00:00`: 1 rows

**AccountStatusComments**
- `None`: 1 rows

**AccountStatusReasonText**
- `None`: 1 rows

**ReviewComment**
- `None`: 1 rows

**MDP_CREATED_DATE**
- `2026-10-23 10:52:15.044854+00:00`: 1 rows

**MDP_MODIFIED_DATE**
- `2026-10-23 10:52:15.044854+00:00`: 1 rows

## Profile

Rows in the latest export: 1.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Account_Key` | LONG | 1 | 0 |  |  |
| `Engagement_Key` | INT | 1 | 0 |  |  |
| `LegalEntity_Key` | INT | 1 | 0 |  |  |
| `Period_Key` | LONG | 1 | 0 |  |  |
| `FiscalYearPeriod_Key` | INT | 1 | 0 |  |  |
| `PreparerUsername` | STRING | 1 | 0 |  |  |
| `PreparerName` | STRING | 1 | 0 |  |  |
| `ApproverUsername` | STRING | 1 | 0 |  |  |
| `ApproverName` | STRING | 1 | 0 |  |  |
| `ReviewerUsername` | STRING | 1 | 0 |  |  |
| `ReviewerName` | STRING | 1 | 0 |  |  |
| `AssignedToUsername` | STRING | 1 | 0 |  |  |
| `AssignedToName` | STRING | 1 | 0 |  |  |
| `AccountStatus` | STRING | 1 | 0 | Not prepared | Not prepared |
| `AccountStatusReason` | STRING | 1 | 0 | None | None |
| `IsFinalized` | BOOLEAN | 1 | 0 | False | False |
| `IsCarriedForward` | BOOLEAN | 1 | 0 | False | False |
| `BalancerAccountUrl` | STRING | 1 | 0 | https://balancer.adra.com/engagements... | https://balancer.adra.com/engagements... |
| `AccountCreatedInPeriod` | TIMESTAMP | 1 | 0 | 2026-10-18 09:40:39.817000 | 2026-10-18 09:40:39.817000 |
| `NoOfDocuments` | INT | 1 | 0 | 0 | 0 |
| `NoOfPreparers` | INT | 1 | 0 | 1 | 1 |
| `NoOfApprovers` | INT | 1 | 0 | 1 | 1 |
| `NoOfReviewers` | INT | 1 | 0 | 1 | 1 |
| `Balance` | DECIMAL | 1 | 0 | 30890 | 30890 |
| `BalanceAbs` | DECIMAL | 1 | 0 | 30890 | 30890 |
| `UnidentifiedBalance` | DECIMAL | 1 | 0 | 0 | 0 |
| `UnIdentifiedBalanceAbs` | DECIMAL | 1 | 0 | 0 | 0 |
| `BalanceEngagement` | DECIMAL | 1 | 0 | 30890 | 30890 |
| `BalanceEngagementAbs` | DECIMAL | 1 | 0 | 30890 | 30890 |
| `UnidentifiedBalanceEngagement` | DECIMAL | 1 | 0 | 0 | 0 |
| `UnIdentifiedBalanceEngagementAbs` | DECIMAL | 1 | 0 | 0 | 0 |
| `StatusComment` | STRING | 1 | 0 | Account Period Created | Account Period Created |
| `AccountPurpose` | STRING | 0 | 1 |  |  |
| `AccountProcedure` | STRING | 0 | 1 |  |  |
| `ExtraField01` | STRING | 0 | 1 |  |  |
| `ExtraField02` | STRING | 0 | 1 |  |  |
| `ExtraField03` | STRING | 0 | 1 |  |  |
| `ExtraField04` | STRING | 0 | 1 |  |  |
| `ExtraField05` | STRING | 0 | 1 |  |  |
| `ExtraField06` | STRING | 0 | 1 |  |  |
| `ExtraField07` | STRING | 0 | 1 |  |  |
| `ExtraField08` | STRING | 0 | 1 |  |  |
| `ExtraField09` | STRING | 0 | 1 |  |  |
| `ExtraField10` | STRING | 0 | 1 |  |  |
| `NoOfRejects` | INT | 1 | 0 | 0 | 0 |
| `AccountPeriodComment_Key` | LONG | 1 | 0 |  |  |
| `AccountPeriodTransaction_Key` | LONG | 1 | 0 |  |  |
| `PreparedByName` | STRING | 0 | 1 |  |  |
| `PreparedByUsername` | STRING | 0 | 1 |  |  |
| `ApprovedByName` | STRING | 0 | 1 |  |  |
| `ApprovedByUsername` | STRING | 0 | 1 |  |  |
| `ReviewedByName` | STRING | 0 | 1 |  |  |
| `ReviewedByUsername` | STRING | 0 | 1 |  |  |
| `PreparedDate` | TIMESTAMP | 0 | 1 |  |  |
| `ApprovedDate` | TIMESTAMP | 0 | 1 |  |  |
| `ReviewedDate` | TIMESTAMP | 0 | 1 |  |  |
| `RejectedDate` | TIMESTAMP | 0 | 1 |  |  |
| `BalanceUpdatedDate` | TIMESTAMP | 1 | 0 | 2026-10-18 09:40:48.373000 | 2026-10-18 09:40:48.373000 |
| `AccountStatusComments` | STRING | 0 | 1 |  |  |
| `AccountStatusReasonText` | STRING | 0 | 1 |  |  |
| `ReviewComment` | STRING | 0 | 1 |  |  |
| `HASH_KEY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-10-23 10:52:15.045000 | 2026-10-23 10:52:15.045000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-10-23 10:52:15.045000 | 2026-10-23 10:52:15.045000 |

## Sample rows

| PreparerUsername | PreparerName | ApproverUsername | ApproverName | ReviewerUsername | ReviewerName | AssignedToUsername | AssignedToName | AccountStatus | AccountStatusReason | IsFinalized | IsCarriedForward | BalancerAccountUrl | AccountCreatedInPeriod | NoOfDocuments | NoOfPreparers | NoOfApprovers | NoOfReviewers | Balance | BalanceAbs | UnidentifiedBalance | UnIdentifiedBalanceAbs | BalanceEngagement | BalanceEngagementAbs | UnidentifiedBalanceEngagement | UnIdentifiedBalanceEngagementAbs | StatusComment | AccountPurpose | AccountProcedure | ExtraField01 | ExtraField02 | ExtraField03 | ExtraField04 | ExtraField05 | ExtraField06 | ExtraField07 | ExtraField08 | ExtraField09 | ExtraField10 | NoOfRejects | PreparedByName | PreparedByUsername | ApprovedByName | ApprovedByUsername | ReviewedByName | ReviewedByUsername | PreparedDate | ApprovedDate | ReviewedDate | RejectedDate | BalanceUpdatedDate | AccountStatusComments | AccountStatusReasonText | ReviewComment | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | <masked> | Not prepared | None | False | False | https://balancer.adra.com/engagements... | 2026-10-18 09:40:39.817000 | 0 | 1 | 1 | 1 | 30890 | 30890 | 0 | 0 | 30890 | 30890 | 0 | 0 | Account Period Created | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | <masked> | NULL | <masked> | NULL | <masked> | NULL | NULL | NULL | NULL | 2026-10-18 09:40:48.373000 | NULL | NULL | NULL | <masked> | 2026-10-23 10:52:15.045000 | <masked> | 2026-10-23 10:52:15.045000 |
