# Recurring pitfalls

## Typography and SVG

- **Web fonts lack superscript and subscript digits** (`⁻⁴`, `₁₀`) and some math brackets (`⟨⟩`). They render as boxes. In SVG tick labels draw exponents as a `<tspan dy="-6" font-size="0.72em">`; in HTML use `<sup>`/`<sub>`; write `x / mean(x) − 1` instead of `⟨x⟩`. Latin-1 `²` and `³` are usually safe.
- **Bands and reference lines leak into the neighbouring panel** when a panel's range excludes them. Clip each panel's band and reference line to that panel, and make ratio-panel ranges include 1.
- **Charts inherit the body serif** unless the container sets the sans font; give every chart container the chart class.

## Layout

- **Long unbroken strings widen the page on phones**: file paths in `<code>`, wide `<select>` options, nowrap pill labels. Use `overflow-wrap: anywhere` on `main code`, cap select widths on small screens, and let pill bars scroll inside their own box.
- **Wide charts** keep a minimum width and scroll inside their card on phones; the page itself must not scroll sideways.
- **Find overflow by measurement**: in the headless browser, list elements whose `getBoundingClientRect().right` exceeds `innerWidth`, excluding chart and table scrollers.

## Data and content

- **Ordering by git dates is wrong** once old reports are edited; prefer the report's stated date, with registry order as the tie-break.
- **Figures from generated caches** get picked up by figure discovery if the cache lives in a task folder; exclude it.
- **Files owned by other users** on shared storage can be unreadable; check `os.access` and skip.
- **Boundary artifacts**: a slice taken exactly on a chunk or tile face overstates seams; take a mid-chunk plane.
- **Error-map colour range**: a range far above the typical error renders a blank map; use about ten times the median error.
- **A ratio below 1 on every scale with r ≈ 1** means an amplitude deficit, not misplaced structure — often a lost high tail of the distribution. Confirm against a control quantity (another field) before reporting it, then explain it in the caption.

## Process

- **Shared hosts are slow**; preview with a local static server and a headless browser, then spot-check the live URL.
- **`pkill -f <pattern>` can match the shell running it** when the pattern also appears in that command line; anchor the pattern (`^python3 -m http.server 8765`) or kill by PID.
- **Heavy statistics belong on compute nodes**; reading large volumes from network storage dominates the time, so read each reference once and reuse its transform for every comparison.
- **Do not edit run records to make a page look right**; fix the page or the build script.
