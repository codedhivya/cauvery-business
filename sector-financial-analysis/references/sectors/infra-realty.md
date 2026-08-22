# Sector: Infrastructure & Real Estate (India)

Covers residential and commercial real-estate developers, and ports and logistics infrastructure.

**Two unlike businesses share this file.** A developer is judged on pre-sales and collections — reported
revenue describes projects sold years ago; a port on cargo volume and concession tenure. **Classify
first**: applying developer metrics to a port, or reading a developer's P&L as its current trading,
produces nonsense.

**REITs and InvITs are not in this file.** They are a distinct asset class — a trust that
passes income through rather than a company that reinvests — and an InvIT's assets are often
transmission lines or toll roads, nothing to do with real estate. See `reit-invit.md`.


## 1. Category taxonomy

| Category | What it is | Examples |
|---|---|---|
| **Residential developer** | Builds and sells homes. Revenue recognition lags sales by years, so **pre-sales, not revenue, is the live metric** | DLF, Prestige Estates, Sobha, Oberoi Realty, Brigade, Anant Raj, Ganesh Housing |
| **Commercial / lease developer** | Builds and leases offices and retail. Annuity income, occupancy-driven | the commercial arms of the above |
| **Ports & logistics** | Cargo handling under long concessions | Adani Ports & SEZ, JSW Infrastructure, Gujarat Pipavav Port |

## 2. How companies in this sector make money

**Residential developers** sell homes before or during construction, then recognise revenue on
completion. This creates a structural lag: **reported revenue describes projects sold two or three years
ago, while pre-sales describe the business today.** A developer can post falling revenue during a record
sales year, or rising revenue while sales collapse. Anyone reading the P&L alone will consistently
misread the business.

The sequence that matters is **pre-sales (bookings) → collections → construction spend → revenue
recognition**. Collections are the cash reality; bookings without collections are a receivable and a
risk. Land bank is the raw material, and how it was acquired — outright purchase, joint development
agreement, or joint venture — determines both capital intensity and margin.

**Commercial developers** lease rather than sell. Income is contracted rent with escalations, so the
metrics are occupancy, leased versus vacant area, rental rate per square foot, and the mark-to-market
gap between in-place and market rents. It is an annuity business valued closer to a REIT than to a
residential developer.

**Ports** operate under long concessions granted by government. Revenue is cargo volume × realisation per
tonne, and the concession defines tenure, tariff freedom and what happens at expiry. Cargo mix matters
enormously — container handling earns far more per tonne than bulk coal.

A developer's **commercial arm** can look superficially like a REIT — contracted rent, occupancy, WALE —
but it sits inside an operating company that retains and reinvests earnings. That is the line: analyse it
here, and analyse the trust in `reit-invit.md`.

## 3. Metric definitions

### Residential developers

- **Pre-sales / bookings (₹ cr and msf)** — value and area sold in the period. **The single most
  important metric**, and the one management guides on.
- **Collections (₹ cr)** — cash actually received. The reality check on bookings.
- **Average realisation (₹/sq ft)** — pricing and mix.
- **Launches (msf)** — new inventory brought to market; the forward pipeline.
- **Unsold inventory** and **inventory overhang** (quarters of sales at current run-rate) — the demand
  health signal. Rising unsold inventory alongside rising launches is the classic warning.
- **Land bank** (acres or msf of development potential), and whether owned, JDA or JV.
- **Net debt and net debt / operating cash flow** — developers have historically failed on leverage, not
  on demand.
- **Revenue recognition backlog** — sold but unrecognised, which is future reported revenue already
  contracted.

### Commercial / lease

- **Leased vs vacant area (msf)**, **occupancy (%)**
- **Rental rate per sq ft** and **mark-to-market gap** on renewals
- **WALE (weighted average lease expiry)** — the longer, the more secure the income

### Ports

- **Cargo volume (MMT)** and **TEU** for containers
- **Cargo mix** — container, bulk, liquid, each with very different realisation
- **Realisation per tonne**
- **Concession tenure remaining** and terms — a port with eight years left is a different asset from one
  with thirty
- **Capacity and utilisation**


## 4. Benchmarks — what good looks like

Indicative; verify against the company's own history and the category.

| Category | Metric | Healthy |
|---|---|---|
| Residential | Pre-sales growth | double digit; and **collections tracking bookings**, not lagging |
| Residential | EBITDA margin | 20–28% |
| Residential | Net debt / operating cash flow | <2× — the sector's historic failure point |
| Residential | Inventory overhang | <8 quarters of sales |
| Commercial | Occupancy | >90% |
| Commercial | WALE | >5 years |
| Ports | EBITDA margin | 55–70% — genuinely high; concession assets with fixed cost bases |
| Ports | Cargo growth | at or above national port-traffic growth |

**What to watch, by category:**

- **Residential** — Are pre-sales growing, and are **collections keeping pace**? Is unsold inventory
  rising? Is the launch pipeline funded? Where is net debt against operating cash flow? Is the land bank
  owned or JDA — the latter is capital-light but shares margin.
- **Commercial** — Is occupancy holding? What is the mark-to-market gap on renewals? Is the leasing
  pipeline converting?
- **Ports** — Is cargo growing above national traffic growth? Is the mix shifting toward containers? How
  much concession tenure remains, and what happens at expiry?

## 5. Regulatory quick reference

| Area | Body / rule |
|---|---|
| Real estate projects | **RERA** — mandatory registration, escrow of collections, delivery timelines. Materially changed developer cash management |
| Ports | **Major Port Authorities Act**; TAMP historically for tariff; concession agreements with the port authority |
| Land and approvals | state-level; approval timelines are a real constraint on launches |
| Industry data | Ministry of Ports for cargo traffic; RERA portals for project data |

**RERA is the defining regulatory fact for developers** — escrowed collections mean cash received is not
freely deployable, which is why collections and net debt must be read together rather than separately.

## 6. Per-mode specifics

### Headline KPIs by category (`dashboard`)

| Category | KPIs |
|---|---|
| Residential | **Pre-sales (₹cr, msf)**, collections, launches, realisation/sq ft, revenue, EBITDA margin, PAT, net debt |
| Commercial | Leased area, occupancy, rental/sq ft, rental income, EBITDA margin, PAT |
| Ports | Cargo volume (MMT), TEU, realisation/t, revenue, EBITDA margin, PAT, net debt |

### Table columns by category (`financials`)

- **Residential** — Period, **Pre-sales (₹cr), Pre-sales (msf), Collections**, Launches, Revenue,
  EBITDA, EBITDA%, PAT, Net debt. **Pre-sales and collections lead the table**, ahead of revenue —
  putting revenue first would foreground the most lagging number in the sector.
- **Commercial** — Period, Leased area, Occupancy, Rental income, EBITDA%, PAT, WALE
- **Ports** — Period, Cargo (MMT), TEU, Realisation/t, Revenue, EBITDA, EBITDA%, PAT, concession note

Add an **inventory and land bank** table for residential: unsold inventory, overhang in quarters, land
bank by city and tenure basis.

### Chart reference lines (`charts`)

| Metric | Line | Label |
|---|---|---|
| Occupancy (commercial) | 90% | "Healthy occupancy" |
| Net debt / operating cash flow (residential) | 2.0× | "Sector comfort" |
| Inventory overhang | 8 quarters | "Comfortable inventory" |

**Chart pre-sales, not revenue, for residential developers**, and say so — a revenue chart shows what was
sold three years ago.

### Profile coverage by category (`business-profile`)

- **Residential** — city presence and project portfolio, land bank with tenure basis (owned/JDA/JV),
  segment focus (luxury/mid/affordable), launch pipeline, brand and delivery track record — in a sector
  with a history of delayed projects, **delivery record is a competitive asset**.
- **Commercial** — portfolio by city and grade, tenant profile and concentration, occupancy, WALE,
  development pipeline.
- **Ports** — port locations and capacity, cargo mix, concession terms and remaining tenure, hinterland
  connectivity, customer concentration.

### Moat candidates by category (`moats`)

- **Land bank in supply-constrained locations** — the residential moat. Land in a prime micro-market
  cannot be replicated, and acquisition cost basis determines margin for a decade.
- **Delivery track record and brand** — in a sector where buyers have been burned by delays, a developer
  who delivers commands a genuine price premium and faster sell-through.
- **Ports — the concession itself.** A long concession at a location with hinterland access is a legal
  and geographic monopoly for its tenure. **The strongest moat in this file**; state remaining tenure,
  since the moat has an expiry date.
- **Commercial — irreplaceable locations** and anchor-tenant relationships.
- **Be sceptical** of land bank size alone. A large land bank in a weak micro-market is trapped capital,
  not an asset — location and cost basis matter more than acreage.

### Valuation (`valuation`)

**Residential developers** are valued on **NAV** — the present value of the development pipeline — rather
than on P/E, because reported earnings reflect projects sold years ago. Price-to-NAV and the premium or
discount to NAV is the standard basis. P/E is a poor primary measure here and should be treated as
secondary with that stated.

**Commercial and ports** — **EV/EBITDA**, with ports also compared on EV per tonne of capacity.

If a listed trust holds the same kind of asset, it is **not** a valuation comparable for an operating
company here — see `reit-invit.md`.

### CB Rating substitutions (`cb-rating`)

Capital-intensive with explicit Debt & Cash Flow, following the `power-energy` precedent.

| Component | Weight | Infra-realty substitution |
|---|---|---|
| Growth | 25% | **Pre-sales growth** (residential) / **cargo growth vs national traffic** (ports) — never reported revenue for developers |
| Profitability | 25% | EBITDA margin against the **category** band (residential 20–28%, ports 55–70%) and direction |
| PAT Quality | 15% | **Collections against bookings** for developers — bookings without collections are a receivable, not profit; PAT adjusted for one-offs elsewhere |
| Debt & Cash Flow | 20% | Net debt / operating cash flow, and whether the launch or capex pipeline is funded |
| Asset Position & Outlook | 15% | Land bank quality and tenure basis, concession tenure remaining, launch or acquisition pipeline |

Total 100%. **This parameter set is for operating companies only.** A trust uses the REIT/InvIT set in
`reit-invit.md`; where a substitution stops making sense, skip the mode rather than forcing it.

### Extra sections (`quarterly-report`)

- **Bookings & Sales** — pre-sales, collections, launches, realisation. Recurs in existing reports and is
  the centrepiece for a developer.
- **Land Bank** — recurs in existing reports; acreage, city, tenure basis, development potential.
- **Inventory & Overhang** — unsold stock and quarters of cover.
- **Concession Profile** — ports: tenure remaining, tariff terms, expiry treatment.
- **Policy** — recurs in existing reports: RERA, port policy and concession terms.

### Event transmission map (`event-impact`, `risks-outlook`)

| Event | Reaches results via | Exposure basis to cite |
|---|---|---|
| Interest-rate change | home-loan affordability and housing demand | residential share of the mix; ticket-size band |
| RERA enforcement change | escrow, launch timelines, working capital | projects under registration |
| Stamp duty change (state) | near-term demand pull-forward or drop | that state's share of bookings |
| Approval or clearance delay | launch pipeline | projects awaiting approval |
| Commercial rent-cycle shift / return-to-office | occupancy, mark-to-market | leased area, expiry schedule |
| Cargo policy or trade volume change | port volumes | cargo mix, trade-route exposure |
| Concession renewal or expiry | revenue continuity | remaining tenure, renewal terms |
| Input cost (cement, steel) move | construction cost, developer margin | under-construction pipeline |

## 7. Where to look (sourcing)

**Tier 1** — quarterly investor presentations. Developers disclose pre-sales, collections, launches,
realisation, unsold inventory and land bank there and typically **not in the press release**, which is
why the presentation is essential rather than optional in this sector. Ports disclose cargo volume and
mix monthly.

**Tier 2 — sector authorities**: **RERA portals** (state-level) for project registration, timelines and
sometimes sales data — an unusually good primary source;
**Ministry of Ports, Shipping and Waterways** for national cargo traffic, the right denominator for a
port's growth claim; **Knight Frank / JLL / Anarock** for city-level absorption and price data, attributed
to the firm.

A developer's pre-sales growth means little without city absorption data alongside — growing 10% in a
market that grew 20% is losing share.

## 8. Company colour palette

**The companies named here are illustrative as at authoring, not the current universe.** Anything listed since belongs in the analysis too — see "Establish the universe before ranking anything" in `source-hierarchy.md`.

| Company | Main | Soft tint |
|---|---|---|
| DLF | #1d4ed8 | #eff6ff |
| Prestige Estates | #c84b2f | #fef3f0 |
| Oberoi Realty | #166534 | #f0fdf4 |
| Sobha | #7f1d1d | #fef2f2 |
| Brigade Enterprises | #ea580c | #fff7ed |
| Godrej Properties | #15803d | #f0fdf4 |
| Anant Raj | #7c3aed | #f5f3ff |
| Ganesh Housing | #a16207 | #fefce8 |
| Adani Ports & SEZ | #be123c | #fff1f2 |
| JSW Infrastructure | #334155 | #f1f5f9 |
| Gujarat Pipavav Port | #0e7490 | #ecfeff |

## 9. Sector-specific CSS

```css
.cat-tag{display:inline-block;padding:2px 10px;border-radius:12px;font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;}
.cat-resi{background:#eff6ff;color:#1d4ed8;}.cat-commercial{background:#f0fdf4;color:#166534;}
.cat-ports{background:#fff1f2;color:#be123c;}
.cat-section-title{font-family:'Playfair Display',serif;font-size:1.15rem;font-weight:700;padding:10px 16px;border-radius:8px;margin:20px 0 14px;display:flex;align-items:center;gap:10px;}

/* pre-sales vs collections — the developer's real scoreboard */
.presales-card{background:var(--surface);border:1px solid var(--border);border-left:4px solid var(--co-color,#181511);border-radius:var(--radius);padding:16px 18px;box-shadow:var(--shadow);}
.ps-row{display:grid;grid-template-columns:1.3fr auto auto;gap:10px;font-size:11.5px;padding:6px 0;border-bottom:1px dashed var(--border);}
.ps-row:last-child{border-bottom:none;}
.ps-gap{font-family:'IBM Plex Mono',monospace;font-weight:700;}
.ps-good{color:var(--pos);}.ps-warn{color:var(--warn);}

/* concession tenure bar — the moat with an expiry date */
.conc-row{display:grid;grid-template-columns:112px 1fr 58px;align-items:center;gap:10px;font-size:11.5px;margin-bottom:6px;}
.conc-wrap{background:var(--surface2);border-radius:4px;height:14px;overflow:hidden;}
.conc-bar{height:100%;border-radius:4px;background:var(--co-color,#181511);}
```

## 10. Mode applicability

All 15 modes apply to the operating companies. Notes:

- **`financials` and `charts`** — lead with **pre-sales and collections** for developers, not revenue.
  Reported revenue describes projects sold years ago and will mislead anyone reading it as current
  performance.
- **`valuation`** — **NAV-based for residential developers**, EV/EBITDA for commercial and ports,
  A single P/E table across these categories is meaningless.
- **`cb-rating`** — five components; growth on pre-sales/cargo/same-store NOI, and collections-vs-bookings
  inside PAT Quality.
- **Cross-sector work** — companies here participate normally on Revenue, EBITDA%, PAT, Mkt Cap, P/E,
  EV/EBITDA and Net Debt, with one caveat: **for a residential developer, revenue is a lagging number**,
  so a growth column sourced from it understates or overstates the business by years. Note it. Pre-sales,
  collections, cargo volume and concession tenure are sector-specific and stay in their own section.
