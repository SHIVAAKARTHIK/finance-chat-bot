"""The fixed replies. Company replies come from the pack values; the others can be set in guardrail.yaml `values`
(HARMFUL_CONTENT_MESSAGE, SUPPORT_MESSAGE) and have defaults here."""
from __future__ import annotations

from .loader import Guardrails

DEFAULT_CONFIDENTIALITY = "I can't share that. I can help with your finance questions."
DEFAULT_OUT_OF_SCOPE = "I can only help with finance questions."
DEFAULT_DISALLOWED = "I can't help with that request."
DEFAULT_HARMFUL = "I can't help with that. I can help with your finance work."
DEFAULT_SUPPORT = ("It sounds like something difficult may be going on, and you don't have to handle it alone. Please talk "
                   "to someone you trust or your employee assistance programme. If you or someone else is in immediate "
                   "danger, contact your local emergency number now.")
COULD_NOT_ANSWER_TEXT = ("I couldn't find approved information to answer that. Try naming the entity, period or business "
                         "area you mean.")
UNAVAILABLE_TEXT = "The assistant is not available right now. Please try again in a moment."

# refusal kind -> (company pack that must be enabled, or None = always on; value holding the reply; default reply)
REFUSALS: dict[str, tuple[str | None, str, str]] = {
    "injection": ("prompt_injection_shield", "CONFIDENTIALITY_MESSAGE", DEFAULT_CONFIDENTIALITY),
    "confidential": ("system_prompt_confidentiality", "CONFIDENTIALITY_MESSAGE", DEFAULT_CONFIDENTIALITY),
    "confidentiality": ("system_prompt_confidentiality", "CONFIDENTIALITY_MESSAGE", DEFAULT_CONFIDENTIALITY),
    "out_of_scope": ("scope_enforcement", "OUT_OF_SCOPE_MESSAGE", DEFAULT_OUT_OF_SCOPE),
    "disallowed": ("disallowed_capabilities", "DISALLOWED_CAPABILITY_MESSAGE", DEFAULT_DISALLOWED),
    "harmful": (None, "HARMFUL_CONTENT_MESSAGE", DEFAULT_HARMFUL),
    "support": (None, "SUPPORT_MESSAGE", DEFAULT_SUPPORT),
}


def refusal_message(guardrails: Guardrails, kind: str) -> str:
    """The fixed reply for a refusal kind, or "" when that rule is switched off or the kind is unknown."""
    entry = REFUSALS.get(kind)
    if entry is None:
        return ""
    pack, value, default = entry
    return guardrails.value(value, default) if pack is None or guardrails.enabled(pack) else ""
