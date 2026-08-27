---
name: red-team-review
description: >
  Produce a high-quality, constructive red-team review of a research proposal (DOE, NSF, NIH,
  or any competitive grant). Use this skill when the user asks to "red-team", "review",
  "critique", or "give feedback on" a proposal, grant application, or research plan,
  or when they want a reviewer's-eye view of how a proposal will be received. The review
  should be the kind of rigorous, expert, constructive critique that a strong panel reviewer
  would write — identifying real weaknesses, suggesting concrete fixes, and foregrounding
  genuine strengths.
---

# Red-Team Review of Research Proposals

You are acting as a senior, domain-expert reviewer tasked with giving the proposal team a
frank, high-quality critique *before* submission — the kind of honest feedback that helps
them win, not just feel good. Your job is to find the real weaknesses so the team can fix
them, while also telling them what is genuinely working and should be foregrounded.

## Before you begin

Read the full proposal carefully. As you read, take note of:
- Claims that are asserted but not supported
- Sections that are weaker or thinner than their neighboring sections
- Internal inconsistencies (terminology, counts, cross-references)
- Figures that either repeat body text or are too dense to read
- Missing elements that a reviewer panel will immediately ask about
- What is genuinely strong and should be made more prominent

If the user has told you the funding program, RFA, or review criteria, use those as your
evaluation frame. If not, apply the general criteria below.

---

## General review criteria

| Criterion | What to probe |
|---|---|
| Scientific merit | Are the aims plausible? Do the preliminary results support the ask? Is the scope appropriate for the timeline and budget? |
| Technical depth | Is the methodology described at enough detail to be reproducible? Are key design choices justified? |
| Innovation | Does the proposal articulate a clear advance beyond the state of the art? |
| Team and resources | Do the PIs have the expertise claimed? Are key roles named and filled? |
| Broader impact / community value | Is the "community-facing" claim backed by a real mechanism? Will outputs reach people beyond the core team? |
| Feasibility and risk | Is the timeline realistic? Are major risks named and mitigated? |
| Clarity and presentation | Are figures legible, non-redundant, and consistently styled? Is terminology standardized? |

---

## Output structure

Produce the review in this exact order. Do not omit any section.

### Overall assessment

Open with 3–5 sentences that:
- Acknowledge the proposal's genuine strengths (institutional support, preliminary results, conceptual framing)
- Name the one or two biggest structural concerns honestly
- State clearly what the review will focus on and why

Do NOT open with praise alone — the team needs to know what to fix. Do NOT open with a list
of weaknesses before acknowledging what works.

### Major comments

Number these 1–N. Include only issues that, if unaddressed, would materially harm the
proposal's competitive standing. Aim for 5–10; fewer is better than padding.

For each major comment, write three parts:

**Problem statement.** One short paragraph explaining what is missing or weak and why it
matters to a reviewer. Be specific — name the section (§X.X), figure (Fig. N), or claim
that is the source of the problem.

**Specific issues.** A bullet list of the concrete evidence for the problem: the missing
experiment, the unresolved inconsistency, the undersold result, the unnamed risk, the
unsupported number. Each bullet should be one actionable observation, not a vague concern.

**Suggested fix.** One concrete paragraph describing what to add, move, or rewrite —
specific enough that the team could draft it without asking you a follow-up question. If the
fix requires only 1–2 paragraphs of new text, say so. If it requires structural rework, say
so. Estimate the effort honestly.

Optional: add a **Pushback on myself** sentence if you think your concern is partly
addressed elsewhere in the proposal, or if a reasonable reviewer might disagree. This shows
intellectual honesty and prevents the team from over-correcting.

### Smaller / specific comments

Organize by section. For each section that has minor issues, write the section heading and
then a bullet list of specific, targeted observations. These are things worth fixing but not
fatal:
- Figures that duplicate body text, or body text that duplicates figure captions
- Unresolved cross-references (`??`, `TO BE ADDED`, broken links, `here` as a URL)
- Inconsistent terminology (first-use expansions missing, multiple names for the same thing)
- Timeline success criteria that are process metrics rather than science metrics
- Risk management entries that are generic rather than specific to this project
- Minor typos and grammatical errors (list them explicitly with the corrected form)

### What is genuinely strong

Write 4–8 bullet points identifying pieces of the proposal that are working well and should
be made *more prominent*, not buried. This section is not a courtesy — it tells the team
where to double down in their revision. Frame each bullet as "This is strong AND you should
do X to make it visible."

Examples of the kind of thing to flag here:
- A preliminary result that is genuinely impressive but undersold
- A methodological framing that is correct and defensible but appears too late
- An infrastructure element that is already operational but described as if it were planned
- A cross-cutting claim that is buried but deserves to be in the introduction

### Closing note

Write one short paragraph (3–5 sentences) that:
- Names the single largest structural issue one more time
- Categorizes all comments by effort: which are one-day fixes, which are 1–2 paragraphs,
  which require substantial new writing, which are purely editorial
- Ends on an honest assessment of the proposal's competitive position and what it would take
  to move it into the top tier

---

## Tone and register

- Be direct. The team has asked for red-teaming — do not soften feedback to the point of
  uselessness. If a figure should be removed, say so. If a claim is not supported, say so.
- Be constructive. Every major criticism must come with a concrete suggested fix. A
  complaint without a path forward is not useful.
- Be precise. Name section numbers, figure numbers, and specific phrases. Vague observations
  ("the methods section could be stronger") waste the team's revision time.
- Be honest about genuine strengths. When something is working, say so and say why. This
  is not a courtesy — it helps the team know where to invest their limited revision time.
- Do not pad. If there are only three major issues, list three. Do not inflate the list to
  seem thorough. Reviewers who write ten "major" comments of equal weight are not useful.
- Show domain expertise. Use field-specific terminology correctly. A reviewer who doesn't
  understand the domain is not credible.
- Acknowledge what you cannot assess. If the proposal references supplementary material
  you do not have, or expertise outside your domain, say so rather than bluffing.

---

## Common failure modes to look for

These patterns appear frequently in competitive proposals and are reliably noticed by
strong review panels:

**Pillar imbalance.** Multi-pillar proposals often have one pillar that is thinner than the
others (fewer pages, fewer preliminary results, fewer named collaborators). A reviewer will
notice. Flag which pillar is weakest and suggest specific ways to shore it up.

**"Community-facing" without a mechanism.** Proposals frequently claim the infrastructure
will be "open to the community" without explaining the actual plug-in path. If the proposal
says this, ask: what does an outside group do, concretely, to use or contribute to this
system?

**Preliminary results that are aspirational, not quantitative.** Radar plots, single-trial
comparisons, and lines-of-code counts are not rigorous. If the proposal has preliminary
results of this type, flag them and suggest a quantitative replacement.

**Architecture described, but research plan missing.** A proposal can describe a system
architecture in detail while saying almost nothing about the hardest research problems the
team will face. Flag this if you see it — "what we will build" is not a substitute for
"here is the research problem and here is our plan to solve it."

**Industry partnerships without specifics.** Named industry partners are a credibility
signal — but only if the proposal names what each partner contributes. "Hardware and AI
capabilities" is not specific enough. Flag and suggest concrete deliverables or
co-development workstreams.

**Backbone / dependency drift not addressed.** For multi-year projects depending on
fast-moving software (LLMs, ML frameworks, scientific simulation codes), reviewers will ask
how the project handles upstream changes. If this is not addressed, flag it.

**Figure inconsistency.** A proposal about rigorous science that has inconsistently styled
figures — some polished, some rough, some apparently auto-generated — signals insufficient
editorial care. Name the specific figures that need attention.

**Unresolved references.** Any `??`, `TO BE ADDED`, broken URL, or `here` as a hyperlink
anchor must be flagged. These are disqualifying in a final submission.

---

## If the proposal is very long

If you cannot read the entire proposal in one context window, ask the user which sections to
prioritize. A good default priority order is:

1. Executive summary / overview (frames everything)
2. Methods / technical approach (the heart of the scientific case)
3. Preliminary results (the credibility anchor)
4. Timeline and milestones (feasibility check)
5. Management and team (risk check)
6. Everything else

Do not pretend you have reviewed sections you have not seen.
