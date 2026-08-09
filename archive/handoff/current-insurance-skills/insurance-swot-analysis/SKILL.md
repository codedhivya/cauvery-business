---
name: insurance-swot-analysis
description: Builds a SWOT analysis (HTML artifact, 4-quadrant grid) for one or more Indian insurance companies — Strengths, Weaknesses, Opportunities, Threats, each grounded in the company's actual latest disclosed numbers rather than generic statements. Use this whenever the user asks for a "SWOT", "SWOT analysis", "strengths and weaknesses", "pros and cons", or wants a structured bull/bear-style qualitative read on LIC, ICICI Prudential Life, HDFC Life, SBI Life, Axis Max Life, Star Health, Niva Bupa, ICICI Lombard, Medi Assist, or any other Indian insurer.
---

# Insurance SWOT Analysis

Produces a evidence-grounded SWOT grid — the discipline here is that every bullet must trace back to
an actual disclosed number or fact, not a generic insurance-industry cliché. Read
`references/design-system.md` for the `.swot-grid`/`.swot-cell` 4-quadrant CSS pattern and
`references/metrics-glossary.md` for category-specific "what good/bad looks like" benchmarks to judge
strengths vs weaknesses against (e.g. VNB margin >25% is a strength for a life insurer, <20% is a
watch item). Follow that file's **Source Hierarchy & Attribution** section whenever pulling figures
from the web: prefer the company's own filings over aggregator sites, and flag any conflicting
figures you find rather than silently picking one.

## Step 1 — Gather the latest numbers

Use the same sourcing discipline as the other skills (user-supplied data first, then web search for
the specific company/period; never fabricate). You need enough data points to ground at least 3–4
bullets per quadrant — if data is thin, keep the analysis proportionally shorter rather than padding
with generic filler.

## Step 2 — Derive each quadrant with discipline

- **Strengths** — things the company is verifiably good at *right now*, cited with a number (market
  share %, margin %, growth rate, solvency level, network size).
- **Weaknesses** — things that are verifiably lagging peers or its own prior period (a metric that
  missed guidance/estimates, a ratio above/below the healthy benchmark, a concentration risk with a %).
- **Opportunities** — external or structural tailwinds the company is positioned to capture (regulatory
  changes like the 0% GST term-insurance exemption, underpenetration stats, untapped channels/products)
  — these should be forward-looking, not restated strengths.
- **Threats** — external or structural risks (competitive intensity from named peers, regulatory risk
  like IRDAI open-architecture bancassurance mandates, equity-market sensitivity of AUM/EV, concentration
  in one distribution channel).
- Cross-check: a "weakness" and a "threat" should not just be reworded — weakness = something already
  happening internally, threat = something that could happen to it externally.

## Step 3 — Build the HTML

1. `.co-hdr-swot` per company: name badge + full name.
2. `.swot-grid` (4-quadrant): top-left Strengths (`.swot-s`), top-right Weaknesses (`.swot-w`),
   bottom-left Opportunities (`.swot-o`), bottom-right Threats (`.swot-t`), each an unordered
   `.swot-ul` list of 3–6 short, number-grounded bullets (one line each, not paragraphs).
3. For a peer comparison, repeat one `.swot-grid` block per company inside a `.g2` grid so two SWOTs
   sit side by side, grouped under category section titles (`.cat-section-title`) if spanning categories.

## Step 4 — Save and present

Save to `/mnt/user-data/outputs/<Company_or_Sector>_SWOT_<Period>.html`, call `present_files`. Keep the
chat reply to one line — the artifact is the deliverable. Do not present the SWOT as investment advice;
it's a structured factual/qualitative read, not a recommendation.
