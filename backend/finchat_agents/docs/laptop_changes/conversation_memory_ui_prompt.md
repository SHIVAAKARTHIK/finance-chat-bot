# Copilot prompts for the UI: conversation memory

Paste these one at a time into Copilot, in the frontend repo, and check each before going to the next.

---

## Prompt 1: "Answering for" line under each answer

```
In the Finance Chat UI, the final response body (the `complete` SSE event of POST /api/invoke/finance-chat/stream,
and the JSON of POST /api/invoke/finance-chat) now has a new optional field:

  answer_context: {
    topics: string[]        // business areas used, e.g. ["Fixed assets"]
    entities: string[]      // e.g. ["UK07"]
    periods: string[]       // e.g. ["Oct 26"]
    other_topics: string[]  // other topics of this conversation, e.g. ["Fynapse subledger journals"]
  } | null

1. Add `answer_context` (optional, nullable) to the TypeScript type of the finance chat response.
2. Under each assistant answer, when answer_context is not null, show one small muted line:
   "Answering for: <topics joined by ', '>" then " · <entities joined by ', '>" if any, then " · <periods>" if any.
   Example: "Answering for: Fixed assets · UK07 · Oct 26".
3. If other_topics is not empty, show small chip buttons after the line: "Switch to <topic>".
   Clicking one sends a new chat message (same send function as the input box, same conversation_id) with the text
   `${topic}: ${the user question of that answer}`. Example: "Fynapse subledger journals: what about last month?".
4. Do not change anything else in the message rendering. Hide the line when answer_context is null or missing
   (older messages, general answers, history items).
```

---

## Prompt 2: clarification options as buttons

```
In the Finance Chat UI, when the final response has status "clarification", the response now also has
`clarification_options: string[]` (and `follow_up_questions`, a JSON string, holds the same options).
Each option is a complete question, e.g. "Fixed assets: total additions in Oct 2026".

1. Add `clarification_options?: string[]` to the response type.
2. For a clarification answer, render the answer text as usual, then one button per option (full-width on mobile,
   wrapped on desktop). Use clarification_options when present, else the parsed follow_up_questions.
3. Clicking a button sends that option text as a new chat message, exactly like typing it into the input box
   (same conversation_id, through the stream endpoint). Disable the buttons after one is clicked.
4. If follow-up buttons are already rendered from follow_up_questions for this message, do not show them twice.
```

---

## Prompt 3: "Clear context" button

```
Add a "Clear context" action to the Finance Chat UI.

Backend: POST /api/invoke/finance-chat/clear-context with JSON body { "conversation_id": "<current conversation id>" }
and the same auth headers as the chat requests. Responses:
  200 { status: "success", conversation_id, cleared: true, context_start_turn: number, message: string }
  403 / 503 { status: "error", message: string }

1. Put a small "Clear context" button (icon + text, e.g. an eraser or refresh icon) in the chat header next to the
   existing actions. Tooltip: "Start fresh: earlier questions stay in the history but are not used to answer."
2. On click, show a small confirm ("Clear the context? Your history stays visible.") with Cancel / Clear.
3. On Clear, call the endpoint with the current conversation_id. If there is no conversation_id yet, do nothing
   except show the divider.
4. On success, keep all existing messages on screen, and add a centered divider line in the message list:
   "Context cleared - new questions start fresh". Keep the same conversation_id for the next questions.
5. On error, show the returned message as a toast; do not add the divider.
6. Disable the button while a chat answer is streaming.
7. Typing "/clear" in the input box also works on the backend, so no special handling is needed for it.
```

---

## Prompt 4 (optional): show the divider again after reload

Skip this for now. The history endpoint doesn't return the clear point yet. Tell me if you want it, and I'll add
`context_start_turn` to the history response.
