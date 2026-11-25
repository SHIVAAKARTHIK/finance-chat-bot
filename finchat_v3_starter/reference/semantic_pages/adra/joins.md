# ADRA joins

Only these joins may be used, always with the full composite key. Partial keys multiply rows (fan-out).

| Join | From | To | Cardinality | Condition |
|---|---|---|---|---|
| `account_fact_to_account` | `adra_account_facts` | `adra_account_dimensions` | many-to-one | `adra_account_facts.ACCOUNT_KEY = adra_account_dimensions.ACCOUNT_KEY AND adra_account_facts.ENGAGEMENT_KEY = adra_account_dimensions.ENGAGEMENT_KEY AND adra_account_facts.LEGAL_ENTITY_KEY = adra_account_dimensions.LEGAL_ENTITY_KEY` |
| `account_fact_to_period` | `adra_account_facts` | `adra_period_dimensions` | many-to-one | `adra_account_facts.PERIOD_KEY = adra_period_dimensions.PERIOD_KEY AND adra_account_facts.ENGAGEMENT_KEY = adra_period_dimensions.ENGAGEMENT_KEY AND adra_account_facts.LEGAL_ENTITY_KEY = adra_period_dimensions.LEGAL_ENTITY_KEY` |
| `account_fact_to_legal_entity` | `adra_account_facts` | `adra_legal_entity_dimensions` | many-to-one | `adra_account_facts.LEGAL_ENTITY_KEY = adra_legal_entity_dimensions.LEGAL_ENTITY_KEY AND adra_account_facts.ENGAGEMENT_KEY = adra_legal_entity_dimensions.ENGAGEMENT_KEY` |
| `transaction_fact_to_account` | `adra_transaction_facts` | `adra_account_dimensions` | many-to-one | `adra_transaction_facts.ACCOUNT_KEY = adra_account_dimensions.ACCOUNT_KEY AND adra_transaction_facts.ENGAGEMENT_KEY = adra_account_dimensions.ENGAGEMENT_KEY AND adra_transaction_facts.LEGAL_ENTITY_KEY = adra_account_dimensions.LEGAL_ENTITY_KEY` |
| `transaction_fact_to_period` | `adra_transaction_facts` | `adra_period_dimensions` | many-to-one | `adra_transaction_facts.PERIOD_KEY = adra_period_dimensions.PERIOD_KEY AND adra_transaction_facts.ENGAGEMENT_KEY = adra_period_dimensions.ENGAGEMENT_KEY AND adra_transaction_facts.LEGAL_ENTITY_KEY = adra_period_dimensions.LEGAL_ENTITY_KEY` |
| `transaction_fact_to_legal_entity` | `adra_transaction_facts` | `adra_legal_entity_dimensions` | many-to-one | `adra_transaction_facts.LEGAL_ENTITY_KEY = adra_legal_entity_dimensions.LEGAL_ENTITY_KEY AND adra_transaction_facts.ENGAGEMENT_KEY = adra_legal_entity_dimensions.ENGAGEMENT_KEY` |
| `legal_entity_to_engagement` | `adra_legal_entity_dimensions` | `adra_engagement_dimensions` | many-to-one | `adra_legal_entity_dimensions.ENGAGEMENT_KEY = adra_engagement_dimensions.Engagement_Key` |
