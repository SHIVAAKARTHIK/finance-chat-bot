---
name: audit_soc_report
schema: silver
layer: silver
domain: null
type: table
status: active
purpose: Summary of the SOC 1 report (period covered; opinion; exceptions).
grain: one row per HASH_KEY (one SOC report)
primary_key:
- HASH_KEY
entity_column: null
period_columns:
- Period_covered
- Issued
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
proposed_fields:
- grain
- primary_key
reviewed: false
---

# audit_soc_report

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
- `KPMG SOC 1 Report`

**Period_covered**
- `2025-10-1 – 2026-9-30`

**Opinion**
- `Unqualified`

**Issued**
- `2026-10-23 00:00:00`

**Control_exceptions**
- `2 noted, none affecting opinion`

**Bridge_letter**
- `Available on request`

**MDP_CREATED_DATE**
- `2026-11-04 14:12:31.295611+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-04 14:12:31.295611+00:00`
