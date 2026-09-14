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

## Apply the worth-doing scorecard

Score each metric from 0 to 4. A higher score must always favor proceeding:

| Metric | Weight | Evidence to evaluate |
|---|---:|---|
| Problem evidence | 15% | Tests, issues, logs, user feedback, duplication, documented limitations, or other proof that the problem exists and matters |
| Expected value | 20% | Improvement to user outcomes, correctness, performance, reliability, scientific productivity, or developer efficiency |
| Project alignment | 15% | Fit with documented architecture, roadmap, milestones, conventions, and current project maturity |
| Leverage and urgency | 10% | Other work unblocked, recurring friction removed, reusable capability created, and whether the need is timely |
| Implementation efficiency | 10% | Expected benefit relative to implementation effort and validation cost |
| Maintenance sustainability | 10% | The project's ability to test, document, operate, support, and evolve the change |
| Risk profile | 10% | How limited and manageable the security, reliability, compatibility, performance, and architectural risks are |
| Opportunity cost | 5% | Whether this is a better use of effort than other priorities visible in the project |
| Reversibility and learning | 5% | Ability to introduce the change incrementally, evaluate it objectively, and reverse it cheaply |

Use these anchors consistently:

- **0 — strongly unfavorable:** repository evidence argues directly against proceeding;
- **1 — unfavorable:** likely cost, weakness, or mismatch outweighs value;
- **2 — mixed or uncertain:** evidence is balanced, incomplete, or highly conditional;
- **3 — favorable:** evidence supports proceeding with manageable qualifications;
- **4 — strongly favorable:** direct evidence shows compelling value and a strong project fit.

Calculate the weighted score on a 0–4 scale:

`score = sum(metric score × metric weight) / 100`

Map the result to the default verdict:

- **3.20–4.00:** Worth doing now
- **2.40–3.19:** Worth doing with revised scope
- **1.60–2.39:** Defer
- **0.00–1.59:** Not worth doing

Treat these weights and thresholds as a consistent starting rubric, not a substitute for judgment. If documented project priorities justify different weighting, explain the deviation. Do not manipulate individual scores merely to reach a preferred verdict.

Report evidence confidence separately:

- **High:** supported by direct implementation evidence, tests, measurements, incidents, or actual user outcomes;
- **Medium:** supported by architecture, plans, recurring code patterns, or closely analogous project experience;
- **Low:** primarily inferred, with important evidence missing.

A low-confidence assessment should not normally receive **Worth doing now** unless the proposed action is a small, reversible experiment.

Apply these override conditions regardless of the numerical score:

- a documented architecture, security, legal, or safety invariant would be violated;
- the project already provides the requested capability;
- success cannot be measured or validated;
- a required prerequisite is missing;
- the change creates disproportionate operational or maintenance responsibility;
- a much smaller change would deliver nearly the same value.

An override does not automatically mean rejection. Use it to cap the verdict at **Worth doing with revised scope** or **Defer**, or choose **Not worth doing** when the conflict is fundamental. Name the override explicitly.

## Give concise decision-ready feedback

Use this structure unless the situation calls for something shorter:

### Verdict

State one verdict, the weighted score, and evidence confidence. Answer the worth-doing question in one or two direct sentences. Name any override that changed the score-based verdict.

### Project evidence

List the few repository findings that materially support the judgment, with file paths or other precise references. Include a compact metric breakdown so the score can be audited without overwhelming the response.

### Tradeoffs

Explain the expected benefit, cost, risks, and opportunity cost. Focus on factors that could change the decision.

### Recommendation

Recommend proceeding as requested, revising the scope, deferring, or declining. When recommending revised scope, make the smallest valuable version concrete.

### Confirmation

End with a specific question stating what implementation scope would proceed if the user approves.

## After the decision

When the user confirms, implement the approved scope using the project's normal instructions and validation practices. Preserve any boundaries agreed during the review. If the user chooses a different approach, update the scope accordingly without treating the earlier recommendation as a constraint.

This skill governs the decision before coding; it does not replace the project's implementation, testing, review, or safety instructions.
