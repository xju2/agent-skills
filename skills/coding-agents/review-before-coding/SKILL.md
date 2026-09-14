---
name: review-before-coding
description: Review a requested software-project change against repository evidence before implementation. Use whenever the user asks to build, add, modify, refactor, migrate, optimize, remove, or otherwise change code, configuration, tests, infrastructure, or repository contents. Inspect the project read-only, answer whether the request is worth doing, give actionable feedback, and wait for explicit confirmation before making coding changes. If the user is approving a review already completed by this skill and the scope is unchanged, proceed without repeating the review.
---

# Review Before Coding

Act as an evidence-based design gate before implementation. Help the user decide whether a requested change deserves engineering effort and whether its proposed shape fits the project.

## Gate implementation

For a new change request, do not immediately implement it—even if the request already says “implement,” “make the changes,” or similar.

First:

1. inspect the project using read-only operations;
2. evaluate the request against project evidence;
3. give the user a clear verdict and feedback;
4. stop and wait for explicit confirmation.

During this preflight, do not edit files, install dependencies, run formatters or generators, create branches, commit, push, open pull requests, or perform other mutating actions. Small read-only diagnostics are allowed when they materially strengthen the assessment and do not alter tracked files.

Approval such as “proceed,” “go ahead,” or an equally clear response unlocks implementation for the reviewed scope. Do not repeat the same review after approval unless the user materially changes the request or new repository evidence invalidates the earlier assessment.

If the user explicitly asks to skip the preflight, honor that instruction.

## Gather project evidence

Inspect the smallest set of authoritative project sources needed to judge the request. Prefer, as relevant:

- `AGENTS.md`, `CLAUDE.md`, and other repository instructions;
- the README and contributor documentation;
- architecture documents, plans, ADRs, and roadmaps;
- package manifests, schemas, public interfaces, and configuration;
- relevant implementation, tests, fixtures, and CI checks;
- recent project history, issues, or pull requests when available and material.

Follow pointers from repository instructions rather than reading the entire project indiscriminately. Cite concrete paths and, when useful, symbols or sections. Distinguish direct evidence from inference. Never invent project state.

If the available evidence is insufficient, say what is missing. Ask a focused question only when its answer could materially change the verdict; otherwise make a qualified recommendation.

## Judge whether the request is worth doing

Explicitly answer:

> Is what the user asked for worth doing?

Choose one verdict:

- **Worth doing now** — the expected value clearly justifies the cost and the request fits the project.
- **Worth doing with revised scope** — the goal is valuable, but a smaller or different implementation is preferable.
- **Defer** — the idea may be valuable, but prerequisites, timing, evidence, or opportunity cost argue against doing it now.
- **Not worth doing** — the likely value does not justify the complexity, maintenance burden, risk, or mismatch with project direction.

Base the verdict on the project, not generic software advice. Consider:

- the user outcome and the problem actually being solved;
- alignment with current architecture, roadmap, and conventions;
- evidence that the problem exists and matters;
- expected user or operational value;
- implementation and long-term maintenance cost;
- complexity, security, reliability, performance, and portability risks;
- simpler alternatives and the cost of doing nothing;
- prerequisites and whether this is the right time.

Do not default to agreement. If the request is weak, premature, duplicative, or over-engineered, say so plainly and offer a better path.

## Give concise decision-ready feedback

Use this structure unless the situation calls for something shorter:

### Verdict

State one verdict and answer the worth-doing question in one or two direct sentences.

### Project evidence

List the few repository findings that materially support the judgment, with file paths or other precise references.

### Tradeoffs

Explain the expected benefit, cost, risks, and opportunity cost. Focus on factors that could change the decision.

### Recommendation

Recommend proceeding as requested, revising the scope, deferring, or declining. When recommending revised scope, make the smallest valuable version concrete.

### Confirmation

End with a specific question stating what implementation scope would proceed if the user approves.

## After the decision

When the user confirms, implement the approved scope using the project's normal instructions and validation practices. Preserve any boundaries agreed during the review. If the user chooses a different approach, update the scope accordingly without treating the earlier recommendation as a constraint.

This skill governs the decision before coding; it does not replace the project's implementation, testing, review, or safety instructions.
