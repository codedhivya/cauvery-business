---
name: insurance-charts-visualizer
description: Builds interactive Chart.js visualizations (HTML artifact) comparing Indian insurance companies — bar charts for VNB/APE/PAT/GWP, Combined Ratio charts with a 100% breakeven reference line, Solvency Ratio charts with the IRDAI 150% minimum line, and multi-metric switchable charts. Use this whenever the user asks to "chart", "graph", "visualize", "plot", or "compare visually" any Indian insurance company's metrics, wants to see trends over time, or wants a side-by-side visual comparison between insurers (e.g. LIC vs HDFC Life, or Star Health vs Niva Bupa).
---

# Insurance Charts — Interactive Visualizer

Produces Chart.js-powered comparison charts for Indian insurance companies, packaged as a single
HTML artifact. Read `references/design-system.md` §6 for the exact Chart.js patterns (value-label
plugins, breakeven/minimum reference lines) and §3 for the company color palette — always color each
company's bar/line with its assigned color so charts stay visually consistent with other skills'
outputs in the same conversation. Read `references/metrics-glossary.md`'s **Source Hierarchy &
Attribution** section when pulling any figure from the web — prefer the company's own filings over
aggregator sites, and flag any conflicting figures you find rather than silently picking one.

## Step 1 — Confirm what's being compared

- **Metric(s)**: PAT, VNB, VNB Margin, APE, GWP/GDPI, Combined Ratio, Solvency Ratio, AUM, EV, etc.
- **Companies**: one company over time, or multiple companies for one period.
- **Time axis**: single period (bar chart across companies) vs multi-period trend (line/bar across
  quarters or years for one or more companies).
Gather the underlying numbers the same way as `insurance-financials-tables` (user-supplied or web
search; never fabricate).

## Step 2 — Pick the chart type

- **Cross-company single-metric comparison** → vertical bar chart, one bar per company, colored by
  company palette, value labels drawn above each bar (don't rely on hover tooltips alone).
- **Trend over time (one or more companies)** → grouped bar or line chart, x-axis = periods, one
  dataset per company.
- **Combined Ratio / CISR** → bar chart + dashed red horizontal line at 100% labeled "Breakeven",
  drawn via an `afterDraw` plugin. Color bars green-tint if below 100%, red-tint if above.
- **Solvency Ratio** → horizontal bar chart (`indexAxis:'y'`) + dashed red vertical line at 150%
  labeled "IRDAI Minimum 150%".
- **VNB Margin / other %-based metrics with a natural "good" threshold** → same reference-line pattern,
  documented value in the chat reply so the user knows what the line represents.
- If the user wants to toggle between metrics interactively, add a small `.metric-sel` button row
  above the chart (see the `updateLifeChart`/`switchLifeMetric` JS pattern: swap `chart.data.datasets`
  and call `chart.update()`).

## Step 3 — Build the HTML

1. Minimal header (title + period), no need for full tab navigation unless bundling 3+ charts — then
   use the tab-nav pattern from the design system so each chart gets its own panel.
2. Each chart lives inside a `.card` with a `.card-lbl` title above the `<canvas>`.
3. Always disable Chart.js legends for single-dataset bar charts; keep legends for multi-company
   trend charts so colors are labeled.
4. Add one sentence of plain-English takeaway text under each chart — a chart without a stated
   takeaway forces the reader to do the analysis themselves, which defeats the point of the artifact.

## Step 4 — Save and present

Save to `/mnt/user-data/outputs/<Scope>_Charts_<Period>.html`, call `present_files`. If the user only
wants one quick chart and is clearly going to keep chatting (not asking for a saved file), consider
using the Visualizer tool for an inline chart instead of a saved HTML artifact — use judgment based on
whether they said "show me" (inline is fine) vs "give me a dashboard/file I can share" (save the HTML).
