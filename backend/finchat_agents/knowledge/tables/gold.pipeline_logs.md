---
name: pipeline_logs
schema: gold
layer: gold
domain: null
type: table
status: active
purpose: Records pipeline executions; source files; outcomes and failure reasons.
grain: one row per Process_ID (one pipeline execution)
primary_key:
- Process_ID
entity_column: null
period_columns:
- Execution_Date
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

# pipeline_logs

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Process_ID` | string |  |  | `Process_ID` |
| `Pipeline_Name` | string |  |  | `Pipeline_Name` |
| `Source_System` | string |  |  | `Source_System` |
| `Execution_Date` | timestamp |  |  | `Execution_Date` |
| `Source_File_Name` | string |  |  | `Source_File_Name` |
| `Status` | string |  |  | `Status` |
| `Reason` | string |  |  | `Reason` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**Pipeline_Name**
- `B1_3_1_PL_FILES_TRANSFER_TO_AAH_INBOUND`
- `B1_4_1_PL_AAH_OUTBOUND_TO_ADLS`
- `B1_2_1_PL_ANOMALY_DETECTION`
- `B1_5_1_AAH_D365_DATA_LOADING`
- `B1_1_1_PL_DATA_INGEST_FROM_SFTP_CLIENT_TO_ABS_MDP`

**Source_System**
- `Concur`
- `Novidea`
- `D365`
- `Fynapse`

**Status**
- `Completed`
- `Failed`

**Reason**
- `None`
- `File transfer to the AAH inbound location failed due to a destination connectivity timeout`
- `Copy activity failed while reading the source file for anomaly detection`
- `Data loading to Dynamics 365 failed due to invalid or missing mandatory field values`
- `Authentication or authorization failed while reading the source file from the client SFTP location`

**MDP_CREATED_DATE**
- `2026-11-06 04:53:40.639754+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-06 04:53:40.639754+00:00`
