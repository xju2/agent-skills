---
name: harness-engineering-prompts
description: Create or revise prompts for AI coding agents such as Claude Code, Codex, or other software-engineering agents using OpenAI-style Harness Engineering principles. Use when the user asks for an implementation prompt, milestone prompt, issue-to-agent prompt, coding-agent task brief, or continuation prompt for an AI-driven software project. Ground the prompt in the target repository's own AGENTS.md, architecture docs, plans, ADRs, tests, and current code; emphasize outcomes and mechanically enforced invariants while preserving local agent autonomy, agent legibility, feedback loops, self-review, and improvements to the development harness.
---

# Harness Engineering Prompts

Create ready-to-paste prompts for capable software-engineering agents. Treat the target repository as the source of truth and the prompt as a compact steering artifact, not a replacement for repository knowledge.

Read `references/harness-principles.md` when constructing or substantially revising a prompt.

## Workflow

1. **Establish the target and current state.**
   - Identify the repository, milestone/issue/task, target coding agent, and any explicit environment constraints.
   - If a repository link or connected repository is available, inspect the smallest useful set of authoritative files before drafting. Start with `AGENTS.md`, then follow its pointers to architecture, plans, ADRs, execution plans, tests, and relevant code.
   - For continuation prompts, inspect what the preceding milestone actually merged rather than relying only on the previous prompt.
   - Do not ask for information that repository inspection can resolve.

2. **Extract intent rather than copying documentation.**
   Capture only what the agent needs to begin:
   - desired outcome / acceptance gate,
   - verified starting state,
   - architectural invariants,
   - scope and explicit non-goals,
   - validation expectations,
   - completion/reporting expectations.

3. **Write a map, not a manual.**
   - Tell the agent where authoritative knowledge lives and require it to inspect relevant contracts before changing code.
   - Avoid pasting large portions of plans or architecture documents into the prompt.
   - Avoid prescribing exact classes, files, libraries, algorithms, or commit boundaries unless the repository already fixes those decisions or the user explicitly requests them.
   - Enforce boundaries centrally; allow implementation autonomy locally.

4. **Make Harness Engineering explicit.**
   Include, when relevant:
   - repository knowledge is the system of record,
   - progressive disclosure of context,
   - humans specify intent and constraints; agents execute,
   - architectural and scientific invariants should be enforced mechanically where practical,
   - agent legibility is a product requirement,
   - failures should prompt the question "what capability is missing from the harness?",
   - discovered recurring friction should produce the smallest durable improvement to docs, tests, tooling, observability, schemas, fixtures, or checks,
   - the next capable agent should need less hidden human context.

5. **Require an executable feedback loop.**
   For non-trivial work, direct the coding agent to:
   - verify the baseline,
   - create/update a repository-local execution plan if that is the project's convention,
   - work depth-first in coherent increments,
   - add or update tests with behavior changes,
   - run focused validation before building further,
   - review its own changes critically,
   - use independent agent/subagent reviews when supported,
   - investigate valid review findings rather than blindly applying comments,
   - run the repository-wide quality suite before completion.

6. **Bias toward outcomes and evidence.**
   - State end-to-end acceptance scenarios, not merely component checklists.
   - Require durable evidence that the gate passes.
   - Do not allow unit tests alone to stand in for an explicitly end-to-end milestone.
   - Preserve failure-path, restart/retry, authorization, provenance, reproducibility, or safety guarantees already required by the repository.

7. **Keep scope disciplined.**
   - Name adjacent milestones/features that must not be implemented when scope creep is plausible.
   - Allow clean extension boundaries for future work without speculative abstractions.

8. **Finish with a concise completion contract.**
   Ask the coding agent to report:
   - outcome / gate status,
   - major decisions,
   - acceptance evidence,
   - validation commands and results,
   - review findings resolved,
   - harness improvements made,
   - commits/branch when relevant,
   - genuine remaining risks or deferred work.

## Prompt shape

Use this as a flexible default, not a mandatory template:

1. Project + task
2. Agent-first operating model
3. Start by inspecting repository knowledge
4. Goal / acceptance gate
5. Load-bearing invariants
6. Task-specific outcomes
7. Harness-engineering requirement
8. Feedback and review loop
9. Scope / non-goals
10. Completion criteria and report

Omit sections that add no value. Prefer a shorter prompt that points to good repository knowledge over a long prompt that duplicates it.

## Quality rules

- Never invent repository state. Inspect it when tools are available; otherwise clearly distinguish supplied facts from assumptions.
- When the user provides a specific coding-agent model or effort level, preserve it in the recommendation but do not tailor technical correctness to model personality.
- Do not make the prompt depend on this Skill being installed. The coding agent should be able to execute from the prompt plus the repository.
- Do not tell the coding agent to rewrite architecture merely because implementation is inconvenient. Require evidence and a documented decision for genuine architectural changes.
- Prefer mechanical guardrails with useful remediation messages over prose-only rules when recurring violations are likely.
- Do not turn every local inconvenience into framework work; improve the harness only for real, recurring, or agent-blocking friction discovered during the task.
- Treat observability, documentation, tests, evaluation harnesses, and repository tooling as part of the engineered system, not ancillary chores.

## Examples of triggering requests

- "M4 is merged. Write the prompt for Claude to do M5."
- "Turn this GitHub issue into a Codex implementation prompt."
- "Draft one prompt for the whole milestone."
- "Write a prompt for an AI agent to implement this feature in my repo."
- "Revise this coding-agent prompt to follow our agent-first development philosophy."
