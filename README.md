# Cauvery Business — CB Research

Equity research tooling for Indian listed companies: a Claude skill that generates research-grade
analysis artifacts, plus the report collection it produces.

The reports are published at **[elangocauvery.github.io/CB-Finance](https://elangocauvery.github.io/CB-Finance/)**.

---

## What's here

| Folder | Contents |
|---|---|
| `sector-financial-analysis/` | The Claude skill — source of truth |
| `staging_reports/` | Generated drafts awaiting review |
| `cb_research_reports/` | Published reports (local mirror of the Pages site) |
| `scripts/` | `download_reports.py` — mirrors published reports locally |
| `docs/` | Report URL lists |
| `archive/handoff/` | Historical: the 9 per-topic insurance skills this replaced |

## The skill

`sector-financial-analysis` is a single skill covering every sector. It routes each request by
**sector → mode → scope**, then loads only the two reference files it needs.

```
sector-financial-analysis/
├── SKILL.md                    router: detect sector(s), mode, scope, layout
└── references/
    ├── design-system.md        shared CSS / Chart.js — sector-agnostic
    ├── source-hierarchy.md     sourcing tiers, attribution, compliance
    ├── output-conventions.md   the only file naming paths or tools
    ├── modes/                  HOW to build (15 files, no sector metrics)
    └── sectors/                WHAT the metrics are (+ _template.md)
```

**15 modes** — dashboard, financials, charts, business-profile, segments, valuation, swot, moats,
risks-outlook, analyst-ratings, verdict, cb-rating, school, quarterly-report, event-impact.

**4 scopes** — single company, head-to-head pair, sector sweep, cross-sector (guardrailed).

**Sectors** — insurance, banking. More via `references/sectors/_template.md`.

### Why one skill

Nine separate insurance skills previously carried byte-identical copies of the same reference files.
At nine skills per sector, adding banking and pharma would have meant 27 skills, each with metadata
permanently loaded and all competing to answer "give me a SWOT".

The split that makes this work: **mode files own the craft, sector files own the domain.** How to build
a SWOT grid is identical everywhere; only the metric names differ. So `modes/swot.md` names no sector
metric at all, and `sectors/banking.md` supplies NIM/GNPA/CASA while `sectors/insurance.md` supplies
VNB/Combined Ratio.

**Adding a sector means writing one file.** No mode file changes — insurance and banking sit at opposite
ends of the metric spectrum and both run on the unmodified modes.

## Workflow

Generated output is a **draft**, never a publication:

```
skill generates  →  staging_reports/  →  you verify  →  cb_research_reports/
```

The skill never writes to `cb_research_reports/` and never promotes a file. Promotion is manual:

```bash
mv staging_reports/<file>.html cb_research_reports/
```

This exists because generated analysis looks finished before it is — every figure needs checking
against the filings before it carries the CB Research name.

## Editorial rules

Enforced in `references/source-hierarchy.md` and applied by every mode:

- **Never fabricate a figure.** Unavailable data is marked "Not disclosed", never estimated.
- **Never invent an attribution** — no imagined brokerage, rating, target price or quote.
- **No buy/sell/hold** in the skill's own voice. Named brokerage views are reported as theirs.
- **Company filings beat aggregators**, and conflicting sources are flagged visibly rather than
  silently resolved.
- **Every artifact carries** a `Source:` line with dates, an as-of date, and the research/educational
  disclaimer.

## Building the skill

The packaging script ships with Anthropic's `skill-creator` skill and needs `pyyaml`:

```bash
python -m scripts.package_skill /path/to/cauvery-business/sector-financial-analysis
```

The resulting `.skill` is a build artifact and is gitignored — distribute it via GitHub Releases.

## Mirroring published reports

```bash
python scripts/download_reports.py docs/report_dashboard_urls.txt
```

Downloads into `cb_research_reports/`.

---

Research and educational content only — **not investment advice**.
