"""The two ai-workflows callers' `config` gates are exact negations (ADR-0028): no event is handled by both or neither."""

import re
from pathlib import Path

WF = Path(__file__).resolve().parents[1] / ".github" / "workflows"


def gate(name: str) -> str:
    m = re.search(r"^  config:\n    if: \$\{\{ (.+) \}\}$", (WF / name).read_text(), re.M)
    assert m, f"{name}: no `if: ${{{{ ... }}}}` on the config job"
    return m.group(1)


def test_normal_caller_gate_is_the_exact_negation_of_the_e2e_gate():
    e2e = gate("caller-e2e.yml")
    assert "e2e-target" in e2e and "e2e/" in e2e
    assert gate("ai-workflows.yml") == f"!({e2e})"
