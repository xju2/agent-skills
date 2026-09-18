# agent-skills

[![skills.sh installs](https://skills.sh/b/xju2/agent-skills)](https://skills.sh/xju2/agent-skills)

A curated collection of reusable agent skills for Claude Code, Codex, and other agents that support the Agent Skills format.

## Install

Install interactively with the Skills CLI:

```bash
npx skills add xju2/agent-skills
```

The CLI discovers the skills in this repository and lets you choose which skills and agents to install them for. By default, skills are installed for the current project. Add `--global` to make them available across projects.

### Common examples

List the available skills without installing them:

```bash
npx skills add xju2/agent-skills --list
```

Install one skill globally for Claude Code and Codex:

```bash
npx skills add xju2/agent-skills \
  --skill review-before-coding \
  --agent claude-code \
  --agent codex \
  --global
```

Install several selected skills:

```bash
npx skills add xju2/agent-skills \
  --skill agent-first-project-bootstrap \
  --skill harness-engineering-prompts
```

Install every skill:

```bash
npx skills add xju2/agent-skills --skill '*'
```

The CLI uses symlinks by default where supported so agents can share one installed copy. Pass `--copy` if you prefer independent copies in each agent's skill directory.

### Update or remove skills

```bash
# Update installed skills
npx skills update

# Remove a skill
npx skills remove review-before-coding
```

The Skills CLI collects anonymous installation telemetry. To opt out, set `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1` when running it.

See the [Skills CLI documentation](https://github.com/vercel-labs/skills) for all supported agents and options.

## Repository layout

Skills live under `skills/` and are grouped by broad primary use case. Each skill is self-contained in its own directory.

```text
skills/
├── coding-agents/
│   ├── agent-first-project-bootstrap/
│   ├── harness-engineering-prompts/
│   └── review-before-coding/
├── proposal/
│   └── red-team-review/
└── writing/
    └── scientific-paper-writing/
```

## Skills

### Coding agents

- [`agent-first-project-bootstrap`](skills/coding-agents/agent-first-project-bootstrap/) — Bootstrap new AI-driven repositories with repository-local knowledge, mechanical invariants, deterministic feedback loops, and agent-legible development practices.
- [`harness-engineering-prompts`](skills/coding-agents/harness-engineering-prompts/) — Draft implementation, milestone, and continuation prompts for Claude Code, Codex, and other coding agents using Harness Engineering principles.
- [`review-before-coding`](skills/coding-agents/review-before-coding/) — Review requested project changes against repository evidence, judge whether they are worth doing, and wait for confirmation before implementation.

### Proposal

- [`red-team-review`](skills/proposal/red-team-review/) — Red-team review support for funding proposals.

### Writing

- [`scientific-paper-writing`](skills/writing/scientific-paper-writing/) — Draft, revise, and review scientific papers for clear structure, precise claims, consistent notation, and publication-ready presentation, including AI/ML conference submissions.

## Organization principles

- Group skills by broad purpose rather than by vendor or technology.
- Keep each skill self-contained.
- Prefer the skill's primary use case when more than one category could fit.
- Add categories only when there is a real skill that needs them.
