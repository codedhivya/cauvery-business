# Maintenance Guide — `sector-financial-analysis`

**The build is complete.** All 17 sector families in the corpus have a file, and none required a
mode-file change. This document is what you need to *maintain* it: how to add a seventeenth sector, the
judgment calls already settled so they aren't re-litigated, and how to keep the skill current as new
reports arrive.

For the hard rules and the validation command, see [AGENTS.md](AGENTS.md). For why the architecture is
shaped this way, see [docs/adr/](docs/adr/README.md).

| | |
|---|---|
| **Sectors** | 17 — every family in the 131-report corpus, plus REITs/InvITs as an asset class |
| **Modes** | 15, unchanged across all four build phases |
| **Coverage** | 123 of 131 reports; the rest are cross-sector scope, 2 news digests, a macro piece and the glossary |
| **Built in** | 5 phases — insurance+banking, then by report count, then a corpus refresh that added `new-age` |

---

## Sector inventory

Derived by auditing all 131 reports. Report counts drive build order — biggest first.

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
| **infra-realty** | 3 | ✅ **Done** | real estate developers, ports & logistics |
| **reit-invit** | 3 | ✅ **Done** | office/retail REITs, transmission & road InvITs — **an asset class, not an industry** |
| **cement** | 2 | ✅ **Done** | |
| **telecom** | 1 | ✅ **Done** | |
| **new-age** | 3 | ✅ **Done** | quick commerce, food delivery, marketplaces — **pre-profit platforms, not judged on PAT** |

**Two sectors contain non-operating asset classes** needing explicit treatment, not exclusion:
`capital-markets` covers mutual funds (AUM, NAV, active share, expense ratio — `edelweiss_ipo_fund_analysis`),
and `reit-invit` covers the trusts (DPU, distribution yield, NDCF coverage, LTV — `india-reit-invit-dashboard`).
Their sector files must say plainly that these are analysed as funds/trusts, not operating companies.


## What the checks cannot verify

`scripts/verify_skill.py` confirms content and rules are present — 62 checks. It **cannot** confirm the
router triggers unprompted, because any session that authored the files has them in context whether the
skill loads or not. That needs a fresh session.

This was tested and passed: a cold session correctly declined a macro question (citing the skill's own
scope boundary), chose `sector-financial-analysis` over a competing stock-analysis skill on a
single-company ask, routed to chat rather than a file, and used `metals.md`'s framing on a sector file
that had never been run.

**If you change the description, re-test triggering.** Two questions suffice — one that should fire
(`what is CASA and why does it matter`) and one that should not (`what's India's GDP growth this year`),
asked without naming the skill, then ask which skill it used.

**Watch for collision with `indian-stock-fundamental-analyser`.** That skill also covers Indian listed
stocks and competes for the same single-company asks. In testing, `sector-financial-analysis` won on
`analyse Tata Steel` — but the two overlap, so any description change risks tipping it the other way. If
a single-company ask starts routing to the other skill, none of the sector work gets used, and the
symptom is subtle: you get a competent generic answer instead of one citing EBITDA per tonne and captive
ore. Test `analyse <company>` after any description edit, not just the two questions above.

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

**All sixteen sector families in the corpus are built, and none required a mode-file change.** They span
insurers, banks, NBFCs, exchanges, hotels, order-book manufacturers, refiners, hospitals, IT services,
vehicle makers, steel mills, cement plants, chemical producers, property developers and telcos — on the
same fifteen unmodified mode files — including `new-age`, added after the corpus refresh. That is the
strongest available evidence the abstraction holds.

The instructions below apply to a **seventeenth** sector, if the corpus grows beyond these families
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
| A trust or fund, not an operating company | `capital-markets.md` (funds), `reit-invit.md` (trusts) | No P&L ranking, substituted CB parameter set, never in a cross-sector operating table |

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

## Taxonomy audit — how sector categories should be derived

Prompted by the REIT/InvIT rebuild (ADR-0012), all 17 sector files were audited against the reports they
were built from, asking one question: **does the file's category taxonomy match how the corpus actually
compares its subjects?**

**13 of 17 passed.** Insurance (Life / Health / General / TPA), banking (PSU / Private / SFB),
capital-markets (Exchange / Depository / RTA / Broker / AMC / Fund) and others match the corpus exactly —
in several cases the report *filenames* carry the taxonomy directly.

**Cement passed on a point worth recording**: its taxonomy is plant type (integrated vs grinding), but
its *organising* axis is regional, and the file already leads with that — "a regional business
masquerading as a national one". A secondary taxonomy is fine as long as the primary axis is the one the
corpus reasons in.

**Four findings**, three of the same kind:

| Sector | Finding | Evidence |
|---|---|---|
| `reit-invit` | Taxonomy built on the wrong axis — a flat list of asset types instead of the author's REIT-vs-InvIT split | ADR-0012 addendum 2 |
| `nbfc-hfc` | **NBFC-MFI missing entirely** — zero mentions of microfinance, PAR or collection efficiency | a dedicated MFI sector report (182 KB) |
| `chemicals` | **Recycling missing entirely** — zero mentions of EPR or scrap spread | a dedicated recycling sector report |
| `power-energy` | **Coal mining missing entirely** — a miner is not a generator, and has no PLF or PPA | a Coal India report |

The three "missing entirely" cases share a cause: the sector was built from the *majority* of its
reports, and a single report covering a distinct business model was absorbed into the nearest category
instead of getting one. **A sector with N reports needs each report's business model represented, not
the modal one.**

**The rule this establishes**: derive a sector's taxonomy from **how the corpus compares its subjects**,
not from how the subjects could plausibly be sorted. The plausible sort for trusts was by underlying
asset, and it was analytically sterile — it could not express that a REIT is perpetual and an InvIT runs
off. The author's sort was by vehicle, and it carried the insight.

**How to re-run this audit** after adding reports:

```bash
python3 scripts/audit_corpus.py     # flags unbuilt sectors and undefined metrics
```

Then, for any sector with a new report, check by hand that the report's business model appears in the
sector file's section 1 — the script checks metrics, not taxonomy.

## Deferred

- **Export bundles** (`scripts/build_exports.py`) for ChatGPT / Gemini — waits until the subscriber
  platform is chosen and sector files stop churning. The discipline that keeps this cheap is already in
  place: no tool names or paths outside `output-conventions.md`.
- **GitHub Release** for the packaged `.skill` — it is gitignored as a build artifact.
- **A `PreToolUse` hook** blocking writes to `reports/published/`, making the staging rule mechanical
  rather than documented. Considered and declined for now.
