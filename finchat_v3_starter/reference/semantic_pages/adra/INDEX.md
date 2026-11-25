# ADRA semantic layer

Account reconciliation data in `lakehouse_mvpai.silver`. Read `rules.md` first, then the pages of the tables you need. Join only through `joins.md`.

| Table | Type | Grain | What it holds |
|---|---|---|---|
| [`adra_legal_entity_dimensions`](adra_legal_entity_dimensions.md) | dim | LEGAL_ENTITY_KEY, ENGAGEMENT_KEY | ADRA legal entities: one row per legal entity within an engagement (code, name, status, country, currency). |
| [`adra_engagement_dimensions`](adra_engagement_dimensions.md) | dim | Engagement_Key | ADRA engagements (client tenants) that legal entities belong to. |
| [`adra_period_dimensions`](adra_period_dimensions.md) | dim | PERIOD_KEY, ENGAGEMENT_KEY, LEGAL_ENTITY_KEY | ADRA fiscal periods per legal entity: period label (e.g. 'Feb 25'), start/end dates and status. |
| [`adra_account_dimensions`](adra_account_dimensions.md) | dim | ACCOUNT_KEY, ENGAGEMENT_KEY, LEGAL_ENTITY_KEY | ADRA reconciliation accounts: one row per GL account per legal entity (number, name, class, type, risk, reconciliation type). |
| [`adra_account_facts`](adra_account_facts.md) | fact | ACCOUNT_KEY, ENGAGEMENT_KEY, LEGAL_ENTITY_KEY, PERIOD_KEY | Account reconciliations: one row per account per legal entity per period, with workflow status, finalized flag, balances, unidentified (unreconciled) balances, documents and rejections. |
| [`adra_transaction_facts`](adra_transaction_facts.md) | fact | HASH_KEY | Reconciling items (transactions) per account, legal entity and period: type, status, amount and age. |

Other pages: [rules.md](rules.md) · [joins.md](joins.md) · [metrics.md](metrics.md) · [verified_queries.md](verified_queries.md)
