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
- PreparedByName
- ApprovedByName
- ReviewedByName
synonyms: []
built_from:
- adra_account_facts (likely)
known_issues: []
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
- `Not prepared`

**AccountStatusReason**
- `None`

**IsFinalized**
- `False`

**IsCarriedForward**
- `False`

**BalancerAccountUrl**
- `https://balancer.adra.com/engagements/y2WelBZytUyYQEvBOKGSGw/accountperiods/16481111`

**AccountCreatedInPeriod**
- `2026-10-18 09:40:39.816853+00:00`

**NoOfDocuments**
- `0`

**NoOfPreparers**
- `1`

**NoOfApprovers**
- `1`

**NoOfReviewers**
- `1`

**Balance**
- `30890`

**BalanceAbs**
- `30890`

**UnidentifiedBalance**
- `0`

**UnIdentifiedBalanceAbs**
- `0`

**BalanceEngagement**
- `30890`

**BalanceEngagementAbs**
- `30890`

**UnidentifiedBalanceEngagement**
- `0`

**UnIdentifiedBalanceEngagementAbs**
- `0`

**StatusComment**
- `Account Period Created`

**AccountPurpose**
- `None`

**AccountProcedure**
- `None`

**ExtraField01**
- `None`

**ExtraField02**
- `None`

**ExtraField03**
- `None`

**ExtraField04**
- `None`

**ExtraField05**
- `None`

**ExtraField06**
- `None`

**ExtraField07**
- `None`

**ExtraField08**
- `None`

**ExtraField09**
- `None`

**ExtraField10**
- `None`

**NoOfRejects**
- `0`

**PreparedDate**
- `None`

**ApprovedDate**
- `None`

**ReviewedDate**
- `None`

**RejectedDate**
- `None`

**BalanceUpdatedDate**
- `2026-10-18 09:40:48.373333+00:00`

**AccountStatusComments**
- `None`

**AccountStatusReasonText**
- `None`

**ReviewComment**
- `None`

**MDP_CREATED_DATE**
- `2026-10-23 10:52:15.044854+00:00`

**MDP_MODIFIED_DATE**
- `2026-10-23 10:52:15.044854+00:00`

## Empty columns

Empty in every row: `AccountPurpose`, `AccountProcedure`, `ExtraField01`, `ExtraField02`, `ExtraField03`, `ExtraField04`, `ExtraField05`, `ExtraField06`, `ExtraField07`, `ExtraField08`, `ExtraField09`, `ExtraField10`, `PreparedByName`, `PreparedByUsername`, `ApprovedByName`, `ApprovedByUsername`, `ReviewedByName`, `ReviewedByUsername`, `PreparedDate`, `ApprovedDate`, `ReviewedDate`, `RejectedDate`, `AccountStatusComments`, `AccountStatusReasonText`, `ReviewComment`. Do not filter or group on them.
