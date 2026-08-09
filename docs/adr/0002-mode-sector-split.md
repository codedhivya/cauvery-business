# ADR-0002: Mode files own the craft; sector files own the domain

**Status**: Accepted · 2026-08-09

## Context

Having decided on one skill for all sectors ([ADR-0001](0001-one-skill-not-nine.md)), the question became
how to divide its content so that adding a sector stays cheap.

The naive split — one folder per sector, each containing its own dashboard/SWOT/charts instructions —
reproduces the original duplication problem inside a single skill. Fifteen sectors × fifteen modes is 225
files, most of them near-identical.

An audit of the 98 existing reports showed why a better split exists: **the structure of these artifacts
is the same across sectors, and only the metric names differ.** The KPI strip is company×metric cards
whether the report is about insurance (`LIC FY26 PAT`), cement (`UltraTech Q4 Revenue`) or hotels
(`IHCL Q4 PAT`). SWOT markup is identical in pharma, cement and banking reports. Shared CSS classes
appear across the corpus at high rates — `card` 84%, `kpi` 75%, `panel` 65%, `badge` 61%.

## Decision

Split by **craft vs domain**, not by sector:

- **`references/modes/*.md` own the craft.** How to lay out a SWOT grid, what distinguishes a moat from
  a strength, when a table needs a footnote, where a chart reference line goes. These files must name
  **zero** sector-specific metrics.
- **`references/sectors/*.md` own the domain.** Category taxonomy, metric definitions, benchmarks,
  colour palette, regulator rules, and a per-mode specifics section that the mode files delegate into.

Concretely: `modes/dashboard.md` says "show the headline KPIs for this company's category, per the sector
file's *Headline KPIs by category* table." `insurance.md` supplies Life → PAT/VNB/VNB Margin/APE/Solvency.
`banking.md` supplies NII/NIM/GNPA/CASA/CRAR.

Each sector file must provide nine delegation targets: headline KPIs, table columns, chart reference
lines, profile coverage, moat candidates, valuation multiple, CB Rating substitutions, extra sections,
and an event transmission map.

## Consequences

- **Adding a sector is a one-file job.** Insurance and banking were built deliberately as opposite ends
  of the metric spectrum — VNB and Combined Ratio share nothing with NIM and GNPA — and both are served
  by the fifteen mode files *without modification*. That is the evidence the abstraction holds.
- The contract is invisible when broken. Putting `VNB` into `modes/swot.md` breaks nothing today; it
  quietly kills the abstraction, and every future sector inherits insurance's vocabulary. This is
  enforced by a grep in the validation suite and stated in `AGENTS.md`.
- Mode files must be written more abstractly than a single-sector skill would need, which makes them
  slightly harder to read in isolation.
- A sector needing something genuinely new must declare it as an *extra section* or a *substitution* in
  its own file rather than editing a mode. If a mode edit seems necessary, that is a signal the sector
  file is incomplete.
