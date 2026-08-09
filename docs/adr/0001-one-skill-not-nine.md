# ADR-0001: Consolidate nine insurance skills into one multi-sector skill

**Status**: Accepted · 2026-08-09

## Context

Nine separate Claude skills existed for Indian insurance analysis — dashboard, financials, charts,
business profile, SWOT, moats, verdict, school, and a composite quarterly report. Each carried its own
`SKILL.md` plus a `references/` folder containing two files: `design-system.md` and
`metrics-glossary.md`.

Those two files were **byte-identical across all nine folders** (verified by md5). Eighteen copies of two
files.

The plan was to extend the same treatment to other sectors — banking, pharma, and more. That does not
scale on two axes:

- **Metadata cost.** A skill's name and description sit in context permanently, used or not. Nine skills
  × N sectors is a lot of always-loaded text for work that is mostly not happening.
- **Trigger collision.** "Give me a SWOT" would have to disambiguate between `insurance-swot-analysis`,
  `banking-swot-analysis`, `pharma-swot-analysis` and so on. Every new sector makes every existing
  trigger less precise.

At three sectors this becomes 27 skills.

## Decision

**One skill, `sector-financial-analysis`, covering every sector.** Sectors are reference files inside it,
not separate skills. The skill count is one today and stays one after thirteen more sectors are added.

A two-skill split was considered — a light "toolkit" for single-slice queries plus a separate "full
report" skill for the heavy composite. Rejected: it doubles the always-loaded metadata per sector, which
is precisely the cost being removed, in order to solve a mode-disambiguation problem the router resolves
with one table lookup. The composite report's weight is a loaded-on-demand concern, not a metadata one.

## Consequences

- Adding a sector means writing one file. No new skill, no new description competing for triggers.
- Per request, roughly two reference files load: one sector, one mode. Cost is independent of how many
  sectors exist.
- The router must correctly detect sector and mode. That routing logic is now a single point of failure
  where previously the skill-selection mechanism handled it — mitigated by keeping the router small
  (~166 lines) and explicit.
- One description must carry the trigger phrases of all fifteen modes. It is necessarily long, and had
  to be compressed to fit the 1024-character limit (see the description in `SKILL.md`).
- Eighteen duplicate reference files were deleted, replaced by one copy each.
