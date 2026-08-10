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
| **Sectors built** | ✅ **all 15** — every sector family in the corpus — 91 reports |
| **Sectors remaining** | **none** — the build is complete |

**The 98 reports break down as:** 91 belong to the 15 sector families (**all 91 covered**), and 7
are cross-sector — handled by the cross-sector *scope* rather than a sector file. **2 of those 7 are the
market-news digests** (`Market_breaking_news_*`), deliberately excluded: a headline roundup is journalism,
not company evaluation. That leaves 5 genuine cross-sector reports (the rankers and multi-sector
dashboards).

Insurance and banking were built together deliberately: their metrics share nothing (VNB / Combined Ratio
vs NIM / GNPA / CASA), so serving both on unmodified mode files proved the abstraction before it was
replicated. Phase 2 confirmed it: four more sectors, spanning order-book manufacturers, hotels, refiners
and hospitals, needed **zero mode-file changes**.

## Sector inventory

Derived by auditing all 98 reports. Report counts drive build order — biggest first.

| Sector | Reports | Status | Notes |
|---|---|---|---|
| **consumer** | 13 | ✅ **Done** | retail, FMCG, alcobev, sugar, dairy, textiles, gold jewellery, hotels, amusement |
| **capital-goods** | 10 | ✅ **Done** | defence, railways, EMS, cables, pumps |
| **power-energy** | 10 | ✅ **Done** | power, solar, oil & gas / OMC |
| **pharma-health** | 9 | ✅ **Done** | pharma, medtech, hospitals |
| **auto** | 7 | ✅ **Done** | 2W, PV, spares, tyres, batteries |
| **banking** | **7** | ✅ **Done** | PSU, private, SFB |
| **capital-markets** | 6 | ✅ **Done** | broking, exchanges, depositories, AMC, **funds/IPO funds** |
| **it-services** | 6 | ✅ **Done** | |
| **nbfc-hfc** | 5 | ✅ **Done** | **separate from banking** — no CASA, borrowing-funded, valued differently |
| **chemicals** | 5 | ✅ **Done** | specialty, PVC, paints, fertilizers, recycling |
| **metals** | 4 | ✅ **Done** | steel, aluminium |
| **insurance** | **3** | ✅ **Done** | life, health (SAHI), general, TPA |
| **infra-realty** | 3 | ✅ **Done** | real estate, ports, **REITs/InvITs** |
| **cement** | 2 | ✅ **Done** | |
| **telecom** | 1 | ✅ **Done** | |

**Two sectors contain non-operating asset classes** needing explicit treatment, not exclusion:
`capital-markets` covers mutual funds (AUM, NAV, active share, expense ratio — `edelweiss_ipo_fund_analysis`),
and `infra-realty` covers REITs/InvITs (DPU, distribution yield, concession period — `india-reit-invit-dashboard`).
Their sector files must say plainly that these are analysed as funds/trusts, not operating companies.

## Phases

- **Phase 1** ✅ — architecture + insurance + banking
- **Phase 2** ✅ — consumer (13), capital-goods (10), power-energy (10), pharma-health (9) → 42 reports
- **Phase 3** ✅ — auto (7), capital-markets (6), it-services (6), nbfc-hfc (5) → 24 reports
- **Phase 4** ✅ — chemicals (5), metals (4), infra-realty (3), cement (2), telecom (1) → 15 reports

Each phase re-runs the full validation suite in [AGENTS.md](AGENTS.md).

---

## The one thing the checks cannot verify

`scripts/verify_skill.py` confirms the skill's content and rules are present and correct — 49 checks.
It cannot confirm the router **triggers unprompted**, because any session that authored the files has
them in context whether the skill loads or not.

That needs a fresh session. Ask these six, in order:

| Ask | Correct behaviour |
|---|---|
| `what is CASA and why does it matter` | Answers **in chat**. Says CASA cannot be bought quickly; gives >40% / >45% |
| `compare HDFC Bank and Tata Steel on EBITDA` | **Refuses** — banks have no meaningful EBITDA. The most dangerous silent failure |
| `what's India's GDP growth this year` | **Stays quiet** — no skill invocation. Over-triggering is the likelier fault |
| `how did Tata Steel do in Q1 FY27` | Chat answer citing EBITDA per tonne and captive ore |
| `should I buy Syrma SGS` | Declines the recommendation, offers a fundamentals read |
| `build me a full report on Polycab` | **Builds a file**, to `reports/staging/`, with the earnings-quality header |

If only three: the first, second and third — they cover doesn't-trigger, triggers-but-breaks-a-guardrail,
and triggers-when-it-shouldn't. If triggering is wrong the fix is the description (`skill-creator` has an
optimisation loop for it); if content is wrong it is a sector-file edit.

## Keeping the skill current with the corpus

The corpus is not frozen — reports arrive that the skill didn't generate. `scripts/audit_corpus.py`
detects the gap between what's in `reports/published/` and what the skill knows:

```bash
python3 scripts/audit_corpus.py            # show drift
python3 scripts/audit_corpus.py --accept   # baseline as reviewed
```

It flags unbuilt sectors, undefined metrics, uncovered sections and unknown CSS classes for any new or
changed report. Run it after a colleague adds a report, and at the start of each phase — `--all` against
the current corpus is a good way to see the remaining work, since it surfaces exactly what the next
sector files need to define.

Extend `SECTOR_KEYWORDS` in the script whenever a sector is added.

## How to add a sector

**All fifteen sector families in the corpus are built, and none required a mode-file change.** They span
insurers, banks, NBFCs, exchanges, hotels, order-book manufacturers, refiners, hospitals, IT services,
vehicle makers, steel mills, cement plants, chemical producers, property developers and telcos — on the
same fifteen unmodified mode files. That is the strongest available evidence the abstraction holds.

The instructions below apply to a **sixteenth** sector, if the corpus ever grows beyond these families
(aviation, shipping, media and healthcare-adjacent services are the plausible candidates).

### Which existing file to copy from

Start from the closest precedent rather than the template alone — it will be substantially complete:

| If the new sector is… | Copy from | Why |
|---|---|---|
| A lender or fee-earning financial | `banking.md`, `nbfc-hfc.md`, `capital-markets.md` | Never uses Debt/Leverage in CB Rating; asset quality or funding substitutes |
| A capital-intensive commodity processor | `metals.md`, `cement.md`, `power-energy.md` | Per-unit economics, Debt & Cash Flow component, growth scored on **volume not revenue** |
| An order-book manufacturer | `capital-goods.md` | Order inflow and book-to-bill into Growth; working-capital table mandatory |
| A people or services business | `it-services.md` | Delivery Quality replaces PAT Quality — utilisation and attrition lead the P&L |
| A consumer-facing brand or retailer | `consumer.md` | Like-for-like growth (SSSG/RevPAR) rather than headline revenue |
| A regulated, licence-gated business | `pharma-health.md`, `telecom.md` | Regulatory standing substitutes into Forward Outlook, because a licence action can remove revenue |
| A trust or fund, not an operating company | `capital-markets.md` (funds), `infra-realty.md` (REITs) | No P&L ranking, no CB Rating, never in a cross-sector table |

### Judgment calls from earlier phases, so they aren't re-litigated

- **Power *equipment* makers belong in `capital-goods`, not `power-energy`.** ABB, Siemens Energy, Hitachi
  Energy, Voltamp and CG Power are order-book businesses judged on book-to-bill; generators are
  capacity-and-tariff businesses judged on PLF. Both are "power" companies and they are analysed
  differently.
- **`power-energy` uses a five-component CB Rating.** Deliberate — see the template's note.
- **Two disciplines are mandatory, not optional**: refiners must separate inventory gain/loss from core
  GRM, and capital-goods reports must carry a working-capital table.
- **`nbfc-hfc` is not banking.** NBFCs cannot take public deposits, so there is no CASA and no low-cost
  funding moat. Cost of funds, borrowing mix, credit rating and ALM replace the deposit-franchise
  discussion entirely, and Funding & Capital replaces Forward Outlook in its CB Rating.
- **A fund is not an operating company.** `capital-markets` covers mutual funds, which have no P&L, no
  EBITDA and no market cap. `financials`, `valuation`, `cb-rating` and `moats` are skipped for them
  rather than forced, and a fund never appears in a cross-sector table.
- **`it-services` substitutes Delivery Quality for PAT Quality** — utilisation, attrition and revenue per
  employee deteriorate before the P&L shows it, which is the point of the substitution.
- **Internet/classifieds names sit inside `it-services` but use different metrics** — billings, paid
  users and segment profitability, never utilisation or TCV.
- **Commodity sectors score growth on volume, not revenue.** `metals` and `cement` both do this: a steel
  company whose revenue rose 30% because steel prices rose 30% has not grown, and revenue-based scoring
  would reward the commodity cycle rather than the company.
- **Developers are read on pre-sales, not revenue.** Reported revenue describes projects sold two or
  three years earlier, so `infra-realty` leads its tables with pre-sales and collections. A developer can
  post falling revenue during a record sales year.
- **Telecom weights liabilities above profit.** Spectrum and AGR dues get a 25% CB component while PAT
  Quality drops to 10%, because reported profit is a weak signal there while servicing government-set
  obligations is the binding constraint. EV must include those dues.
- **`chemicals` is five businesses, not one.** Specialty behaves like pharma, commodity like metals,
  fertilisers are subsidy-administered, pipes are building materials and paints are consumer. Margin
  bands span 8–25%; a single sector band would be meaningless.

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
