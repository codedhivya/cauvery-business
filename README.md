# Cauvery Business — CB Research

Equity research tooling for Indian listed companies: a Claude skill that generates research-grade
analysis artifacts, plus the report collection it produces.

The reports are published at **[elangocauvery.github.io/CB-Finance](https://elangocauvery.github.io/CB-Finance/)**.

---

## What's here

Working on this repo with an AI agent? See **[AGENTS.md](AGENTS.md)** for the constraints that aren't
discoverable from the code — chiefly that generated reports never go straight to `reports/published/`,
and that mode files must never name a sector-specific metric. (`CLAUDE.md` symlinks to it.)

| Folder | Contents |
|---|---|
| `sector-financial-analysis/` | The Claude skill — source of truth |
| `reports/staging/` | Generated drafts awaiting review |
| `reports/published/` | Published reports (local mirror of the Pages site) |
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

**Sectors** — all 16 built: banking, NBFC/housing finance, insurance, capital markets, IT services,
pharma/healthcare, auto, consumer, capital goods, power & energy, metals, cement, chemicals,
infra/realty, telecom, new-age platforms. See [MAINTENANCE.md](MAINTENANCE.md) for the inventory and how
to add another.

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

## What you can ask

Ask in plain language — you don't need to name the skill, a mode, or a sector. The router works out which
sector file to load, which mode applies, and whether you want an answer or a document.

### Just ask — you get an answer in chat

The default. Concept questions, single figures, quick reads. No file is produced.

| Ask | What you get |
|---|---|
| `what is CASA and why does it matter` | The metric explained, with benchmarks and why it's a moat |
| `explain GNPA vs NNPA vs slippage` | Plain English, with which one actually matters |
| `what was HDFC Life's VNB margin last quarter` | The figure, sourced |
| `how did SBI do` | A short read on the quarter |
| `why do insurers use VNB instead of profit` | The reasoning, with a worked example |
| `is Dixon's 3% EBITDA margin bad` | No — with the EMS value-ladder explaining why |

Twenty questions in a row produce twenty answers, not twenty files.

### Ask it to build — you get an HTML report in `reports/staging/`

Say "build", "report", "dashboard", or ask for a full comparison.

| Mode | Ask like this |
|---|---|
| `dashboard` | `build me a dashboard for the top 3 private banks` |
| `financials` | `detailed Q1 financials for Sun Pharma and Cipla` |
| `charts` | `chart Tata Steel vs JSW Steel EBITDA per tonne` |
| `business-profile` | `how does Bajaj Finance actually make money — full writeup` |
| `segments` | `revenue by segment for Reliance` |
| `valuation` | `valuation comparison across the top 4 IT companies` |
| `swot` | `SWOT on Asian Paints` |
| `moats` | `what's UltraTech's moat` |
| `risks-outlook` | `risks and FY27 outlook for Vodafone Idea` |
| `analyst-ratings` | `what are analysts saying about Lupin` |
| `verdict` | `which is better — HDFC Bank or ICICI Bank` |
| `cb-rating` | `rank the EMS companies on CB Score` |
| `school` | `teach me how to read a bank's asset quality` |
| `quarterly-report` | `full report on Polycab for Q1 FY27` |
| `event-impact` | `how do the US generic tariffs hit Indian pharma` |

### Scope — one company or many

The same question works at four scopes, and the output adapts:

- **One company** — `how did Tata Steel do this quarter`
- **Head-to-head** — `compare Angel One and Groww`
- **Sector sweep** — `Q1 FY27 across all listed cement companies`
- **Cross-sector** — `rank Reliance, TCS and HDFC Bank` *(restricted to universal metrics — see below)*

### What it will refuse

Not gaps — deliberate limits, each for a reason:

| Ask | Response |
|---|---|
| `should I buy Syrma SGS` | Declines the recommendation, gives the fundamentals read instead |
| `compare HDFC Bank and Tata Steel on EBITDA` | Refuses — banks have no meaningful EBITDA; marks it "n/a — not comparable for this sector" |
| `what's the P/E of the Edelweiss IPO fund` | A fund isn't valued on a multiple |
| `what happened in the markets this week` | Not company evaluation — that's journalism |
| `what's India's GDP growth` | Macro, not a company or sector — answers plainly without the skill |

If no real brokerage view can be sourced, the Analyst Ratings section is **omitted** rather than invented.
If a figure can't be found after a targeted search, it's marked **"Not disclosed"** rather than estimated.

## Workflow

Generated output is a **draft**, never a publication:

```
skill generates  →  reports/staging/  →  you verify  →  reports/published/
```

The skill never writes to `reports/published/` and never promotes a file. Promotion is manual:

```bash
mv reports/staging/<file>.html reports/published/
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

## Syncing published reports

`reports/published/` mirrors the Pages site. To bring it up to date after new reports are published —
save the member portal page from your browser, then:

```bash
python3 scripts/sync_reports.py ~/Downloads/"CB Research — Member Portal.html"
python3 scripts/audit_corpus.py
```

The first downloads only what's missing. The second tells you whether the new reports introduce a sector,
metric or section the skill doesn't yet cover — findings are advisory, a human decides what to fold in.
Once folded in, `python3 scripts/audit_corpus.py --accept` baselines them as reviewed.

`scripts/download_reports.py` remains for re-downloading from an explicit URL list.

---

Research and educational content only — **not investment advice**.
