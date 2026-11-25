---
name: manage_close_adra_reconciliation
schema: gold
layer: gold
domain: recon
type: view
status: active
purpose: Shows ADRA account reconciliations with legal entity; preparer/reviewer; due date and status.
grain: one row per account reconciliation
primary_key:
- ACCOUNT
- LEGAL_ENTITY
- PERIOD_NAME
entity_column: LEGAL_ENTITY
period_columns:
- DUE
- PERIOD_NAME
pii_columns:
- PREPARER
- REVIEWER
synonyms: []
built_from:
- adra_account_dimensions
- adra_account_facts
- adra_transaction_facts
known_issues: []
row_count: 97
proposed_fields: []
reviewed:
- superseded_by
superseded_by:
- silver.adra_account_facts
---

# manage_close_adra_reconciliation

> Superseded: this table is a copy of ADRA data. Answers use the source of truth `silver.adra_account_facts` (decision 21 Nov 2026).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ACCOUNT` | string |  |  | `ACCOUNT` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `ENTITY_NAME` | string |  |  | `ENTITY_NAME` |
| `PREPARER` | string |  |  | `PREPARER` |
| `REVIEWER` | string |  |  | `REVIEWER` |
| `DUE` | date |  |  | `DUE` |
| `STATUS` | string |  |  | `STATUS` |
| `ACTION` | string |  |  | `ACTION` |
| `PERIOD_NAME` | string |  |  | `PERIOD_NAME` |

## Values

**DUE**
- `2026-11-10 00:00:00`: 97 rows

**STATUS**
- `Not prepared`: 58 rows
- `Approved`: 23 rows
- `Prepared`: 16 rows

## Profile

Rows in the latest export: 97.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ACCOUNT` | STRING | 79 | 0 | 101101 ABC Test Account | 333420 Non Admitted Assets - Prepaid ... |
| `LEGAL_ENTITY` | STRING | 8 | 1 |  |  |
| `ENTITY_NAME` | STRING | 8 | 1 |  |  |
| `PREPARER` | STRING | 4 | 0 |  |  |
| `REVIEWER` | STRING | 4 | 0 |  |  |
| `DUE` | DATE | 1 | 0 | 2026-11-10 00:00:00 | 2026-11-10 00:00:00 |
| `STATUS` | STRING | 3 | 0 | Approved | Prepared |
| `ACTION` | STRING | 98 | 0 | https://balancer.adra.com/engagements... | https://balancer.adra.com/engagements... |
| `PERIOD_NAME` | STRING | 3 | 0 |  |  |

## Sample rows

| ACCOUNT | PREPARER | REVIEWER | DUE | STATUS | ACTION | PERIOD_NAME |
|---|---|---|---|---|---|---|
| 109036 IBA Bank Account CAD | <masked> | <masked> | 2026-11-10 00:00:00 | Not prepared | https://balancer.adra.com/engagements... | (altered in export) |
| 109023 CMC control account | <masked> | <masked> | 2026-11-10 00:00:00 | Not prepared | https://balancer.adra.com/engagements... | (altered in export) |
| 109023 CMC control account | <masked> | <masked> | 2026-11-10 00:00:00 | Not prepared | https://balancer.adra.com/engagements... | (altered in export) |
| 199001 IBA Debtor | <masked> | <masked> | 2026-11-10 00:00:00 | Not prepared | https://balancer.adra.com/engagements... | (altered in export) |
| 109036 IBA Bank Account CAD | <masked> | <masked> | 2026-11-10 00:00:00 | Not prepared | https://balancer.adra.com/engagements... | (altered in export) |
