"""Text patterns shared by the input and output checks. Deliberately narrow so finance values (amounts, dates, account
and document numbers) are not changed."""
from __future__ import annotations

import re

REMOVED = "[removed]"

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
# only clear phone numbers: +<country> ..., (555) 123-4567, or a number right after a phone word
PHONE = re.compile(
    r"(?<![\w+])\+\d{1,3}(?:[ -]\(?\d{2,5}\)?){2,4}(?![\w]|[.,]\d)"  # spaces or hyphens: never an amount
    r"|\(\d{3}\)[ .-]?\d{3}[ .-]\d{4}(?!\w)"
    r"|(?:(?<=phone )|(?<=phone: )|(?<=mobile )|(?<=mobile: )|(?<=tel: ))\+?\d[\d .-]{7,}\d",
    re.I,
)
SECRET = re.compile(
    r"AKIA[0-9A-Z]{16}|dapi[0-9a-f]{32}|sk-ant-[A-Za-z0-9_-]{8,}"
    r"|eyJ[A-Za-z0-9_-]{8,}\.eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]+"
    r"|-----BEGIN [A-Z ]+-----"
    r"|(?:password|client[_ ]secret|api[_ ]?key|access[_ ]token)\s*[:=]\s*\S+",
    re.I,
)
PATH = re.compile(
    r"\b(?:abfss?|wasbs?|s3a?|dbfs|adl|file):/{1,3}[^\s\"')\]]+"
    r"|\b[A-Za-z]:\\[^\s\"')\]]+"
    r"|(?<![\w/.])/(?:Volumes|Workspace|mnt|home|dbfs|Users|app)/[^\s\"')\]]+"
)
MODEL = re.compile(
    r"\b(?:(?:us|eu|apac|global)\.)?(?:anthropic|openai)\.[\w.:-]+"
    r"|\bclaude(?:[ -](?:sonnet|opus|haiku))(?:[ -]?\d+(?:[.-]\d+)*)?"
    r"|\bclaude[ -]?\d+(?:[.-]\d+)*"
    r"|\bgpt-oss[\w.:-]*"
    r"|\bAnthropic\b",
    re.I,
)
