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
row_count: 10
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
- `Finance`: 10 rows

**NUMBER_OF_REPORTEES**
- `2`: 10 rows

**APPLICATION**
- `D365`: 3 rows
- `UI`: 3 rows
- `FYNAPSE`: 2 rows
- `POWERBI`: 2 rows

**ACCESS_TYPE**
- `No Access`: 2 rows
- `Approver`: 2 rows
- `Read`: 2 rows
- `Admin`: 1 rows
- `AR Analyst`: 1 rows
- `AP Analyst`: 1 rows
- `Read/Write`: 1 rows

## Profile

Rows in the latest export: 10.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `MANAGER_NAME` | STRING | 1 | 0 |  |  |
| `EMAIL_ID` | STRING | 1 | 0 |  |  |
| `DEPARTMENT` | STRING | 1 | 0 | Finance | Finance |
| `NUMBER_OF_REPORTEES` | LONG | 1 | 0 | 2 | 2 |
| `REPORTEE_NAME` | STRING | 2 | 0 |  |  |
| `REPORTEE_EMAIL_ID` | STRING | 2 | 0 |  |  |
| `APPLICATION` | STRING | 4 | 0 | D365 | UI |
| `LEGAL_ENTITY` | STRING | 5 | 0 |  |  |
| `ACCESS_TYPE` | STRING | 7 | 0 | AP Analyst | Read/Write |

## Sample rows

| MANAGER_NAME | EMAIL_ID | DEPARTMENT | NUMBER_OF_REPORTEES | REPORTEE_NAME | REPORTEE_EMAIL_ID | APPLICATION | ACCESS_TYPE |
|---|---|---|---|---|---|---|---|
| <masked> | <masked> | Finance | 2 | <masked> | <masked> | D365 | Read |
| <masked> | <masked> | Finance | 2 | <masked> | <masked> | D365 | No Access |
| <masked> | <masked> | Finance | 2 | <masked> | <masked> | FYNAPSE | Approver |
| <masked> | <masked> | Finance | 2 | <masked> | <masked> | POWERBI | Read/Write |
| <masked> | <masked> | Finance | 2 | <masked> | <masked> | UI | AP Analyst |
