Task 07 (after Monday): conversation summaries and the 30-question limit. Read CLAUDE.md and docs/SPEC.md first.

1. Keep the last N turns verbatim in the agent context. When the conversation context passes a token threshold
   (config, default 6,000 tokens), gpt-oss updates the rolling summary (entities, periods, tables used, open threads,
   key numbers with their source question) and stores it in finance_chat_conversations.summary / summary_through_turn.
2. Follow-ups ("split that by account type") use the summary + last turns; the supervisor writes a standalone_question.
3. At question 30 in a conversation: answer it, then add a notice that the limit is reached; the next message starts a
   new conversation seeded with the summary (conversation_id changes; return the new id).
4. User memory (finance_chat_user_memory): frequent entities and periods from the last 30 answered questions, used only
   as a hint when the user omits an entity and has a clear habit; the answer says which one it assumed.

Acceptance: tests for threshold summarisation, follow-up rewriting, rollover at 30, and memory hint wording.
