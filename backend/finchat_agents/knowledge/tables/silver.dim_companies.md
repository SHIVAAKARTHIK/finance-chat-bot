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
- `Royal Premium Budget`
- `A.J. Kaufman Institute, LLC`
- `RBJ`
- `Burns & Wilcox, Ltd`
- `INS62`
- `HWKGL`
- `INS63`
- `Global Excess Partners`
- `Noremac Marketing`
- `Canadian Reports`
- `DAT`
- `Sterling Enterprises`
- `Node`
- `INS24`
- `Evergreen Solutions`
- `RB Jones, Marine`
- `Burns & Wilcox, LTD`
- `INS33`
- `Grandview Holdings`
- `Burns & Wilcox Canada Claims`
- `CAN`
- `AJK Enterprises, Inc.`
- `CIBL`
- `INS36`
- `PrimeEdge Inc.`
- `INS27`
- `INS14`
- `Pinnacle Ventures`
- `INS08`
- `INS59`
- `US Reports`
- `INSHOLDING`
- `HKEUR`
- `INS28`
- `Burns & Wilcox, RE`
- `INS25`
- `INS65`
- `Node International`
- `AJK Enterprises`
- `INS26`
- `INS38`
- `INS01`
- `INS30`
- `AJK Canada Insurance Holdings`

**KNOWN_AS**
- `None`

**LANGUAGE_ID**
- `None`

**PARTY_NUMBER**
- `7408`
- `5505`
- `7212`
- `8401`
- `7405`
- `7216`
- `7414`
- `7215`
- `7406`
- `7404`
- `7303`
- `5502`
- `{2CE71508-E13F-48A0-BB18-0B3518F330D3}`
- `7302`
- `7207`
- `5503`
- `7407`
- `7415`
- `7209`
- `7410`
- `7204`
- `7409`
- `7214`
- `7203`
- `7419`
- `7201`
- `7306`
- `7416`
- `7205`
- `5504`
- `7412`
- `7206`
- `7202`
- `7301`
- `7411`
- `7304`
- `7305`
- `7417`
- `7211`
- `7213`
- `5501`
- `7210`
- `7208`
- `7413`
- `7418`

**SOURCE_FILE_NAME**
- `companies__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:43:18.248801+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:43:18.248801+00:00`

## Empty columns

Empty in every row: `KNOWN_AS`, `LANGUAGE_ID`. Do not filter or group on them.
