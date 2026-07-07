# Session Conductor

Session Conductor is an agent skill for substantial work sessions that need
coordination, bounded delegation, adversarial review, verification, and clear
handoff state.

The conductor keeps judgment. Delegates can gather evidence, perform bounded
mechanical work, or try to return "no" against a claim, but the conductor
reviews receipts and makes the final decision.

## Use It When

- The task spans multiple steps, files, stores, or checks.
- Parallel evidence gathering would help, but final judgment must remain in one
  place.
- A risky change needs an independent opposition pass.
- A session might be interrupted and needs a useful handoff.
- Delegates or subagents are available, but their scope must be tightly bounded.

Skip it for small deterministic tasks that one agent can finish directly.

## What The Package Includes

- `SKILL.md` - the conductor operating contract.
- `assets/handoff_template.md` - a concise handoff skeleton for resumable work.
- `scripts/self_test.py` - static regression checks for the required boundaries,
  dispatch shape, handoff sections, and "conductor keeps judgment" rule.
- `agents/openai.yaml` - skill metadata for runtimes that display skill cards.
- `SHA256SUMS.txt` - drift manifest.

## Operating Model

```text
ground first
-> define the slice
-> delegate bounded work only when the host exposes delegates
-> inspect returned receipts
-> oppose consequential claims when possible
-> verify before reporting
-> hand off at human-needed breakpoints
```

Delegation is optional. If the current runtime exposes no delegate or subagent
tool, conduct locally and state that delegation was unavailable.

## Dispatch Prompt Shape

A good delegate prompt includes:

- exact scope and allowed files or stores;
- forbidden actions;
- acceptance checks the delegate can actually run;
- required output format with findings first;
- instruction to flag contradictions rather than silently resolve them.

Do not run two write delegates whose build, test, or output surfaces overlap.
Parallelize read-only delegates when the runtime supports it.

## Handoff

Copy the template when a fresh session must resume the work:

```bash
cp assets/handoff_template.md /path/to/project/HANDOFF.md
```

Use a different filename if that better fits the project. The point is not the
name; the point is scoped state, decisions, blockers, and next actions that a
fresh agent can verify.

## Install As An Agent Skill

```bash
git clone https://github.com/ap7x42a/session-conductor.git
cp -a session-conductor ~/.codex/skills/session-conductor
```

For project-local skill surfaces, copy the directory into the location your
runtime uses, such as `.agents/skills/session-conductor`.

## Verify The Package

```bash
python3 scripts/self_test.py
sha256sum -c SHA256SUMS.txt
```

## Limits

This skill does not authorize external agent launches or irreversible actions.
It only structures the current session: scope, delegation, verification, and
handoff discipline.
