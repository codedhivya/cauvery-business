---
name: insurance-dashboard-kpi
description: Builds a KPI snapshot dashboard (HTML artifact) for one or more Indian insurance companies — PAT, VNB, VNB margin, GWP/GDPI, Combined Ratio, Solvency, AUM etc. shown as headline KPI cards plus per-company summary cards, grouped by Life/Health/General/TPA. Use this whenever the user asks for an insurance company "dashboard", "snapshot", "overview", "at a glance" view, or wants headline numbers for LIC, ICICI Prudential Life, HDFC Life, SBI Life, Axis Max Life, Star Health, Niva Bupa, ICICI Lombard, Medi Assist, or any other Indian insurer — even if they don't say the word "dashboard" explicitly (e.g. "give me the numbers for HDFC Life this quarter").
---

# Insurance Dashboard — KPI Snapshot

Produces the top-level "at a glance" view of one or more Indian insurance companies for a given
period (quarter or full year): a KPI strip + per-company summary cards, grouped by category
(Life / Health / General / TPA). This is the entry-point view — pair it with other insurance skills
(financials, charts, SWOT, moats, verdict) if the user wants deeper analysis, or use
`insurance-quarterly-report` directly if they want the full multi-tab dashboard in one go.

Read `references/design-system.md` before writing any HTML — it has the CSS variables, company
color palette, and reusable card classes. Read `references/metrics-glossary.md` for metric
definitions and what "good" looks like per category — and always follow its **Source Hierarchy &
Attribution** section when pulling any figure from the web: prefer the company's own filings over
aggregator sites, and flag any conflicting figures you find rather than silently picking one.

## Step 1 — Scope the request

Figure out, from the user's message (ask only if genuinely ambiguous):
- **Which company/companies?** One company, a peer set, or "the sector" (pick 5–8 representative names).
- **Which period?** A specific quarter (e.g. Q1 FY27) or full year. If not stated, ask or default to
  the most recent period you can find reliable data for.
- **Data source**: if the user pasted numbers or uploaded a file, use those. Otherwise, web-search for
  the company's latest quarterly results / investor presentation (search terms like
  "<company> Q<n> FY<yy> results VNB combined ratio investor presentation"). Never fabricate figures —
  mark anything unavailable as "Not disclosed this period."

## Step 2 — Classify each company

| Category | Headline KPIs to show |
|---|---|
| Life | PAT, VNB, VNB Margin, APE, Solvency, AUM/EV |
| Health (SAHI) | PAT, GWP, Combined Ratio (or CISR), Loss Ratio, Solvency |
| General | PAT, GDPI, Combined Ratio, Solvency, ROE |
| TPA | Revenue, PAT (reported vs adjusted if they diverge), EBITDA margin, Market Share |

## Step 3 — Build the HTML

Structure (single HTML file, no tabs needed for this skill — it's a single-panel snapshot):
1. Dark header bar with title, period, and a colored chip per company (see design system §3 palette).
2. KPI strip (`.kpi-row`) — 4–6 headline numbers with YoY/QoQ delta arrows (▲/▼, `.pos`/`.neg`).
3. Category section headers (`.cat-section-title`) grouping companies — Life, then Health, then
   General, then TPA — each followed by a grid of `.co-card` cards (use `.g2` for 2 cards, `.g3` for 3+).
   Each card: company name in its palette color, category tag, then 5–8 `.m-row` metric lines, then a
   `.badge-row` with 2–3 short takeaway badges (e.g. "VNB +26%", "CR above 100%").
4. A closing "Sector Quick Snapshot" card: a small table with cross-company context (market leader by
   metric, fastest grower, etc.) if 3+ companies are being compared.
5. Footer per design system §7.

If only one company was requested, skip the category grouping and just show one detailed `.co-card`
plus the KPI strip built from that company's own numbers (don't invent a sector comparison it didn't ask for).

## Step 4 — Save and present

Save to `/mnt/user-data/outputs/<Company_or_Sector>_Dashboard_<Period>.html`, then call `present_files`.
Keep the chat reply short — a one-line summary of the headline takeaway, then let the artifact speak.
