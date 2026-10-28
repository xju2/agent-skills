---
name: software-tutorial-deck
description: Build a software tutorial / integration walkthrough deck: goal and deliverables, progressive algorithm build, architecture swimlanes, code stage by stage, validation, baseline comparison, caveats and status.
---

# Software Tutorial Deck

Build a slide deck that teaches how a piece of software works and where it lives in the code: what the algorithm does stage by stage, how it is integrated, how it was validated, and what is done and what is not. The audience should be able to follow the talk from slide titles and subtitle lines alone.

## When to use
- A tutorial or walkthrough of a software component, pipeline, plugin or integration.
- A project / qualification-task / milestone summary for a software or computing audience.
- A talk where the audience must understand both what the algorithm does and where it lives in the code.
Not for: marketing decks, pure results talks with no code, API reference docs.

## Step 1: Gather inputs (ask once, in one message)
1. Audience and venue, live or pre-read, slot length.
2. The goal and 3-6 concrete deliverables.
3. Pipeline stages in order, each with where it runs (CPU/GPU/service) and a one-line job.
4. One running example (one event/request/file) drawable after every stage, with a number per stage.
5. Code locations: repo, branch/tag, file path and line range per stage.
6. The exact run command / config flag.
7. Evidence: validation plots or benchmarks, baseline comparison, timeline of MRs/PRs with dates.
8. Known limitations and status of each deliverable (done / TBD).
Done when: each item is provided or marked "not available".

## Step 2: Storyboard (fixed arc)
1. Title: accent caps kicker, title, one-line subtitle, presenter + affiliations, event + date in accent, logo row.
2. Motivation: tinted "Goal" box + numbered deliverables (accent circles).
3. "How <X> works" build series: same title each slide, one stage per slide, same figure and scale accumulating state.
4. "What went into <codebase>": CPU/GPU swimlane architecture with real class names, short prose, monospace run command.
5. "Same <core>, <host> around it": standalone (gray) vs this integration (accent tint), rows Inputs / Shared code / After / Build.
6. "The code, stage by stage" series: one slide per stage, sub-stages 5a, 5b...
7. Validation and approval: dated MR timeline (merge in green) + before/after plot of the fix.
8. Compared with the baseline: plots + bullets with both numbers.
9. Caveats: two cards (e.g. Physics / Compute).
10. Summary: the same deliverables as slide 2 with status pills (green "done", outline "TBD").
11. Backup: "Backup: <topic>", one plot + short bullets.
Rules: slide 2 and Summary use identical wording; each series keeps one title; subtitle line = bold accent "<n> <Stage> (GPU)" then one sentence with a number.
Done when: the talk can be followed from titles + subtitle lines alone.

## Step 3: Code-stage slide archetype
- Breadcrumb strip of all stages (pills + arrows, CPU/GPU tag under each), current stage outlined/tinted in accent; second smaller breadcrumb for sub-stages.
- Left ~60%: editor-style code panel (window dots, file path, branch tag, line numbers, 9-10pt monospace, gray comments, green literals). 8-20 real lines; never invent code.
- Right ~40%: figure panel with caption bar ("ttbar, pileup 200" / "real event"), scale bar, one-line footnote.

## Step 4: Visual system
White background, one sans font, near-black bold titles top-left 32-36pt, body 16-18pt. One accent for step numbers, current stage, "this work" tints; green only for done/merged; everything else gray. Footer "<Event> - <Presenter> <short name>" + page number.

## Step 5: Copy rules
Every stage line carries a number or threshold; results bullets compare to baseline with both numbers; real identifiers in monospace; caveats stated plainly.

## Step 6: Build

Use the presentation tooling the agent has. If a dedicated slide or PowerPoint skill is installed, follow it; otherwise build the `.pptx` with [python-pptx](https://python-pptx.readthedocs.io/) (`pip install python-pptx`):

1. Set up the master first: slide size, fonts, colours, footer and page number, in the slide layouts rather than on each slide.
2. Build one slide of each series (build step, code stage, backup) and verify it before making the rest. Create the others from the same layout with the same shape positions and sizes, so geometry is identical across a series; change only text, highlight and figure.
3. Insert images with `slide.shapes.add_picture(path, left, top, width=...)`, giving the width only so the aspect ratio is kept.
4. Render every slide and look at it: `soffice --headless --convert-to pdf deck.pptx` then `pdftoppm -png -r 80 deck.pdf slide`, and inspect each PNG for overflow, overlap and text below 9 pt. Trim code lines rather than shrinking the font.

Done when: every slide has been rendered and inspected, the breadcrumb highlight matches the subtitle stage on every code slide, and slide 2 and the Summary use identical deliverable wording.
