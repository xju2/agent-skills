# Harness Engineering principles for coding-agent prompts

Source of inspiration: OpenAI, **“Harness engineering: leveraging Codex in an agent-first world”**, published February 11, 2026:
https://openai.com/index/harness-engineering/

This file is a concise operational distillation for prompt construction, not a reproduction of the article.

## Core principles

### Humans steer; agents execute
Human attention should operate at the level of goals, constraints, acceptance criteria, and judgment. Agents should perform repository inspection, implementation, tests, documentation, tooling, review, and iteration when the environment supports it.

### Fix the environment when the agent struggles
Repeated failure is often evidence of a missing capability, unclear contract, weak feedback loop, hidden knowledge, or poor tooling. Ask what must become more legible and enforceable rather than merely telling the agent to try harder.

### Give the agent a map, not an encyclopedia
Keep the top-level agent instructions short and stable. Point to structured repository-local sources of truth. Use progressive disclosure so only task-relevant context is loaded.

### Repository knowledge is the system of record
Important architecture, plans, design history, schemas, operational knowledge, and decisions should be discoverable in versioned repository artifacts. Do not rely on hidden chat history or people's memory as the only source of a durable rule.

### Agent legibility is a design goal
Make the application and development environment inspectable by agents. Useful examples include deterministic fixtures, queryable structured logs, metrics/traces, clear errors, reproducible local environments, executable acceptance scenarios, and repository-local commands.

### Enforce invariants; do not micromanage implementations
Rigid, mechanically checked boundaries enable local autonomy. Prompts should be strict about correctness, architecture direction, security, reproducibility, provenance, and other load-bearing properties while leaving ordinary implementation choices to the coding agent.

### Encode taste and lessons into the harness
When review finds a recurring failure pattern, prefer promoting the lesson into tests, linters, schemas, docs, generators, or repository tools rather than repeatedly adding prompt prose.

### Work depth-first with fast feedback
For substantial changes, build coherent slices, validate each slice, review it, and fix problems before stacking more work on top. Integration and self-review are part of implementation, not an afterthought.

### Agent-to-agent review can reduce human bottlenecks
When supported, ask independent agents/subagents to review correctness, architecture, security, testing, and maintainability. Treat their comments as hypotheses to verify, not commands to accept blindly.

### All engineering artifacts count
Code, tests, CI, docs, observability, evaluation harnesses, developer tools, release tooling, and design history can all be agent-generated and should all be held to the same repository quality standard.

### Autonomy grows from encoded feedback loops
The more setup, validation, testing, review, remediation, and recovery are explicit and machine-legible, the more safely a capable agent can carry work end to end and escalate only when human judgment is actually required.

### Continuously control entropy
Agents replicate existing patterns, including bad ones. Prefer small, continuous cleanup and centrally encoded “golden principles” over occasional large manual cleanup efforts.

## Implications for prompts

A strong coding-agent prompt should therefore:

- identify the outcome and acceptance gate;
- point to repository sources of truth instead of restating them;
- preserve mechanically enforced invariants;
- ask the agent to inspect actual current state before planning;
- require tests and end-to-end evidence appropriate to the task;
- ask the agent to improve genuine missing harness capabilities it discovers;
- require self-review and independent review when available;
- leave implementation freedom inside established boundaries;
- keep adjacent scope out;
- make the repository more legible to the next agent.

A weak prompt often does the opposite: it pastes huge docs, dictates speculative implementation details, depends on hidden conversation context, lists components without an end-to-end outcome, or treats tests/docs/observability as optional cleanup.
