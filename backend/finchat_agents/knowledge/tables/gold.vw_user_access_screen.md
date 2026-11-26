---
name: vw_user_access_screen
schema: gold
layer: gold
domain: null
type: table
status: active
purpose: Shows managers and their reportees with application and legal-entity access.
grain: one row per manager; reportee; application and legal entity
primary_key:
- EMAIL_ID
- REPORTEE_EMAIL_ID
- APPLICATION
- LEGAL_ENTITY
entity_column: null
period_columns: []
pii_columns:
- MANAGER_NAME
- EMAIL_ID
- REPORTEE_NAME
- REPORTEE_EMAIL_ID
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

# vw_user_access_screen

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `MANAGER_NAME` | string |  |  | `MANAGER_NAME` |
| `EMAIL_ID` | string |  |  | `EMAIL_ID` |
| `DEPARTMENT` | string |  |  | `DEPARTMENT` |
| `NUMBER_OF_REPORTEES` | long |  |  | `NUMBER_OF_REPORTEES` |
| `REPORTEE_NAME` | string |  |  | `REPORTEE_NAME` |
| `REPORTEE_EMAIL_ID` | string |  |  | `REPORTEE_EMAIL_ID` |
| `APPLICATION` | string |  |  | `APPLICATION` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `ACCESS_TYPE` | string |  |  | `ACCESS_TYPE` |

## Values

**DEPARTMENT**
- `Finance`

**NUMBER_OF_REPORTEES**
- `2`

**APPLICATION**
- `D365`
- `UI`
- `FYNAPSE`
- `POWERBI`

**ACCESS_TYPE**
- `No Access`
- `Approver`
- `Read`
- `Admin`
- `AR Analyst`
- `AP Analyst`
- `Read/Write`
