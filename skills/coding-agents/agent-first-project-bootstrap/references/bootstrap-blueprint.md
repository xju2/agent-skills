# Agent-First Bootstrap Blueprint

Use this as a maturity guide, not a fixed template.

## Level 0 — Intent and deterministic entry point

Minimum for a small project or proof of concept:

- README with purpose and quick start
- concise AGENTS.md
- pinned or reproducible dependency setup
- one canonical test/validation command
- explicit definition of the first useful outcome

Do not progress merely to add structure. Progress when the project needs stronger guarantees.

## Level 1 — Architecture and quality boundaries

Add when multiple modules, contributors, or agents will work independently:

- architecture/system-intent document
- dependency/module boundaries
- lint/format/type/test checks appropriate to the stack
- CI running the same checks as local development
- one or more mechanical architecture checks when boundaries matter

## Level 2 — Milestones and executable acceptance

Add when the project has multi-stage delivery:

- milestone plan with dependency order
- explicit acceptance gates
- small end-to-end acceptance scenarios
- valid/invalid fixtures for key contracts
- execution-plan convention for non-trivial work

## Level 3 — Durable decisions and agent legibility

Add when architecture and operations are becoming consequential:

- ADR/decision log
- structured logs and correlation identifiers
- health/readiness and diagnostics
- deterministic test doubles for external systems
- documented failure/recovery procedures
- provenance/reproducibility rules where relevant

## Level 4 — Automated review and evaluation

Add when agent throughput and change volume justify stronger automation:

- generated-contract consistency checks
- policy/invariant CI gates
- replayable end-to-end evals
- regression fixtures from prior failures
- automated or independent agent review workflows
- repository tooling that detects stale or contradictory knowledge

## Suggested repository concepts

Names are adaptable. The concepts matter more than exact paths.

```text
AGENTS.md
ARCHITECTURE.md
PLANS.md
README.md

docs/
  decisions/
  exec-plans/
    active/
    completed/

tests/
  architecture/
  integration/
```

Create only the directories justified by the current maturity level.

## Bootstrap acceptance questions

A bootstrap is successful when a fresh capable agent can answer, from repository-local evidence:

1. What are we building and why?
2. What is the next accepted milestone?
3. What architectural rules may not be violated?
4. Where are durable decisions recorded?
5. How do I set up the environment?
6. How do I run focused and full validation?
7. How do I know the implementation satisfies the milestone?
8. How do I diagnose ordinary failures?
9. What knowledge is authoritative when documents disagree?
10. What should I improve in the harness if I hit recurring friction?
