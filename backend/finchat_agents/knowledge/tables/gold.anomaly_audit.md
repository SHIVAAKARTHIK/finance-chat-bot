---
name: anomaly_audit
schema: gold
layer: gold
domain: null
type: table
status: active
purpose: Flags anomalies in insurance and expense transactions for data-quality review.
grain: one row per HASH_KEY (one flagged or evaluated source transaction)
primary_key:
- HASH_KEY
entity_column: null
period_columns:
- TRANSACTION_DATE
- ACCOUNTING_DATE
- EFFECTIVE_DATE
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

# anomaly_audit

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `SOURCE_SYSTEM_ID` | string |  |  | `SOURCE_SYSTEM_ID` |
| `TRANSACTION_REFERENCE_NO` | string |  |  | `TRANSACTION_REFERENCE_NO` |
| `POLICY_VERSION` | string |  |  | `POLICY_VERSION` |
| `RISK_UNIQUE_ID` | string |  |  | `RISK_UNIQUE_ID` |
| `COVERAGE_NUMBER` | string |  |  | `COVERAGE_NUMBER` |
| `TRANSACTION_DATE` | date |  |  | `TRANSACTION_DATE` |
| `SEQUENCE` | int |  |  | `SEQUENCE` |
| `ACCOUNTING_DATE` | date |  |  | `ACCOUNTING_DATE` |
| `EFFECTIVE_DATE` | date |  |  | `EFFECTIVE_DATE` |
| `BUSINESS_EVENT` | string |  |  | `BUSINESS_EVENT` |
| `BUSINESS_SUB_EVENT` | string |  |  | `BUSINESS_SUB_EVENT` |
| `PERCENT_EARNED_INCEPTION` | int |  |  | `PERCENT_EARNED_INCEPTION` |
| `AMOUNT` | decimal |  |  | `AMOUNT` |
| `COMMISSION_AMOUNT` | decimal |  |  | `COMMISSION_AMOUNT` |
| `TERM_AMOUNT` | decimal |  |  | `TERM_AMOUNT` |
| `COMMISSION_RATE` | decimal |  |  | `COMMISSION_RATE` |
| `ITEM_CODE` | string |  |  | `ITEM_CODE` |
| `RATE_CATEGORY` | string |  |  | `RATE_CATEGORY` |
| `CLASS_CODE` | int |  |  | `CLASS_CODE` |
| `OPERATOR_UNIQUE_ID` | string |  |  | `OPERATOR_UNIQUE_ID` |
| `source_file_name` | string |  |  | `source_file_name` |
| `timestamp` | date |  |  | `timestamp` |
| `DQ_RULE` | string |  |  | `DQ_RULE` |
| `anomaly_type` | string |  |  | `anomaly_type` |
| `anomaly_flag` | string |  |  | `anomaly_flag` |
| `ANOMALY_AMOUNT` | decimal |  |  | `ANOMALY_AMOUNT` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**SOURCE_SYSTEM_ID**
- `RPM`
- `Concur`
- `Novidea`

**TRANSACTION_REFERENCE_NO**
- `G021920821-202609-66309080-TEST23`
- `W031522657-202609-66315498-TEST21`
- `W031251681-202609-66312585-TEST20`
- `W021687062-202609-66307553-TEST18`
- `W031251681-202609-66312585-TEST24`
- `W021687062-202609-66307553-TEST22`
- `W023699378-202609-66312437-TEST01`
- `G021920821-202609-66309080-TEST19`
- `W031522657-202609-66315498-TEST17`
- `W027006975-202609-66309787-TEST04`
- `W031515581-202609-66311238-TEST08`
- `G031533211-202609-66313529-TEST11`
- `W031520697-202609-66311133-TEST07`
- `W021687062-202609-66307553-TEST13`
- `W031475966-202609-66310430-TEST06`
- `G021920821-202609-66309080-TEST14`
- `None`
- `W013362694-202609-66307916-TEST03`
- `W025943118-202609-66312992-TEST10`
- `W031522657-202609-66315498-TEST12`
- `W031532495-202609-66311425-TEST09`
- `W031251681-202609-66312585-TEST15`

**POLICY_VERSION**
- `G021920821-2026/09/18`
- `W021687062-2026/08/14`
- `W031251681-2026/09/21`
- `W031522657-2026/09/18`
- `W023699378-2026/03/20`
- `W031532495-2026/09/18`
- `W031439765-2026/09/14`
- `W031475966-2026/09/18`
- `G031533211-2026/09/25`
- `W027006975-2025/11/25`
- `W025943118-2025/08/25`
- `W013362694-2026/09/17`
- `W031520697-2026/09/18`
- `W031515581-2026/09/18`

**RISK_UNIQUE_ID**
- `W031251681`
- `W021687062`
- `G021920821`
- `W031522657`
- `W023699378`
- `W031475966`
- `W027006975`
- `G031533211`
- `W013362694`
- `W025943118`
- `W031439765`
- `W031520697`
- `W031532495`
- `W031515581`

**COVERAGE_NUMBER**
- `W031251681-410-W02`
- `W021687062-421-W03`
- `G021920821-FLF-G03`
- `W031522657-SC2-W01`
- `W023699378-480-W02`
- `W025943118-410-W02`
- `G031533211-FLL-G03`
- `None`
- `W027006975-421-W03`
- `W031532495-EMP-W03`
- `W031515581-410-W02`
- `W031439765-EMP-W03`
- `W013362694-FG4-W03`
- `W031520697-SC2-W02`

**TRANSACTION_DATE**
- `2026-09-18 00:00:00`
- `2026-09-02 00:00:00`
- `2026-08-04 00:00:00`
- `2026-07-26 00:00:00`
- `2026-09-17 00:00:00`
- `2026-09-01 00:00:00`
- `None`

**SEQUENCE**
- `1`
- `2`
- `4`
- `5`
- `3`

**ACCOUNTING_DATE**
- `2026-09-01 00:00:00`
- `None`

**EFFECTIVE_DATE**
- `2026-09-18 00:00:00`
- `2026-08-14 00:00:00`
- `2026-09-21 00:00:00`
- `2026-09-14 00:00:00`
- `2026-10-01 00:00:00`
- `2026-09-17 00:00:00`
- `2026-09-12 00:00:00`
- `None`
- `2026-01-06 00:00:00`

**BUSINESS_EVENT**
- `FS`
- `NB`
- `RB`
- `CM`

**BUSINESS_SUB_EVENT**
- `RPM-A`
- `RPM-SC2`
- `RPM-R`
- `RPM-FLF`
- `RPM-X`
- `RPM-EMP`
- `RPM-FG4`
- `RPM-FLL`

**PERCENT_EARNED_INCEPTION**
- `0`
- `1`

**AMOUNT**
- `31`
- `34`
- `33`
- `32`
- `480`
- `0`
- `120`
- `300`
- `100`
- `230`
- `920`
- `1000`
- `110`

**COMMISSION_AMOUNT**
- `0`
- `151.6`
- `None`
- `-6`
- `-3.5`
- `1.12`
- `-68.1`

**TERM_AMOUNT**
- `0`
- `1516`
- `143.5`
- `0.01`
- `-98`
- `14`
- `-2`
- `2`
- `66.69`
- `-171`
- `-717`
- `115.6`
- `0.18`

**COMMISSION_RATE**
- `0`
- `0.1`
- `0.11`
- `0.12`
- `0.15`
- `0.08`
- `0.13`

**ITEM_CODE**
- `001FIREC`
- `SURPLUS`
- `001FSLSOFE`
- `001ALLIED1`
- `001EMPATFEE02`
- `001LIAB`
- `001FIGA23`
- `001SURPLUS`
- `001FIRE1`
- `001FSLSO`
- `001ALLIEDC`

**RATE_CATEGORY**
- `None`

**CLASS_CODE**
- `None`
- `271`

**OPERATOR_UNIQUE_ID**
- `None`

**source_file_name**
- `policy_transaction.csv.csv`
- `Novidea_20260101_000000.csv`
- `Concur_20260101_000000.csv`

**timestamp**
- `2026-10-22 00:00:00`

**DQ_RULE**
- `None`
- `DQ05`
- `DQ09`
- `DQ03`
- `DQ02`
- `DQ01`
- `DQ04`

**anomaly_type**
- `None`
- `CURRENCY_CODE_NULL`
- `INVALID_GL_ACCOUNT_CODE`
- `MISSING_DATE_FIELD`
- `MISSING_MANDATORY_FIELD`
- `UNUSUAL_AMOUNT_OUTLIER`
- `DATE_VALIDATION_ISSUE`
- `DUPLICATE_RECORD`

**anomaly_flag**
- `Y`
- `N`

**ANOMALY_AMOUNT**
- `0`
- `31`
- `34`
- `32`
- `33`
- `120`
- `300`
- `1000`
- `100`
- `230`
- `12480`
- `920`
- `110`

**MDP_CREATED_DATE**
- `2026-11-06 04:53:40.964516+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-06 04:53:40.964516+00:00`

## Empty columns

Empty in every row: `RATE_CATEGORY`, `OPERATOR_UNIQUE_ID`. Do not filter or group on them.
