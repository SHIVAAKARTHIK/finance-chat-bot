---
name: vw_audit_soc_report_deepplinks
schema: gold
layer: gold
domain: null
type: view
status: active
purpose: Provides links to the SOC 1 report and bridge letter.
grain: one row per HASH_KEY (one document link)
primary_key:
- HASH_KEY
entity_column: null
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from:
- audit_soc_report_deepplinks
known_issues: []
row_count: 2
proposed_fields:
- grain
- primary_key
reviewed: false
---

# vw_audit_soc_report_deepplinks

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Name` | string |  |  | `Name` |
| `Link` | string |  |  | `Link` |
| `source_file_name` | string |  |  | `source_file_name` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**Name**
- `Request Bridge Letter`: 1 rows
- `Download SOC 1 report`: 1 rows

**Link**
- `https://kpmgus.sharepoint.com/sites/US-Digital_Finance_and_AI/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FUS...`: 1 rows

**source_file_name**
- `audit_soc_report_deeplinks.csv`: 2 rows

**MDP_CREATED_DATE**
- `2026-11-04 10:51:15.137620+00:00`: 2 rows

**MDP_MODIFIED_DATE**
- `2026-11-04 10:51:15.137620+00:00`: 2 rows

## Profile

Rows in the latest export: 2.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Name` | STRING | 2 | 0 | Download SOC 1 report | Request Bridge Letter |
| `Link` | STRING | 2 | 0 | https://kpmgus.sharepoint.com/sites/U... | https://kpmgus.sharepoint.com/sites/U... |
| `source_file_name` | STRING | 1 | 0 | audit_soc_report_deeplinks.csv | audit_soc_report_deeplinks.csv |
| `HASH_KEY` | STRING | 2 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-04 10:51:15.138000 | 2026-11-04 10:51:15.138000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-04 10:51:15.138000 | 2026-11-04 10:51:15.138000 |

## Sample rows

| Name | Link | source_file_name | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|
| Request Bridge Letter | https://kpmgus.sharepoint.com/sites/U... | audit_soc_report_deeplinks.csv | <masked> | 2026-11-04 10:51:15.138000 | <masked> | 2026-11-04 10:51:15.138000 |
| Download SOC 1 report | https://kpmgus.sharepoint.com/sites/U... | audit_soc_report_deeplinks.csv | <masked> | 2026-11-04 10:51:15.138000 | <masked> | 2026-11-04 10:51:15.138000 |
