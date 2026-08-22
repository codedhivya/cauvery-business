# ADR-0012 — REITs and InvITs get their own file, because they are an asset class, not an industry

**Status**: Accepted
**Date**: 2026-08-22

## Context

REITs and InvITs were originally a fourth category inside `sectors/infra-realty.md`, alongside
residential developers, commercial developers, and ports. The reasoning was proximity: a REIT holds
buildings, real-estate developers build buildings, so one file could serve both.

That reasoning does not survive contact with what these trusts actually hold. Counting entity mentions
across the three REIT/InvIT reports in the corpus:

| Entity | Mentions | What it holds |
|---|---|---|
| IndiGrid | 23 | **power transmission lines** |
| Embassy Office Parks | 22 | offices |
| Mindspace | 17 | offices |
| Brookfield India | 16 | offices |
| IRB InvIT | 7 | **toll roads** |
| PowerGrid InvIT | 6 | **power transmission** |
| Cube Highways | 1 | **toll roads** |

The single most-covered entity is a **transmission** InvIT. Keyword counts in the same reports run
transmission 39, power 55, highway 17, pipeline 18, telecom tower 3, renewable 10 — against office 48.
**The majority of the assets have nothing to do with real estate.**

Under the old placement, `audit_corpus.py` matched `reit`/`invit` to `infra-realty` and then checked
those reports against pre-sales, collections, cargo volume and RERA. For IndiGrid, IRB InvIT and
PowerGrid InvIT, every one of those is the wrong yardstick.

The strain was already visible in the file itself. `infra-realty.md`'s CB Rating table carried the
warning *"Do not apply this to a REIT or InvIT without substituting throughout"*, and its mode
applicability section listed the modes that "do not apply" to trusts. A sector file that must exempt one
of its own categories from its own scoring method is describing two sectors.

## Decision

**`sectors/reit-invit.md` is a distinct sector file — the seventeenth.**

`infra-realty.md` keeps developers and ports and points to the new file. The REIT/InvIT metric block,
benchmarks, palette entries, trust CSS and the cross-sector refusal all moved.

Three things follow from "asset class, not industry":

1. **The vehicle frame is constant, the assets vary.** DPU, distribution yield, NDCF coverage, LTV, NAV
   per unit and the SEBI trust regulations apply identically whether the trust holds offices or
   transmission lines. That shared frame is what makes it one file.
2. **Where the underlying asset's drivers matter, load that sector file too.** A transmission InvIT's
   availability is best read alongside `power-energy.md`. The router already supports loading 1..N
   sector files, so this needs no new mechanism.
3. **The CB Rating parameter set is fully substituted** — Distribution Durability 30%, DPU Growth Quality
   20%, Asset Quality & Residual Life 20%, Balance Sheet 20%, Governance & Sponsor 10%. Revenue Growth,
   EBITDA margin and PAT Quality do not appear at all, because all three are misleading for a
   pass-through trust.

## Consequences

**Good.**

- A transmission or road InvIT is no longer graded on pre-sales and cargo.
- `infra-realty.md` gets simpler: two related operating businesses instead of three unlike ones, with no
  self-exemption in its own CB table.
- The cross-sector refusal now lives in the file it protects.
- The distinctions that matter to an income vehicle became stateable once there was room for them:
  **availability-based versus volume-based** revenue (a transmission InvIT is near-bond-like; a toll road
  carries traffic risk), distribution **coverage** below 1×, and the **tax composition** of a
  distribution — a payout heavy in capital return is partly a return of the investor's own money, so a
  headline yield overstates income. None of these fitted in a shared file.

**Costs, stated honestly.**

- **Office REITs genuinely do need real-estate knowledge** — occupancy, WALE, mark-to-market rents. That
  now spans two files rather than one. Mitigated by the explicit instruction to load both, but it is a
  real seam and the first sector in the skill that routinely wants a second file.
- **"Sector" is now doing two jobs** in the taxonomy: fifteen industries, one asset class, and
  `capital-markets.md` already quietly holding funds. The axis is really "which metric vocabulary to
  load", which this fits — but the name no longer describes it precisely.
- Corpus evidence is thin: **3 reports**. The decision rests on the conceptual argument and on what those
  trusts hold, not on report volume. If it proves wrong, the merge back is mechanical.
- `reit`/`invit` are matched as bare substrings in `audit_corpus.py`, before `infra-realty`. Order now
  carries meaning in that dict, which is a subtle dependency.

## Alternatives rejected

**Leave it in `infra-realty`.** Rejected: it forces transmission and road InvITs through real-estate
metrics, and the file was already exempting them from its own scoring.

**Split by underlying asset** — office REITs to `infra-realty`, transmission InvITs to `power-energy`,
road InvITs to `infra-realty`. Rejected: it scatters one analytical frame across three files, so the
coverage, LTV and tax-composition discipline would have to be written three times and would drift. It
also puts a pass-through trust inside a file whose CB parameters assume retained earnings.

**A generic `trusts-and-funds` file** covering REITs, InvITs and the IPO fund in `capital-markets.md`.
Rejected as over-abstraction: a mutual fund's NAV, active share and expense ratio share almost nothing
with a trust's DPU, availability and concession tenure beyond "not an operating company".

## Addendum — after reading the corpus reports in full (2026-08-22)

The decision was taken before reading the three REIT/InvIT reports closely. Doing so afterwards
corrected two things and confirmed the rest.

**Corrected.** An earlier argument here leaned on "the single most-covered entity is IndiGrid, a
transmission InvIT". True, but selectively framed: **in aggregate, office and retail REITs are 54% of
entity mentions.** The majority of the corpus content *is* real estate. The 46% that is not — transmission,
roads, renewables, storage — still had no sensible home in a developer file, so the decision stands, but
on a narrower margin than first stated.

Separately, a claim that the reports "call the group *investment trust* 8 times" was wrong. Every one of
those occurrences is an acronym expansion ("REIT (Real Estate Investment Trust)") or a SEBI regulation
title. **The author uses no collective noun** — the masthead reads "5 Mainboard REITs · 7 Public InvITs"
and a dedicated tab compares "REIT vs InvIT". The filename `reit-invit.md` therefore matches the house
convention; `investment-trusts.md` would have invented a label the corpus does not use.

**Confirmed, and strengthened.** The trusts' underlying assets are far wider than the original six
categories: one REIT holds Grade-A offices, **hospitality** and **solar generation**; an InvIT holds
transmission, renewables and **battery storage**; another holds retail alongside **ticketed
attractions**. A vehicle spanning that range cannot sit inside any one industry file. Trusts are also
reclassified as their mix shifts.

**Self-sufficiency (author's decision).** The file duplicates property metrics — NOI, occupancy, WALE,
mark-to-market — rather than deferring to `infra-realty.md`. The seam noted in the original Consequences
is therefore closed at the cost of accepting duplication. The rationale is not only convenience: pulling
in an operating-company file invites its *framing* along with its definitions, and a trust must be read
through distribution and coverage. The accepted risk is definition drift between the two files.

**Gaps the corpus exposed**, now folded in: NOI as the headline operating metric; occupancy stated **by
value versus by area**; tenant diversification; credit rating and sponsor type as first-class displayed
attributes; SM REITs as a full category; sponsor holding-reduction as the flagged investor risk; and the
"REIT vs InvIT" contrast as a recognised section type.

## Second addendum — the taxonomy was built on the wrong axis (2026-08-22)

The first version of `reit-invit.md` organised the class as a flat list of nine asset categories —
office, retail, transmission, roads, pipelines, logistics, SM REIT, private placement. **That structure
was invented here, not taken from the corpus.**

The author's own structure is a **two-way split: REIT versus InvIT** — real estate on one side, all other
infrastructure on the other. The report's masthead counts them separately ("5 Mainboard REITs · 7 Public
InvITs"), they get separate tabs, and a dedicated **"REIT vs InvIT"** tab contrasts them across twelve
dimensions: asset class, revenue driver, contract length, risk profile, yield band, SEBI distribution
mandate, minimum investment, asset life, NAV basis, market size, credit ratings, SEBI classification.

Restructuring on that axis surfaced **the single most important fact in the class, which the flat list
had lost entirely**:

> **A REIT's assets are perpetual. An InvIT's concession assets run off to zero.**

That is why InvIT yields sit structurally above REIT yields — **part of an InvIT's distribution is return
of capital, not income**, because the asset is being consumed over the concession term. A REIT at 7% and
an InvIT at 11% are not offering the same thing. Ranking them on headline yield is the central error the
file now exists to prevent, and the flat taxonomy could not express it because it had no REIT/InvIT axis
to hang it on.

Two related facts came with it: **NAV means different things** in each — an independent property
valuation for a REIT, a **DCF of remaining concession cash flows** for an InvIT, so a discount to NAV may
merely reflect run-off the DCF already assumes — and SEBI classifies REITs as **equity** and InvITs as a
**hybrid** instrument, which affects index inclusion and institutional eligibility.

**The general lesson, beyond this sector**: a sector file's taxonomy should be lifted from how the corpus
*compares* its subjects, not from how the subjects could plausibly be sorted. The plausible sort here was
by underlying asset, and it was analytically sterile. The author's sort was by vehicle, and it carried
the insight. Asset-type categories remain in the file, but as sub-categories underneath the REIT/InvIT
split rather than as the organising level.

