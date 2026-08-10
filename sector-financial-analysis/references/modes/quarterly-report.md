# Mode: Quarterly Report — The Full Composite Artifact

The complete report that the other modes each cover one slice of. Use it when someone wants the whole
picture for a period — one company, a head-to-head, or a sector sweep. For a narrower ask ("just the
SWOT", "just a chart"), use the focused mode instead; this one is heavy and should be reserved for
genuine full-report requests.

This mode **composes** the others rather than restating them. For each section included, follow that
mode's file for its content rules.

## Step 1 — Scope

- **Confirm the period** and that results are actually published for it. If a named company hasn't
  reported yet, say so rather than producing a result for it.

### Mixed reporting seasons — the common case, handled explicitly

For a multi-company report, companies rarely all report on the same day. Rather than waiting for the
slowest or silently omitting them, **show the latest available period per company and label it plainly**:

- State the coverage in the header — e.g. "<period> (+ prior quarter for companies yet to report)" and
  "<n> of <total> declared <period> as of <date>".
- Tag each company's row or card with the period its figures come from. A reader scanning a table must
  never have to assume every row is the same quarter.
- Never compare a company's current quarter against another's prior quarter as though they were the
  same period. If a ranking would mix periods, either restrict it to companies that have reported or
  show the period column alongside.
- When the laggards report, the report is regenerated rather than patched — see prior-report continuity.

This is worth doing well because a mixed-period table that *looks* uniform is one of the easiest ways to
mislead a reader who trusts the layout.
- **Confirm the company scope** — single deep dive, head-to-head, or sector sweep grouped by category.
- **Confirm the depth.** Drop sections nobody asked for. A focused five-section report beats a bloated
  twelve-section one — every unwanted section dilutes the ones that matter and adds surface area for
  errors.

## Step 2 — Choose the layout deliberately

Per `design-system.md` §5:

- **Tabbed** — six or more sections, or several companies each needing the same section set.
- **Single-page scroll** — a focused single-company read or a narrative argument, where making a reader
  hunt through tabs costs more than it saves.

Neither is the default. Pick from the shape of the content.

## Step 3 — Gather before writing any HTML

Collect everything first: the metrics for each company's category, growth rates, capital position,
business-model facts, and — where genuinely available — analyst views and valuation multiples. Use
supplied data first; source the rest per `source-hierarchy.md`.

Never invent a number, a brokerage call or a quote. Mark gaps "Not disclosed this period" and continue —
a report with a few honestly-labelled gaps is far more trustworthy than one with confident fabrications,
and this mode aggregates so many figures that a single invention undermines all of them.

## Step 4 — Assemble the sections

Default set, each built per its own mode file:

| Section | Mode file |
|---|---|
| Dashboard / KPIs | `dashboard.md` |
| Financials | `financials.md` |
| Charts | `charts.md` |
| Business Profile | `business-profile.md` |
| Segments | `segments.md` |
| Valuation | `valuation.md` |
| SWOT | `swot.md` |
| Moats | `moats.md` |
| Risks & Outlook | `risks-outlook.md` |
| Analyst Ratings | `analyst-ratings.md` — omit entirely if no real views can be sourced |
| CB Rating | `cb-rating.md` |
| Verdict | `verdict.md` |

Add a **School** section per `school.md` where the audience needs the metric-education layer. Add any
**sector-specific sections** the loaded sector file declares — these carry real analytical weight in
their sectors and shouldn't be dropped for uniformity.

Include the **AI assist panel** by default per `design-system.md` §7; omit it only if unwanted.

## Step 5 — Wire it up

- `showTab(id, btn)` toggling `.panel` / `.tab-btn` active classes, for the tabbed layout.
- Charts initialised **lazily on tab-open**, guarded by an `inited` flag — canvases sized while hidden
  come out wrong, and re-creating them on every tab switch leaks.
- Metric switchers keep a `DATA` object keyed by metric; swap `chart.data.datasets[0].data` and call
  `chart.update()` rather than rebuilding.
- No external API calls unless an interactive feature was explicitly requested.

## Step 6 — Footer

Data as-of date, the explicit `Source:` line with dates per `source-hierarchy.md`, and the
research/educational disclaimer.

## Prior-report continuity

When regenerating an existing report for a new period, read the previous artifact for **company scope,
section selection, layout, chart types and any custom sections** — then re-source every number for the
current period. Inherit the structure; never inherit the figures. A ratio carried forward from a prior
artifact is how a stale number survives across quarters unnoticed.

## Scope behaviour

**Single company** — deeper per section; skip cross-company comparison sections.
**Pair** — parallel structure throughout so the two can be read across.
**Sweep** — group by category; add the cross-company summary sections.
**Cross-sector** — comparison sections use universal metrics with a `Sector` column and "n/a — not
comparable for this sector" where a metric doesn't apply; give each sector its own section for its own
metrics.

## Deliver

Follow `output-conventions.md`. Give a two-to-four sentence summary of the period's headline story
alongside the file — don't drop it with no framing.
