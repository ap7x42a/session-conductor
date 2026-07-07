---
name: session-conductor
description: >-
  Use at the start of substantial agent sessions that need coordination,
  delegation, adversarial review, handoff discipline, or survival across
  context clearing. The conductor keeps judgment, defines contracts, delegates
  bounded work only when the current host exposes delegates, verifies receipts,
  and writes a human-readable handoff at any human-needed breakpoint.
metadata:
  self_test: "python3 scripts/self_test.py"
---

# Session Conductor

The conductor owns judgment. Delegation is for bounded evidence gathering,
mechanical sweeps, narrow implementation tasks with explicit acceptance checks,
and adversarial review. The conductor plans, decides, reviews, verifies, and
reports.

Do not launch external agent processes from this skill. Use only delegates or
subagents actually exposed by the current host. If none are available, conduct
locally and state that delegation was unavailable.

## Operating Contract

1. **Ground first.** Read the current user request, live worktree or artifact
   state, relevant handoffs, and the files or stores that define the work.
   Treat summaries as pointers, not proof.
2. **Define the slice.** State the outcome, non-goals, forbidden outcomes,
   acceptance checks, and surfaces that must remain untouched.
3. **Delegate bounded work.** A delegate receives scope, forbidden actions,
   expected output, and checks it can actually run. Do not delegate final
   judgment, irreversible actions, commits, or completion claims.
4. **Oppose consequential work.** For risky diffs or decisions, get an
   independent "try to return no" pass when the current host can provide one.
5. **Integrate with receipts.** Read delegate outputs critically, inspect any
   changed files yourself, and keep verified, unverified, and refuted claims
   distinct.
6. **Stop at human-needed boundaries.** If the next action is destructive,
   outward-facing, irreversible, or blocked on unavailable access, write a
   handoff with the safe prep already completed.

## Roles

| Role | Does | Never does |
|---|---|---|
| Conductor | Plans, decides, reviews, verifies, reports, handoffs | Outsources judgment or claims success without receipts |
| Executor | Executes one bounded plan with acceptance checks | Changes scope silently, commits, or substitutes design judgment |
| Adversary | Tries to return "no" against claims, diffs, and receipts | Rubber-stamps or replaces verification |

## Dispatch Prompt Shape

Include:

- the exact scope and allowed files or stores;
- forbidden actions;
- acceptance checks;
- required output format: findings first, exact paths or commands, changed files
  if any, and unresolved uncertainty;
- instruction to flag contradictions rather than silently resolve them.

Never run two write delegates whose build, test, or output surfaces overlap.
Parallelize read-only delegates freely when the host supports it.

## Handoff

When a fresh session must resume from a human-readable artifact, copy
`assets/handoff_template.md` into the workspace and fill it. Use `HANDOFF.md`
only if that naming convention fits the project; otherwise use a clearly named
handoff file.

Required sections:

1. State of the world
2. In flight
3. Decisions already made
4. Next actions
5. Blocked on the operator
6. Where things live

Delete or archive stale handoffs when consumed so they cannot masquerade as live
state.

## Closing Introspection

At session close or in the final handoff, answer:

1. What am I least confident about?
2. What important risk or fact might the operator be missing?
3. If this breaks later, what is the most likely reason?
4. What useful unrequested improvement became visible?
5. Which earlier recommendation am I least sure about now?
6. What unresolved uncertainty should be carried forward?

## Done Means

- The conductor made the final decision.
- Delegated outputs were independently inspected.
- Consequential claims have receipts.
- Handoff state exists when needed and is clearly scoped.
- No broader success is implied than the evidence supports.
