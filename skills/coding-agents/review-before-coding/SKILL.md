---
name: review-before-coding
description: Give brief, evidence-backed feedback on a requested software change before implementing it. Use when the user asks to build, add, modify, refactor, migrate, optimize, remove, or otherwise change code, configuration, tests, infrastructure, or repository contents. Inspect only the project evidence needed to sanity-check the request, state any important concern or improvement concisely, then proceed with the coding work unless a material issue requires the user's decision.
---

# Review Before Coding

Before making code changes, briefly sanity-check the request against the project.

## Review first

Use read-only inspection to look at only the repository evidence needed to understand the request. Prefer the most relevant sources, such as:

- repository instructions such as `AGENTS.md` or `CLAUDE.md`;
- relevant architecture or planning documents;
- the implementation, tests, configuration, or interfaces directly affected by the request.

Do not perform a broad repository audit unless the request requires one.

## Give brief feedback

Before coding, tell the user what you think of the request.

Keep this feedback short and direct:

- usually 1-3 bullets or a short paragraph;
- focus only on observations that may affect the implementation;
- support important claims with concrete repository evidence, such as file paths, symbols, tests, or documented constraints;
- distinguish evidence from inference;
- mention a simpler or better approach only when it is materially useful.

Do not produce scores, weighted rubrics, confidence ratings, lengthy tradeoff analyses, or report-style sections. Do not argue at length about whether the work is "worth doing."

If the request is sensible, say so briefly and continue. If there is a minor concern, mention it and continue with the best reasonable implementation.

Pause for the user's decision only when repository evidence reveals a material issue that changes the requested scope, conflicts with project constraints, creates significant risk, or leaves multiple consequential choices that cannot be resolved from the project.

## Then implement

After the brief feedback, carry out the requested coding work using the project's normal instructions and validation practices.

If the user explicitly asks to skip the review, proceed directly to implementation.
