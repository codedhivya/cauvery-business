# Mode: Charts — Interactive Visualisations

Chart.js comparisons packaged as a single HTML artifact. A good chart here answers a question the reader
already has; a bad one makes them do the analysis themselves.

Read `design-system.md` §6 for the Chart.js patterns and the palette rule. Read the loaded sector file
for **chart reference lines** — the thresholds that matter in that sector and what each one means.

## Step 1 — Confirm what's being compared

- **Metric(s)** — from the sector file's metric set, or a universal metric for cross-sector work.
- **Entities** — one company over time, or several companies in one period.
- **Time axis** — a single period (bar across companies) or multiple periods (trend).

Source the underlying numbers exactly as `financials.md` does. Never fabricate a data point; a chart
makes an invented number look more authoritative than a table does, which makes it more damaging.

## Step 2 — Pick the chart type

- **Cross-entity, single metric** → vertical bar, one bar per company in its palette colour, value
  labels drawn above each bar.
- **Trend over time** → grouped bar or line, x-axis = periods, one dataset per company, legend kept.
- **A metric with a meaningful threshold** → bar chart plus a dashed reference line at that threshold,
  labelled with what it represents. Take the threshold and its label from the sector file — it is
  sector knowledge, not a chart property. Tint bars by which side of the line they fall on.
- **A ratio where lower is better, or a ranked list** → horizontal bar (`indexAxis:'y'`), which reads
  more naturally for rankings and leaves room for long company names.
- **Several metrics the reader may want to toggle** → add a `.metric-sel` button row; the handler swaps
  `chart.data.datasets[0].data` and calls `chart.update()`.

## Step 3 — Build

1. Minimal header (title, period). For 3+ charts, use the tabbed layout so each chart gets its own panel.
2. Each chart inside a `.card` with a `.card-lbl` title above the `<canvas>`.
3. Disable the legend for single-dataset bars; keep it for multi-company trends where colour needs
   naming.
4. Initialise charts lazily on tab-open — canvases sized while hidden come out wrong.
5. **One sentence of plain-English takeaway under each chart.** A chart without a stated takeaway hands
   the interpretive work back to the reader, which is the opposite of what the artifact is for.

## Scope behaviour

**Single company** — trend over time is usually the more informative shape than a one-bar comparison.
**Pair / sweep** — cross-company bars for a period, or multi-series trends.
**Cross-sector** — chart only universal metrics. Sector-specific thresholds (a regulatory minimum, an
industry breakeven) apply only within their own sector's chart, never across a mixed set, since the same
line means different things in different sectors.

## Deliver

Follow `output-conventions.md`. If someone wants one quick chart mid-conversation rather than a file to
keep, an inline chart is the better answer — use judgement on "show me" versus "build me something I can
share".
