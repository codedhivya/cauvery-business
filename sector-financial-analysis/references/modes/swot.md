# Mode: SWOT — Evidence-Grounded Four-Quadrant Analysis

A SWOT is only worth building if every bullet traces to a disclosed number or a verifiable fact. The
failure mode is industry cliché — "strong brand", "growing market" — which could be written about any
company in any sector and therefore tells the reader nothing.

Read the loaded sector file for the benchmarks that decide whether a given metric counts as a strength
or a watch item. Read `design-system.md` for the `.swot-grid` classes.

## Step 1 — Gather

Same sourcing discipline as every other mode. You need enough data points to ground 3–4 bullets per
quadrant. **If the data is thin, write a shorter SWOT** — padding with generic filler is worse than a
sparse grid, because it dilutes the bullets that are real.

## Step 2 — Derive each quadrant with discipline

- **Strengths** — what the company is verifiably good at *right now*, each cited with a number: market
  share, margin, growth rate, capital buffer, network size.
- **Weaknesses** — what verifiably lags peers or its own prior period: a metric that missed guidance, a
  ratio the wrong side of the sector benchmark, a concentration risk with a percentage attached.
- **Opportunities** — external or structural tailwinds the company is positioned to capture: regulatory
  change, under-penetration, an untapped channel or product. These must be **forward-looking**, not
  strengths restated in future tense.
- **Threats** — external risks: competitive intensity from *named* peers, regulatory change, input-cost
  or market sensitivity, dependence on one channel or customer.

**The cross-check that keeps it honest:** a weakness is something already happening *inside* the company;
a threat is something that could happen *to* it from outside. If a bullet could sit in either box, it's
probably phrased too vaguely to be useful in either.

## Step 3 — Build

1. `.co-hdr-swot` per company — colour badge plus full name.
2. `.swot-grid`: Strengths (`.swot-s`) top-left, Weaknesses (`.swot-w`) top-right, Opportunities
   (`.swot-o`) bottom-left, Threats (`.swot-t`) bottom-right. Each an `.swot-ul` of 3–6 short,
   number-grounded bullets — one line each, not paragraphs.
3. For a peer comparison, one `.swot-grid` per company inside a `.g2` so two sit side by side, grouped
   under category sections where they span categories.

## Scope behaviour

**Single company** — one grid, more bullets per quadrant.
**Pair** — two grids side by side; keep bullet ordering parallel so differences surface by position.
**Sweep** — one grid per company, grouped by category.
**Cross-sector** — one grid per company within its own sector framing. Don't build a merged SWOT across
sectors; "threats" mean different things in different industries and merging them produces mush.

## Deliver

Follow `output-conventions.md`. This is a structured factual read, not a recommendation — don't present
it as investment advice.
