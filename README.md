# agent-skills

A curated collection of reusable agent skills for Claude Code and Codex.

## Install

Clone the repository and run the interactive installer:

```bash
git clone https://github.com/xju2/agent-skills.git
cd agent-skills
python3 install.py
```

The installer lets you choose:

- Claude Code, Codex, or both;
- a user-wide or project-local installation;
- one, several, or all available skills.

It copies each selected skill as a self-contained directory, including its references and other supporting files.

### Non-interactive examples

Install one skill for both agents in the current user's global skill directories:

```bash
python3 install.py \
  --agent claude \
  --agent codex \
  --skill harness-engineering-prompts
```

Install selected skills into a project:

```bash
python3 install.py \
  --agent codex \
  --scope project \
  --project-root /path/to/project \
  --skill agent-first-project-bootstrap \
  --skill harness-engineering-prompts
```

Install every skill for Claude Code:

```bash
python3 install.py --agent claude --all
```

Useful options:

```text
--list       List discoverable skills
--dry-run    Preview destinations without copying
--force      Replace an existing selected skill
```

Existing skill directories are left untouched unless `--force` is specified.

### Installation locations

| Agent | User-wide | Project-local |
|---|---|---|
| Claude Code | `~/.claude/skills/<skill-name>` | `<project>/.claude/skills/<skill-name>` |
| Codex | `~/.agents/skills/<skill-name>` | `<project>/.agents/skills/<skill-name>` |

Restart the agent after installing or updating skills so it can rediscover them.

## Repository layout

Skills live under `skills/` and are grouped by broad primary use case. Each skill is self-contained in its own directory.

```text
skills/
├── coding-agents/
│   ├── agent-first-project-bootstrap/
│   └── harness-engineering-prompts/
└── proposal/
    └── red-team-review/
```

## Skills

### Coding agents

- [`agent-first-project-bootstrap`](skills/coding-agents/agent-first-project-bootstrap/) — Bootstrap new AI-driven repositories with repository-local knowledge, mechanical invariants, deterministic feedback loops, and agent-legible development practices.
- [`harness-engineering-prompts`](skills/coding-agents/harness-engineering-prompts/) — Draft implementation, milestone, and continuation prompts for Claude Code, Codex, and other coding agents using Harness Engineering principles.

### Proposal

- [`red-team-review`](skills/proposal/red-team-review/) — Red-team review support for funding proposals.

## Organization principles

- Group skills by broad purpose rather than by vendor or technology.
- Keep each skill self-contained.
- Prefer the skill's primary use case when more than one category could fit.
- Add categories only when there is a real skill that needs them.
