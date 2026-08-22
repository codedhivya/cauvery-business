# Agent Context — Cauvery Business (CB Research)

Equity research tooling for Indian listed companies. This is **not a typical application repo** — there
is no build, no test suite, no runtime. It contains a Claude skill (markdown) and the report collection
it produces (static HTML).

```
sector-financial-analysis/   the skill — source of truth
reports/published/           131 verified reports; the author stands behind these
reports/staging/             generated drafts awaiting human review
scripts/sync_reports.py      mirrors published reports from the Pages site
docs/                        report URL lists
```

Reports are published at <https://elangocauvery.github.io/CB-Finance/>.

**Maintaining or extending it?** See **[MAINTENANCE.md](MAINTENANCE.md)** — the sector inventory, the
recipe for adding a seventeenth sector, and the judgment calls already settled. **All 17 sectors are
built**; the build is complete. Don't re-derive the sector taxonomy by re-auditing the corpus — it's
already recorded there.

**About to change something that looks arbitrary?** See **[docs/adr/](docs/adr/README.md)**. Several of
these decisions are counterintuitive and were made against specific corpus evidence — why one skill
rather than nine, why mode files may not name a sector metric, why cross-sector tables refuse EBITDA for
banks, why the skill never copies a figure from a prior report.

---

## Hard rules

These are not style preferences. Each exists because breaking it causes a specific, hard-to-detect
failure.

### 1. Never write to `reports/published/`

Generated output goes to `reports/staging/`. The author verifies figures against filings, then promotes
manually with `mv`. **Promotion is never an agent's action**, even when asked to "publish" or "finalise"
— say what the command is and let the author run it.

*Why*: these reports go to subscribers who will not independently check the numbers. Generated analysis
looks finished before it is, and writing straight to the published folder collapses the verification
step silently.

### 2. Never fabricate a figure or an attribution

- Unavailable data is marked **"Not disclosed"** — never estimated, interpolated, or inferred.
- No invented brokerage name, rating, target price, or quote. If no real named view can be sourced,
  **omit the section**.
- Never issue buy/sell/hold in the skill's own voice. Report named third-party views as theirs.
- Every artifact carries a `Source:` line **with dates**, an as-of date, and the research/educational
  disclaimer.

*Why*: a reader has no way to distinguish a filing-sourced figure from an invented one. The attribution
is the difference between research and decoration.

### 3. Never put a sector metric in a mode file

`references/modes/*.md` must contain **zero** sector-specific metrics — no `VNB`, `Combined Ratio`,
`NIM`, `GNPA`, `CASA`, `IRDAI`, `EV/EBITDA`. Those live in `references/sectors/*.md`.

*Why*: this is the contract that makes the skill multi-sector. Nothing visibly breaks when a metric leaks
into a mode file — but the abstraction dies, and every future sector inherits one sector's vocabulary.
Adding a sector must remain a one-file job.

### 4. Never hardcode a period or a figure

No `Q1FY27` literals and no company numbers inside `references/`. Sector files hold only durable facts
(definitions, benchmarks, palette, regulator rules). Every run sources figures live.

---

## The skill's architecture

One skill, all sectors. It routes each request by **sector → mode → scope**, loading only the two
reference files it needs.

```
sector-financial-analysis/
├── SKILL.md                      router
└── references/
    ├── design-system.md          shared CSS / Chart.js — sector-agnostic
    ├── source-hierarchy.md       sourcing tiers, attribution, compliance
    ├── output-conventions.md     THE ONLY FILE NAMING PATHS OR TOOLS
    ├── modes/                    HOW to build (15 files)
    └── sectors/                  WHAT the metrics are (17 files + _template.md)
```

**The split**: mode files own the craft, sector files own the domain. How to build a SWOT grid is
identical in every sector; only the metric names differ. Insurance (VNB, Combined Ratio) and banking
(NIM, GNPA, CASA) sit at opposite ends of the metric spectrum and both run on the *unmodified* modes.

**Adding a sector** = copy `references/sectors/_template.md`, fill it in, add a row to the router's
sector table. **No mode file should change.** If a sector seems to require editing a mode, it almost
certainly needs a substitution declared in its own sector file instead.

**Paths and tool names live only in `output-conventions.md`.** This is what keeps the skill portable to
other agent environments — porting means editing one file, not fifteen.

---

## After changing the skill, run this

```bash
python3 scripts/verify_skill.py
```

62 checks in one command: the structural contracts (no sector metric in a mode file, no tool name or path
outside `output-conventions.md`, no hardcoded period, every CSS class resolves), per-sector completeness
(10 numbered sections, 9 delegation targets, CB weights totalling 100%), that each sector still carries
its defining insight, that every refusal survives, and that the router's depth-routing and scope limits
are intact. Exit 1 on failure, so it works in CI or a pre-commit hook.

**What it cannot check**: whether the router triggers unprompted. That needs a session that did not
author the files — see the triggering test in [MAINTENANCE.md](MAINTENANCE.md).

The individual greps below are what the script automates, kept here for when you want to run one in
isolation:

```bash
cd sector-financial-analysis/references

# no sector metric leaked into a mode file
# (note: EV/EBITDA, P/E, EBITDA%, Net Debt are UNIVERSAL cross-sector metrics
#  and legitimately appear in modes — do not add them to this pattern)
grep -nE 'VNB|Combined Ratio|IRDAI|persistency|GWP|GDPI|Embedded Value|\bNIM\b|GNPA|NNPA|\bCASA\b|CRAR|CET-1|slippage|USFDA' modes/*.md

# no tool name or path outside output-conventions.md
grep -nE 'SendUserFile|present_files|reports/' modes/*.md sectors/*.md

# no hardcoded period
grep -nE 'Q[1-4] ?FY[0-9]{2}' modes/*.md sectors/*.md
```

All three must return nothing. Then validate and package — the script ships with Anthropic's
`skill-creator` skill and needs `pyyaml`:

```bash
python -m scripts.quick_validate <abs-path>/sector-financial-analysis
python -m scripts.package_skill  <abs-path>/sector-financial-analysis
```

The `.skill` output is a build artifact and is gitignored; distribute via GitHub Releases.

Also check: every CSS class referenced in `modes/*.md` resolves to a definition in `design-system.md`
or the owning sector file, and each sector's CB Rating substitution table totals 100%.

---

## Syncing new published reports

The published collection is a local mirror of the Pages site. When reports are added there, the mirror
falls behind — and since the sector files were built from that mirror, anything it hasn't seen is
knowledge the skill doesn't have.

```bash
# 1. pull anything the site has that the mirror doesn't
python3 scripts/sync_reports.py

# 2. find out whether the new reports introduce anything the skill lacks
python3 scripts/audit_corpus.py

# 3. fold in what belongs (a human decides — findings are advisory), then:
python3 scripts/audit_corpus.py --accept

# 4. if step 3 changed the skill:
python3 scripts/verify_skill.py
```

Step 1 reads the live index directly — no browser step. The index builds its links in JavaScript, so
the report list comes from the embedded `file:` entries rather than from hrefs. It downloads only what's
missing and rewrites `docs/report_dashboard_urls.txt`. Pass a saved portal page as an argument to read
that instead.

A 404 in step 1 is a **broken link on the site itself** — worth fixing at the source, since members hit
it too. Two are currently live: `Banking_Q1FY27.html` and `india_steel_fy26_dashboard.ai.html`.

Step 2 is the one that matters. It flags **unbuilt sectors**, **metrics not defined** in the matching
sector file, **sections no mode covers**, and **unknown CSS classes**. Not everything it flags needs
acting on — a new metric may deserve a sector-file entry, or may be a one-off the author chose. Extend
`SECTOR_KEYWORDS` in the script whenever a sector is added.

## When a report arrives that the skill didn't generate

Reports written by hand — by a colleague, or before the skill existed — often carry knowledge the skill
lacks: a sector with no file, a metric no sector file defines, a section type no mode covers. Left
unnoticed, that knowledge stays stranded in static HTML, which is the problem the skill exists to solve.

```bash
python3 scripts/audit_corpus.py            # what's new, and what it introduces
python3 scripts/audit_corpus.py --accept   # baseline the corpus as reviewed
python3 scripts/audit_corpus.py --all      # re-audit everything, ignoring the baseline
```

It compares `reports/published/` against a checksum baseline (`docs/corpus-manifest.json`) and flags, for
new or changed reports: **unbuilt sectors**, **metrics not defined** in the matching sector file,
**sections no mode covers**, and **CSS classes** absent from `design-system.md`. Exit code 1 when action
is needed, so it works in CI or a pre-commit hook.

Findings are **advisory**. A new metric may deserve a sector-file entry, or may be a one-off the author
chose deliberately — a human decides. After folding in what belongs, re-baseline with `--accept`.

When adding a sector, extend `SECTOR_KEYWORDS` in the script so its reports classify correctly.

## Conventions

- **Report filenames**: `<Scope>_<Mode>_<Period>.html` — e.g. `HDFCLife_Dashboard_Q1FY27.html`,
  `Cement_Companies_Dashboard_Q4FY26.html`. Match the existing collection.
- **Regenerating a report for a new period**: read the prior *published* report for company scope,
  section selection, layout and chart types — then re-source every number. Inherit structure, never
  figures. A ratio carried forward is how a stale number survives across quarters.
- **Don't force an artifact onto a short question.** "What's HDFC Life's VNB margin?" deserves an inline
  answer with the same sourcing discipline, not an HTML file.

## Recovering the superseded skills

This repo previously held 9 separate insurance skills, removed once the consolidated skill was verified
lossless. They remain in git history:

```bash
git show dcb9d8f:archive/handoff/HANDOFF.md
git checkout dcb9d8f -- archive/          # restore the whole folder
```
