# Handoff: Insurance Sector Skills → Multi-Sector Skill Architecture

**Target repo:** `/Users/dhivya/coderepos/cauvery-business`
**Handed off from:** a claude.ai chat session, 9 Aug 2026
**Status:** 9 working insurance skills exist and are validated. A consolidation decision is
pending before scaling to more sectors (banking, pharma, etc.).

---

## 1. What already exists (in `current-insurance-skills/` in this handoff package)

Nine separate Claude skills were built for Indian insurance-sector analysis, each producing an
HTML artifact:

1. `insurance-dashboard-kpi` — KPI snapshot cards
2. `insurance-financials-tables` — detailed line-item financial tables
3. `insurance-charts-visualizer` — Chart.js comparisons (Combined Ratio breakeven line, Solvency
   minimum line, etc.)
4. `insurance-business-profile` — business model / product mix / distribution writeups
5. `insurance-swot-analysis` — evidence-grounded 4-quadrant SWOT
6. `insurance-moats-analysis` — competitive-moat writeups
7. `insurance-verdict-scorecard` — comparative scoring + category-winner synthesis
8. `insurance-sector-school` — generic metrics education (VNB, Combined Ratio, etc.), works
   standalone or personalized to a company
9. `insurance-quarterly-report` — the master/composite skill: full multi-tab dashboard combining
   all of the above for a given quarter

Each of the 9 skill folders has its own `SKILL.md` plus a `references/` folder containing **two
duplicated files**: `design-system.md` (shared CSS/HTML/Chart.js patterns) and
`metrics-glossary.md` (metric definitions, category benchmarks, and — importantly — a
**"Source Hierarchy & Attribution"** section added in the last round of work). These two files are
byte-identical copies across all 9 skill folders right now — that duplication is exactly the
management problem we're trying to fix.

All 9 have been validated with `/mnt/skills/examples/skill-creator/scripts/package_skill.py` (or
your local equivalent) and pass.

## 2. Why we're consolidating

The person plans to build equivalent skills for other sectors (banking, pharma, etc.). At 9 skills
per sector, this doesn't scale:
- **Metadata overhead**: every skill's name+description is always loaded into context regardless of
  use. 9 skills × N sectors = a lot of permanently-loaded metadata.
- **Trigger collision**: "give me a SWOT" would need to disambiguate between
  `insurance-swot-analysis`, `banking-swot-analysis`, `pharma-swot-analysis`, etc.

## 3. Target architecture (per Anthropic's own skill-authoring guidance on "domain organization" —
   a skill that supports multiple domains should be organized by variant, with Claude reading only
   the relevant reference file)

```
sector-financial-analysis/
  SKILL.md                     ← router: detect sector + detect mode, point to the right files
  references/
    design-system.md           ← shared CSS/HTML/Chart.js patterns (sector-agnostic, already exists)
    modes/
      dashboard.md             ← from insurance-dashboard-kpi/SKILL.md body
      financials.md            ← from insurance-financials-tables/SKILL.md body
      charts.md                ← from insurance-charts-visualizer/SKILL.md body
      business-profile.md      ← from insurance-business-profile/SKILL.md body
      swot.md                  ← from insurance-swot-analysis/SKILL.md body
      moats.md                 ← from insurance-moats-analysis/SKILL.md body
      verdict.md                ← from insurance-verdict-scorecard/SKILL.md body
      school.md                ← from insurance-sector-school/SKILL.md body
      quarterly-report.md      ← from insurance-quarterly-report/SKILL.md body (composite mode,
                                   references the other mode files)
    sectors/
      insurance.md             ← metrics glossary + color palette + category structure +
                                   source-hierarchy rule, specific to insurance (already exists,
                                   just needs to be de-duplicated to live in ONE place)
      _template.md              ← blank template to copy when onboarding a new sector
```

**Unresolved decision** (the person hadn't picked yet when this was handed off): whether to build
this as **one single skill** covering all 9 modes including the heavy composite quarterly-report, or
**two skills** — a lightweight "toolkit" skill for single-slice queries (dashboard/financials/charts/
etc.) plus a separate "full report" skill for the composite. Ask the person which they want before
doing the full folder rebuild, or propose a default (one skill) and let them redirect if they disagree.

## 4. What the router `SKILL.md` needs to do

1. **Detect sector** from the company/request (e.g. "HDFC Life" → insurance; if a future request
   names a bank → banking). Load the matching `references/sectors/<sector>.md`. If the sector can't
   be confidently identified, ask, don't guess.
2. **Detect mode** from the request phrasing (dashboard / financials / charts / business profile /
   SWOT / moats / verdict / school / full report) — the individual insurance skills' descriptions
   (in their YAML frontmatter, still present in `current-insurance-skills/*/SKILL.md`) are a good
   source of the trigger phrases to fold into the router's mode-detection logic.
3. Load `references/modes/<mode>.md` and follow its instructions, using `references/design-system.md`
   for all HTML/CSS/Chart.js patterns and the loaded sector file for metrics/definitions/benchmarks.
4. Keep the **Source Hierarchy & Attribution** rule (currently duplicated at the bottom of every
   `metrics-glossary.md`) as sector-agnostic — it belongs in a shared file (e.g.
   `references/source-hierarchy.md`) rather than repeated inside each sector file, since it's a
   research-discipline rule, not a sector fact.

## 5. Suggested first Claude Code prompt in this repo

```
Read HANDOFF.md and the current-insurance-skills/ folder in this repo. Rebuild the 9 insurance
skills into the target architecture described in section 3 — one consolidated
sector-financial-analysis skill with references/modes/*.md, references/sectors/insurance.md, and a
shared references/source-hierarchy.md. [state your one-skill-vs-two-skill decision here]. Validate
the result with the skill-creator packaging script before finishing, and show me a diff-style
summary of what moved where.
```

## 6. Compliance/behavior rules to preserve during the rebuild

- Never fabricate a financial figure — mark unavailable data "Not disclosed."
- Never issue buy/sell/hold recommendations in the skill's own voice; only report real, named,
  sourced brokerage views.
- Prefer company filings/investor presentations over aggregator sites; flag conflicting figures
  found across sources rather than silently picking one (this is the Source Hierarchy rule).
- Treat all analysis as research/educational, not investment advice — this disclaimer belongs in
  every output artifact's footer.
