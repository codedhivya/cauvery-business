---
name: insurance-financials-tables
description: Builds detailed financial-results tables (HTML artifact) for Indian insurance companies — full line-by-line quarter or full-year P&L-equivalent tables (GWP/APE/VNB/VNB margin/PAT/Embedded Value for life insurers; GWP/Combined Ratio/Loss Ratio/PAT for health and general insurers; Revenue/EBITDA/PAT for TPAs) plus multi-year premium/revenue trend tables. Use this whenever the user asks for "financials", "results", "numbers in detail", "P&L", a breakdown of a company's quarter/year, or wants to see exact figures rather than a high-level summary — for LIC, ICICI Prudential Life, HDFC Life, SBI Life, Axis Max Life, Star Health, Niva Bupa, ICICI Lombard, Medi Assist, or any other Indian insurer.
---

# Insurance Financials — Detailed Results Tables

Produces the detailed, line-item financial tables behind a company's (or peer set's) results — the
layer below the KPI dashboard. Read `references/design-system.md` for table CSS classes
(`table`, `th`, `td.num`, `td.tpos`/`td.tneg`, `td.tb`) and `references/metrics-glossary.md` for
what each line item means and typical footnote caveats (e.g. consolidated vs standalone PAT,
one-off tax credits, MTM investment gains/losses distorting a quarter). Always follow that file's
**Source Hierarchy & Attribution** section when pulling figures from the web: prefer the company's
own filings over aggregator sites, and flag any conflicting figures you find rather than silently
picking one.

## Step 1 — Gather the numbers

Same sourcing rules as `insurance-dashboard-kpi`: use user-supplied data first, then web search for
the specific quarter's exchange filing / investor presentation / earnings-call transcript if you have
search access. Mark anything not disclosed as "Not disclosed" rather than guessing. Always capture,
where available:
- Current period value, same-period-last-year value, and the YoY % or bps change (compute it yourself
  if only the two raw numbers are given — don't rely on a pre-computed % that might be stale).
- Any asterisked caveat the company itself flagged (GST/tax one-offs, MTM swings, consolidated vs
  standalone basis, exceptional items) — put these in a `.fnote` under the table, never silently omit them.

## Step 2 — Pick the right table shape by category

**Life insurer table columns**: GWP/Total Premium, YoY, APE, VNB, VNB Margin, PAT, Embedded Value, Solvency.

**Health/SAHI table columns**: Period, GWP, YoY, Combined Ratio (or CISR), Loss Ratio, Expense Ratio,
Underwriting Profit/Loss, PAT, Market Share.

**General insurer table columns**: Period, GDPI, YoY, Net Earned Premium, Combined Ratio, Claims Ratio,
PAT, ROE, Solvency.

**TPA table columns**: Period, Revenue, YoY, EBITDA, EBITDA%, PAT (Reported), PAT (Adjusted — if it
diverges from reported, always show both and footnote why), Premiums Administered.

If comparing multiple companies of the *same* category, put them in one table (rows = companies) so
the reader can scan across. If comparing across categories (e.g. a life insurer vs a health insurer),
use separate tables per category — don't force incompatible metrics into one row set.

## Step 3 — Build the HTML

1. Header + short section title identifying the period and "as reported" basis.
2. One `<table>` per category/company-group as scoped above, using `td.num`/`td.tpos`/`td.tneg` for
   right-aligned figures with color-coded direction.
3. A `.fnote` block under each table for caveats (mandatory whenever a one-off item, basis change, or
   consolidated/standalone distinction exists — this is where past dashboards lost credibility if skipped).
4. Optional: a "3-Year Trend" table (FY-2, FY-1, current FY, with 2Y CAGR) if the user wants historical
   context and you can source it — otherwise skip rather than fabricate history.

## Step 4 — Save and present

Save to `/mnt/user-data/outputs/<Company_or_Sector>_Financials_<Period>.html`, call `present_files`.
If the user just wants 2–3 numbers conversationally, answer inline in chat instead of forcing a file —
this skill is for when they want the full table.
