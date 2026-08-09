---
name: insurance-sector-school
description: Builds a plain-English educational explainer (HTML artifact or in-chat answer) teaching how to read Indian insurance-company metrics — VNB, VNB Margin, Embedded Value, RoEV, Persistency, Combined Ratio, CISR, Solvency Ratio, TPA, GWP/APE/GDPI — using the manufacturing-company analogy and worked numeric examples, optionally personalized to a specific company's real numbers. Use this whenever the user is confused by insurance jargon, asks "what is VNB/embedded value/combined ratio/persistency", wants to "learn" or be "taught" how insurance companies are analyzed, is new to investing in insurance stocks, or asks "how do I read this dashboard/these numbers".
---

# Insurance Sector School

A teaching skill — no company-specific data is strictly required (it can run standalone as pure
education), but it becomes much stronger when grounded in a real company's actual numbers as the
worked example. Read `references/metrics-glossary.md` in full before writing anything — it is the
canonical source of every definition and the manufacturing analogy this skill is built around, and
its **Source Hierarchy & Attribution** section governs how to source any real numbers used as worked
examples: prefer the company's own filings over aggregator sites, and flag any conflicting figures
rather than silently picking one. Read `references/design-system.md` for the card/table CSS if
producing an HTML artifact.

## Step 1 — Figure out the scope and depth

- **Pure concept explainer** ("what is VNB?") → a short, direct in-chat answer is usually enough:
  1-2 paragraphs, the manufacturing analogy line, and one small worked numeric example. Don't force an
  HTML artifact for a single-term question.
  - **Full "school" reference document** (the person wants to understand the whole metric system, is
  studying for investing, or explicitly asks for a guide/cheat-sheet) → build the full HTML artifact.
- **Personalized to a company** — if the user names a company or you're already mid-analysis of one in
  the conversation, pull its real disclosed numbers (from what's already been discussed, or search if
  needed) into the worked examples instead of generic placeholder numbers — concrete real numbers teach
  faster than invented ones.

## Step 2 — Structure the full artifact (when warranted)

1. **Manufacturing vs Insurance analogy table** (from the glossary) — always lead with this; it's the
   single fastest mental model for a newcomer.
2. **Quick reference table** — "what to watch by category" (Life / Health / General / TPA), from the glossary.
3. **Metric cards**, grouped by category, each following this exact pattern (mirrors the source
   dashboards' proven format):
   - A short colored "tag" badge with the metric's short code (e.g. "VNB", "COMB", "SOLV")
   - Full name + one-line "= X in Manufacturing" analogy subtitle
   - "What it is" / "Formula" — 2-3 sentences, plain English, no unexplained jargon
   - A worked "💡 Example" box: use real numbers (a named company's actual disclosed figures) walking
     through the calculation step by step, ending with what the result means for that company specifically.
4. **IRDAI regulatory quick-reference table** (from the glossary) if the audience needs to understand
   solvency/investment rules.
5. **Closing "How to read a company in 60 seconds" box** — a 3-column checklist (Life / Health /
   General, or fewer if scope is narrower) of 5 yes/no questions a reader should ask, optionally with
   a specific company's actual checklist answers filled in if this is personalized.

## Step 3 — Tone and pedagogy rules

- Always define a term before using it elsewhere in the same document — don't assume the reader already
  knows VNB when explaining Embedded Value, for instance.
- Prefer one concrete worked example over an abstract formula-only explanation.
- Keep each metric card self-contained — a reader should be able to jump straight to "Combined Ratio"
  without having read the ones before it.
- Don't turn this into investment advice — the point is to teach the reader to interpret numbers
  themselves, not to tell them what to do with the interpretation.

## Step 4 — Save and present

If a full artifact: save to `/mnt/user-data/outputs/Insurance_Metrics_School<_CompanyName>.html`, call
`present_files`. If it was a quick concept question, just answer in chat — no file needed.
