# Mode: Financials — Detailed Results Tables

The line-item layer beneath the dashboard: exact figures, in tables, with the caveats attached. Use this
when someone wants the numbers themselves rather than a summary of them.

Read the loaded sector file for **table columns by category** and for the caveats that typically distort
that sector's results. Read `design-system.md` for the table classes.

## Step 1 — Gather

User-supplied data first, then source per `source-hierarchy.md`. For every line, capture where available:

- Current-period value, same-period-prior-year value, and the YoY % or bps change. **Compute the change
  yourself** from the two raw figures — a pre-computed percentage found elsewhere may be stale or based
  on a restated prior period.
- **Any caveat the company itself flagged**: one-off tax credits, MTM swings, consolidated vs standalone
  basis, exceptional items, a change in accounting standard. These go in a `.fnote` under the table.

Mark anything undisclosed "Not disclosed" rather than guessing.

## Step 2 — Pick the table shape

Take the column set for each company's category from the sector file.

If comparing multiple companies **of the same category**, put them in one table with companies as rows —
that's what makes a peer set scannable. If comparing **across categories**, use separate tables per
category. Forcing incompatible metrics into one row set produces columns that are empty for half the
rows and misread for the other half.

## Step 3 — Build

1. Header plus a short section title stating the period and the reporting basis ("as reported",
   "consolidated", "standalone").
2. One `<table>` per category or company group, wrapped in `.tbl-wrap` so wide tables scroll rather than
   breaking the layout. Use `td.num` / `td.tpos` / `td.tneg` for right-aligned, direction-coloured
   figures.
3. **A `.fnote` block under each table** wherever a one-off item, basis change, or
   consolidated/standalone distinction exists. This is mandatory, and it is the element most often
   skipped — a clean-looking table that hides a one-off tax credit misleads precisely the reader who
   trusts it most.
4. Optionally a multi-year trend table (prior years plus CAGR) where the data can be sourced. Skip it
   rather than reconstructing history you can't verify.

## Scope behaviour

**Single company** — one table for the period plus, where sourceable, its own multi-year trend.
**Pair / sweep** — companies as rows within a category table.
**Cross-sector** — universal metrics only, with a `Sector` column and "n/a — not comparable for this
sector" wherever a metric doesn't apply; sector-specific line items stay in their own tables.

## Deliver

Follow `output-conventions.md`. If someone only wants two or three figures conversationally, answer
inline — this mode is for when they want the full table.
