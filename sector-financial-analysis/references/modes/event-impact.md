# Mode: Event Impact — Policy Events & Corporate Actions

Answers one question: **something happened — which listed companies does it hit, how hard, and what
should I watch next?**

Two event classes are in scope:

- **Policy or regulatory events** — tariffs, duties, regulator circulars, tax changes, licensing rules,
  price caps, trade agreements.
- **Corporate actions** — demergers, mergers, buybacks, stake sales, open offers, IPO listings.

**Out of scope: news digests and headline roundups.** "What happened in the market this week" is
journalism, not company evaluation, and this mode should not drift into it. The test for whether
something qualifies: **can the event be tied to named companies with a stated exposure basis?** If not,
it isn't this mode.

This mode also runs as a *section inside* another report — most quarterly reports carry a policy or
corporate-action element — so the discipline below applies whether it is the whole artifact or one block
of one.

## The six-step spine

**1 — Establish the event factually.** What was actually announced, filed, or ruled, from a primary
source. Separate **confirmed** from **proposed** from **speculated**; these get conflated constantly and
the difference usually determines whether there is any impact at all. Date it.

**2 — Trace the transmission mechanism.** How does this reach a company's results? Which line, through
what path, on what timeline? Take this from the loaded sector file's **event transmission map** — it is
the only genuinely sector-specific step here.

**3 — Name the exposed companies with a stated exposure basis.** Not "pharma is affected" but "Company
X — 31% of FY25 revenue from US generics". The exposure basis is what makes the claim checkable, and
without it the analysis is just a list of tickers. Where exposure varies in kind rather than degree, say
how.

**4 — Quantify where disclosed; refuse where not.** If the impact cannot yet be sized from real
disclosure, **say so plainly** — "immediate impact: none yet, here's what would change that" is a
legitimate and often correct finding. Manufacturing an impact estimate to fill the section is the main
failure mode of event analysis, and readers act on those numbers.

**5 — Second-order effects.** Who *gains*? Competitors, substitutes, suppliers, downstream buyers. A
policy that hurts importers usually helps someone domestic, and the one-sided version of the story
misses half of it.

**6 — What to watch next.** The concrete triggers, dates and thresholds that would change the read —
an implementation date, a court ruling, a scheme record date, a threshold price.

## Corporate actions specifically

For demergers, mergers and similar, add:

- A **structure map** — what the entity looks like before and after, and which businesses go where.
- The **resulting entities**, each with the segments and financials attributable to it where disclosed.
- **Mechanics**: share entitlement ratio, record date, expected listing timeline, treatment of debt.
- Where value is claimed to be "unlocked", state whose estimate that is and on what basis. Unlock
  arguments are frequently sell-side narrative rather than disclosure, and must be attributed.

## Build

1. Header stating the event and its date.
2. **What was announced** — the factual block, with confirmed/proposed clearly separated.
3. **Transmission** — how it reaches results, in plain English.
4. **Exposed companies table** — company, exposure basis with the number, direction of impact, an
   exposure tag (`.badge`), and a quantified estimate only where genuinely sourceable.
5. **Second-order / opportunity** block.
6. **What to watch** list.
7. `.fnote` for anything uncertain, and the standard footer.

## Scope behaviour

**Single company** — deep exposure analysis for one name.
**Sector-wide** — a table of affected companies ranked by exposure, which is the most common shape.
**Cross-sector** — where an event spans sectors (a budget, a currency move), group affected companies by
sector and state the transmission mechanism **per sector**, since the same event reaches different
sectors through entirely different mechanisms.

## Compliance

Report exposure and mechanism. Do not translate that into a buy or sell in this skill's own voice. An
event analysis is where the temptation to editorialise is strongest and the evidence is usually thinnest.

## Deliver

Follow `output-conventions.md`.
