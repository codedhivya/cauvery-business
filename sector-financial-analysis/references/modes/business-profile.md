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
