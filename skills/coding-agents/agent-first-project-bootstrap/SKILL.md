---
name: agent-first-project-bootstrap
description: Bootstrap a new AI-driven or agent-first software project using Harness Engineering principles. Use when ChatGPT is asked to create, initialize, scaffold, or plan a new repository intended to be developed substantially by coding agents such as Claude Code, Codex, or similar systems. Establish repository-local knowledge, concise AGENTS.md guidance, architecture and milestone plans, deterministic setup and validation, executable acceptance criteria, mechanically enforced invariants, agent-legible observability, ADR and execution-plan conventions, and feedback loops that improve the development harness over time.
---

# Agent-First Project Bootstrap

Bootstrap the **development harness**, not just the initial source tree.

The goal is to create a repository that a capable coding agent can inspect, understand, modify, test, review, and resume with minimal hidden human context.

Read `references/harness-principles.md` for the underlying design principles. Read `references/bootstrap-blueprint.md` when deciding which repository artifacts to create.

## 1. Establish intent before scaffolding

Determine only the information that materially affects the harness:

1. What is being built, for whom, and what does success mean?
2. Is this a new repository or an existing skeleton?
3. What language/runtime or major stack constraints already exist?
4. Which coding agents or agent environments are expected to work on it?
5. What deployment, security, data, compliance, or infrastructure constraints must be visible from day one?

If the user has already supplied these answers, do not ask again.

Do not begin by generating a large framework. First identify the smallest repository structure that can make the project's intent and invariants explicit and executable.

## 2. Inspect before modifying an existing skeleton

If a repository already exists:

- inspect its README, agent instructions, package manifests, CI, tests, architecture docs, and current source layout;
- preserve useful local conventions instead of replacing them with generic boilerplate;
- identify contradictions, undocumented assumptions, and missing feedback loops;
- treat merged repository knowledge as authoritative unless the user explicitly asks to change it.

## 3. Choose the minimum useful harness maturity

Use the maturity ladder in `references/bootstrap-blueprint.md`.

Default to the **lowest level that makes the next milestone safe and agent-legible**. Do not create empty directories or policy documents merely because a template contains them.

Prefer growing the harness in response to real project needs.

## 4. Create repository-local knowledge

For a non-trivial agent-first project, normally establish these concepts, adapting filenames to local conventions:

- a short `AGENTS.md` that acts as a map, not a manual;
- a canonical architecture/system-intent document;
- a milestone or execution plan with explicit outcomes and acceptance gates;
- an ADR/decision-record convention for durable architectural choices;
- an execution-plan convention for non-trivial agent tasks;
- deterministic setup, run, test, lint, type-check, and validation commands;
- explicit ownership of authoritative schemas, manifests, configuration, and operational knowledge.

Keep `AGENTS.md` concise. Point from it to deeper repository documents rather than duplicating them.

## 5. Encode invariants mechanically

Translate important architectural rules into executable checks whenever practical.

Examples:

- dependency-direction tests;
- schema validation;
- generated-code consistency checks;
- API compatibility checks;
- migration tests;
- forbidden-import rules;
- deterministic manifest hashing;
- provenance completeness tests;
- resource or retry bounds;
- secret-scanning and repository hygiene checks.

Use prose for rationale and executable checks for enforcement.

Do not rely on repeated prompt reminders for rules the repository can enforce itself.

## 6. Design for agent legibility

Make ordinary development and failure diagnosis inspectable without hidden operator knowledge.

Prefer:

- deterministic fixtures;
- structured logs with stable identifiers;
- clear error messages with remediation hints;
- one-command or well-documented local setup;
- explicit health/readiness checks;
- observable state transitions;
- test helpers that model important external systems;
- repository-local examples of valid and invalid inputs;
- small end-to-end acceptance scenarios.

Ask: **Can a fresh capable agent determine what happened, why it happened, and how to verify a fix using repository-local evidence?**

If not, improve the harness.

## 7. Build feedback loops early

Create fast, layered feedback:

1. focused unit and contract tests;
2. architecture/invariant checks;
3. integration tests for meaningful boundaries;
4. small executable end-to-end acceptance scenarios;
5. CI running the same commands documented for local use.

Keep external credential-dependent tests opt-in with explicit skip reasons, but provide deterministic test doubles for the same contracts.

Avoid a development model where meaningful validation occurs only after a large implementation phase.

## 8. Separate outcome constraints from implementation autonomy

Specify strongly:

- product outcome;
- architectural invariants;
- acceptance criteria;
- safety/security boundaries;
- required evidence;
- validation commands.

Avoid prematurely prescribing:

- class names;
- file-by-file implementations;
- unnecessary framework choices;
- speculative abstractions for distant milestones.

Give agents freedom inside mechanically enforced boundaries.

## 9. Establish the improvement loop

Make this rule part of the project's working model:

> When an agent repeatedly struggles, do not only patch the immediate task. Determine whether the repository is missing documentation, tooling, fixtures, observability, validation, or an executable invariant. Make the smallest durable harness improvement that prevents the same class of struggle from recurring.

This is a core deliverable of an agent-first project.

## 10. Bootstrap deliverables

Adapt to project size, but a strong initial outcome usually includes:

- initial repository structure;
- concise `AGENTS.md`;
- architecture/system-intent document;
- dependency and module boundaries;
- initial milestone plan with acceptance scenarios;
- deterministic development commands;
- quality gates and CI;
- architecture/invariant tests where justified;
- ADR and execution-plan conventions;
- at least one executable vertical-slice acceptance test or fixture;
- documentation of known constraints and deferred decisions.

Do not claim the project is agent-ready merely because these files exist. Verify that another agent could follow them mechanically.

## 11. Review the bootstrap as a fresh agent

Before completion, perform a fresh-context review:

- Can a new agent find the source of truth quickly?
- Is setup deterministic?
- Are important decisions discoverable?
- Are architectural boundaries explicit and enforced?
- Are acceptance criteria executable where practical?
- Can failures be diagnosed without tribal knowledge?
- Are stale docs likely to be detected?
- Is there unnecessary boilerplate that should be removed?
- Does the harness make the next milestone easier than the bootstrap milestone?

Fix material findings before declaring the bootstrap complete.

## 12. Output style

When asked to **plan** a new project, provide a repository bootstrap plan organized around outcomes, invariants, and maturity rather than a large generic directory dump.

When asked to **create or scaffold** the repository and tools are available, make the changes directly, validate them, and report:

- repository knowledge created;
- mechanical invariants established;
- development/CI feedback loops;
- acceptance scenarios;
- important decisions and deferred decisions;
- remaining harness gaps.

If the repository will later use the `harness-engineering-prompts` Skill, ensure the bootstrap leaves enough authoritative repository knowledge that future task prompts can stay concise.
