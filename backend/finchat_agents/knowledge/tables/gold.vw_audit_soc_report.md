---
name: vw_audit_soc_report
schema: gold
layer: gold
domain: null
type: view
status: active
purpose: Summarizes the SOC 1 report; coverage period; opinion and exceptions.
grain: one row per HASH_KEY (one SOC report)
primary_key:
- Period_covered
- Issued
entity_column: HASH_KEY
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from:
- audit_soc_report
known_issues: []
row_count: 1
proposed_fields:
- entity_column
- grain
reviewed: false
---

# vw_audit_soc_report

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Report` | string |  |  | `Report` |
| `Period_covered` | string |  |  | `Period_covered` |
| `Opinion` | string |  |  | `Opinion` |
| `Issued` | date |  |  | `Issued` |
| `Control_exceptions` | string |  |  | `Control_exceptions` |
| `Bridge_letter` | string |  |  | `Bridge_letter` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**Report**
- `KPMG SOC 1 Report`: 1 rows

**Period_covered**
- `2025-10-1 – 2026-9-30`: 1 rows

**Opinion**
- `Unqualified`: 1 rows

**Issued**
- `2026-10-23 00:00:00`: 1 rows

**Control_exceptions**
- `2 noted, none affecting opinion`: 1 rows

**Bridge_letter**
- `Available on request`: 1 rows

**MDP_CREATED_DATE**
- `2026-11-04 14:12:31.295611+00:00`: 1 rows

**MDP_MODIFIED_DATE**
- `2026-11-04 14:12:31.295611+00:00`: 1 rows

## Profile

Rows in the latest export: 1.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Report` | STRING | 1 | 0 | KPMG SOC 1 Report | KPMG SOC 1 Report |
| `Period_covered` | STRING | 1 | 0 | 2025-10-1 – 2026-9-30 | 2025-10-1 – 2026-9-30 |
| `Opinion` | STRING | 1 | 0 | Unqualified | Unqualified |
| `Issued` | DATE | 1 | 0 | 2026-10-23 00:00:00 | 2026-10-23 00:00:00 |
| `Control_exceptions` | STRING | 1 | 0 | 2 noted, none affecting opinion | 2 noted, none affecting opinion |
| `Bridge_letter` | STRING | 1 | 0 | Available on request | Available on request |
| `HASH_KEY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-04 14:12:31.296000 | 2026-11-04 14:12:31.296000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-04 14:12:31.296000 | 2026-11-04 14:12:31.296000 |

## Sample rows

| Report | Period_covered | Opinion | Issued | Control_exceptions | Bridge_letter | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|
| KPMG SOC 1 Report | 2025-10-1 – 2026-9-30 | Unqualified | 2026-10-23 00:00:00 | 2 noted, none affecting opinion | Available on request | <masked> | 2026-11-04 14:12:31.296000 | <masked> | 2026-11-04 14:12:31.296000 |
