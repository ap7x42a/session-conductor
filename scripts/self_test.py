#!/usr/bin/env python3
"""Self-test for the public session-conductor skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_SECTIONS = [
    "State of the world",
    "In flight",
    "Decisions already made",
    "Next actions",
    "Blocked on the operator",
    "Where things live",
]


def main() -> int:
    failures: list[str] = []
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    template = (ROOT / "assets" / "handoff_template.md").read_text(encoding="utf-8")

    for needle in (
        "The conductor owns judgment",
        "Do not launch external agent processes",
        "Delegate bounded work",
        "Oppose consequential work",
        "Integrate with receipts",
    ):
        if needle not in skill:
            failures.append(f"missing doctrine phrase: {needle}")

    for section in REQUIRED_SECTIONS:
        if not re.search(re.escape(section), skill):
            failures.append(f"SKILL.md missing section name: {section}")
        if not re.search(re.escape(section), template):
            failures.append(f"handoff template missing section name: {section}")

    if "fable-method" in skill or "NeuroLedger" in skill or "GrimWatch" in skill:
        failures.append("public skill leaked project-specific doctrine")

    if failures:
        print("SELF-TEST FAILED")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("SELF-TEST PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
