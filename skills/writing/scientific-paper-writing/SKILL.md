---
name: scientific-paper-writing
description: Draft, revise, or review scientific papers for clear structure, concise prose, consistent terminology and notation, defensible claims, and publication-ready figures, tables, equations, and references. Use for abstracts, titles, introductions, methods, results, discussions, conclusions, captions, full manuscripts, and paper-style technical writing, including AI/ML conference submissions. Follow the target venue and the user's explicit requirements over this skill's defaults.
---

# Scientific Paper Writing

Write for technically capable readers who may not share the authors' narrow specialty. Make the scientific contribution easy to find, the reasoning easy to follow, and the strength of each claim proportionate to its evidence.

This skill adapts the generally applicable guidance in the [ATLAS Style Guide](https://cds.cern.ch/record/1110290/files/gen-pub-2008-001.pdf). It deliberately omits ATLAS-specific terminology, collaboration procedures, author policies, templates, and physics-only conventions.

## Resolve constraints first

Apply instructions in this order:

1. the user's explicit request and intended meaning;
2. the target venue's current author instructions, template, and page limits;
3. established conventions in the manuscript or project;
4. the defaults in this skill.

Do not silently impose a preferred spelling system, citation style, section structure, voice, or typographic convention when the venue or manuscript already chooses one. Preserve valid LaTeX commands, labels, citations, mathematical notation, and domain terminology unless the task requires changing them.

Never invent results, methods, citations, comparisons, limitations, or numerical precision. Do not strengthen a claim beyond the evidence provided. When information is missing, use a clearly marked placeholder only if the user asked for a draft that permits placeholders; otherwise flag the gap concisely.

## Establish the paper's argument

Before drafting or substantially restructuring, identify:

- the intended audience and venue;
- the problem and why it matters;
- the specific gap in existing work;
- the paper's contribution or research question;
- the evidence that supports the central claims;
- the limitations and scope conditions.

Build a logical outline when the requested work is more than a local edit. Each section should advance the paper's argument. Keep background proportional to what readers need, and move secondary details out of the main narrative when they interrupt the logic.

For AI/ML papers, make the distinction between method, empirical evidence, and interpretation explicit. Tie claims of improvement, generality, efficiency, robustness, or autonomy to the evaluations that establish them. State important evaluation conditions, baselines, datasets, metrics, uncertainty, and limitations where the argument depends on them.

## Shape the main elements

### Title

Make the title concise, clear, descriptive, and specific enough to distinguish the work. Prefer sentence case unless the venue requires another style. Signal the actual contribution without promotional language or unsupported claims of novelty, generality, or superiority.

### Abstract

Make the abstract self-contained and readable as a single paragraph unless the venue specifies otherwise. Establish the problem or context, identify the approach, report the principal result or evidence, and state the main conclusion. Include concrete quantitative results when they are central and available.

Avoid citations, footnotes, undefined acronyms, unexplained symbols, and unnecessary jargon. Do not introduce information on which the main paper depends only in the abstract. Make the abstract inviting but do not overstate significance.

### Introduction

Move efficiently from the broader problem to the specific gap and contribution. Explain why the problem matters, summarize only the prior context needed to establish the gap, and make the paper's contribution easy to identify. Use a roadmap only when the organization is not already obvious or the venue expects one.

### Methods, evidence, and results

Describe the work with enough information to understand and assess the claims. Explain consequential choices and assumptions instead of merely listing them. Keep the distinction between observations and interpretation clear: present evidence precisely, then explain what it supports. Report uncertainty and failure conditions when they affect the conclusions.

### Discussion and conclusion

Interpret the findings in relation to the research question and prior work. State what the evidence supports, what it does not establish, and where the result is likely to apply. The conclusion should stand on its own, restate the main contribution and evidence without copying the abstract, introduce no new claims, and avoid references to figures or tables unless the venue convention favors them.

## Write clear scientific prose

- Prefer short, direct sentences and familiar words. Split sentences that carry several independent ideas.
- Use active voice when it makes the actor and action clearer. Use passive voice when the process or result matters more than the actor. Personal pronouns are acceptable when consistent with the venue and authorship context.
- Put the subject and main verb near each other. Avoid long introductory clauses and deep nesting.
- Give each paragraph one main purpose. State its point early, develop it with evidence or explanation, and connect it to the next step in the argument.
- Prefer precise verbs over abstract noun phrases and inflated wording. Remove throat-clearing, repetition, management language, and claims that merely announce importance.
- Avoid slang, fashionable expressions, metaphors that obscure technical meaning, and field-specific shorthand that the intended audience may not know.
- Define specialized terms and abbreviations at first use. Introduce an abbreviation only when it will be reused enough to reduce cognitive load.
- Use present tense for enduring facts, the paper's argument, and results being interpreted as current knowledge. Use past tense for completed procedures, data collection, training, and experiments. Describe document navigation in the present tense: “Section 3 presents,” not “Section 3 will present.”
- Keep tense internally consistent and prefer simple tenses when they convey the same meaning.

## Maintain consistency and precision

Choose one spelling variant and apply it consistently unless quotations or official names require otherwise. Keep terminology, capitalization, hyphenation, symbols, variable names, dataset names, model names, and notation consistent across text, equations, figures, tables, captions, and appendices.

Use hyphens where compound modifiers would otherwise be ambiguous, but do not over-hyphenate. Use punctuation to clarify structure, not to sustain sentences that should be split. Capitalize proper names and terms whose official form requires it; do not capitalize ordinary technical concepts for emphasis.

Use numbers and notation consistently:

- write a leading zero before a decimal fraction;
- use digits for measured values, units, decimals, and percentages;
- use appropriate significant figures and do not imply unsupported precision;
- put a nonbreaking space between a numerical value and its unit when the format supports it;
- use SI units unless the field or venue has a different established convention;
- typeset variables in italic and units and standard functions in roman type;
- use proper mathematical symbols rather than textual substitutes.

Treat equations as parts of sentences and punctuate them accordingly. Display equations that are not short and simple. Number only equations that are referenced or that the venue requires numbered.

## Make figures and tables carry evidence

Every figure and table must have a purpose in the argument and be cited in the text in a sensible order. Place it near the relevant discussion when the format permits.

- Use a consistent visual and typographic style throughout the paper.
- Prefer simple, information-dense graphics over decorative effects.
- Label every axis, row, and column clearly, including units where applicable.
- Use legends, line styles, markers, patterns, or direct labels so meaning does not depend on color alone.
- Check readability at the final publication size, including labels, subscripts, superscripts, line widths, and multi-panel tags.
- Retain editable source files and prefer vector formats for line art and plots when supported.
- Align numerical table entries by decimal point or another meaningful delimiter; use consistent precision.

Captions should make the figure or table understandable with minimal dependence on the main text. Define panels, symbols, curves, abbreviations, evaluation conditions, uncertainty representations, and normalization when they are needed for interpretation. Do not force readers to infer the mapping between a caption and multi-panel content.

## Handle sources responsibly

Follow the venue's citation and bibliography style. Cite relevant, durable, publicly accessible sources when possible, and prefer primary sources for technical claims. Verify bibliographic facts and that each citation supports the statement attached to it. Never fabricate a citation or cite a work solely because another paper cited it.

Use footnotes sparingly. Keep them brief and never place information essential to understanding the paper only in a footnote.

## Revise in passes

For a substantial revision, separate concerns so local polishing does not conceal structural problems:

1. **Argument:** Check that the problem, gap, contribution, evidence, and limitations form a coherent chain.
2. **Structure:** Reorder sections and paragraphs where needed; keep heading depth modest and balanced.
3. **Claims:** Match every important claim to evidence and calibrate scope, certainty, and novelty.
4. **Paragraphs and sentences:** Improve focus, transitions, syntax, concision, and word choice.
5. **Consistency:** Check terminology, notation, tense, spelling, capitalization, abbreviations, and references.
6. **Presentation:** Check figures, tables, equations, captions, cross-references, and final-size readability.
7. **Compliance:** Check the venue template, anonymity rules, page limits, required sections, and submission format.

Preserve the authors' technical intent and useful individual voice. Do not flatten all prose into uniform generic academic language. When revising user-provided text, return the requested deliverable first; add a short note only for unresolved scientific ambiguities, missing evidence, or consequential editorial choices.

## Final check

Before finishing, confirm that:

- the title and abstract accurately represent the paper;
- the contribution is explicit and supported;
- readers can follow the argument without hidden assumptions;
- claims do not exceed the reported evidence;
- terms, abbreviations, notation, units, and spelling are consistent;
- figures, tables, and captions are legible and interpretable;
- references and cross-references resolve correctly;
- the conclusion adds no unsupported claim; and
- the manuscript follows the target venue's instructions.
