"""The guardrail layer.

    loader.py        reads guardrail.yaml, packs/, overrides/ and application_notes.md from GUARDRAILS_DIR
                     (default: this folder; the company's packs/ and guardrail.yaml are added by hand)
    input_checks/    before anything runs: redact.py (sensitive data typed by the user), intent.py (the input check)
    output_checks/   before the user sees anything: answer.py (answer check), filters.py (remove content in code)
    bedrock.py       optional AWS Bedrock Guardrail, used on questions and answers
    replies.py       the fixed replies
    check.py         verify the setup;  evaluate.py + evals/  attack tests

Data and action guardrails stay next to the code they protect. The index of all of them is docs/GUARDRAILS.md.
"""
from .loader import GuardrailError, Guardrails, Pack, load_from_settings

__all__ = ["GuardrailError", "Guardrails", "Pack", "load_from_settings"]
