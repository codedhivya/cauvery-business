# Mode: Segments — Revenue by Product, Business Line & Geography

Where the money actually comes from, broken down. A headline revenue number can hide a shrinking core
funded by one growing line, or a geography carrying the whole result — the segment split is where that
becomes visible.

Read the loaded sector file for **how that sector segments**: product lines, business lines, customer
type, or geography, and which split its companies actually disclose.

## Step 1 — Establish the disclosed split

Companies report segments on their own terms, and those terms change. Take the split from the company's
own disclosure rather than imposing a tidier structure — a segment table that doesn't match the filing is
impossible for a reader to reconcile.

Where segment definitions changed between periods, say so. A segment that grew 40% because its definition
widened is not a segment that grew 40%, and this is a common and easily-missed distortion.

Where a company discloses only partially — a percentage without absolute figures, or three named
segments plus "others" — show what's disclosed and mark the rest. Don't infer a residual and present it
as reported.

## Step 2 — Choose the cut

- **Revenue / volume by product or business line** — the default.
- **By geography** — where a company has meaningful multi-region exposure. Often the more revealing cut
  when a policy or currency event is in play.
- **By customer type or channel** — where the sector's economics turn on mix rather than product.
- **Profitability by segment** — the most useful cut of all where disclosed, since revenue mix and profit
  mix frequently point in opposite directions.

Show mix **and** growth together. A segment at 12% of revenue growing 60% matters more than one at 40%
growing 3%, and a static mix table hides that entirely.

## Step 3 — Build

1. Per company, a `.grp-hdr` then `.seg-row` bars for the mix — label, bar, percentage.
2. Where absolute figures are disclosed, a table alongside: segment, current value, prior value, YoY,
   share of total.
3. For geography, either segment bars or a small table — a map is rarely worth the complexity.
4. One or two sentences per company on what the mix shift shows. This is the payoff of the mode.
5. A `.fnote` for any definitional change or partial disclosure.

## Scope behaviour

**Single company** — the natural home; go deeper, including profitability by segment where disclosed.
**Pair** — same segment categories side by side where the companies segment comparably; where they don't,
say so rather than forcing a mapping.
**Sweep** — one block per company; a summary table of the dominant segment per company helps.
**Cross-sector** — segment structures aren't comparable across sectors. Present each within its own
sector and skip any cross-sector segment table.

## Deliver

Follow `output-conventions.md`.
