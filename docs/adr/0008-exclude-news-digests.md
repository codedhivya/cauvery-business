# ADR-0008: Exclude news digests; keep policy and corporate-action analysis

**Status**: Accepted · 2026-08-09

## Context

Some reports are event-driven rather than results-driven. The audit found event content is far more
pervasive than it first appears: **77 of 96 reports (80%)** carry policy/regulatory or corporate-action
material — aluminium tariffs, steel safeguard duty, telecom AGR, banking open offers, battery stake
sales.

The split matters. Only **two** are standalone event reports (`Q1FY27_Analysis_USGenericTariff`,
`Vedanta_Demerger_Dashboard`). Roughly 75 carry event content as a *section inside* a quarterly report —
telecom's "Key Policy Catalyst", steel's "Safeguard Duty Protection".

Two further reports are news digests (`Market_breaking_news_*`, "SectorWire") — headline roundups of what
happened in the market.

## Decision

**Keep event analysis. Exclude news digests.**

`event-impact.md` covers two event classes:
- **Policy or regulatory events** — tariffs, duties, circulars, tax changes, price caps
- **Corporate actions** — demergers, mergers, buybacks, stake sales, open offers, IPO listings

It serves double duty: a standalone report type, and the discipline invoked whenever event content
appears inside another mode.

**The dividing line**: an event qualifies only if it can be tied to **named companies with a stated
exposure basis**. "What happened in the market this week" is journalism, not company evaluation, and the
mode file says so explicitly so the router does not drift into it.

The six-step spine is lifted from the tariff report: establish the event factually from a primary source
(separating confirmed from proposed from speculated) → trace the transmission mechanism to a P&L line →
name exposed companies with a stated exposure basis → quantify where disclosed and **refuse where not** →
second-order effects including who gains → what to watch next.

## Consequences

- Steps 1 and 3–6 are pure method, identical for a tariff, a rate cut or a demerger. Only step 2 —
  transmission mechanism — is domain knowledge, so each sector file carries an **event transmission map**
  linking common events to the metric they hit and the exposure basis to cite.
- The two news-digest reports are not reproducible by the skill. That is deliberate.
- The tariff report's own framing sets the standard for honesty here: its heading reads *"IMMEDIATE
  IMPACT — there isn't one, yet"*. Manufacturing an impact estimate to fill the section is the main
  failure mode of event analysis, and readers act on those numbers.
