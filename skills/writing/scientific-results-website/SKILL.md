---
name: scientific-results-website
description: Build and maintain a static website that presents a research project's scientific results — a curated public overview plus a structured, hierarchical results library that becomes the project's primary place to share and store results. Use when asked to publish, showcase, organise or share simulation, ML-model, validation or benchmark results on a web page or project site; to turn reports, logs and evaluation outputs into browsable pages; or to add interactive plots (spectra, distributions, slices, per-target or per-version comparisons) to such a site. Not for papers, slide decks or dashboards of live operational metrics.
---

# Scientific Results Website

Turn a project's results into a site that a collaborator can browse and a newcomer can trust: one curated overview page, and a results library that holds everything, organised by what it is about. The site is generated from the project's own reports and evaluation outputs, so it stays the single place results are shared and kept.

## Resolve constraints first

Before designing anything, establish:

1. **Where it is served and who can see it.** A path served as static files (lab web space, GitHub Pages, an object store). Assume everything published is world-readable unless the host says otherwise, and say so to the user before publishing internal logs.
2. **What the results are.** Inventory the sources: written reports (Markdown, notebooks), evaluation outputs (JSON, NPZ, HDF5, text tables, figures), catalogs or databases. Note which are produced by a tool the project already has.
3. **The dimensions of the results.** Typically *which result* (model version, checkpoint set, simulation), *which view* (statistic or QA category) and *which quantity* (field, metric, target). These drive the page design.
4. **What compute is allowed.** If a statistic the pages need does not exist yet, ask before using shared compute (batch or interactive allocations) to make it.

Follow the user's explicit requirements over this skill's defaults.

## Information architecture

Two views of one site. The split is a reading level, not access control: everything is reachable from the same site.

- **Overview (public-facing).** A hand-written, long-form page in the style of a model announcement: title, short dek, one interactive hero figure, a few chapters with key numbers and one or two interactive charts each. Only verified numbers. Each figure links to the full result behind it ("Full report →").
- **Results library (developer-facing).** Generated, exhaustive and hierarchical:
  - `results/` — home: a few headline numbers, one card per area with its latest entries, what the overview uses, recently updated.
  - `results/<area>/` — area page: an explorer for the area's structured results (below), then series tables, then reports, logs and documents grouped by kind.
  - `results/<kind>/<name>/` — one page per result, with breadcrumbs and a sticky table of contents.
  - `results/all/` — the ledger: every entry, newest first, with search and filters.

Promotion is a flag, not a copy: mark a result `public: <section>` in the registry; the library shows a "Public · Section" badge linking to the overview section, and the overview links back.

## Generate the library from sources

Write one build script, kept in the project repository, that regenerates the whole library from scratch on every run:

- **Auto-discover** written reports (for example every `docs/*.md` and `tasks/*.md`) and attach the figures of each task's working folder. Skip generated caches when discovering figures.
- **A small registry file** (YAML) adds what discovery cannot know: results that live outside the repository (evaluation reports, figure directories), structured kinds and their parameters (for example the arms of a validation), title or area overrides, series definitions, short labels for menus, and `public:` flags.
- **Dates come from the report's own `Date:` line** when it has one, else the last change. Git commit dates reorder results whenever a report is edited.
- **Rewrite links**: links between reports become library links; local images are copied next to the page; links to code or data paths become plain annotated text rather than broken links.
- **Write data bundles**, not data embedded per page: one compact JSON per explorer (round to about five significant figures), plus shared image folders, so every page that shows the explorer uses the same files.
- **Skip unreadable files** (shared storage often has files owned by others) instead of failing.
- **Fix permissions** at the end (directories `o+rx`, files `o+r`) when the host serves only world-readable files.

No build tools or JavaScript libraries are needed: hand-written HTML/CSS, one small vanilla-JS file for charts, inline SVG, and web fonts.

## The explorer pattern

When results have three dimensions, show them in one component instead of a long page of charts:

1. **A menu for the result** (version, checkpoint set, report), newest first, with "Open this result →" when it differs from the page's own.
2. **Pill tabs for the view** (for example Slices, P1D, Power spectrum, r(k), PDF, Pointwise error, Codebooks).
3. **One card** with the view's title, an in-card pill menu for the quantity (field, metric, target, arm), a legend with real line or marker samples, the chart, a one-paragraph caption that states units, normalisation and what "good" looks like, and a download button for the plotted data as CSV.

Rules that matter:

- The same explorer heads the area page and every result page, preselected to that result.
- Keep state in the URL (`?tab=…&field=…&v=…`) so a link opens one exact chart, but write it **only after the reader interacts**, and always with the explorer's own anchor, so plain links and links to other sections stay clean.
- Hide controls a view does not use; show "not available for this version" rather than an empty chart.
- Keep precise numbers in tables below the explorer; the explorer is for seeing, tables are for quoting.

See [references/explorer.md](references/explorer.md) for the data bundle shape and the component skeleton.

## Structured result pages

For each structured kind (a validation, a QA report, a benchmark run):

1. **Header**: kicker (kind · version), title, dek, date, area, public badge, source path.
2. **At a glance**: three or four key-number tiles, each with its change against the comparison arm or baseline (coloured by whether it is an improvement), then the report's own Summary section.
3. **The explorer**, preselected.
4. **Tables**: per-quantity metrics with the better value in bold, health or diagnostic statistics, flagged samples.
5. **Provenance**: run identifiers, checkpoints with a hash prefix, configs, inputs; downloadable data files.
6. **The written report**, each top-level section folded (`<details>`), so the page is structured but nothing is lost.

Plain documents get a header, a table of contents from their headings, and their figures in a grid.

## Scientific figures

- **Compare against the reference, always.** The reference (simulation, truth, baseline) is drawn in ink, every other series in a distinct colour and dash; add a ratio panel with a shaded tolerance band (±1%, ±5%, ±10%) under spectra and distributions.
- **Use the statistics the field uses**: dimensionless power Δ²(k) on log axes, cross-correlation r(k) with an r ≥ 0.9 band, PDFs on a log axis, paired differences with confidence intervals as a forest plot, per-target results ordered by environment. Mark physical scales on the axis (for example the resolution of one token or cell).
- **Slices**: same colour scale from the reference for every run; a drag-to-compare view of reference and reconstruction plus an error map whose range is about ten times the typical error, so structure is visible; a full-plane and a native-resolution zoom. Choose planes away from artificial boundaries (chunk or tile faces), which would overstate artifacts, and say in the caption what visible seams are.
- **If a needed statistic does not exist, compute it** rather than showing a placeholder, and validate the new code before trusting it: compare against a direct calculation on a small case, and check a control quantity that should come out right.
- **When a number is surprising, check the pipeline first, then explain it in the caption.** A real finding stated plainly in the caption is worth more than a figure that looks good.

## Verify before handing over

Serve the site locally (`python -m http.server`) — shared hosts are often slow — and drive it with a headless browser (Playwright) at desktop and phone widths:

- no console errors, no failed requests, no page-level horizontal scroll;
- click every tab and change every menu at least once; screenshot each view and look at it;
- when something overflows, list the elements whose right edge passes the viewport instead of guessing.

See [references/pitfalls.md](references/pitfalls.md) for the failures that recur.

## Keep it the primary store

After the site exists, every new result goes through it: write the report, add structured outputs to the registry, rebuild. Record in the project's task notes how to regenerate each data product, and keep generated data and caches out of version control while keeping the build scripts in it.

Done when: every area page and structured page loads with no errors at desktop and phone width, every explorer view has been exercised, the overview's numbers match the library, and the user knows the site is public.
