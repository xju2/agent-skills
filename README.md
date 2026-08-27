# agent-skills

A curated collection of reusable agent Skills.

## Repository layout

Skills live under `skills/` and are grouped by broad primary use case. Each Skill is self-contained in its own directory.

```text
skills/
├── coding-agents/
│   └── harness-engineering-prompts/
└── proposal/
    └── red-team-review/
```

## Skills

### Coding agents

- [`harness-engineering-prompts`](skills/coding-agents/harness-engineering-prompts/) — Draft implementation, milestone, and continuation prompts for Claude Code, Codex, and other coding agents using Harness Engineering principles.

### Proposal

- [`red-team-review`](skills/proposal/red-team-review/) — Red-team review support for funding proposals.

## Organization principles

- Group Skills by broad purpose rather than by vendor or technology.
- Keep each Skill self-contained.
- Prefer the Skill's primary use case when more than one category could fit.
- Add categories only when there is a real Skill that needs them.
