---
name: finance_chat_eval_results
schema: gold
layer: gold
domain: null
type: table
status: active
purpose: Stores finance-chat evaluation case outcomes; correctness checks and latency measurements.
grain: one row per evaluation test case execution
primary_key:
- run_id
- test_case_id
- executed_at
entity_column: null
period_columns:
- executed_at
pii_columns: []
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: table is empty (0 rows)
proposed_fields: []
reviewed: false
---

# finance_chat_eval_results

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `run_id` | string |  |  | `run_id` |
| `test_case_id` | string |  |  | `test_case_id` |
| `implementation` | string |  |  | `implementation` |
| `application_version` | string |  |  | `application_version` |
| `planner_version` | string |  |  | `planner_version` |
| `executed_at` | timestamp |  |  | `executed_at` |
| `actual_behavior` | string |  |  | `actual_behavior` |
| `actual_resolved_question` | string |  |  | `actual_resolved_question` |
| `actual_category` | string |  |  | `actual_category` |
| `actual_metric` | string |  |  | `actual_metric` |
| `actual_dimension` | string |  |  | `actual_dimension` |
| `actual_period` | string |  |  | `actual_period` |
| `actual_source` | string |  |  | `actual_source` |
| `actual_sql` | string |  |  | `actual_sql` |
| `sql_execution_status` | string |  |  | `sql_execution_status` |
| `actual_result` | string |  |  | `actual_result` |
| `actual_answer` | string |  |  | `actual_answer` |
| `clarification_triggered` | boolean |  |  | `clarification_triggered` |
| `actual_clarification_question` | string |  |  | `actual_clarification_question` |
| `abstention_triggered` | boolean |  |  | `abstention_triggered` |
| `authorization_outcome` | string |  |  | `authorization_outcome` |
| `planner_latency_ms` | long |  |  | `planner_latency_ms` |
| `sql_generation_latency_ms` | long |  |  | `sql_generation_latency_ms` |
| `data_execution_latency_ms` | long |  |  | `data_execution_latency_ms` |
| `response_latency_ms` | long |  |  | `response_latency_ms` |
| `total_latency_ms` | long |  |  | `total_latency_ms` |
| `error_type` | string |  |  | `error_type` |
| `error_message` | string |  |  | `error_message` |
| `result_accuracy_pass` | boolean |  |  | `result_accuracy_pass` |
| `financial_semantics_pass` | boolean |  |  | `financial_semantics_pass` |
| `followup_context_pass` | boolean |  |  | `followup_context_pass` |
| `clarification_accuracy_pass` | boolean |  |  | `clarification_accuracy_pass` |
| `clarification_resolution_pass` | boolean |  |  | `clarification_resolution_pass` |
| `abstention_pass` | boolean |  |  | `abstention_pass` |
| `faithfulness_pass` | boolean |  |  | `faithfulness_pass` |
| `authorization_safety_pass` | boolean |  |  | `authorization_safety_pass` |
| `overall_test_status` | string |  |  | `overall_test_status` |
| `failure_reason` | string |  |  | `failure_reason` |

## Empty columns

Empty in every row: `run_id`, `test_case_id`, `implementation`, `application_version`, `planner_version`, `executed_at`, `actual_behavior`, `actual_resolved_question`, `actual_category`, `actual_metric`, `actual_dimension`, `actual_period`, `actual_source`, `actual_sql`, `sql_execution_status`, `actual_result`, `actual_answer`, `clarification_triggered`, `actual_clarification_question`, `abstention_triggered`, `authorization_outcome`, `planner_latency_ms`, `sql_generation_latency_ms`, `data_execution_latency_ms`, `response_latency_ms`, `total_latency_ms`, `error_type`, `error_message`, `result_accuracy_pass`, `financial_semantics_pass`, `followup_context_pass`, `clarification_accuracy_pass`, `clarification_resolution_pass`, `abstention_pass`, `faithfulness_pass`, `authorization_safety_pass`, `overall_test_status`, `failure_reason`. Do not filter or group on them.
