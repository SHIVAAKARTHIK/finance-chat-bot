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
row_count: 1
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
- `Not set`: 1 rows

**AccountClass**
- `Not set`: 1 rows

**AccountType**
- `Normal`: 1 rows

**IsKeyAccount**
- `False`: 1 rows

**ReconciliationType**
- `Basic`: 1 rows

**RiskType**
- `Not set`: 1 rows

**PrepareFrequency**
- `Month end`: 1 rows

**ApproveFrequency**
- `Month end`: 1 rows

**ReviewFrequency**
- `Month end`: 1 rows

**Account_Id**
- `2267785`: 1 rows

**ParentAccountId**
- `0`: 1 rows

**AccountNumber**
- `101101`: 1 rows

**AccountName**
- `ABC Test Account`: 1 rows

**Account**
- `101101 ABC Test Account`: 1 rows

**AccountSubClass**
- `None`: 1 rows

**SystemCertify**
- `Not allowed`: 1 rows

**CarryForward**
- `Never`: 1 rows

**AccountProcedure**
- `None`: 1 rows

**AccountPurpose**
- `None`: 1 rows

**MDP_CREATED_DATE**
- `2026-10-23 10:52:07.081835+00:00`: 1 rows

**MDP_MODIFIED_DATE**
- `2026-10-23 10:52:07.081835+00:00`: 1 rows

## Profile

Rows in the latest export: 1.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Account_Key` | LONG | 1 | 0 |  |  |
| `BaseClass` | STRING | 1 | 0 | Not set | Not set |
| `Engagement_Key` | INT | 1 | 0 |  |  |
| `ParentAccount_Key` | LONG | 1 | 0 |  |  |
| `AccountClass` | STRING | 1 | 0 | Not set | Not set |
| `AccountType` | STRING | 1 | 0 | Normal | Normal |
| `IsKeyAccount` | BOOLEAN | 1 | 0 | False | False |
| `ReconciliationType` | STRING | 1 | 0 | Basic | Basic |
| `RiskType` | STRING | 1 | 0 | Not set | Not set |
| `PrepareFrequency` | STRING | 1 | 0 | Month end | Month end |
| `ApproveFrequency` | STRING | 1 | 0 | Month end | Month end |
| `ReviewFrequency` | STRING | 1 | 0 | Month end | Month end |
| `Account_Id` | LONG | 1 | 0 | 2267785 | 2267785 |
| `ParentAccountId` | LONG | 1 | 0 | 0 | 0 |
| `AccountNumber` | STRING | 1 | 0 | 101101 | 101101 |
| `AccountName` | STRING | 1 | 0 | ABC Test Account | ABC Test Account |
| `Account` | STRING | 1 | 0 | 101101 ABC Test Account | 101101 ABC Test Account |
| `AccountSubClass` | STRING | 0 | 1 |  |  |
| `SystemCertify` | STRING | 1 | 0 | Not allowed | Not allowed |
| `CarryForward` | STRING | 1 | 0 | Never | Never |
| `AccountProcedure` | STRING | 0 | 1 |  |  |
| `AccountPurpose` | STRING | 0 | 1 |  |  |
| `LegalEntity_Key` | INT | 1 | 0 |  |  |
| `HASH_KEY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-10-23 10:52:07.082000 | 2026-10-23 10:52:07.082000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-10-23 10:52:07.082000 | 2026-10-23 10:52:07.082000 |

## Sample rows

| BaseClass | AccountClass | AccountType | IsKeyAccount | ReconciliationType | RiskType | PrepareFrequency | ApproveFrequency | ReviewFrequency | Account_Id | ParentAccountId | AccountNumber | AccountName | Account | AccountSubClass | SystemCertify | CarryForward | AccountProcedure | AccountPurpose | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Not set | Not set | Normal | False | Basic | Not set | Month end | Month end | Month end | 2267785 | 0 | 101101 | ABC Test Account | 101101 ABC Test Account | NULL | Not allowed | Never | NULL | NULL | <masked> | 2026-10-23 10:52:07.082000 | <masked> | 2026-10-23 10:52:07.082000 |
