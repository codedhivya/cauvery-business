# Mode: Valuation — Multiples & Relative Pricing

What the market is paying for these earnings, and whether that looks cheap, fair or expensive against
peers and the company's own history. Distinct from `verdict.md`, which weighs valuation alongside growth
and quality to reach an overall read — this mode does valuation properly on its own terms.

Read the loaded sector file for **which multiple leads** in that sector. This matters more than it
sounds: applying a P/E to a business the market values on book, or on embedded value, or on distribution
yield produces a number that is arithmetically correct and analytically meaningless.

## Step 1 — Establish the right multiple

Every sector has a primary multiple its investors actually use, plus secondary ones for context. Take
both from the sector file. Where a company straddles categories, show the multiple appropriate to each
rather than averaging into something nobody uses.

Only state a valuation if you have real market data — market cap, share price, the relevant denominator.
**If you can't source it, omit the column rather than estimating.** An invented multiple is worse than an
absent one, because valuation is exactly where readers anchor.

## Step 2 — Give the multiple context

A bare multiple tells a reader very little. Two comparisons make it useful:

- **Against peers** — the same multiple for comparable companies in the same period.
- **Against its own history** — where sourceable, the company's own range over recent years, so a reader
  can see whether today is high or low *for this company*.

Where a business has structurally different economics from its peer set, note it. A higher multiple on
better returns is not the same thing as an expensive stock, and a table alone won't make that distinction.

## Step 3 — Build

1. A valuation table: companies as rows; columns for market cap, the primary multiple, secondary
   multiples, and a returns measure where the sector uses one.
2. Where history is available, a small trend of the primary multiple.
3. A short paragraph stating what the numbers show — including the case against the obvious reading.
   The cheapest name in a table is often cheap for a reason worth naming.
4. A `.fnote` for anything distorting a multiple: a one-off in the earnings base, a recent capital
   raise, a demerger changing the share count.

## Scope behaviour

**Single company** — its multiples against its own history and its peer band.
**Pair / sweep** — the comparison table is the natural output.
**Cross-sector** — use only universal multiples (P/E, EV/EBITDA, P/B, market cap) with a **`Sector`
column**, and state valuation as a position *within the company's own sector band* rather than ranking
raw multiples across sectors. A 15× P/E means something different in IT than in cement, and ranking them
against each other implies a comparison that doesn't exist. Where a sector's primary multiple has no
cross-sector equivalent, the cell reads **"n/a — not comparable for this sector"**.

## Compliance

Report what the multiples are and how they compare. Do not translate that into a buy, sell or hold in
this skill's own voice — see `source-hierarchy.md`.

## Deliver

Follow `output-conventions.md`.
