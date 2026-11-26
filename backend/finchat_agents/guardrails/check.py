"""Check the guardrail folder without starting the app (no model or database calls):

    python -m finchat_agents.guardrails.check            # uses GUARDRAILS_DIR
    python -m finchat_agents.guardrails.check <folder>
"""
from __future__ import annotations

import sys
from pathlib import Path

from .loader import AUDIENCE, GuardrailError, Guardrails


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    from ..config import Settings

    settings = Settings()
    folder = Path(args[0]) if args else settings.resolve_path(settings.guardrails_dir)
    try:
        guardrails = Guardrails.load(folder)
    except GuardrailError as exc:
        print(f"NOT OK: {exc}")
        return 1
    print(f"OK: {folder}")
    for pack in guardrails.packs:
        print(f"  {pack.order:>3}  {pack.id}  ({pack.source})")
    for audience in AUDIENCE:
        print(f"  {audience}: {', '.join(guardrails.packs_for(audience)) or '-'}")
    print("  application notes:", "yes" if guardrails.notes else "no")
    if settings.bedrock_guardrail_id:
        print("  Bedrock content filter: configured, version", settings.bedrock_guardrail_version or "MISSING")
    else:
        print("  Bedrock content filter: off (BEDROCK_GUARDRAIL_ID not set)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
