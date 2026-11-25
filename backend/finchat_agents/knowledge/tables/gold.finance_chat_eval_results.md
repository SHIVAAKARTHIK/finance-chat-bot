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
row_count: 0
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

## Profile

Rows in the latest export: 0.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `run_id` | STRING | 0 | 0 |  |  |
| `test_case_id` | STRING | 0 | 0 |  |  |
| `implementation` | STRING | 0 | 0 |  |  |
| `application_version` | STRING | 0 | 0 |  |  |
| `planner_version` | STRING | 0 | 0 |  |  |
| `executed_at` | TIMESTAMP | 0 | 0 |  |  |
| `actual_behavior` | STRING | 0 | 0 |  |  |
| `actual_resolved_question` | STRING | 0 | 0 |  |  |
| `actual_category` | STRING | 0 | 0 |  |  |
| `actual_metric` | STRING | 0 | 0 |  |  |
| `actual_dimension` | STRING | 0 | 0 |  |  |
| `actual_period` | STRING | 0 | 0 |  |  |
| `actual_source` | STRING | 0 | 0 |  |  |
| `actual_sql` | STRING | 0 | 0 |  |  |
| `sql_execution_status` | STRING | 0 | 0 |  |  |
| `actual_result` | STRING | 0 | 0 |  |  |
| `actual_answer` | STRING | 0 | 0 |  |  |
| `clarification_triggered` | BOOLEAN | 0 | 0 |  |  |
| `actual_clarification_question` | STRING | 0 | 0 |  |  |
| `abstention_triggered` | BOOLEAN | 0 | 0 |  |  |
| `authorization_outcome` | STRING | 0 | 0 |  |  |
| `planner_latency_ms` | LONG | 0 | 0 |  |  |
| `sql_generation_latency_ms` | LONG | 0 | 0 |  |  |
| `data_execution_latency_ms` | LONG | 0 | 0 |  |  |
| `response_latency_ms` | LONG | 0 | 0 |  |  |
| `total_latency_ms` | LONG | 0 | 0 |  |  |
| `error_type` | STRING | 0 | 0 |  |  |
| `error_message` | STRING | 0 | 0 |  |  |
| `result_accuracy_pass` | BOOLEAN | 0 | 0 |  |  |
| `financial_semantics_pass` | BOOLEAN | 0 | 0 |  |  |
| `followup_context_pass` | BOOLEAN | 0 | 0 |  |  |
| `clarification_accuracy_pass` | BOOLEAN | 0 | 0 |  |  |
| `clarification_resolution_pass` | BOOLEAN | 0 | 0 |  |  |
| `abstention_pass` | BOOLEAN | 0 | 0 |  |  |
| `faithfulness_pass` | BOOLEAN | 0 | 0 |  |  |
| `authorization_safety_pass` | BOOLEAN | 0 | 0 |  |  |
| `overall_test_status` | STRING | 0 | 0 |  |  |
| `failure_reason` | STRING | 0 | 0 |  |  |
