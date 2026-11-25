# adra_period_dimensions

**Domain:** ADRA  
**Type:** dimension table  
**Full name:** `lakehouse_mvpai.silver.adra_period_dimensions`  
**Grain:** one row per (PERIOD_KEY, ENGAGEMENT_KEY, LEGAL_ENTITY_KEY)  
**Also called:** period, fiscal period, month  

ADRA fiscal periods per legal entity: period label (e.g. 'Feb 25'), start/end dates and status.

> All columns are stored as text (STRING). Cast numbers and dates as shown in *SQL expression*; compare text with `trim()` and `lower()`.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `PERIOD_KEY` | string | Period key (join with ENGAGEMENT_KEY and LEGAL_ENTITY_KEY). |  | `trim(PERIOD_KEY)` |
| `ENGAGEMENT_KEY` | string | Engagement key. |  | `trim(ENGAGEMENT_KEY)` |
| `LEGAL_ENTITY_KEY` | string | Legal entity key. |  | `trim(LEGAL_ENTITY_KEY)` |
| `PERIOD_NAME` | string | Period label as users say it, e.g. 'Feb 25', 'Oct 26'. | period, month | `trim(PERIOD_NAME)` |
| `FISCAL_YEAR_NAME` | string | Fiscal year label. | fiscal year | `trim(FISCAL_YEAR_NAME)` |
| `PERIOD_START` | date | First day of the period. |  | `TRY_CAST(PERIOD_START AS DATE)` |
| `PERIOD_END` | date | Last day of the period (use for 'latest period'). | period end, month end | `TRY_CAST(PERIOD_END AS DATE)` |
| `PERIOD_STATUS` | string | Period status (open/closed). | period status | `trim(PERIOD_STATUS)` |
## Joins (approved, use the full key)

| Join | To table | Cardinality | Condition |
|---|---|---|---|
| `account_fact_to_period` | `adra_account_facts` | many-to-one | `adra_account_facts.PERIOD_KEY = adra_period_dimensions.PERIOD_KEY AND adra_account_facts.ENGAGEMENT_KEY = adra_period_dimensions.ENGAGEMENT_KEY AND adra_account_facts.LEGAL_ENTITY_KEY = adra_period_dimensions.LEGAL_ENTITY_KEY` |
| `transaction_fact_to_period` | `adra_transaction_facts` | many-to-one | `adra_transaction_facts.PERIOD_KEY = adra_period_dimensions.PERIOD_KEY AND adra_transaction_facts.ENGAGEMENT_KEY = adra_period_dimensions.ENGAGEMENT_KEY AND adra_transaction_facts.LEGAL_ENTITY_KEY = adra_period_dimensions.LEGAL_ENTITY_KEY` |
