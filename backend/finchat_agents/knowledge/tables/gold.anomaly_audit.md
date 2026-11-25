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
row_count: 31
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
- `RPM`: 15 rows
- `Concur`: 8 rows
- `Novidea`: 8 rows

**TRANSACTION_REFERENCE_NO**
- `G021920821-202609-66309080-TEST23`: 2 rows
- `W031522657-202609-66315498-TEST21`: 2 rows
- `W031251681-202609-66312585-TEST20`: 2 rows
- `W021687062-202609-66307553-TEST18`: 2 rows
- `W031251681-202609-66312585-TEST24`: 2 rows
- `W021687062-202609-66307553-TEST22`: 2 rows
- `W023699378-202609-66312437-TEST01`: 2 rows
- `G021920821-202609-66309080-TEST19`: 2 rows
- `W031522657-202609-66315498-TEST17`: 2 rows
- `W027006975-202609-66309787-TEST04`: 1 rows
- `W031515581-202609-66311238-TEST08`: 1 rows
- `G031533211-202609-66313529-TEST11`: 1 rows
- `W031520697-202609-66311133-TEST07`: 1 rows
- `W021687062-202609-66307553-TEST13`: 1 rows
- `W031475966-202609-66310430-TEST06`: 1 rows
- `G021920821-202609-66309080-TEST14`: 1 rows
- `None`: 1 rows
- `W013362694-202609-66307916-TEST03`: 1 rows
- `W025943118-202609-66312992-TEST10`: 1 rows
- `W031522657-202609-66315498-TEST12`: 1 rows
- `W031532495-202609-66311425-TEST09`: 1 rows
- `W031251681-202609-66312585-TEST15`: 1 rows

**POLICY_VERSION**
- `G021920821-2026/09/18`: 5 rows
- `W021687062-2026/08/14`: 5 rows
- `W031251681-2026/09/21`: 5 rows
- `W031522657-2026/09/18`: 5 rows
- `W023699378-2026/03/20`: 2 rows
- `W031532495-2026/09/18`: 1 rows
- `W031439765-2026/09/14`: 1 rows
- `W031475966-2026/09/18`: 1 rows
- `G031533211-2026/09/25`: 1 rows
- `W027006975-2025/11/25`: 1 rows
- `W025943118-2025/08/25`: 1 rows
- `W013362694-2026/09/17`: 1 rows
- `W031520697-2026/09/18`: 1 rows
- `W031515581-2026/09/18`: 1 rows

**RISK_UNIQUE_ID**
- `W031251681`: 5 rows
- `W021687062`: 5 rows
- `G021920821`: 5 rows
- `W031522657`: 5 rows
- `W023699378`: 2 rows
- `W031475966`: 1 rows
- `W027006975`: 1 rows
- `G031533211`: 1 rows
- `W013362694`: 1 rows
- `W025943118`: 1 rows
- `W031439765`: 1 rows
- `W031520697`: 1 rows
- `W031532495`: 1 rows
- `W031515581`: 1 rows

**COVERAGE_NUMBER**
- `W031251681-410-W02`: 5 rows
- `W021687062-421-W03`: 5 rows
- `G021920821-FLF-G03`: 5 rows
- `W031522657-SC2-W01`: 5 rows
- `W023699378-480-W02`: 2 rows
- `W025943118-410-W02`: 1 rows
- `G031533211-FLL-G03`: 1 rows
- `None`: 1 rows
- `W027006975-421-W03`: 1 rows
- `W031532495-EMP-W03`: 1 rows
- `W031515581-410-W02`: 1 rows
- `W031439765-EMP-W03`: 1 rows
- `W013362694-FG4-W03`: 1 rows
- `W031520697-SC2-W02`: 1 rows

**TRANSACTION_DATE**
- `2026-09-18 00:00:00`: 17 rows
- `2026-09-02 00:00:00`: 5 rows
- `2026-08-04 00:00:00`: 5 rows
- `2026-07-26 00:00:00`: 1 rows
- `2026-09-17 00:00:00`: 1 rows
- `2026-09-01 00:00:00`: 1 rows
- `None`: 1 rows

**SEQUENCE**
- `1`: 21 rows
- `2`: 6 rows
- `4`: 2 rows
- `5`: 1 rows
- `3`: 1 rows

**ACCOUNTING_DATE**
- `2026-09-01 00:00:00`: 29 rows
- `None`: 2 rows

**EFFECTIVE_DATE**
- `2026-09-18 00:00:00`: 13 rows
- `2026-08-14 00:00:00`: 5 rows
- `2026-09-21 00:00:00`: 5 rows
- `2026-09-14 00:00:00`: 3 rows
- `2026-10-01 00:00:00`: 1 rows
- `2026-09-17 00:00:00`: 1 rows
- `2026-09-12 00:00:00`: 1 rows
- `None`: 1 rows
- `2026-01-06 00:00:00`: 1 rows

**BUSINESS_EVENT**
- `FS`: 15 rows
- `NB`: 7 rows
- `RB`: 5 rows
- `CM`: 4 rows

**BUSINESS_SUB_EVENT**
- `RPM-A`: 7 rows
- `RPM-SC2`: 6 rows
- `RPM-R`: 5 rows
- `RPM-FLF`: 5 rows
- `RPM-X`: 4 rows
- `RPM-EMP`: 2 rows
- `RPM-FG4`: 1 rows
- `RPM-FLL`: 1 rows

**PERCENT_EARNED_INCEPTION**
- `0`: 24 rows
- `1`: 7 rows

**AMOUNT**
- `31`: 5 rows
- `34`: 5 rows
- `33`: 5 rows
- `32`: 5 rows
- `480`: 2 rows
- `0`: 2 rows
- `120`: 1 rows
- `300`: 1 rows
- `100`: 1 rows
- `230`: 1 rows
- `920`: 1 rows
- `1000`: 1 rows
- `110`: 1 rows

**COMMISSION_AMOUNT**
- `0`: 19 rows
- `151.6`: 5 rows
- `None`: 2 rows
- `-6`: 2 rows
- `-3.5`: 1 rows
- `1.12`: 1 rows
- `-68.1`: 1 rows

**TERM_AMOUNT**
- `0`: 6 rows
- `1516`: 5 rows
- `143.5`: 5 rows
- `0.01`: 5 rows
- `-98`: 2 rows
- `14`: 1 rows
- `-2`: 1 rows
- `2`: 1 rows
- `66.69`: 1 rows
- `-171`: 1 rows
- `-717`: 1 rows
- `115.6`: 1 rows
- `0.18`: 1 rows

**COMMISSION_RATE**
- `0`: 14 rows
- `0.1`: 6 rows
- `0.11`: 5 rows
- `0.12`: 2 rows
- `0.15`: 2 rows
- `0.08`: 1 rows
- `0.13`: 1 rows

**ITEM_CODE**
- `001FIREC`: 7 rows
- `SURPLUS`: 5 rows
- `001FSLSOFE`: 5 rows
- `001ALLIED1`: 5 rows
- `001EMPATFEE02`: 2 rows
- `001LIAB`: 2 rows
- `001FIGA23`: 1 rows
- `001SURPLUS`: 1 rows
- `001FIRE1`: 1 rows
- `001FSLSO`: 1 rows
- `001ALLIEDC`: 1 rows

**RATE_CATEGORY**
- `None`: 31 rows

**CLASS_CODE**
- `None`: 29 rows
- `271`: 2 rows

**OPERATOR_UNIQUE_ID**
- `None`: 31 rows

**source_file_name**
- `policy_transaction.csv.csv`: 15 rows
- `Novidea_20260101_000000.csv`: 8 rows
- `Concur_20260101_000000.csv`: 8 rows

**timestamp**
- `2026-10-22 00:00:00`: 31 rows

**DQ_RULE**
- `None`: 13 rows
- `DQ05`: 7 rows
- `DQ09`: 4 rows
- `DQ03`: 3 rows
- `DQ02`: 2 rows
- `DQ01`: 1 rows
- `DQ04`: 1 rows

**anomaly_type**
- `None`: 13 rows
- `CURRENCY_CODE_NULL`: 4 rows
- `INVALID_GL_ACCOUNT_CODE`: 4 rows
- `MISSING_DATE_FIELD`: 3 rows
- `MISSING_MANDATORY_FIELD`: 3 rows
- `UNUSUAL_AMOUNT_OUTLIER`: 2 rows
- `DATE_VALIDATION_ISSUE`: 1 rows
- `DUPLICATE_RECORD`: 1 rows

**anomaly_flag**
- `Y`: 18 rows
- `N`: 13 rows

**ANOMALY_AMOUNT**
- `0`: 15 rows
- `31`: 2 rows
- `34`: 2 rows
- `32`: 2 rows
- `33`: 2 rows
- `120`: 1 rows
- `300`: 1 rows
- `1000`: 1 rows
- `100`: 1 rows
- `230`: 1 rows
- `12480`: 1 rows
- `920`: 1 rows
- `110`: 1 rows

**MDP_CREATED_DATE**
- `2026-11-06 04:53:40.964516+00:00`: 31 rows

**MDP_MODIFIED_DATE**
- `2026-11-06 04:53:40.964516+00:00`: 31 rows

## Profile

Rows in the latest export: 31.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `SOURCE_SYSTEM_ID` | STRING | 3 | 0 | Concur | RPM |
| `TRANSACTION_REFERENCE_NO` | STRING | 21 | 1 | G021920821-202609-66309080-TEST14 | W031532495-202609-66311425-TEST09 |
| `POLICY_VERSION` | STRING | 14 | 0 | G021920821-2026/09/18 | W031532495-2026/09/18 |
| `RISK_UNIQUE_ID` | STRING | 14 | 0 | G021920821 | W031532495 |
| `COVERAGE_NUMBER` | STRING | 12 | 1 | G021920821-FLF-G03 | W031532495-EMP-W03 |
| `TRANSACTION_DATE` | DATE | 6 | 1 | 2026-07-26 00:00:00 | 2026-09-18 00:00:00 |
| `SEQUENCE` | INT | 5 | 0 | 1 | 5 |
| `ACCOUNTING_DATE` | DATE | 1 | 2 | 2026-09-01 00:00:00 | 2026-09-01 00:00:00 |
| `EFFECTIVE_DATE` | DATE | 8 | 1 | 2026-01-06 00:00:00 | 2026-10-01 00:00:00 |
| `BUSINESS_EVENT` | STRING | 4 | 0 | CM | RB |
| `BUSINESS_SUB_EVENT` | STRING | 8 | 0 | RPM-A | RPM-X |
| `PERCENT_EARNED_INCEPTION` | INT | 2 | 0 | 0 | 1 |
| `AMOUNT` | DECIMAL | 13 | 0 | 0 | 1000 |
| `COMMISSION_AMOUNT` | DECIMAL | 6 | 2 | -68.1 | 151.6 |
| `TERM_AMOUNT` | DECIMAL | 13 | 0 | -717 | 1516 |
| `COMMISSION_RATE` | DECIMAL | 7 | 0 | 0 | 0.15 |
| `ITEM_CODE` | STRING | 11 | 0 | 001ALLIED1 | SURPLUS |
| `RATE_CATEGORY` | STRING | 0 | 31 |  |  |
| `CLASS_CODE` | INT | 1 | 29 | 271 | 271 |
| `OPERATOR_UNIQUE_ID` | STRING | 0 | 31 |  |  |
| `source_file_name` | STRING | 3 | 0 | Concur_20260101_000000.csv | policy_transaction.csv.csv |
| `timestamp` | DATE | 1 | 0 | 2026-10-22 00:00:00 | 2026-10-22 00:00:00 |
| `DQ_RULE` | STRING | 6 | 13 | DQ01 | DQ09 |
| `anomaly_type` | STRING | 7 | 13 | CURRENCY_CODE_NULL | UNUSUAL_AMOUNT_OUTLIER |
| `anomaly_flag` | STRING | 2 | 0 | N | Y |
| `ANOMALY_AMOUNT` | DECIMAL | 13 | 0 | 0 | 12480 |
| `HASH_KEY` | STRING | 30 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-06 04:53:40.965000 | 2026-11-06 04:53:40.965000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-06 04:53:40.965000 | 2026-11-06 04:53:40.965000 |

## Sample rows

| SOURCE_SYSTEM_ID | TRANSACTION_REFERENCE_NO | POLICY_VERSION | RISK_UNIQUE_ID | COVERAGE_NUMBER | TRANSACTION_DATE | SEQUENCE | ACCOUNTING_DATE | EFFECTIVE_DATE | BUSINESS_EVENT | BUSINESS_SUB_EVENT | PERCENT_EARNED_INCEPTION | AMOUNT | COMMISSION_AMOUNT | TERM_AMOUNT | COMMISSION_RATE | ITEM_CODE | RATE_CATEGORY | CLASS_CODE | OPERATOR_UNIQUE_ID | source_file_name | timestamp | DQ_RULE | anomaly_type | anomaly_flag | ANOMALY_AMOUNT | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RPM | W023699378-202609-66312437-TEST01 | W023699378-2026/03/20 | W023699378 | W023699378-480-W02 | 2026-09-18 00:00:00 | 4 | 2026-09-01 00:00:00 | 2026-09-14 00:00:00 | CM | RPM-X | 0 | 480 | -6 | -98 | 0.12 | 001LIAB | NULL | 271 | NULL | policy_transaction.csv.csv | 2026-10-22 00:00:00 | NULL | NULL | N | 0 | <masked> | 2026-11-06 04:53:40.965000 | <masked> | 2026-11-06 04:53:40.965000 |
| RPM | W023699378-202609-66312437-TEST01 | W023699378-2026/03/20 | W023699378 | W023699378-480-W02 | 2026-09-18 00:00:00 | 4 | 2026-09-01 00:00:00 | 2026-09-14 00:00:00 | CM | RPM-X | 0 | 480 | -6 | -98 | 0.12 | 001LIAB | NULL | 271 | NULL | policy_transaction.csv.csv | 2026-10-22 00:00:00 | DQ01 | DUPLICATE_RECORD | Y | 12480 | <masked> | 2026-11-06 04:53:40.965000 | <masked> | 2026-11-06 04:53:40.965000 |
| RPM | W013362694-202609-66307916-TEST03 | W013362694-2026/09/17 | W013362694 | W013362694-FG4-W03 | 2026-07-26 00:00:00 | 1 | 2026-09-01 00:00:00 | 2026-09-17 00:00:00 | FS | RPM-FG4 | 0 | 1000 | 0 | 66.69 | 0 | 001FIGA23 | NULL | NULL | NULL | policy_transaction.csv.csv | 2026-10-22 00:00:00 | DQ02 | UNUSUAL_AMOUNT_OUTLIER | Y | 1000 | <masked> | 2026-11-06 04:53:40.965000 | <masked> | 2026-11-06 04:53:40.965000 |
| RPM | W027006975-202609-66309787-TEST04 | W027006975-2025/11/25 | W027006975 | W027006975-421-W03 | 2026-09-17 00:00:00 | 5 | 2026-09-01 00:00:00 | 2026-09-12 00:00:00 | CM | RPM-X | 0 | 920 | -3.5 | -171 | 0.1 | 001ALLIEDC | NULL | NULL | NULL | policy_transaction.csv.csv | 2026-10-22 00:00:00 | DQ02 | UNUSUAL_AMOUNT_OUTLIER | Y | 920 | <masked> | 2026-11-06 04:53:40.965000 | <masked> | 2026-11-06 04:53:40.965000 |
| RPM | NULL | W031439765-2026/09/14 | W031439765 | W031439765-EMP-W03 | 2026-09-18 00:00:00 | 2 | 2026-09-01 00:00:00 | 2026-09-14 00:00:00 | FS | RPM-EMP | 1 | 120 | 0 | -2 | 0 | 001EMPATFEE02 | NULL | NULL | NULL | policy_transaction.csv.csv | 2026-10-22 00:00:00 | DQ03 | MISSING_MANDATORY_FIELD | Y | 120 | <masked> | 2026-11-06 04:53:40.965000 | <masked> | 2026-11-06 04:53:40.965000 |
