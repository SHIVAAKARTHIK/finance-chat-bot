-- Summary agent cards (task 09). Target: lakehouse_mvpai.aiops. Same conventions as finance_chat_memory_delta.sql:
-- UUID strings from the app, CHECK constraints instead of enums, informational primary keys (write with MERGE),
-- no defaults (the app sets every value). NOT TESTED on Databricks: run each statement and fix any error.

-- 1. One row per scheduled run
CREATE TABLE IF NOT EXISTS lakehouse_mvpai.aiops.finance_chat_summary_runs (
  run_id              STRING    NOT NULL COMMENT 'UUID',
  trigger_type        STRING    NOT NULL COMMENT 'schedule | manual',
  status              STRING    NOT NULL COMMENT 'running | succeeded | partial | failed',
  domains             ARRAY<STRING> COMMENT 'Domains processed in this run',
  cards_created       INT       NOT NULL,
  cards_flagged       INT       NOT NULL COMMENT 'Big changes sent to the investigator',
  llm_call_count      INT       NOT NULL,
  input_tokens        INT       NOT NULL,
  output_tokens       INT       NOT NULL,
  error_message       STRING,
  started_at          TIMESTAMP NOT NULL,
  completed_at        TIMESTAMP,
  CONSTRAINT pk_finance_chat_summary_runs PRIMARY KEY (run_id)
)
USING DELTA
CLUSTER BY (started_at)
COMMENT 'One row per summary agent run';

ALTER TABLE lakehouse_mvpai.aiops.finance_chat_summary_runs
  ADD CONSTRAINT chk_sum_run_status CHECK (status IN ('running', 'succeeded', 'partial', 'failed'));
ALTER TABLE lakehouse_mvpai.aiops.finance_chat_summary_runs
  ADD CONSTRAINT chk_sum_run_trigger CHECK (trigger_type IN ('schedule', 'manual'));

-- 2. One row per card
CREATE TABLE IF NOT EXISTS lakehouse_mvpai.aiops.finance_chat_summary_cards (
  card_id             STRING    NOT NULL COMMENT 'UUID',
  run_id              STRING    NOT NULL COMMENT 'Refers to finance_chat_summary_runs',
  domain              STRING    NOT NULL COMMENT 'recon | subledger | fa | ar | ap | gl | cash (viewer sees only their role domains)',
  card_type           STRING    NOT NULL COMMENT 'key_change | status | highlight',
  rank                SMALLINT  NOT NULL COMMENT '1 = most important within the run and domain',
  period_label        STRING    COMMENT 'e.g. Oct 26, FY2026 P9',
  comparison_label    STRING    COMMENT 'e.g. vs Sep 26',
  metric_name         STRING    NOT NULL COMMENT 'Business name of the measure',
  source_tables       ARRAY<STRING> COMMENT 'Tables the fact came from',
  current_value       DECIMAL(38,6),
  previous_value      DECIMAL(38,6),
  change_abs          DECIMAL(38,6),
  change_pct          DECIMAL(18,6),
  is_flagged          BOOLEAN   NOT NULL COMMENT 'Big change: investigator ran',
  title               STRING    NOT NULL COMMENT 'Short card title',
  card_text           STRING    NOT NULL COMMENT 'Card body written by the response model from the facts',
  explanation         STRING    COMMENT 'Investigator explanation, or "no cause found in 2 queries"',
  explanation_status  STRING    COMMENT 'explained | no_cause_found | not_flagged | failed',
  investigator_sql    ARRAY<STRING> COMMENT 'Audit only, never shown to users (max 2)',
  status              STRING    NOT NULL COMMENT 'active | superseded | hidden',
  created_at          TIMESTAMP NOT NULL,
  CONSTRAINT pk_finance_chat_summary_cards PRIMARY KEY (card_id)
)
USING DELTA
CLUSTER BY (domain, created_at)
COMMENT 'Summary agent cards; filtered by viewer role domains at display time';

ALTER TABLE lakehouse_mvpai.aiops.finance_chat_summary_cards
  ADD CONSTRAINT chk_card_status CHECK (status IN ('active', 'superseded', 'hidden'));
ALTER TABLE lakehouse_mvpai.aiops.finance_chat_summary_cards
  ADD CONSTRAINT chk_card_type CHECK (card_type IN ('key_change', 'status', 'highlight'));
ALTER TABLE lakehouse_mvpai.aiops.finance_chat_summary_cards
  ADD CONSTRAINT chk_card_expl CHECK (explanation_status IS NULL OR explanation_status IN
    ('explained', 'no_cause_found', 'not_flagged', 'failed'));

-- Typical read (UI): latest active cards for the viewer's domains
--   SELECT * FROM lakehouse_mvpai.aiops.finance_chat_summary_cards
--    WHERE status = 'active' AND domain IN (:domains)
--    ORDER BY domain, rank LIMIT 20;
