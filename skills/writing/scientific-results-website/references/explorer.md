# Explorer: data bundle and component skeleton

## Markup (generated per page)

The explorer sits in a section with a stable `id`; the URL writer uses it as the anchor.

```html
<section id="explore">
<div class="explorer" data-kind="tokenizer" data-src="../tokenizer/explorer.json"
     data-base="../" data-version="docs/validation_v13">
  <div class="ex-top">
    <label class="pill-select"><span>Version</span><select class="ex-version"></select></label>
    <a class="ex-open" href="#">Open this validation →</a>
  </div>
  <div class="ex-tabs" role="tablist" aria-label="View">
    <button role="tab" data-tab="p1d" data-title="Flux power spectrum">P1D</button>
    <!-- one pill per view; data-title is the card title -->
  </div>
  <div class="ex-card">
    <div class="ex-head"><h3 class="ex-title"></h3><button type="button" class="ex-download"
        aria-label="Download the data behind this chart (CSV)" title="Download data (CSV)">⤓</button></div>
    <div class="ex-controls"></div>   <!-- in-card menus the view needs -->
    <div class="ex-legend"></div>
    <div class="ex-body chart"></div>
    <p class="ex-caption"></p>
  </div>
</div>
</section>
```

The download icon is decorative; the `aria-label` names the action for screen readers.

## Data bundle (one JSON per explorer)

```json
{
  "versions": [
    {"id": "docs/validation_v13", "version": "v13", "date": "2026-08-11",
     "arms": [{"run": "run_v13_main", "name": "v13 main"}, {"run": "run_v13_ctrl", "name": "v13 control"}]}
  ],
  "sims":  {"reference_run": {"p1d": {"k": [], "p": []}, "pk": {"field": {"k": [], "p": []}},
                              "hist": {"field": {"centers": [], "p": [], "domain": [-1, 0.5], "floor": 1e-6}},
                              "slices": "tokenizer/slices/reference_run", "ranges": {"field": {"lo": 0, "hi": 1}}}},
  "runs":  {"run_v13_main": {"sim": "reference_run", "p1d": {}, "pk": {"field": {"k": [], "p_reco": [], "ratio": [], "r": []}},
                             "hist": {"field": []}, "fields": {"field": {"l1": 0.0, "rmse": 0.0}},
                             "slices": "tokenizer/slices/run_v13_main", "error": {"field": {"span": 0.15, "unit": "dex"}}}},
  "fields": ["baryon_density", "..."], "fieldNames": {}, "fieldShort": {}
}
```

Keep the reference's own curves once (under `sims`), not repeated per run. Every path is relative to the library root and joined with `data-base` in the browser.

## Component skeleton (vanilla JS)

```js
function explorer(root) {
  fetch(root.dataset.src).then((r) => r.json()).then((D) => {
    const q = new URLSearchParams(location.search);
    const S = { version: q.get("v") || root.dataset.version, tab: q.get("tab") || "p1d",
                field: q.get("field") || D.fields[0] };
    let touched = false;                       // write URL state only after interaction
    const views = {
      p1d(ctx)  { /* controls.innerHTML = ""; lineChart(body, {...}); legend; caption; csv = [...] */ },
      pk(ctx)   { /* controls.innerHTML = fieldMenu(...); ... */ },
    };
    const render = () => {
      const ctx = contextFor(S.version);       // version + its arms with colours and dashes
      markSelectedTab(S.tab);
      title.textContent = `${tabTitle(S.tab)} · ${ctx.v.version}`;
      views[S.tab](ctx);                       // each view fills controls, legend, body, caption, csv
      bindControls(() => { touched = true; render(); });
      if (!touched) return;
      const u = new URLSearchParams(location.search);
      u.set("tab", S.tab); u.set("field", S.field);
      // Persist the version too, unless it is the page's own result (keeps links short).
      if (S.version !== root.dataset.version) u.set("v", S.version); else u.delete("v");
      const anchor = root.closest("section[id]")?.id;
      history.replaceState(null, "", `${location.pathname}?${u}${anchor ? `#${anchor}` : ""}`);
    };
    render();
  });
}
document.querySelectorAll(".explorer").forEach(explorer);
```

Each view is a small function: set its controls (or none), draw into the card body, set the legend and caption, and set the CSV payload (or `null` to hide the download button). New result kinds reuse the shell and add their own views.

## Chart building blocks worth having

- **Multi-panel line chart**: shared x axis (log or linear), per-panel y axis, a clipped tolerance band and reference line per panel, crosshair tooltip that snaps to the reference's x values.
- **Dot rows**: one row per category (field, codebook level), one marker shape per series, a grey line spanning the series; log or linear x.
- **Forest plot**: one row per paired comparison, mean and 95% interval, colour by sign when the interval excludes zero, p-value at the right.
- **Per-target chart**: targets ordered by environment on x, single samples as open marks, means as filled marks joined by lines.
- **Wipe compare**: two stacked images with a `clip-path: inset(0 0 0 var(--pos))` top layer, a handle, and a range input for keyboard users.
