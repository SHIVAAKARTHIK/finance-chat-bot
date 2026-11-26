---
name: manage_close_recon_account_dims
schema: silver
layer: silver
domain: recon
type: table
status: active
purpose: Reconciliation account attributes used by the Manage the Close screen.
grain: one row per Account_Key (one reconciliation account)
primary_key:
- Account_Key
entity_column: null
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from:
- adra_account_dimensions (likely)
known_issues: []
proposed_fields:
- grain
- primary_key
reviewed:
- superseded_by
superseded_by:
- silver.adra_account_dimensions
---

# manage_close_recon_account_dims

> Superseded: this table is a copy of ADRA data. Answers use the source of truth `silver.adra_account_dimensions` (decision 21 Nov 2026).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Account_Key` | long |  |  | `Account_Key` |
| `BaseClass` | string |  |  | `BaseClass` |
| `Engagement_Key` | int |  |  | `Engagement_Key` |
| `ParentAccount_Key` | long |  |  | `ParentAccount_Key` |
| `AccountClass` | string |  |  | `AccountClass` |
| `AccountType` | string |  |  | `AccountType` |
| `IsKeyAccount` | boolean |  |  | `IsKeyAccount` |
| `ReconciliationType` | string |  |  | `ReconciliationType` |
| `RiskType` | string |  |  | `RiskType` |
| `PrepareFrequency` | string |  |  | `PrepareFrequency` |
| `ApproveFrequency` | string |  |  | `ApproveFrequency` |
| `ReviewFrequency` | string |  |  | `ReviewFrequency` |
| `Account_Id` | long |  |  | `Account_Id` |
| `ParentAccountId` | long |  |  | `ParentAccountId` |
| `AccountNumber` | string |  |  | `AccountNumber` |
| `AccountName` | string |  |  | `AccountName` |
| `Account` | string |  |  | `Account` |
| `AccountSubClass` | string |  |  | `AccountSubClass` |
| `SystemCertify` | string |  |  | `SystemCertify` |
| `CarryForward` | string |  |  | `CarryForward` |
| `AccountProcedure` | string |  |  | `AccountProcedure` |
| `AccountPurpose` | string |  |  | `AccountPurpose` |
| `LegalEntity_Key` | int |  |  | `LegalEntity_Key` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**BaseClass**
- `Not set`

**AccountClass**
- `Not set`

**AccountType**
- `Normal`

**IsKeyAccount**
- `False`

**ReconciliationType**
- `Basic`

**RiskType**
- `Not set`

**PrepareFrequency**
- `Month end`

**ApproveFrequency**
- `Month end`

**ReviewFrequency**
- `Month end`

**Account_Id**
- `2267785`

**ParentAccountId**
- `0`

**AccountNumber**
- `101101`

**AccountName**
- `ABC Test Account`

**Account**
- `101101 ABC Test Account`

**AccountSubClass**
- `None`

**SystemCertify**
- `Not allowed`

**CarryForward**
- `Never`

**AccountProcedure**
- `None`

**AccountPurpose**
- `None`

**MDP_CREATED_DATE**
- `2026-10-23 10:52:07.081835+00:00`

**MDP_MODIFIED_DATE**
- `2026-10-23 10:52:07.081835+00:00`

## Empty columns

Empty in every row: `AccountSubClass`, `AccountProcedure`, `AccountPurpose`. Do not filter or group on them.
