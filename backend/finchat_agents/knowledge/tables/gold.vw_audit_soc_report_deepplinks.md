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
- `Request Bridge Letter`
- `Download SOC 1 report`

**Link**
- `https://kpmgus.sharepoint.com/sites/US-Digital_Finance_and_AI/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FUS...`

**source_file_name**
- `audit_soc_report_deeplinks.csv`

**MDP_CREATED_DATE**
- `2026-11-04 10:51:15.137620+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-04 10:51:15.137620+00:00`
