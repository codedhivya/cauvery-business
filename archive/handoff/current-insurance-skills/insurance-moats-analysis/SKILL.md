---
name: insurance-moats-analysis
description: Builds a competitive-moat / structural-advantage analysis (HTML artifact) for Indian insurance companies — identifies each company's durable competitive edge (distribution monopoly, embedded-value lock-in, brand franchise, data/AI network effects, diversified platform, etc.) grounded in real numbers. Use this whenever the user asks about a company's "moat", "competitive advantage", "USP", "why is this company hard to compete with", or wants a Buffett-style durability read on LIC, ICICI Prudential Life, HDFC Life, SBI Life, Axis Max Life, Star Health, Niva Bupa, ICICI Lombard, Medi Assist, or any other Indian insurer.
---

# Insurance Moats & USPs

Produces a structural-advantage writeup — deeper and more durability-focused than a SWOT strength;
a moat should be something a well-funded competitor *couldn't* replicate quickly even if it wanted to
(distribution scale built over decades, regulatory-license scarcity, proprietary data/AI, locked-in
embedded value, brand trust). Read `references/design-system.md` for the `.moat-card` layout and
`references/metrics-glossary.md` for the definitions underpinning moat claims (e.g. explain EV as
"locked-in future profit" when citing it as a moat). Follow that file's **Source Hierarchy &
Attribution** section whenever pulling figures from the web: prefer the company's own filings over
aggregator sites, and flag any conflicting figures you find rather than silently picking one.

## Step 1 — Identify moat candidates by category (don't force-fit if the company genuinely lacks one)

- **Life insurers**: bank/agent distribution scale that can't be replicated quickly (cite branch/agent
  counts), Embedded Value as locked-in decades of future profit, brand + government backing (for LIC),
  product-mix quality (annuity/protection leadership), independent EV validation by an actuarial firm
  (adds a governance-trust moat).
- **Health insurers**: hospital network breadth (cite count), claims-data depth built up over years
  (better actuarial pricing), digital CX / global-parent actuarial IP transfer (for JV-backed insurers),
  agent specialization vs generalist agents.
- **General insurers**: line-of-business diversification (few peers span Motor+Health+Commercial+Crop),
  investment-income engine size (cite portfolio ₹ and yield), balance-sheet solvency cushion enabling
  aggressive growth without capital raises.
- **TPA**: AI/data network effects (a fraud-detection or claims model that improves with every claim,
  raising insurer switching costs), market-share-driven data moat, platform-model stickiness.
- If a company genuinely has a thin moat (a new entrant, commoditized product, no distribution scale),
  say so plainly rather than manufacturing a moat that isn't there — false moats destroy the analysis's credibility.

## Step 2 — Build the HTML

1. Category section header, then one `.moat-card` per company: company name (in its palette color),
   a short punchy moat title (e.g. "State Trust + Agent Network Monopoly"), then 3–5 sentences of
   `.moat-body` prose that names the specific numbers backing the claim (branch counts, EV ₹, market
   share %, fraud-₹-detected, etc.), then a `.moat-tag` one-line label (e.g. "DISTRIBUTION MONOPOLY").
2. Use `.g2`/`.g3` grids to lay out 2–3 moat cards side by side within a category.
3. Optional closing comparison table if 3+ companies: "Moat Dimension" rows × company columns, so the
   reader can see at a glance which company leads on which specific moat axis (distribution, brand,
   capital cushion, data/tech, value lock-in).

## Step 3 — Save and present

Save to `/mnt/user-data/outputs/<Company_or_Sector>_Moats.html`, call `present_files`. This analysis
ages slower than a quarterly dashboard (moats are structural, not quarter-specific) — feel free to note
in the chat reply that the underlying numbers are as of the period sourced, but the moat thesis itself
is a longer-run view.
