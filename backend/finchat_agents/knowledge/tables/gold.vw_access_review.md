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
row_count: 38
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
- `Finance`: 15 rows
- `Testing`: 8 rows
- `Risk`: 8 rows
- `IT Controls`: 7 rows

**NO_OF_REPORTEES**
- `3`: 23 rows
- `2`: 15 rows

**APPLICATION**
- `D365`: 12 rows
- `Fynapse`: 11 rows
- `Power BI`: 8 rows
- `UI`: 6 rows
- `None`: 1 rows

**ACCESS_TYPE**
- `Admin`: 10 rows
- `Approver`: 9 rows
- `Viewer`: 4 rows
- `Read`: 4 rows
- `User`: 4 rows
- `No Access`: 3 rows
- `Contributor`: 2 rows
- `Read / Write`: 2 rows

**APPROVED_TIMESTAMP**
- `None`: 38 rows

**CERTIFY_ENABLED**
- `True`: 38 rows

## Profile

Rows in the latest export: 38.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `MANAGER_EMAIL` | STRING | 5 | 0 |  |  |
| `MANAGER` | STRING | 5 | 0 |  |  |
| `DEPARTMENT` | STRING | 4 | 0 | Finance | Testing |
| `NO_OF_REPORTEES` | INT | 2 | 0 | 2 | 3 |
| `REPORTEE` | STRING | 13 | 0 |  |  |
| `REPORTEE_EMAIL` | STRING | 12 | 0 |  |  |
| `APPLICATION` | STRING | 4 | 1 | D365 | UI |
| `LEGAL_ENTITY` | STRING | 6 | 1 |  |  |
| `ACCESS_TYPE` | STRING | 8 | 0 | Admin | Viewer |
| `APPROVED_BY` | STRING | 0 | 38 |  |  |
| `APPROVED_TIMESTAMP` | TIMESTAMP | 0 | 38 |  |  |
| `CERTIFY_ENABLED` | BOOLEAN | 1 | 0 | True | True |

## Sample rows

| MANAGER_EMAIL | MANAGER | DEPARTMENT | NO_OF_REPORTEES | REPORTEE | REPORTEE_EMAIL | APPLICATION | ACCESS_TYPE | APPROVED_BY | APPROVED_TIMESTAMP | CERTIFY_ENABLED |
|---|---|---|---|---|---|---|---|---|---|---|
| <masked> | <masked> | IT Controls | 2 | <masked> | <masked> | Fynapse | Approver | <masked> | NULL | True |
| <masked> | <masked> | IT Controls | 2 | <masked> | <masked> | Power BI | Viewer | <masked> | NULL | True |
| <masked> | <masked> | IT Controls | 2 | <masked> | <masked> | D365 | Read | <masked> | NULL | True |
| <masked> | <masked> | IT Controls | 2 | <masked> | <masked> | UI | User | <masked> | NULL | True |
| <masked> | <masked> | IT Controls | 2 | <masked> | <masked> | D365 | No Access | <masked> | NULL | True |
