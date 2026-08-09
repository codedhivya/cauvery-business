# Mode: CB Rating — Composite Score & Ranker

The house scoring framework: a single 0–100 composite per company, a colour band, a signal label, and —
for larger sets — an interactive ranker.

The value of a proprietary score is consistency. A score computed one way this quarter and another way
next quarter is worse than no score, because readers will compare across reports assuming the basis held.
Everything here exists to keep the basis fixed and visible.

## The canonical method

**Core weights**, applied on a 0–100 scale:

| Component | Weight | What it measures |
|---|---|---|
| Revenue Growth | 30% | topline momentum vs prior period and vs peers |
| Profitability | 25% | the margin or return measure appropriate to the sector |
| PAT Quality | 25% | profit growth, and whether reported profit is clean — one-offs, tax credits, exceptional items |
| Forward Outlook | 20% | guidance, order book, visible pipeline, near-term drivers |

**PAT Quality is deliberately about quality, not just growth.** A profit number inflated by a one-off tax
credit scores worse than a smaller clean one — that distinction is the reason this component exists
rather than folding into growth.

## Sector substitutions

A single rigid formula cannot span every sector, and forcing one produces scores that are precise and
wrong. **Each sector file declares its own substitution table**, which must still total 100%.

The common cases: capital-intensive sectors substitute part of Profitability for **Debt / Leverage** and
**Cash Flow**; financial sectors — banks, insurers — cannot use leverage as a negative at all, since
balance-sheet gearing is the business model, and substitute **capital adequacy** and **asset quality**
instead. Take the substitution from the loaded sector file; never improvise one.

## Bands and signals

| Score | Band | Colour |
|---|---|---|
| ≥ 75 | strong | 🟢 green |
| 55–74 | moderate | 🟡 amber |
| < 55 | weak | 🔴 red |

Pair the number with a short signal word rather than a recommendation — "Selective", "Watch",
"Improving", "Under pressure". These describe the company's state, not an action for the reader to take.

## Step 1 — Score

Score each component from sourced figures, note which substitution table was applied, and keep the
component scores — not just the total. A composite whose components are hidden can't be argued with,
which makes it less useful, not more.

Where a component genuinely can't be scored from available disclosure, say so and state how the total was
handled. Don't silently redistribute weight.

## Step 2 — Build

1. A score table: company, sector, the component scores, the composite, the band colour, the signal.
2. **A visible method note** stating the weights used and any sector substitution — every rendered score
   must show how it was derived.
3. For larger sets, the ranker treatment: rank column with medal styling for the top three, filter
   buttons by band and by group, and sort controls on the main components. Keep the interaction simple —
   swap the sort key and re-render rather than rebuilding the table.
4. A short note on notable movers where a prior period's scores are available.

## Scope behaviour

**Single company** — the component breakdown matters more than the composite; show the working.
**Pair / sweep** — the score table, ranked.
**Cross-sector** — the composite is designed to survive this, since components are normalised and each
sector applies its own substitution. Keep the **`Sector` column** visible so a reader can see which
substitution applied, and never compare raw component inputs across sectors — only the normalised scores.

## Compliance

The score is a structured read of disclosed fundamentals, not a recommendation. The signal word must
never read as an instruction to buy or sell. State the as-of period — a composite silently carrying
stale components is exactly the drift this framework exists to prevent.

## Deliver

Follow `output-conventions.md`.
