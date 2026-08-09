---
name: insurance-verdict-scorecard
description: Builds a comparative "verdict" scorecard (HTML artifact) ranking or comparing Indian insurance companies across Growth, Profitability, Moat, and Valuation dimensions, culminating in a category-winner / best-in-class call and a comparative investment-scorecard table. Use this whenever the user asks "which is better", "who wins", wants a "verdict", "scorecard", "ranking", "best insurance stock", or wants a side-by-side final call comparing two or more of LIC, ICICI Prudential Life, HDFC Life, SBI Life, Axis Max Life, Star Health, Niva Bupa, ICICI Lombard, Medi Assist, or other Indian insurers.
---

# Insurance Verdict & Comparative Scorecard

Produces the synthesis output that sits on top of the other insurance skills — pulls together growth,
profitability, moat, and valuation signals into a final comparative read and (for 3+ companies) a
"category winner" call. Read `references/design-system.md` for the `.score-row`/scorecard table
patterns and `references/metrics-glossary.md` for the benchmark thresholds used to score each
dimension. Follow that file's **Source Hierarchy & Attribution** section whenever pulling figures
from the web: prefer the company's own filings over aggregator sites, and flag any conflicting
figures you find rather than silently picking one.

**Guardrail**: this is a research/education synthesis, not investment advice. Frame the "winner" as
"best quarter/best fundamentals by the numbers reviewed" — never as a buy/sell/hold recommendation in
your own voice. If the user explicitly wants brokerage buy/sell views, only report *named, real*
brokerage calls you can substantiate (from the data provided or a web search) — never invent one.

## Step 1 — Gather comparable data across companies

Pull the underlying numbers via the same discipline as other skills in this family. You need, at
minimum, one growth metric, one profitability/margin metric, one balance-sheet/capital metric, and
(if available) a valuation multiple (P/EV for life, P/B for general/TPA) per company.

## Step 2 — Score each company across 4 lenses (adapt per category — don't force a life-insurer lens onto a TPA)

- **Growth** — topline/new-business growth vs peers and vs its own prior period.
- **Profitability** — VNB margin / Combined Ratio / PAT growth / EBITDA margin, whichever fits the
  category, benchmarked against the glossary's "what good looks like" thresholds.
- **Moat** — pull from (or quickly re-derive) the moat thesis: distribution scale, brand, data edge, capital cushion.
- **Valuation** — cheap/fair/expensive relative to the metric investors actually use for that category
  (P/EV for life insurers, P/B or P/E for general/TPA) — only state this if you have real market-cap/
  valuation data; otherwise omit the column rather than guess.

## Step 3 — Build the HTML

1. A hero "Star Player" or headline verdict card (gradient background per design system gold accents)
   naming the standout company for the period with 3–4 supporting KPI mini-boxes and a 3–5 sentence
   "why" paragraph that explicitly acknowledges the runner-up's case too (avoid one-sided cheerleading —
   note what the runner-up did better, e.g. "Company B grew GWP faster, but Company A's underwriting
   quality was structurally stronger").
2. Individual "Business & Investment Analysis" cards per company (badges + 4 KPI boxes + one analysis
   paragraph each) if doing a multi-company deep dive.
3. A "Comparative Scorecard" table: rows = companies, columns = Category tag, Growth, Profitability,
   Moat, Valuation (score out of 10 or a short qualitative tag), an Analyst-style stance badge if you
   have real sourced views, and a one-line Key Risk per company.
4. A "Category Winner" table if spanning categories (Life/Health/General/TPA), naming the best-in-category
   company with a one-line reason, plus an overall pick if the user wants one clear headline call.
5. Close with a short "Investment Theme / Outlook" paragraph tying the individual verdicts to the
   sector-level structural story (from `references/metrics-glossary.md` context), and a disclaimer line.

## Step 4 — Save and present

Save to `/mnt/user-data/outputs/<Scope>_Verdict_<Period>.html`, call `present_files`. Keep the chat
reply to the one-line headline verdict — let the artifact carry the supporting detail.
