# agent-skills

[![skills.sh installs](https://skills.sh/b/xju2/agent-skills)](https://skills.sh/xju2/agent-skills)

Reusable agent skills for Claude Code, Codex, and other agents that support the [Agent Skills](https://agentskills.io/) format.

## Install

```bash
npx skills add xju2/agent-skills
```

The installer lets you select skills and target agents. Add `--global` to install them across projects. See the [Skills CLI documentation](https://github.com/vercel-labs/skills) for more options.

## Skills

- [`agent-first-project-bootstrap`](skills/coding-agents/agent-first-project-bootstrap/) — Bootstrap AI-driven repositories with agent-legible documentation, invariants, and feedback loops.
- [`harness-engineering-prompts`](skills/coding-agents/harness-engineering-prompts/) — Create implementation and milestone prompts for coding agents using Harness Engineering principles.
- [`review-before-coding`](skills/coding-agents/review-before-coding/) — Review whether a requested change is worth doing before implementation.
- [`red-team-review`](skills/proposal/red-team-review/) — Red-team funding proposals.
- [`scientific-paper-writing`](skills/writing/scientific-paper-writing/) — Draft and revise scientific papers, including AI/ML conference submissions.

## Other useful skills and plugins

- [Ponytail](https://github.com/dietrichgebert/ponytail) — Encourages coding agents to choose the smallest solution that meets the task without sacrificing safety.
- [Humanizer](https://github.com/blader/humanizer) — Removes common signs of AI-generated writing.
- [US ATLAS Marketplace](https://github.com/usatlas/marketplace) — Claude Code plugins for ATLAS analysis facilities, ATLAS software, and HEP Python tooling.
