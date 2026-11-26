"""The guardrail layer.

    loader.py        company packs and values, read from GUARDRAILS_DIR (not part of this repository)
    input_checks/    before anything runs: redact.py (sensitive data typed by the user), intent.py (the input check)
    output_checks/   before the user sees anything: answer.py (answer check), filters.py (remove content in code)
    bedrock.py       optional AWS Bedrock Guardrail, used on questions and answers
    replies.py       the fixed replies
    check.py         verify the setup;  evaluate.py + evals/  attack tests

Data and action guardrails stay next to the code they protect. The index of all of them is docs/GUARDRAILS.md.
"""
from .loader import GuardrailError, Guardrails, Pack, load_from_settings

__all__ = ["GuardrailError", "Guardrails", "Pack", "load_from_settings"]
