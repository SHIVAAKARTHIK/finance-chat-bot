---
name: vw_access_review
schema: gold
layer: gold
domain: null
type: view
status: active
purpose: Shows managers; reportees and assigned application access for certification.
grain: one row per manager; reportee; application and legal entity
primary_key:
- MANAGER_EMAIL
- REPORTEE_EMAIL
- APPLICATION
- LEGAL_ENTITY
entity_column: null
period_columns: []
pii_columns:
- MANAGER_EMAIL
- MANAGER
- REPORTEE
- REPORTEE_EMAIL
- APPROVED_BY
synonyms: []
built_from:
- access_screen_dim_employee
- access_screen_fact_employee_access
- access_screen_rel_manager_reportee
- access_screen_dim_role
- access_screen_dim_application
- access_screen_dim_legal_entity
known_issues: []
proposed_fields: []
reviewed: false
---

# vw_access_review

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `MANAGER_EMAIL` | string |  |  | `MANAGER_EMAIL` |
| `MANAGER` | string |  |  | `MANAGER` |
| `DEPARTMENT` | string |  |  | `DEPARTMENT` |
| `NO_OF_REPORTEES` | int |  |  | `NO_OF_REPORTEES` |
| `REPORTEE` | string |  |  | `REPORTEE` |
| `REPORTEE_EMAIL` | string |  |  | `REPORTEE_EMAIL` |
| `APPLICATION` | string |  |  | `APPLICATION` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `ACCESS_TYPE` | string |  |  | `ACCESS_TYPE` |
| `APPROVED_BY` | string |  |  | `APPROVED_BY` |
| `APPROVED_TIMESTAMP` | timestamp |  |  | `APPROVED_TIMESTAMP` |
| `CERTIFY_ENABLED` | boolean |  |  | `CERTIFY_ENABLED` |

## Values

**DEPARTMENT**
- `Finance`
- `Testing`
- `Risk`
- `IT Controls`

**NO_OF_REPORTEES**
- `3`
- `2`

**APPLICATION**
- `D365`
- `Fynapse`
- `Power BI`
- `UI`
- `None`

**ACCESS_TYPE**
- `Admin`
- `Approver`
- `Viewer`
- `Read`
- `User`
- `No Access`
- `Contributor`
- `Read / Write`

**APPROVED_TIMESTAMP**
- `None`

**CERTIFY_ENABLED**
- `True`

## Empty columns

Empty in every row: `APPROVED_BY`, `APPROVED_TIMESTAMP`. Do not filter or group on them.
