---
name: access_screen_dim_employee
schema: silver
layer: silver
domain: null
type: table
status: active
purpose: People (managers and reportees) in the access review with department; history kept by effective dates.
grain: one row per employee_email + effective_from (one person version)
primary_key:
- employee_email
- effective_from
entity_column: null
period_columns:
- effective_from
- effective_to
pii_columns:
- employee_email
- employee_name
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: effective_to is null on all rows (all current)
proposed_fields:
- grain
reviewed: false
---

# access_screen_dim_employee

Access screen: people (managers + reportees), SCD2 on email. Current row = effective_to IS NULL.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `employee_email` | string |  |  | `employee_email` |
| `employee_name` | string |  |  | `employee_name` |
| `department` | string |  |  | `department` |
| `row_hash` | string |  |  | `row_hash` |
| `effective_from` | timestamp |  |  | `effective_from` |
| `effective_to` | timestamp |  |  | `effective_to` |
| `source_batch_id` | string |  |  | `source_batch_id` |
| `created_at` | timestamp |  |  | `created_at` |
| `updated_at` | timestamp |  |  | `updated_at` |

## Values

**department**
- `Finance`
- `Risk`
- `Testing`
- `IT Controls`

**row_hash**
- `4724a40a36b9be347667b5ce926a038debf952ddc804843ede5e36a124b67221`
- `8e4dba911de0335c8621da1ab80ca644a3096ad0dfe38707f7972b20759c6641`
- `4fe117b7f75ed57971b4b5fd1f65611d147efba389532c5b6ca9e859afca88e9`
- `e326eaaab87a5aa94f41c0999f4838815d414d080ed9e52801080057bb327b7e`
- `d05e485f2246286b47a109d164ce435dcd3ec767d824255c5c7e6071a701f926`
- `535a86a2f613710777536fa2fc355a5d573714aefab312c1ccb205582aee1177`
- `9b95550dcad305ac3d9d69fa8c045dbb6d0bf59959f27d8e6ff24dea03b49c0d`
- `672db7693b17656869fad9d62fc32d3ac08a22c4ba6f0a946622490290eec937`
- `2505d3e567d4a87f2f4168a625c1c079b92625e4fe8e254b946f2f826b0653b5`
- `c0da2b0330ff8343cf3bb2ea599c1756640154a1874b443de879f7154c27eec9`
- `9a217e4936dceb02e99143f8d88236e3895f6382e8d4313236f90dda1d2c9ded`
- `32bcc62020d45ef5f756d4c53fc1f4ecbbf3ba56c9f6fbcbd33117c6f94e7e25`
- `866e344d75f064bcc907847aab2a9c62a6b778e85e2d5071340de628c2b09b5d`
- `590aa1b4ac5f96a50d51216194520c23a4a136cce5b146fb45ec753d79b84fd8`
- `897e06c9ce02ba8dd607c1a3f9ced5b96745745a8a84ddfb05bc8ccd2d2dcc81`
- `1f1652c41ef849071f0c3206ec111616a521fcf7f7df159b375426a600009d7a`
- `927d798fa6129275c648a10b92e3c5136f46e51dfeb6083ba50d063e178602ee`
- `08e4df3ec1ec4ddc6097f7f8031f6e64ad27d5ccb201d1be4bbdc057b0174109`

**effective_from**
- `2025-11-01 09:00:00+00:00`

**effective_to**
- `None`

**source_batch_id**
- `BATCH-20251101-01`

**created_at**
- `2026-11-18 15:44:41.328002+00:00`
- `2026-11-20 06:14:23.875979+00:00`
- `2026-11-19 11:01:52.789665+00:00`

**updated_at**
- `2026-11-18 15:44:41.328002+00:00`
- `2026-11-20 06:14:23.875979+00:00`
- `2026-11-19 11:01:52.789665+00:00`

## Empty columns

Empty in every row: `effective_to`. Do not filter or group on them.
