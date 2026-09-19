---
name: review-before-coding
description: Give brief, evidence-backed feedback on a requested software change before implementation. Use when the user asks to build, add, modify, refactor, migrate, optimize, remove, or otherwise change code, configuration, tests, infrastructure, or repository contents. Inspect only the project evidence needed to sanity-check the request, give concise feedback, then stop and wait for explicit user confirmation before making any coding changes. If the user is approving a review already completed by this skill and the scope is unchanged, proceed without repeating the review.
---

# Review Before Coding

Before making code changes, briefly sanity-check the request against the project.

## Review first

Use read-only inspection to look at only the repository evidence needed to understand the request. Prefer the most relevant sources, such as:

- repository instructions such as `AGENTS.md` or `CLAUDE.md`;
- relevant architecture or planning documents;
- the implementation, tests, configuration, or interfaces directly affected by the request.

Do not perform a broad repository audit unless the request requires one.

During this review, do not edit files, install dependencies, run generators or formatters, create branches, commit, push, open pull requests, or perform other mutating actions.

## Give brief feedback

Tell the user what you think of the request before coding.

Keep the feedback short and direct:

- usually 1-3 bullets or a short paragraph;
- focus only on observations that may affect the implementation;
- support important claims with concrete repository evidence, such as file paths, symbols, tests, or documented constraints;
- distinguish evidence from inference;
- mention a simpler or better approach only when it is materially useful.

Do not produce scores, weighted rubrics, confidence ratings, lengthy tradeoff analyses, or report-style sections. Do not argue at length about whether the work is "worth doing."

## Stop for confirmation

After the feedback, stop and wait for explicit user confirmation before making any coding changes.

End with a short confirmation question, for example: "Proceed with this implementation?"

Approval such as "proceed", "go ahead", or an equally clear response unlocks implementation for the reviewed scope. Do not repeat the review after approval unless the user materially changes the request or new repository evidence invalidates the earlier feedback.

If the user explicitly asks to skip the review, proceed directly to implementation.
