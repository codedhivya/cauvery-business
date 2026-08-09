# ADR-0010: Inherit structure from prior reports; never inherit figures

**Status**: Accepted · 2026-08-09

## Context

The established workflow was to fork the previous quarter's report for a sector and update the numbers.
That has a genuine advantage — the prior artifact is complete and proven, its company scope and layout
already tuned over several quarters.

It also has a measurable cost, visible throughout the corpus audit. Forking propagates defects and never
propagates fixes:

- Tab markup diverged into two conventions (`tab-btn` in 49 files, `tab` in others)
- A footer appears in **19%** of reports
- An explicit `Source:` line appears in **42%**
- The `.fnote` caveat block — which flags one-off tax credits, MTM swings and basis changes — appears in
  **1 of 98**
- CB Score fragmented into four incompatible methods on three scales ([ADR-0005](0005-cb-rating-unification.md))

None of this is carelessness; it is what forking does mechanically. The existing metrics glossary already
warned about the matching failure mode: *"a persistency ratio quietly copied wrong from quarter to
quarter."*

## Decision

**A three-way split of what the skill takes from where:**

| Layer | Source | When |
|---|---|---|
| **Durable sector knowledge** — metric definitions, benchmarks, taxonomy, palette, transmission maps | mined **once** from the reports into `sectors/*.md` | read from the sector file at runtime |
| **Point-in-time facts** — quarterly figures, ratings, valuations | sourced **live** per run | never baked into any file |
| **Continuity reference** — company scope, section selection, layout, chart types | the prior period's report, on request | only when regenerating |

**Structure and expertise are inherited; numbers never are.** When regenerating a report for a new
period, read the prior artifact for scope and layout, then re-source every figure.

Prefer a *published* prior over a staged one — a staged draft may contain figures nobody has verified.

## Consequences

- The advantage of the fork workflow is kept; the drift is not. Fix the missing `.fnote` rule once and
  all report types get it.
- If the skill pulled figures from stored reports, a Q2 report would silently inherit Q1 values. This is
  the exact failure the glossary warned about, and it is why the split is stated explicitly rather than
  left to judgement.
- Two things the skill does not replace, stated so expectations stay honest: **generation is
  non-deterministic** (a fork reproduces byte-for-byte, a regeneration does not), and **bespoke editorial
  angles** — "Why DMart Differs", "Budget Warfare", "Milk Chain" — come from the author, not the
  template.
- The framing: the skill guarantees the floor — structure, caveats, sourcing, scoring consistency — so
  attention goes to the insight rather than the scaffolding.
