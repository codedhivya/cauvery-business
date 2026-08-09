---
name: insurance-quarterly-report
description: Builds a complete multi-tab quarterly (or full-year) intelligence dashboard (HTML artifact) for one, two, or several Indian insurance companies once their results for a given quarter are published — combining Dashboard/KPIs, Financials, Charts, Business Profile, Investments, SWOT, Analyst Ratings, Moats, and a Verdict tab, all in one navigable file, plus an optional AI Q&A chat panel. Use this whenever the user wants a full "quarterly results" dashboard, asks to analyze/compare a specific quarter (e.g. "Q1 FY27 results for HDFC Life and ICICI Pru", "build me a dashboard for LIC's latest quarter"), wants everything about a company's quarter in one place, or explicitly asks for a complete report rather than one narrow slice.
---

# Insurance Quarterly Report — Full Multi-Tab Dashboard

The master/composite skill: produces the complete tabbed dashboard that the other insurance skills in
this family each cover one slice of. Use this when the user wants the whole thing at once for a given
quarter (or full year) — one company, a head-to-head pair (e.g. ICICI Pru vs HDFC Life), or a sector
sweep of several companies. For a narrower ask ("just the SWOT", "just a chart"), prefer the focused
skill instead — this one is heavier and should be reserved for genuine "full dashboard" requests.

Read `references/design-system.md` in full before starting — it defines the header, tab-nav, and every
CSS class referenced below. Read `references/metrics-glossary.md` for definitions and category
benchmarks used throughout, and follow its **Source Hierarchy & Attribution** section for every figure
pulled from the web: prefer the company's own filings over aggregator sites, and flag any conflicting
figures you find rather than silently picking one — this matters even more here than in the focused
skills, since a full report aggregates many figures across many tabs. The individual skills `insurance-dashboard-kpi`,
`insurance-financials-tables`, `insurance-charts-visualizer`, `insurance-business-profile`,
`insurance-swot-analysis`, `insurance-moats-analysis`, `insurance-verdict-scorecard`, and
`insurance-sector-school` each describe one tab's content rules in more depth — consult the relevant
one if you want more detail on how to build a specific tab correctly.

## Step 1 — Scope: which quarter, which companies, how many tabs

- **Confirm the quarter/year** (e.g. "Q1 FY27" = Apr–Jun 2026) and that results are actually published
  for it — if a named company hasn't reported yet, say so rather than fabricating a result.
- **Confirm company scope**: single-company deep dive, a head-to-head (2 companies), or a multi-company
  sector sweep (group by Life/Health/General/TPA category).
- **Confirm depth**: if the user only cares about a subset of tabs, drop the ones they don't need — a
  focused 4-tab dashboard beats a bloated 11-tab one nobody asked for. Default full tab set: Dashboard,
  Financials, Charts, Business Profile, Investments & Returns, SWOT, Analyst Ratings, Moats, Verdict.
  Add a School tab if the audience seems to need the metric-education layer, and a CB-Assist-style Q&A
  panel only if the user specifically wants an interactive chat feature in the artifact.

## Step 2 — Gather data before writing any HTML

Collect, per company: PAT, VNB/Combined-Ratio-family metrics per its category, growth rates, solvency,
distribution/business-model facts, and (if available) analyst/brokerage views and valuation multiples.
Use whatever the user supplied first; web-search the specific quarter's investor presentation/exchange
filing/earnings-call commentary for anything missing, if you have search access. Never invent a number,
a brokerage call, or a quote — mark gaps as "Not disclosed this period" and keep going; a dashboard with
a few honestly-labeled gaps is far more trustworthy than one with confident fabrications.

## Step 3 — Build the page skeleton

1. **Header**: dark bar, `.hdr-left` title + sub-line (period, scope), `.hdr-right` company chips + a
   date chip.
2. **Tab nav**: one `.tab-btn` per included tab (see design system §5), each toggling a `.panel` with
   matching `id="tab-<name>"`, first one `active` by default. Emoji-prefix tab labels lightly (📊 💰 📈
   🏢 🏦 🔍 🎯 🛡️ 🏆 🎓) as the source dashboards do — it's a readability aid, not a requirement.
3. **Dashboard tab** — KPI strip + category-grouped `.co-card`s per `insurance-dashboard-kpi`'s rules.
4. **Financials tab** — per-category detailed tables per `insurance-financials-tables`'s rules,
   including a multi-year trend table if data supports it.
5. **Charts tab** — 2-4 Chart.js visualizations per `insurance-charts-visualizer`'s rules (metric-switcher
   buttons for the primary chart, plus a Combined-Ratio and/or Solvency chart with reference lines if
   relevant to the companies in scope). Charts must be initialized lazily on tab-open
   (`if (id==='charts') initCharts();` inside `showTab`) so canvases aren't sized incorrectly while hidden.
6. **Business Profile tab** — per `insurance-business-profile`'s rules, grouped by category.
7. **Investments & Returns tab** — IRDAI regulatory framework recap (`.reg-card`) + per-company
   `.inv-card` investment-portfolio breakdowns (AUM, yield, asset allocation, equity sensitivity) —
   include the Combined Ratio/EV market-sensitivity caveat where relevant (equity-market corrections can
   swing EV or MTM investment income sharply in a single quarter — always flag this if it happened).
8. **SWOT tab** — per `insurance-swot-analysis`'s rules, one 4-quadrant grid per company, grouped by category.
9. **Analyst Ratings tab** — only include real, sourced brokerage views (name the brokerage, the rating,
   target price if disclosed) with a clear disclaimer that this reflects third-party views, not the
   dashboard author's own recommendation. If no real brokerage data is available, omit this tab rather
   than inventing ratings.
10. **Moats tab** — per `insurance-moats-analysis`'s rules.
11. **Verdict tab** — per `insurance-verdict-scorecard`'s rules: hero headline call + comparative
    scorecard table + category winners if multi-category.
12. **School tab (optional)** — per `insurance-sector-school`'s rules, personalized with this dashboard's
    real numbers as worked examples.
13. **Footer**: data-as-of date, "for research/educational purposes only, not investment advice", and a
    plain statement that figures come from publicly available company disclosures.

## Step 4 — JS wiring

- `showTab(id, btn)` function toggling `.panel`/`.tab-btn` `active` classes (design system §5).
- Charts initialized once, lazily, guarded by an `inited` flag so switching tabs back and forth doesn't
  re-create canvases.
- If including an interactive metric-switcher (e.g. VNB vs APE vs Margin bar chart), keep a small
  `DATA` object keyed by metric name so the switch handler only swaps `chart.data.datasets[0].data` and
  calls `chart.update()` — don't rebuild the whole chart object on every click.
- Do not wire up any external API calls (e.g. a live LLM chat panel) unless the user explicitly asks for
  an interactive AI Q&A feature — if they do, keep it clearly labeled as a separate, optional feature and
  follow the same no-fabrication data discipline for any system-prompt "known facts" you embed in it.

## Step 5 — Save and present

Save to `/mnt/user-data/outputs/<Scope>_Q<n>FY<yy>_Dashboard.html` (or `_FY<yy>_Dashboard.html` for a
full year), call `present_files`. In chat, give a 2-4 sentence summary of the headline story for the
quarter before/after presenting the file — don't just silently drop the file with no framing.
