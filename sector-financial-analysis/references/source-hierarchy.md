# Source Hierarchy, Attribution & Compliance

This is a research-discipline rule, not a sector fact — it applies identically to every sector and every
mode. Read it before pulling any figure from anywhere.

The reason it matters more than it looks: these artifacts are dense with numbers, and a reader has no way
to tell a filing-sourced figure from one scraped off a content farm. The attribution *is* the difference
between research and decoration.

---

## The five tiers

Prefer sources in this order. Don't silently blend tiers — where a disputed or headline figure matters,
say which tier it came from.

**Tier 1 — the company itself.** Exchange filings (BSE/NSE), the company's own investor presentation or
press release, earnings-call transcripts and management commentary, annual reports. Most authoritative;
wins any conflict with a lower tier. Search terms like `"<company> investor presentation Q<n> FY<yy>
filetype:pdf"` or `"<company> BSE filing"` surface this tier far better than a generic
`"<company> results"` query.

**Tier 2 — named data providers and regulators.** Cite the body by name rather than presenting its number
as the company's own disclosure. Which bodies are authoritative differs by sector — **the loaded sector
file's "Where to look" section names them**, along with ratings agencies (CRISIL / ICRA / CARE) and
ownership data providers (Prime Database, and shareholding patterns filed with the exchanges).

**Tier 3 — named brokerage and analyst research.** Only ever attribute a view to a *specific, real, named
firm* you can substantiate. Never invent a brokerage call or a target price. Always framed as a
third-party view, never as this skill's own recommendation. A named consensus poll belongs here too.

**Tier 4 — general financial news.** Reuters, Bloomberg, Business Standard, Mint, Economic Times,
Moneycontrol articles and similar. Reliable for context and colour; re-verify any exact figure (a ratio,
a ₹ amount, a %) against Tier 1 before it drives a table cell.

**Tier 5 — aggregators, blogs and SEO content farms.** Lowest priority. Usable for orientation, but
cross-check against Tier 1 before placing anything from here in a table. This is where transcription
errors and stale figures most often originate — a ratio quietly copied wrong from one period to the next
is the classic case. Treat an unusual or headline number from this tier with real suspicion until
confirmed.

## The required attribution format

Every artifact carries an explicit `Source:` line, and it names **the source plus the date**. That second
half is what makes it checkable:

- `Source: IndiGo exchange filing, 29 May 2026`
- `Source: audited/reported Q4 FY26 consolidated results, BSE/NSE filings`
- `Source: company investor presentation, 11–12 May 2026`

Along with it, state the data as-of date. A number without a date has no shelf life, and a reader six
weeks later cannot tell whether it is current.

Where a genuinely unattributable claim must appear, say "unattributed" rather than inventing a source.
**Never fabricate an attribution.** A made-up source is worse than no source, because it survives
scrutiny just long enough to be repeated.

## Conflict handling

If two sources disagree, don't quietly pick one. Prefer the higher tier — especially Tier 1 — and add a
short visible note flagging the discrepancy, which source you went with, and why. That note is more
useful to a reader than false confidence in a single figure, and it is exactly the situation where a
silent choice does the most damage.

## Never fabricate a figure

If a number wasn't supplied and can't be sourced reliably, mark it **"Not disclosed"** (or "Not disclosed
this period") and move on. A report with a few honestly-labelled gaps is far more trustworthy than one
with confident inventions, and the gaps themselves are often informative — a company declining to
disclose something is a fact about that company.

This applies equally to quotes, brokerage views, management commentary and analyst targets.

## …but earn the "Not disclosed" first

The rule above has a failure mode worth naming: **"Not disclosed" can quietly become an excuse for an
unfinished search.** A gap labelled that way *looks* disciplined while actually meaning "my search didn't
happen to return it" — and those are entirely different claims to a reader.

**"Not disclosed" means: I made a targeted attempt for this specific figure and it is genuinely
unavailable.** It does not mean a general search failed to surface it.

### One query per company for market data

Price, market cap, P/E, P/B and 52-week ranges come from market-data aggregators, and **a combined query
naming several companies typically returns only one of them.** Searching "A, B, C and D market cap P/E"
and accepting whatever comes back produces a table with one populated row and three false "Not disclosed"
markers — each of which looks like a disclosure gap and is actually a search gap.

**Run one query per company for market data.** The same applies to any per-company figure a batch search
returns partially.

### Completeness check before publishing a table

For any table with N companies and a given field, you should be able to say for each cell: this is a real
figure, or I looked for this specific one and it isn't available. If a row is empty simply because a
batch search returned nothing for it, **that is not finished work** — go back and query for it directly.

This matters most exactly where the reader is most likely to act: valuation multiples, regulatory status,
and any figure that drives a ranking or a score.

## Always show direction

Show the YoY (or QoQ) change alongside the absolute number, and compute it yourself from the two raw
figures rather than trusting a pre-computed percentage that may be stale. A number without direction
doesn't tell an investor anything.

## Compliance

- **Never issue a buy / sell / hold recommendation in this skill's own voice.** Named brokerage views can
  be reported factually and clearly attributed; a synthesised "verdict" must be framed as a
  research/educational read of the disclosed numbers.
- **Use the house standing disclaimer** on any artifact carrying a rating, score or ranking. The
  established wording is:

  > ⚠ Earnings-quality analysis only · No buy / sell / hold recommendation

  It is better than a generic disclaimer because it says what the analysis *is*, not merely what it
  isn't — the work is an assessment of how sound reported earnings are, which is a factual question,
  rather than a view on what a reader should do. Place it in the header near the title, where it frames
  the whole artifact, and keep the fuller disclaimer in the footer.
- Where a "winner" or ranking is produced, frame it as *best on the fundamentals reviewed*, not as
  investment advice.
- Every artifact footer states that it is for research/educational purposes and is not investment advice.
- These outputs may be published to readers who will not independently verify them. That raises the
  stakes on every rule above rather than relaxing any of them.
