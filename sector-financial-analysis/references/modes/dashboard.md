# Mode: Dashboard — KPI Snapshot

The top-level "at a glance" view for one or more companies in a period: a KPI strip plus per-company
summary cards, grouped by the sector's own categories. This is the entry-point view — it should answer
"how did they do?" in about fifteen seconds of scanning.

Read the loaded sector file for **Headline KPIs by category** and for what "good" looks like on each
metric. Read `design-system.md` before writing any HTML.

## Step 1 — Scope the request

Settle these, asking only if genuinely ambiguous:

- **Which companies?** One company, a peer pair, a sector sweep (5–8 representative names), or a
  cross-sector set.
- **Which period?** A quarter or a full year. If unstated, use the most recent period with reliable
  published data, and say which one you used.
- **Where the data comes from.** User-supplied figures first; otherwise source per `source-hierarchy.md`.
  Never fabricate — mark anything unavailable "Not disclosed this period."

## Step 2 — Classify each company

Assign each company to its category from the sector file's taxonomy, then pull that category's headline
KPI set. Different categories within a sector genuinely need different KPIs; forcing one metric row
across incompatible categories produces a table that looks tidy and means nothing.

## Step 3 — Build

1. **Header** — dark `.hdr` bar: title, period, and a `.chip` per company in its palette colour.
2. **KPI strip** (`.kpi-row`) — 4–6 headline numbers with YoY/QoQ deltas (▲/▼, `.pos`/`.neg`).
3. **Category sections** — group companies under category headers, each followed by a grid of `.co-card`
   (`.g2` for two, `.g3` for three or more). Each card: company name in its colour, category tag, 5–8
   `.m-row` metric lines, then a `.badge-row` with 2–3 short takeaways.
4. **Closing snapshot** — for 3+ companies, a small table of cross-company context: leader by metric,
   fastest grower, notable mover.
5. **Footer** per `design-system.md` §9.

## Scope behaviour

**Single company** — skip category grouping entirely. Show the KPI strip built from that company's own
numbers plus one detailed `.co-card`. Don't invent a sector comparison that wasn't asked for; a reader
who wanted peers would have named them.

**Pair** — two `.co-card`s side by side in `.g2`, same metric rows in the same order so the eye can
compare down the column. Where one leads, let the numbers show it rather than adding commentary.

**Sector sweep** — full category grouping, plus the closing cross-company snapshot.

**Cross-sector** — the comparison table may use **only universal metrics** (Revenue, EBITDA%, PAT,
growth %, Mkt Cap, P/E, EV/EBITDA, Net Debt), and must carry a **`Sector` column**. Sector-specific
metrics stay quarantined in their own per-sector section. Where a sector genuinely lacks a universal
metric — banks and insurers have no meaningful EBITDA — the cell reads **"n/a — not comparable for this
sector"**, never a blank and never a number borrowed from a different concept. A number that looks
comparable but isn't is worse than an honest gap.

## Deliver

Follow `output-conventions.md`. Keep the chat reply to a line or two of headline takeaway.
