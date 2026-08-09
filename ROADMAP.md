# Roadmap — Sector Coverage

Status and remaining work for `sector-financial-analysis`. Read this before starting a new phase; it
carries an audit of `reports/published/` that is expensive to re-derive.

**Goal**: every report type in the 98-report collection reproducible by the skill, so the analytical work
in those reports isn't stranded in static HTML.

---

## Status

| | |
|---|---|
| **Architecture** | ✅ Complete — router, 15 modes, 3 shared references, template |
| **Sectors built** | ✅ `insurance`, `banking` — 10 of 98 reports |
| **Sectors remaining** | 13 sectors, 81 reports |
| **Cross-sector reports** | 7 — handled by the cross-sector *scope*, not a sector file |
| **Deliberately excluded** | 2 market-news digests (`Market_breaking_news_*`) — headline roundups are journalism, not company evaluation |

Insurance and banking were built together deliberately: their metrics share nothing (VNB / Combined Ratio
vs NIM / GNPA / CASA), so serving both on unmodified mode files proves the abstraction before it is
replicated 13 more times.

## Sector inventory

Derived by auditing all 98 reports. Report counts drive build order — biggest first.

| Sector | Reports | Status | Notes |
|---|---|---|---|
| consumer | 13 | ⬜ Phase 2 | retail, FMCG, alcobev, sugar, dairy, textiles, gold jewellery, hotels, amusement |
| capital-goods | 10 | ⬜ Phase 2 | defence, railways, EMS, cables, pumps |
| power-energy | 10 | ⬜ Phase 2 | power, solar, oil & gas / OMC |
| pharma-health | 9 | ⬜ Phase 2 | pharma, medtech, hospitals |
| auto | 7 | ⬜ Phase 3 | 2W, PV, spares, tyres, batteries |
| **banking** | **7** | ✅ **Done** | PSU, private, SFB |
| capital-markets | 6 | ⬜ Phase 3 | broking, exchanges, depositories, AMC, **funds/IPO funds** |
| it-services | 6 | ⬜ Phase 3 | |
| nbfc-hfc | 5 | ⬜ Phase 3 | **separate from banking** — no CASA, borrowing-funded, valued differently |
| chemicals | 5 | ⬜ Phase 4 | specialty, PVC, paints, fertilizers, recycling |
| metals | 4 | ⬜ Phase 4 | steel, aluminium |
| **insurance** | **3** | ✅ **Done** | life, health (SAHI), general, TPA |
| infra-realty | 3 | ⬜ Phase 4 | real estate, ports, **REITs/InvITs** |
| cement | 2 | ⬜ Phase 4 | |
| telecom | 1 | ⬜ Phase 4 | |

**Two sectors contain non-operating asset classes** needing explicit treatment, not exclusion:
`capital-markets` covers mutual funds (AUM, NAV, active share, expense ratio — `edelweiss_ipo_fund_analysis`),
and `infra-realty` covers REITs/InvITs (DPU, distribution yield, concession period — `india-reit-invit-dashboard`).
Their sector files must say plainly that these are analysed as funds/trusts, not operating companies.

## Phases

- **Phase 1** ✅ — architecture + insurance + banking
- **Phase 2** — consumer (13), capital-goods (10), power-energy (10), pharma-health (9) → 42 reports
- **Phase 3** — auto (7), capital-markets (6), it-services (6), nbfc-hfc (5) → 24 reports
- **Phase 4** — chemicals (5), metals (4), infra-realty (3), cement (2), telecom (1) → 15 reports

Each phase re-runs the full validation suite in [AGENTS.md](AGENTS.md).

---

## How to add a sector

**This should be a one-file job.** If a sector seems to need a mode file changed, it almost certainly
needs a substitution declared in its own sector file instead — check `insurance.md` and `banking.md`
first, since they sit at opposite ends of the metric spectrum and neither required a mode change.

### 1. Find the sector's existing reports

```bash
ls reports/published/ | grep -iE '<sector keywords>'
```

### 2. Mine them — this is where the accumulated work lives

The reports are the source of truth for what this sector actually needs. Extract:

```bash
# metrics the sector's reports actually use
python3 - <<'EOF'
import re,collections
files=[...]  # the sector's reports
c=collections.Counter()
for f in files:
    t=re.sub(r'<[^>]+>',' ',open(f,encoding='utf-8',errors='ignore').read())
    for m in re.findall(r'\b([A-Z]{2,6}|EBITDA|Margin|Yield)\b',t): c[m]+=1
print(c.most_common(40))
EOF

# section titles — reveals sector-specific tabs the mode set doesn't cover
grep -ohE 'class="(tab|tab-btn|section-title)[^"]*"[^>]*>[^<]{3,40}' reports/published/<file>.html
```

Look for: the category taxonomy, metric definitions, benchmark levels, the primary valuation multiple,
sector-specific sections, the regulator(s), and the company colour palette already in use.

### 3. Copy the template and fill all 10 sections

```bash
cp sector-financial-analysis/references/sectors/_template.md \
   sector-financial-analysis/references/sectors/<sector>.md
```

Every section matters, but three carry the most weight:
- **§6 per-mode specifics** — the delegation targets mode files reach into. All nine must exist.
- **§6 event transmission map** — the only genuinely sector-specific part of event analysis.
- **§10 cross-sector note** — which universal metrics (Revenue, EBITDA%, PAT, Mkt Cap, P/E, EV/EBITDA,
  Net Debt) do **not** apply, so a cross-sector table renders "n/a — not comparable for this sector"
  rather than a misleading figure. This is the single most important line for preventing silent
  misrepresentation.

### 4. Register it in the router

Add a row to the sector-detection table in `sector-financial-analysis/SKILL.md` (Step 1).

### 5. Validate

Run the three greps and the packaging script from [AGENTS.md](AGENTS.md). Also confirm the CB Rating
substitution table totals 100%.

### 6. Exercise it once

Run one real request against the new sector and check the output. `banking.md` looked complete until a
real report was built from it — that run is what surfaced the missing "Extra sections" declaration and
the mixed-reporting-season convention.

---

## Deferred

- **Export bundles** (`scripts/build_exports.py`) for ChatGPT / Gemini — waits until the subscriber
  platform is chosen and sector files stop churning. The discipline that keeps this cheap is already in
  place: no tool names or paths outside `output-conventions.md`.
- **GitHub Release** for the packaged `.skill` — it is gitignored as a build artifact.
- **A `PreToolUse` hook** blocking writes to `reports/published/`, making the staging rule mechanical
  rather than documented. Considered and declined for now.

## Open items

- The two staged reports in `reports/staging/` need figure verification before promotion. The private
  banks report is missing slippage ratio and credit cost for all five banks, and the life insurance
  verdict's P/EV multiples come from a single low-tier source.
