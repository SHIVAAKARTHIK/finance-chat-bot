---
name: fact_customer_payment_journal_headers
schema: silver
layer: silver
domain: ar
type: table
status: active
purpose: Header of each customer payment journal batch (name; posted flag).
grain: one row per HASH_KEY (one customer payment journal batch)
primary_key:
- HASH_KEY
entity_column: dataAreaId
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
row_count: 2
proposed_fields:
- grain
- primary_key
reviewed: false
---

# fact_customer_payment_journal_headers

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `dataAreaId` | string |  |  | `dataAreaId` |
| `JournalBatchNumber` | string |  |  | `JournalBatchNumber` |
| `JournalName` | string |  |  | `JournalName` |
| `OverrideSalesTax` | string |  |  | `OverrideSalesTax` |
| `Description` | string |  |  | `Description` |
| `IsPosted` | string |  |  | `IsPosted` |
| `source_file_name` | string |  |  | `source_file_name` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**JournalBatchNumber**
- `100-000227`: 1 rows
- `100-000234`: 1 rows

**JournalName**
- `CPJ`: 2 rows

**OverrideSalesTax**
- `No`: 2 rows

**Description**
- `Customer payment journal`: 2 rows

**IsPosted**
- `Yes`: 1 rows
- `No`: 1 rows

**source_file_name**
- `customerpaymentjournalheaders__20261116_105417.csv`: 2 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:43:08.189448+00:00`: 2 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:43:08.189448+00:00`: 2 rows

## Profile

Rows in the latest export: 2.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `dataAreaId` | STRING | 1 | 0 |  |  |
| `JournalBatchNumber` | STRING | 2 | 0 | 100-000227 | 100-000234 |
| `JournalName` | STRING | 1 | 0 | CPJ | CPJ |
| `OverrideSalesTax` | STRING | 1 | 0 | No | No |
| `Description` | STRING | 1 | 0 | Customer payment journal | Customer payment journal |
| `IsPosted` | STRING | 2 | 0 | No | Yes |
| `source_file_name` | STRING | 1 | 0 | customerpaymentjournalheaders__202611... | customerpaymentjournalheaders__202611... |
| `HASH_KEY` | STRING | 2 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:43:08.189000 | 2026-11-16 11:43:08.189000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:43:08.189000 | 2026-11-16 11:43:08.189000 |

## Sample rows

| JournalBatchNumber | JournalName | OverrideSalesTax | Description | IsPosted | source_file_name | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|
| 100-000227 | CPJ | No | Customer payment journal | Yes | customerpaymentjournalheaders__202611... | <masked> | 2026-11-16 11:43:08.189000 | <masked> | 2026-11-16 11:43:08.189000 |
| 100-000234 | CPJ | No | Customer payment journal | No | customerpaymentjournalheaders__202611... | <masked> | 2026-11-16 11:43:08.189000 | <masked> | 2026-11-16 11:43:08.189000 |
