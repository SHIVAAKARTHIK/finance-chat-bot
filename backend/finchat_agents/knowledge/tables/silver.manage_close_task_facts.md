---
name: manage_close_task_facts
schema: silver
layer: silver
domain: recon
type: table
status: active
purpose: Close tasks with status and preparer used by the Manage the Close screen.
grain: one row per HASH_KEY (one close task)
primary_key:
- HASH_KEY
entity_column: CompanyKey
period_columns: []
pii_columns:
- TaskPreparer
- TaskPreparedByUsername
- TaskLastApprovedByUsername
- TaskAddedByUsername
- MDP_CREATED_BY
- MDP_MODIFIED_BY
- TaskPreparerName
- TaskApprover
- TaskApproverName
- TaskPreparedByName
- TaskLastApprovedByName
- TaskAddedByName
synonyms: []
built_from:
- adra_tasks_task_facts (likely)
known_issues: []
proposed_fields:
- grain
- primary_key
reviewed:
- superseded_by
superseded_by:
- silver.adra_tasks_task_facts
---

# manage_close_task_facts

> Superseded: this table is a copy of ADRA data. Answers use the source of truth `silver.adra_tasks_task_facts` (decision 21 Nov 2026).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `TaskKey` | long |  |  | `TaskKey` |
| `EngagementKey` | string |  |  | `EngagementKey` |
| `CompanyKey` | int |  |  | `CompanyKey` |
| `DepartmentKey` | int |  |  | `DepartmentKey` |
| `FrequencyKey` | int |  |  | `FrequencyKey` |
| `ExtraFieldsKey` | long |  |  | `ExtraFieldsKey` |
| `TaskListKey` | int |  |  | `TaskListKey` |
| `TaskSettingsKey` | long |  |  | `TaskSettingsKey` |
| `TeamKey` | int |  |  | `TeamKey` |
| `TaskId` | long |  |  | `TaskId` |
| `TaskCheckListItemFactKey` | long |  |  | `TaskCheckListItemFactKey` |
| `TaskPreparer` | string |  |  | `TaskPreparer` |
| `TaskPreparerName` | string |  |  | `TaskPreparerName` |
| `TaskApprover` | string |  |  | `TaskApprover` |
| `TaskApproverName` | string |  |  | `TaskApproverName` |
| `TaskStatus` | string |  |  | `TaskStatus` |
| `TaskApprovalStatus` | string |  |  | `TaskApprovalStatus` |
| `TaskIsFinalized` | boolean |  |  | `TaskIsFinalized` |
| `TaskFinalized` | timestamp |  |  | `TaskFinalized` |
| `TaskDueDateTime` | timestamp |  |  | `TaskDueDateTime` |
| `TaskReminderDateTime` | timestamp |  |  | `TaskReminderDateTime` |
| `TaskPreparedByName` | string |  |  | `TaskPreparedByName` |
| `TaskPreparedByUsername` | string |  |  | `TaskPreparedByUsername` |
| `TaskPreparedDateTime` | timestamp |  |  | `TaskPreparedDateTime` |
| `TaskLastApprovedByName` | string |  |  | `TaskLastApprovedByName` |
| `TaskLastApprovedByUsername` | string |  |  | `TaskLastApprovedByUsername` |
| `TaskApprovedDateTime` | timestamp |  |  | `TaskApprovedDateTime` |
| `TaskNumberOfRejects` | int |  |  | `TaskNumberOfRejects` |
| `TaskAddedByName` | string |  |  | `TaskAddedByName` |
| `TaskAddedByUsername` | string |  |  | `TaskAddedByUsername` |
| `TaskAddedDateTime` | timestamp |  |  | `TaskAddedDateTime` |
| `PrecedingTasks` | int |  |  | `PrecedingTasks` |
| `SucceedingTasks` | int |  |  | `SucceedingTasks` |
| `NotFinalizedPrecedingTasks` | int |  |  | `NotFinalizedPrecedingTasks` |
| `NotFinalizedSucceedingTasks` | int |  |  | `NotFinalizedSucceedingTasks` |
| `TaskActualCompletionTime` | int |  |  | `TaskActualCompletionTime` |
| `TaskNumberOfAttachments` | int |  |  | `TaskNumberOfAttachments` |
| `TaskIsChecklist` | boolean |  |  | `TaskIsChecklist` |
| `TaskChecklistCompleteness` | int |  |  | `TaskChecklistCompleteness` |
| `OffsetZeroDays` | int |  |  | `OffsetZeroDays` |
| `TaskLink` | string |  |  | `TaskLink` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**EngagementKey**
- `949e65cb-7216-4cb5-9840-4bc138a1921b`

**DepartmentKey**
- `2455`
- `2454`
- `2453`
- `2457`
- `2456`
- `2458`
- `2459`

**FrequencyKey**
- `2`
- `1`

**TaskListKey**
- `16388`
- `None`
- `16387`
- `16386`

**TeamKey**
- `2330`
- `2331`
- `2332`

**TaskStatus**
- `Prepared`
- `Not Started`
- `Closed`
- `Approved`

**TaskApprovalStatus**
- `Not approved`
- `Approval not needed`
- `Approved`

**TaskIsFinalized**
- `True`
- `False`

**TaskFinalized**
- `None`
- `2026-10-19 07:47:59.521671+00:00`
- `2026-10-23 06:08:17.756128+00:00`
- `2026-10-19 07:48:42.792601+00:00`
- `2026-10-23 06:10:28.653271+00:00`
- `2026-10-23 06:19:10.375264+00:00`
- `2026-10-23 06:08:32.402352+00:00`
- `2026-10-19 07:48:26.073347+00:00`
- `2026-10-23 06:17:36.643039+00:00`
- `2026-10-19 07:48:06.355993+00:00`
- `2026-10-23 06:09:39.303061+00:00`
- `2026-10-23 06:04:35.663965+00:00`
- `2026-10-23 06:13:28.880451+00:00`
- `2026-10-19 07:48:34.583791+00:00`
- `2026-10-23 06:16:33.360198+00:00`
- `2026-10-19 08:59:13.696122+00:00`
- `2026-10-23 06:18:25.402951+00:00`
- `2026-10-23 06:05:07.036077+00:00`
- `2026-10-22 09:03:18.932988+00:00`
- `2026-10-23 06:12:25.848743+00:00`
- `2026-10-23 06:17:11.541181+00:00`
- `2026-10-23 06:11:21.113126+00:00`
- `2026-10-23 06:08:04.181476+00:00`
- `2026-10-23 06:10:02.975586+00:00`
- `2026-10-23 06:06:01.963658+00:00`
- `2026-10-22 09:03:13.855989+00:00`
- `2026-10-19 07:47:50.390140+00:00`
- `2026-10-19 07:38:10.561285+00:00`
- `2026-10-19 07:48:58.647491+00:00`
- `2026-10-19 07:48:49.309005+00:00`
- `2026-10-23 06:05:21.467636+00:00`
- `2026-10-23 06:10:56.245746+00:00`
- `2026-10-19 09:45:07.418317+00:00`
- `2026-10-23 06:05:47.779027+00:00`
- `2026-10-23 06:15:00.263443+00:00`

**TaskDueDateTime**
- `2026-11-03 10:30:00+00:00`
- `2026-11-04 10:30:00+00:00`
- `2026-11-03 22:00:00+00:00`
- `2026-11-07 05:30:00+00:00`
- `2026-11-11 10:30:00+00:00`
- `2026-10-27 06:30:00+00:00`
- `2026-10-23 06:30:00+00:00`
- `2026-10-25 06:30:00+00:00`
- `2026-10-24 06:30:00+00:00`
- `2026-10-26 06:30:00+00:00`
- `2026-11-06 10:30:00+00:00`
- `2026-11-06 22:00:00+00:00`
- `2026-11-07 04:30:00+00:00`
- `2026-11-11 22:00:00+00:00`
- `2026-11-04 22:00:00+00:00`
- `2026-10-29 08:30:00+00:00`
- `2026-11-06 08:30:00+00:00`
- `2026-11-05 10:30:00+00:00`
- `2026-11-07 10:30:00+00:00`
- `2026-11-06 04:30:00+00:00`
- `2026-10-31 00:30:00+00:00`
- `2026-11-07 22:00:00+00:00`
- `2026-10-24 08:30:00+00:00`

**TaskReminderDateTime**
- `2026-11-03 10:30:00+00:00`
- `None`
- `2026-11-03 22:00:00+00:00`
- `2026-11-04 10:30:00+00:00`
- `2026-10-25 06:30:00+00:00`
- `2026-11-07 05:30:00+00:00`
- `2026-10-23 06:30:00+00:00`
- `2026-10-27 06:30:00+00:00`
- `2026-10-26 06:30:00+00:00`
- `2026-11-11 10:30:00+00:00`
- `2026-10-24 06:30:00+00:00`
- `2026-11-06 10:30:00+00:00`
- `2026-11-06 22:00:00+00:00`
- `2026-11-05 10:30:00+00:00`
- `2026-11-11 22:00:00+00:00`
- `2026-11-04 22:00:00+00:00`
- `2026-11-07 10:30:00+00:00`
- `2026-11-07 22:00:00+00:00`
- `2026-10-29 08:30:00+00:00`
- `2026-10-24 08:30:00+00:00`

**TaskPreparedDateTime**
- `None`
- `2026-10-23 06:12:25.846282+00:00`
- `2026-10-23 06:11:21.110686+00:00`
- `2026-10-23 06:18:25.400616+00:00`
- `2026-10-23 06:08:32.400202+00:00`
- `2026-10-23 06:15:00.260834+00:00`
- `2026-10-23 06:10:56.242874+00:00`
- `2026-10-23 06:09:39.300390+00:00`
- `2026-10-19 09:45:56.984583+00:00`
- `2026-10-19 08:59:13.693953+00:00`
- `2026-10-23 06:05:47.776389+00:00`
- `2026-10-23 06:04:35.661238+00:00`
- `2026-10-23 06:05:07.028445+00:00`
- `2026-10-23 06:06:01.961418+00:00`
- `2026-10-23 06:08:17.753732+00:00`
- `2026-10-23 06:10:02.973364+00:00`
- `2026-10-23 06:08:04.177247+00:00`
- `2026-10-19 08:58:30.718948+00:00`
- `2026-10-23 06:16:33.354914+00:00`
- `2026-10-23 06:17:36.640500+00:00`
- `2026-10-19 09:45:07.412497+00:00`
- `2026-10-23 06:10:28.650280+00:00`
- `2026-10-23 06:05:21.465422+00:00`
- `2026-10-23 06:19:09.758251+00:00`
- `2026-10-23 06:13:28.878092+00:00`
- `2026-10-23 06:17:11.537041+00:00`

**TaskApprovedDateTime**
- `None`
- `2026-10-22 09:03:18.930817+00:00`
- `2026-10-22 09:03:13.853852+00:00`

**TaskNumberOfRejects**
- `0`

**TaskAddedDateTime**
- `2026-10-19 07:59:31.331936+00:00`
- `2026-10-22 10:42:52.675378+00:00`
- `2026-10-19 07:59:31.331941+00:00`
- `2026-10-22 10:37:00.071732+00:00`
- `2026-10-22 10:40:27.478559+00:00`
- `2026-10-19 07:59:31.331938+00:00`
- `2026-10-19 07:59:31.331942+00:00`
- `2026-10-19 07:59:31.331935+00:00`
- `2026-10-17 16:01:20.914305+00:00`
- `2026-10-19 07:59:31.331937+00:00`
- `2026-10-19 07:59:31.331939+00:00`
- `2026-10-19 07:59:31.331940+00:00`
- `2026-10-19 07:59:31.331934+00:00`
- `2026-10-17 16:01:20.914306+00:00`
- `2026-10-22 09:15:10.899523+00:00`
- `2026-10-17 15:59:24.404039+00:00`
- `2026-10-22 10:42:52.675376+00:00`
- `2026-10-17 15:59:24.404041+00:00`
- `2026-10-19 07:59:31.331931+00:00`
- `2026-10-17 15:59:24.404042+00:00`
- `2026-10-19 07:59:31.331943+00:00`
- `2026-10-17 16:01:20.914303+00:00`
- `2026-10-19 08:52:49.585445+00:00`
- `2026-10-22 10:37:00.071730+00:00`
- `2026-10-19 07:02:28.303094+00:00`
- `2026-10-22 10:40:27.478557+00:00`

**PrecedingTasks**
- `0`
- `1`

**SucceedingTasks**
- `0`
- `1`

**NotFinalizedPrecedingTasks**
- `0`

**NotFinalizedSucceedingTasks**
- `0`
- `1`

**TaskActualCompletionTime**
- `0`

**TaskNumberOfAttachments**
- `0`

**TaskIsChecklist**
- `False`

**TaskChecklistCompleteness**
- `0`

**OffsetZeroDays**
- `0`
- `1`
- `5`
- `4`
- `2`
- `7`
- `-2`
- `3`
- `-5`

**MDP_CREATED_DATE**
- `2026-10-23 10:51:27.606140+00:00`

**MDP_MODIFIED_DATE**
- `2026-10-23 10:51:27.606140+00:00`
