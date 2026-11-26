"""Sensitive data typed by the user is removed before the question is sent to a model, traced or saved:
passwords and keys, email addresses, phone numbers, payment card numbers and social security numbers.

Finance identifiers (account, invoice, journal and entity numbers) are left alone: card numbers need card grouping or
the word "card" and a valid check digit, and social security numbers need to be named.
"""
from __future__ import annotations

import re

from ..patterns import EMAIL, PHONE, REMOVED, SECRET

PASSWORD = re.compile(
    r"\b(password|passwd|pwd|passcode|client[_ ]secret|secret[_ ]key|api[_ -]?key|access[_ ]token)\b"
    r"(\s*(?:is|:|=)\s*)(?!\[removed\])\S+",
    re.I,
)
GROUPED_CARD = re.compile(r"(?<![\w-])(?:(?:\d{4}[ -]){3}\d{1,4}|\d{4}[ -]\d{6}[ -]\d{5})(?![\w-])")
NAMED_CARD = re.compile(r"(\bcard(?:\s+(?:number|no\.?))?(?:\s+is)?\s*[:#]?\s*)(\d{13,19})(?!\d)", re.I)
SSN = re.compile(r"(\b(?:ssn|social security(?:\s+number)?)\b\D{0,12}?)\d{3}-?\d{2}-?\d{4}(?!\d)", re.I)


def _luhn(number: str) -> bool:
    digits = [int(c) for c in number if c.isdigit()]
    if not 13 <= len(digits) <= 19:
        return False
    total = sum(d if i % 2 == 0 else (d * 2 - 9 if d > 4 else d * 2) for i, d in enumerate(reversed(digits)))
    return total % 10 == 0


def redact_question(text: str) -> tuple[str, list[str]]:
    """(question without sensitive data, the kinds removed)."""
    kinds: list[str] = []

    def note(kind: str, replacement: str) -> str:
        if kind not in kinds:
            kinds.append(kind)
        return replacement

    text = PASSWORD.sub(lambda m: note("password or key", f"{m.group(1)}{m.group(2)}{REMOVED}"), text)
    text = SECRET.sub(lambda m: m.group(0) if REMOVED in m.group(0) else note("password or key", REMOVED), text)
    text = EMAIL.sub(lambda m: note("email address", REMOVED), text)
    text = NAMED_CARD.sub(lambda m: note("card number", m.group(1) + REMOVED) if _luhn(m.group(2)) else m.group(0), text)
    text = GROUPED_CARD.sub(lambda m: note("card number", REMOVED) if _luhn(m.group(0)) else m.group(0), text)
    text = SSN.sub(lambda m: note("social security number", m.group(1) + REMOVED), text)
    text = PHONE.sub(lambda m: note("phone number", REMOVED), text)
    return text, kinds


def redaction_notice(kinds: list[str]) -> str:
    return "Sensitive details were removed from your question before it was processed: " + ", ".join(kinds) + "."
