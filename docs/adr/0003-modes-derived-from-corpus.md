# ADR-0003: Derive the mode set from the report corpus, not from the nine insurance skills

**Status**: Accepted · 2026-08-09

## Context

The obvious way to build the consolidated skill was to convert each of the nine insurance skills into one
mode file — a mechanical one-to-one migration.

Before doing that, the 98 reports in `reports/published/` were audited to check whether those nine
actually covered the work. They did not. Insurance is only 3 of 98 reports; normalising on it would have
encoded one small sector's habits as the shape of everything.

Of the 68 multi-tab reports, the nine insurance modes did recur strongly — Dashboard 100%, Charts 89%,
Analyst 70%, SWOT 58%, Financials 55%, Business Profile 50%, Moats 44%, Verdict 44%, School 42%. The
abstraction was sound. But several recurring report sections had no corresponding mode.

## Decision

Six modes were added beyond the insurance nine, each justified by frequency in the corpus:

| Mode | Reports | Why insurance missed it |
|---|---|---|
| `valuation` | 35 | Insurance hides valuation as one column inside Verdict, because P/EV is its only meaningful multiple. Most sectors give it a full tab — it appears in **more reports than Moats (30) or Verdict (30)**. |
| `analyst-ratings` | 47 | Its own discipline: only real, named, substantiable firms. Was a tab inside the insurance composite, never a standalone concern. |
| `segments` | 24 | Insurance folds this into business-profile as "product mix". Most sectors need a standalone revenue-by-segment/geography cut. |
| `risks-outlook` | 24 | Distinct from SWOT's Threats quadrant — that is structural, this is live and near-term. |
| `cb-rating` | 15 | The house scoring framework. See [ADR-0005](0005-cb-rating-unification.md). |
| `event-impact` | 77 | Policy and corporate-action analysis. See [ADR-0008](0008-exclude-news-digests.md). |

Two candidates were rejected: *Peer Comparison* (9 reports) folds into `verdict`/`dashboard`, which
already compare across companies; *Management/Governance* (3) folds into `business-profile`.

Final count: **fifteen modes**.

## Consequences

- The mode set reflects fifteen sectors' worth of practice rather than one sector's. Normalising on
  insurance would have deleted a top-five mode (`valuation`) outright.
- Three other corpus findings were folded in at the same time: **layout is a separate axis** from mode
  (27 reports are single-page scroll, 46 tabbed — both are now first-class); the **AI assist panel** is
  the house default rather than an exception (85 of 98 reports carry it, against the insurance skill's
  instruction to add it "only if the user specifically wants" it); and ten CSS classes the skills
  referenced were never defined anywhere, so every run improvised them.
- More modes means a longer skill description and more surface area to keep sector-free.
- The audit is recorded in [MAINTENANCE.md](../../MAINTENANCE.md) so it need not be re-derived.
