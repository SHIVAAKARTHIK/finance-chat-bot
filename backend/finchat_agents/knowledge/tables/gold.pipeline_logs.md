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
row_count: 870
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
- `B1_3_1_PL_FILES_TRANSFER_TO_AAH_INBOUND`: 174 rows
- `B1_4_1_PL_AAH_OUTBOUND_TO_ADLS`: 174 rows
- `B1_2_1_PL_ANOMALY_DETECTION`: 174 rows
- `B1_5_1_AAH_D365_DATA_LOADING`: 174 rows
- `B1_1_1_PL_DATA_INGEST_FROM_SFTP_CLIENT_TO_ABS_MDP`: 174 rows

**Source_System**
- `Concur`: 315 rows
- `Novidea`: 207 rows
- `D365`: 174 rows
- `Fynapse`: 174 rows

**Status**
- `Completed`: 866 rows
- `Failed`: 4 rows

**Reason**
- `None`: 866 rows
- `File transfer to the AAH inbound location failed due to a destination connectivity timeout`: 1 rows
- `Copy activity failed while reading the source file for anomaly detection`: 1 rows
- `Data loading to Dynamics 365 failed due to invalid or missing mandatory field values`: 1 rows
- `Authentication or authorization failed while reading the source file from the client SFTP location`: 1 rows

**MDP_CREATED_DATE**
- `2026-11-06 04:53:40.639754+00:00`: 870 rows

**MDP_MODIFIED_DATE**
- `2026-11-06 04:53:40.639754+00:00`: 870 rows

## Profile

Rows in the latest export: 870.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Process_ID` | STRING | 841 | 0 | R-1001 | R-1870 |
| `Pipeline_Name` | STRING | 5 | 0 | B1_1_1_PL_DATA_INGEST_FROM_SFTP_CLIEN... | B1_5_1_AAH_D365_DATA_LOADING |
| `Source_System` | STRING | 4 | 0 | Concur | Novidea |
| `Execution_Date` | TIMESTAMP | 873 | 0 | 2026-07-22 00:04:00 | 2026-10-22 20:58:00 |
| `Source_File_Name` | STRING | 873 | 0 | AAH_INBOUND_R-1003.csv | D365_LOAD_R-1870.csv |
| `Status` | STRING | 2 | 0 | Completed | Failed |
| `Reason` | STRING | 3 | 866 | Authentication or authorization faile... | File transfer to the AAH inbound loca... |
| `HASH_KEY` | STRING | 907 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-06 04:53:40.640000 | 2026-11-06 04:53:40.640000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-06 04:53:40.640000 | 2026-11-06 04:53:40.640000 |

## Sample rows

| Process_ID | Pipeline_Name | Source_System | Execution_Date | Source_File_Name | Status | Reason | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|
| R-1325 | B1_5_1_AAH_D365_DATA_LOADING | Fynapse | 2026-07-22 00:04:00 | D365_LOAD_R-1325.csv | Completed | NULL | <masked> | 2026-11-06 04:53:40.640000 | <masked> | 2026-11-06 04:53:40.640000 |
| R-1139 | B1_4_1_PL_AAH_OUTBOUND_TO_ADLS | D365 | 2026-07-22 03:10:00 | AAH_OUTBOUND_R-1139.csv | Completed | NULL | <masked> | 2026-11-06 04:53:40.640000 | <masked> | 2026-11-06 04:53:40.640000 |
| R-1714 | B1_4_1_PL_AAH_OUTBOUND_TO_ADLS | D365 | 2026-07-22 05:35:00 | AAH_OUTBOUND_R-1714.csv | Completed | NULL | <masked> | 2026-11-06 04:53:40.640000 | <masked> | 2026-11-06 04:53:40.640000 |
| R-1528 | B1_3_1_PL_FILES_TRANSFER_TO_AAH_INBOUND | Concur | 2026-07-22 08:41:00 | AAH_INBOUND_R-1528.csv | Completed | NULL | <masked> | 2026-11-06 04:53:40.640000 | <masked> | 2026-11-06 04:53:40.640000 |
| R-1342 | B1_2_1_PL_ANOMALY_DETECTION | Concur | 2026-07-22 11:47:00 | ANOMALY_R-1342.csv | Completed | NULL | <masked> | 2026-11-06 04:53:40.640000 | <masked> | 2026-11-06 04:53:40.640000 |
