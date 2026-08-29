# Mode: Business Profile — How the Company Actually Works

The qualitative complement to the metric modes: what this company does, how it earns, who sells for it,
and who runs it. Answers "what am I actually looking at?" before any ratio makes sense.

Read the loaded sector file for **profile coverage by category** — what a profile must cover differs
genuinely by sector — and for the sector's own terminology, so the same concept is named the same way
across every artifact.

## Step 1 — Gather structural facts

Look for: promoter / ownership / JV structure, founding year, market position or rank, the MD & CEO,
distribution or delivery footprint (branches, agents, dealers, plants, partnerships), and the revenue mix
by product, segment or channel.

Where a precise mix percentage isn't disclosed, say so rather than manufacturing false precision. An
approximate range sourced from the company's own disclosure ("~40–45%") is fine; an invented exact figure
is not, and reads as more authoritative than the underlying evidence supports.

## Step 2 — Cover management and governance

Fold leadership and governance in here rather than treating it as a separate output: who runs the
company, recent leadership changes, board composition where notable, promoter pledging, related-party
concerns, auditor changes. These are often the earliest signal of trouble and the easiest thing to omit
because no ratio surfaces them.

Report what is disclosed and attributable. Don't editorialise about integrity from thin evidence.

## Step 3 — Build

1. A `.grp-hdr` banner per company: name, ownership, founding year, one-line positioning.
2. A `.g2` grid — left card "Business Model": one dense paragraph of 4–6 sentences carrying real
   numbers, not adjectives. Right card either "Revenue / Product Mix" as `.seg-row` segment bars, or
   "Key Metrics" as an `.m-row` list where a mix breakdown isn't the most useful framing.
3. A short management/governance block where there is anything material to report.
4. For several companies, repeat the block per company, grouped under category sections.

The test of a good profile: someone who has never heard of the company could explain how it makes money
after reading it once.

## Scope behaviour

**Single company** — the natural home of this mode; go deeper on model and mix.
**Pair** — same section order for both so structures can be compared directly.
**Sweep** — one block per company, grouped by category.
**Cross-sector** — profile each company within its own sector's framing. Business models across sectors
aren't comparable in a table, and forcing them into one flattens the very differences the profile exists
to explain.

## Deliver

Follow `output-conventions.md`. For a simple "how does X make money" question with no request for an
artifact, two to four sentences in chat is often the better answer.

## Ownership and shareholding

Recurs as its own section across sectors, and it is one of the few places where a number changes the
read on management rather than on the business.

Cover, when disclosed:

- **Promoter holding, and the change** over recent quarters. Direction matters more than level — a
  falling promoter stake asks a question that the rest of the report should answer.
- **Promoter pledge** as a share of promoter holding. **A pledge is a leverage position on the company's
  own stock**, and a high or rising pledge is a governance and forced-selling risk regardless of how the
  operating numbers look. Say so plainly when it appears.
- **FII and DII holding, and the trend.** Institutional accumulation or exit over several quarters is a
  signal; a single quarter's move is noise.
- **Public float and liquidity** — a thin float exaggerates price moves and makes any valuation multiple
  less reliable.
- **Recent placements, offers for sale or lock-in expiries**, which change the float on a known date.

**State the as-of date.** Shareholding is a quarterly filing, so it is always at least somewhat stale
relative to the price it is being read against.

**Do not infer intent from a stake change.** Report the movement and the disclosed reason where one
exists. A promoter sale can fund an unrelated obligation, and a report that guesses at motive has left
research for speculation.

## When a quarter looks worse than the business

A recurring reader problem, and the corpus answers it directly rather than leaving the reader to
reconcile two conflicting impressions.

When a headline number falls sharply, **decompose it before narrating it**:

- **Year-on-year against quarter-on-quarter** — these routinely tell opposite stories, and which one is
  fair depends on the business. A seasonal business must be read year-on-year; a business in a
  step-change must be read sequentially. **Say which frame you are using and why.**
- **One-offs on both sides.** A prior-period gain — a tariff refund, an asset sale, a tax writeback —
  makes the current quarter look weak against a base that was never operating performance. Report the
  **steady-state figure alongside the reported one**, and say which lines were excluded.
- **Base effects.** A period compared against an exceptional quarter is not deteriorating; state the
  comparison base explicitly where it is unusual.
- **Mix.** Falling realisation with rising volume is a mix shift, not a pricing failure.

Where the honest answer is that the business did weaken, say that too. **The purpose is to separate the
optics from the operations, not to explain away the number.**
