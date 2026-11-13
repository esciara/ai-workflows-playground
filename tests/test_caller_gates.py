"""The ai-workflows callers' `config` gates cover every event exactly once (ADR-0028, ADR-0056 transition).

The three slot callers (caller-e2e-<n>.yml) each route their own items; the single-slot caller (caller-e2e.yml,
kept until PR-B deletes it) takes the remaining e2e items; the normal caller is the exact negation of all four.
"""

import re
from pathlib import Path

WF = Path(__file__).resolve().parents[1] / ".github" / "workflows"
SLOTS = (1, 2, 3)


def gate(name: str) -> str:
    m = re.search(r"^  config:\n    if: \$\{\{ (.+) \}\}$", (WF / name).read_text(), re.M)
    assert m, f"{name}: no `if: ${{{{ ... }}}}` on the config job"
    return m.group(1)


def test_normal_caller_gate_is_the_exact_negation_of_the_e2e_gates():
    slots = {n: gate(f"caller-e2e-{n}.yml") for n in SLOTS}
    for n, s in slots.items():
        assert f"'e2e/{n}/'" in s and f"'e2e-target-{n}'" in s
    union = " || ".join(f"({slots[n]})" for n in SLOTS)
    e2e = gate("caller-e2e.yml")
    suffix = f" && !({union})"
    assert e2e.endswith(suffix), "caller-e2e.yml must exclude the three slot gates"
    old = e2e.removesuffix(suffix)
    assert "'e2e-target'" in old and "'e2e/'" in old
    assert gate("ai-workflows.yml") == f"!({old} || {union})"
