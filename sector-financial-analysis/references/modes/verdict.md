# Mode: Verdict — Comparative Scorecard & Synthesis

The synthesis that sits on top of the other modes: growth, profitability, moat and valuation pulled into
a comparative read, and — for three or more companies — a category winner.

**Guardrail, stated up front:** this is a research and education synthesis, not investment advice. Frame
any "winner" as *best on the fundamentals reviewed*, never as a buy/sell/hold in this skill's own voice.
Where brokerage views are wanted, report only real named calls per `analyst-ratings.md`.

Read the loaded sector file for benchmark thresholds and the valuation multiple that applies.

## Step 1 — Gather comparable inputs

Per company, at minimum: one growth metric, one profitability metric, one balance-sheet or capital
metric, and — where real market data exists — a valuation multiple. Same sourcing discipline as
everywhere else.

## Step 2 — Score across four lenses

Adapt each lens to the company's category from the sector file; don't force one sector's lens onto
another's business model.

- **Growth** — topline or new-business growth against peers and against its own prior period.
- **Profitability** — the margin or return measure that fits the category, judged against the sector
  file's benchmarks rather than an absolute.
- **Moat** — the durability read, drawn from or re-derived per `moats.md`.
- **Valuation** — cheap / fair / expensive on the sector's own multiple. State this only with real
  market data; otherwise drop the lens rather than guessing.

## Step 3 — Build

1. **A headline verdict card** naming the standout for the period, with 3–4 supporting KPI boxes and a
   3–5 sentence "why" that **explicitly makes the runner-up's case too**. One-sided cheerleading is the
   most common way a verdict loses credibility — noting that "B grew faster, though A's underwriting
   quality was structurally stronger" is what makes the call trustworthy.
2. **Per-company analysis cards** for a multi-company deep dive — badges, KPI boxes, one paragraph each.
3. **A comparative scorecard table** using `.score-row`: companies as rows; columns for category, the
   four lenses (a score or a short qualitative tag), a sourced analyst stance where one genuinely
   exists, and a one-line key risk per company.
4. **A category-winner table** where the set spans categories, naming the best in each with a one-line
   reason.
5. A closing paragraph tying individual verdicts to the sector-level structural picture, plus the
   disclaimer line.

State the basis of any score. A reader who can't see how a 7/10 was reached has no reason to believe it.

## Scope behaviour

**Single company** — no ranking to do. Give the four-lens read against sector benchmarks and its own
history, and say plainly that this is an assessment, not a comparison.
**Pair** — head-to-head across the four lenses, with an explicit statement of what each does better.
Resist declaring an overall winner where the lenses genuinely split — saying "A on quality, B on growth,
depending on what you weight" is more useful than a forced verdict.
**Sweep** — full scorecard plus category winners.

**Cross-sector** — this is where ranking is most tempting and most dangerous. Rank only on **universal
metrics** (Revenue growth, EBITDA%, PAT growth, Mkt Cap, P/E, EV/EBITDA, Net Debt), always with a
**`Sector` column**. Express valuation as a position within the company's *own* sector band rather than
a raw cross-sector comparison. Where a sector lacks a universal metric — banks and insurers have no
meaningful EBITDA — the cell reads **"n/a — not comparable for this sector"**. Sector-specific metrics
stay out of the ranking table entirely and live in their own per-sector section.

## Deliver

Follow `output-conventions.md`. Keep the chat reply to the one-line headline; let the artifact carry the
support.
