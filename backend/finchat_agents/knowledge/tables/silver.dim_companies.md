---
name: dim_companies
schema: silver
layer: silver
domain: gl
type: table
status: active
purpose: D365 companies (data areas) with names.
grain: one row per HASH_KEY (one company)
primary_key:
- HASH_KEY
entity_column: DATA_AREA
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: KNOWN_AS, LANGUAGE_ID all null
row_count: 45
proposed_fields:
- grain
- primary_key
reviewed: false
---

# dim_companies

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA` | string |  |  | `DATA_AREA` |
| `NAME` | string |  |  | `NAME` |
| `KNOWN_AS` | string |  |  | `KNOWN_AS` |
| `LANGUAGE_ID` | string |  |  | `LANGUAGE_ID` |
| `PARTY_NUMBER` | string |  |  | `PARTY_NUMBER` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**NAME**
- `Royal Premium Budget`: 2 rows
- `A.J. Kaufman Institute, LLC`: 1 rows
- `RBJ`: 1 rows
- `Burns & Wilcox, Ltd`: 1 rows
- `INS62`: 1 rows
- `HWKGL`: 1 rows
- `INS63`: 1 rows
- `Global Excess Partners`: 1 rows
- `Noremac Marketing`: 1 rows
- `Canadian Reports`: 1 rows
- `DAT`: 1 rows
- `Sterling Enterprises`: 1 rows
- `Node`: 1 rows
- `INS24`: 1 rows
- `Evergreen Solutions`: 1 rows
- `RB Jones, Marine`: 1 rows
- `Burns & Wilcox, LTD`: 1 rows
- `INS33`: 1 rows
- `Grandview Holdings`: 1 rows
- `Burns & Wilcox Canada Claims`: 1 rows
- `CAN`: 1 rows
- `AJK Enterprises, Inc.`: 1 rows
- `CIBL`: 1 rows
- `INS36`: 1 rows
- `PrimeEdge Inc.`: 1 rows
- `INS27`: 1 rows
- `INS14`: 1 rows
- `Pinnacle Ventures`: 1 rows
- `INS08`: 1 rows
- `INS59`: 1 rows
- `US Reports`: 1 rows
- `INSHOLDING`: 1 rows
- `HKEUR`: 1 rows
- `INS28`: 1 rows
- `Burns & Wilcox, RE`: 1 rows
- `INS25`: 1 rows
- `INS65`: 1 rows
- `Node International`: 1 rows
- `AJK Enterprises`: 1 rows
- `INS26`: 1 rows
- `INS38`: 1 rows
- `INS01`: 1 rows
- `INS30`: 1 rows
- `AJK Canada Insurance Holdings`: 1 rows

**KNOWN_AS**
- `None`: 45 rows

**LANGUAGE_ID**
- `None`: 45 rows

**PARTY_NUMBER**
- `7408`: 1 rows
- `5505`: 1 rows
- `7212`: 1 rows
- `8401`: 1 rows
- `7405`: 1 rows
- `7216`: 1 rows
- `7414`: 1 rows
- `7215`: 1 rows
- `7406`: 1 rows
- `7404`: 1 rows
- `7303`: 1 rows
- `5502`: 1 rows
- `{2CE71508-E13F-48A0-BB18-0B3518F330D3}`: 1 rows
- `7302`: 1 rows
- `7207`: 1 rows
- `5503`: 1 rows
- `7407`: 1 rows
- `7415`: 1 rows
- `7209`: 1 rows
- `7410`: 1 rows
- `7204`: 1 rows
- `7409`: 1 rows
- `7214`: 1 rows
- `7203`: 1 rows
- `7419`: 1 rows
- `7201`: 1 rows
- `7306`: 1 rows
- `7416`: 1 rows
- `7205`: 1 rows
- `5504`: 1 rows
- `7412`: 1 rows
- `7206`: 1 rows
- `7202`: 1 rows
- `7301`: 1 rows
- `7411`: 1 rows
- `7304`: 1 rows
- `7305`: 1 rows
- `7417`: 1 rows
- `7211`: 1 rows
- `7213`: 1 rows
- `5501`: 1 rows
- `7210`: 1 rows
- `7208`: 1 rows
- `7413`: 1 rows
- `7418`: 1 rows

**SOURCE_FILE_NAME**
- `companies__20261116_105417.csv`: 45 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:43:18.248801+00:00`: 45 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:43:18.248801+00:00`: 45 rows

## Profile

Rows in the latest export: 45.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `DATA_AREA` | STRING | 44 | 0 |  |  |
| `NAME` | STRING | 43 | 0 | A.J. Kaufman Institute, LLC | US Reports |
| `KNOWN_AS` | STRING | 0 | 45 |  |  |
| `LANGUAGE_ID` | STRING | 0 | 45 |  |  |
| `PARTY_NUMBER` | STRING | 45 | 0 | 5501 | {2CE71508-E13F-48A0-BB18-0B3518F330D3} |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | companies__20261116_105417.csv | companies__20261116_105417.csv |
| `HASH_KEY` | STRING | 45 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:43:18.249000 | 2026-11-16 11:43:18.249000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:43:18.249000 | 2026-11-16 11:43:18.249000 |

## Sample rows

| NAME | KNOWN_AS | LANGUAGE_ID | PARTY_NUMBER | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|
| DAT | NULL | NULL | {2CE71508-E13F-48A0-BB18-0B3518F330D3} | companies__20261116_105417.csv | <masked> | 2026-11-16 11:43:18.249000 | <masked> | 2026-11-16 11:43:18.249000 |
| Evergreen Solutions | NULL | NULL | 5501 | companies__20261116_105417.csv | <masked> | 2026-11-16 11:43:18.249000 | <masked> | 2026-11-16 11:43:18.249000 |
| PrimeEdge Inc. | NULL | NULL | 5502 | companies__20261116_105417.csv | <masked> | 2026-11-16 11:43:18.249000 | <masked> | 2026-11-16 11:43:18.249000 |
| Sterling Enterprises | NULL | NULL | 5503 | companies__20261116_105417.csv | <masked> | 2026-11-16 11:43:18.249000 | <masked> | 2026-11-16 11:43:18.249000 |
| Grandview Holdings | NULL | NULL | 5504 | companies__20261116_105417.csv | <masked> | 2026-11-16 11:43:18.249000 | <masked> | 2026-11-16 11:43:18.249000 |
