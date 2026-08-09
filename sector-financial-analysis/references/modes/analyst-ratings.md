# Mode: Analyst Ratings — Third-Party Brokerage Views

Reported, never computed. This mode carries what *named external firms* have said — their rating, target
price, and reasoning — clearly marked as their view rather than this skill's.

It carries the highest fabrication risk of any mode in the skill, because an invented brokerage call is
both highly specific and completely unverifiable by a casual reader. Everything below exists to prevent
that.

## The rule

**Only real, named, substantiable firms.** If you cannot identify which specific firm said something,
it does not go in. Never invent a brokerage, a rating, a target price, or a quote — and never present an
aggregate "analysts think..." without being able to name who.

If no genuine brokerage view can be sourced for the companies in scope, **omit the section entirely**.
An absent Analyst Ratings section costs a reader nothing. A fabricated one destroys the credibility of
every other number in the artifact.

## Step 1 — Source

Search for genuine post-results brokerage coverage per `source-hierarchy.md` (Tier 3). Capture, per view:

- **Firm name** — the specific house.
- **Rating** — in that firm's own vocabulary (Buy / Add / Accumulate / Neutral / Reduce / Sell). Don't
  normalise across firms; "Add" and "Buy" aren't the same call and flattening them misrepresents both.
- **Target price** — where disclosed, with its currency and horizon.
- **Date** — a rating without a date is unusable; ratings move.
- **A one-line rationale** where available.

A named consensus poll can be included as a source in its own right, attributed to the poll.

## Step 2 — Build

1. A table: Firm, Rating (as a `.badge` — `.b-buy` / `.b-hold` / `.b-sell`), Target Price, Date,
   Rationale.
2. Where several firms cover the same company, show the spread — the range of targets and the split of
   ratings. Disagreement among analysts is information; a single cherry-picked view implies a consensus
   that may not exist.
3. A visible disclaimer line stating these are third-party views, not this artifact's recommendation.
4. Where coverage is sparse, say so plainly — "two brokerage views located" is honest and useful.

## Step 3 — Keep the boundary visible

The reader must never be able to confuse a brokerage's opinion with this skill's analysis. Keep them in a
clearly-headed section, attributed inline, and never carry a brokerage's rating forward into a verdict,
scorecard or summary as if it were a finding of this artifact.

## Scope behaviour

**Single company** — all located views, with the spread.
**Pair / sweep** — grouped by company; note where coverage is uneven, since a well-covered large cap and
a thinly-covered small cap aren't comparable on consensus.
**Cross-sector** — group by company; don't compare rating distributions across sectors, since coverage
intensity varies structurally by sector and market cap.

## Deliver

Follow `output-conventions.md`.
