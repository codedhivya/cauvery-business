# Sector: Power & Energy (India)

Covers electricity generation, renewable energy and solar manufacturing, oil & gas and refining/marketing,
and the power exchanges.

**Boundary note**: this file covers companies that *generate, refine or trade* energy. Companies that
*make equipment for* the power sector — transformers, switchgear, grid equipment — belong in
`capital-goods.md`, because they are order-book businesses analysed on book-to-bill rather than on
capacity and tariff.

## 1. Category taxonomy

| Category | What it is | Examples |
|---|---|---|
| **Thermal / Conventional IPP** | Coal and gas generation, sold under PPAs or merchant | Adani Power, JSW Energy, NTPC-type utilities |
| **Renewable IPP** | Solar and wind generation assets | ACME Solar, renewable platforms |
| **Solar Manufacturing** | Cell and module manufacturing — a *manufacturing* business, not a generation one | Emmvee, integrated cell-to-module players |
| **Integrated Utility** | Generation plus transmission, distribution and retail supply | Tata Power |
| **Oil & Gas — Upstream** | Exploration and production | ONGC, Oil India |
| **Oil & Gas — Downstream / OMC** | Refining and fuel marketing | IOC, BPCL, HPCL |
| **Integrated Energy & Petchem** | Refining, petrochemicals and adjacent businesses | Reliance Industries |
| **Power Exchange** | Trading platform for electricity; a *market operator*, not a generator | IEX |

The categories are measured on genuinely different bases. A generator is judged on capacity, PLF and
tariff; a refiner on GRM and throughput; a solar manufacturer on cell/module capacity and ALMM listing;
an exchange on traded volume and take rate. **Do not carry one category's metrics into another.**

## 2. How companies in this sector make money

**Generation** sells electricity either under a long-term Power Purchase Agreement at a contracted tariff,
or on the merchant market at prevailing prices. PPA-backed capacity is predictable and lower-margin;
merchant capacity is volatile and can be highly profitable when demand is tight. The mix between the two
is the single most important structural fact about a generator.

Fuel is the other half. For thermal, coal cost and availability drive variable cost — much of which may
be a pass-through under regulated tariffs, so a fuel price rise is not automatically a margin hit. State
the pass-through position rather than assuming.

**Renewables** have near-zero marginal cost, so once built, output is almost pure contribution. The
economics are decided at the point of construction: capital cost per MW, tariff won at auction, and cost
of debt. A renewable IPP is effectively a spread between auction tariff and financing cost.

**Solar manufacturing** is a different business entirely — a capacity and technology cycle, exposed to
global module prices, domestic-content policy (ALMM) and import duty. Being *on* the ALMM list is a
commercial gate, not a technicality.

**Refining** earns the Gross Refining Margin — the spread between crude cost and product realisation —
multiplied by throughput. **Marketing** earns a per-litre margin on fuel retail, which in India is
subject to informal pricing restraint during periods of high crude, and that restraint is the sector's
recurring political risk.

**A power exchange** earns a small fee on volume traded. It is a network business with operating leverage
and near-zero marginal cost, and is analysed like a market infrastructure company.

## 3. Metric definitions

### Generation

- **Installed / operational capacity (MW or GW)** — the asset base. Distinguish operational from
  under-construction and from "pipeline", which may be neither.
- **PLF (Plant Load Factor, %)** — actual generation ÷ maximum possible. Utilisation of a thermal asset.
  For renewables the equivalent is the **CUF (Capacity Utilisation Factor)**, structurally much lower
  (~20–25% solar, ~30%+ wind) and not comparable to thermal PLF.
- **PPA-tied vs merchant capacity (%)** — the visibility-versus-upside mix.
- **Merchant tariff (₹/kWh)** — realised price on uncontracted power; the swing factor in profitability.
- **Fuel cost per unit and pass-through status** — whether a fuel price change hits margin or is recovered.
- **Receivables from discoms** — state distribution companies are chronically slow payers. Days
  receivable is a real risk metric here, not a housekeeping one.
- **Capacity addition pipeline (MW under construction, commissioning timeline)**.

### Solar manufacturing

- **Cell and module capacity (GW)**, and whether the company is **integrated** (cell + module) or
  module-only — integration is the margin difference.
- **ALMM listing status** — the approved-list gate for government-linked projects.
- **Capacity utilisation**, **realisation or ASP per watt**, **order book** where module supply is
  contracted. Capacity is quoted in **GWp** (gigawatt-peak — nameplate DC rating under standard test
  conditions); a module's GWp rating is not the same as the AC output an installation delivers, so do not
  equate manufacturing GWp with generation capacity.

### Project finance (applies to IPPs and renewable platforms)

- **DSCR (Debt Service Coverage Ratio)** = cash available for debt service ÷ debt service due. The
  covenant that matters in project-financed assets; below ~1.2× is tight, and lenders typically require
  a minimum. More informative than net debt/EBITDA for a single-asset SPV, because it asks whether the
  cash flow actually services the debt on schedule.
- **Project IRR / equity IRR** — the return the asset was underwritten at. Auction-won renewable projects
  live or die on whether realised IRR matches the bid assumption, and a falling cost of debt after
  commissioning is the main lever that improves it.

### Oil & gas

- **GRM (Gross Refining Margin, $/bbl)** — the refining spread. Compare against the **benchmark
  (Singapore) GRM**; the premium or discount to benchmark is the real performance signal.
- **Throughput / refinery utilisation (%)**.
- **Marketing margin (₹/litre)** — fuel retail profitability.
- **Crude price and its lag** — inventory gains or losses arise because crude is bought before it is
  processed; a quarter's reported profit can swing on inventory revaluation with no operational change.
  **Always separate inventory gain/loss from core GRM** — this is the most common way an oil result is
  misread.
- **Upstream: realisation per barrel, production volumes, reserve replacement**.
- **Petchem: spreads on key products, cracker utilisation**.

### Power exchange

- **Traded volume (MU)**, **market share**, **take rate / fee per unit**, and the operating leverage —
  incremental volume carries almost no incremental cost.

- **RoNW (Return on Net Worth)** — net profit ÷ net worth. Quoted in IPO offer documents and
  required in prospectus disclosure, so it appears whenever a company in this sector lists. Report
  it alongside the sector's usual return measure rather than in place of it.

## 4. Benchmarks — what good looks like

Indicative; verify against current conditions, which move more in this sector than most.

| Metric | Healthy |
|---|---|
| Thermal PLF | >65%; >75% strong |
| Solar CUF | ~20–25% (do not compare to thermal PLF) |
| Wind CUF | ~30%+ |
| PPA-tied share | higher = more visibility, lower = more merchant upside; neither is "better" absent a view on tariffs |
| Discom receivable days | <90 comfortable; >150 a real risk |
| Refinery utilisation | >95% |
| GRM vs Singapore benchmark | at or above benchmark |
| Solar module capacity utilisation | >70% |
| Net debt / EBITDA (IPP) | <5× is normal for infrastructure-like assets — do not apply a manufacturing threshold here |
| Net debt / EBITDA (refining) | <2× |

**What to watch, by category:**

- **Thermal IPP** — Is PLF improving? What share is merchant, and where are merchant tariffs? Are discom
  receivables lengthening? Is fuel cost passed through?
- **Renewable IPP** — Is the commissioning pipeline on schedule? What tariff did recent auction wins
  carry? Is the cost of debt falling (the main value lever after commissioning)?
- **Solar manufacturing** — Is the company ALMM-listed? Is it integrated to cell? What is utilisation, and
  how exposed is it to imported module price?
- **OMC / refining** — Is GRM above benchmark? How much of the result is inventory gain rather than
  operations? Is marketing margin under political pressure?
- **Exchange** — Is traded volume growing? Is market share holding against new entrants? Any regulatory
  change to market coupling?

## 5. Regulatory quick reference

Heavily regulated, and policy is frequently the largest single earnings driver.

| Area | Body / rule |
|---|---|
| Tariff determination, inter-state transmission | **CERC** (central), SERCs (state) |
| Sector planning, generation data | **CEA** |
| Renewable policy, solar mission | **MNRE** |
| Approved solar module list | **ALMM** (MNRE) |
| Renewable capacity auctions | **SECI** |
| Petroleum and gas regulation | **PNGRB** |
| Fuel pricing | nominally deregulated; subject to informal restraint in practice |
| Renewable purchase obligations | RPO targets on discoms and obligated entities |

Levels and lists change frequently — check the current notification rather than carrying a figure forward.

## 6. Per-mode specifics

### Headline KPIs by category (`dashboard`)

| Category | KPIs |
|---|---|
| Thermal IPP | Revenue, PAT, Capacity (MW), PLF, merchant share, EBITDA margin, net debt |
| Renewable IPP | Revenue, PAT, Operational capacity, CUF, pipeline MW, EBITDA margin, net debt |
| Solar Manufacturing | Revenue, Cell/module capacity, utilisation, realisation/W, EBITDA margin, PAT |
| Integrated Utility | Revenue, PAT, generation capacity, distribution units sold, EBITDA margin, net debt |
| Upstream O&G | Revenue, PAT, production volume, realisation/bbl, EBITDA margin |
| OMC / Refining | Revenue, PAT, GRM, throughput, marketing margin, inventory gain/loss |
| Power Exchange | Revenue, PAT, traded volume, market share, EBITDA margin |

### Table columns by category (`financials`)

- **Generation** — Period, Revenue, YoY, Capacity, PLF/CUF, Merchant share, EBITDA, EBITDA%, PAT, Net debt
- **Refining/OMC** — Period, Revenue, GRM ($/bbl), Benchmark GRM, Throughput, Marketing margin,
  **Inventory gain/(loss)**, EBITDA, PAT
- **Solar manufacturing** — Period, Revenue, Capacity (GW), Utilisation, Realisation/W, EBITDA%, PAT
- **All generation categories** — a receivables table showing discom dues and ageing.

**The inventory gain/loss row for refiners is mandatory**, with a `.fnote` explaining it. A refining
result read without separating inventory effects from core GRM is misleading in both directions.

### Chart reference lines (`charts`)

| Metric | Line | Label |
|---|---|---|
| Thermal PLF | 65% | "Healthy PLF" |
| Refinery utilisation | 95% | "Full utilisation" |
| GRM | benchmark GRM for the period | "Singapore benchmark" — label the period, it moves |
| Discom receivable days | 90 | "Comfortable receivables" |
| Solar CUF | 22% | "Typical solar CUF" — never plot on the same axis as thermal PLF |

### Profile coverage by category (`business-profile`)

- **IPP** — capacity by fuel and by state, PPA vs merchant split with counterparties, plant-level detail,
  fuel sourcing (linkage vs imported vs captive), pipeline and commissioning schedule.
- **Renewable** — operational vs under-construction capacity, auction wins and tariffs, land and
  evacuation status, offtaker credit quality (a low tariff with a weak discom is not a good asset).
- **Solar manufacturing** — integration level (wafer/cell/module), technology (TOPCon, PERC), ALMM
  status, customer mix, expansion plans.
- **Refining/OMC** — refinery complexity (Nelson index), throughput capacity, retail outlet network,
  product slate, petchem integration.
- **Exchange** — market segments, participant base, market share, regulatory position.

### Moat candidates by category (`moats`)

- **Generation** — long-tenor PPAs with creditworthy offtakers (contracted cash flows competitors cannot
  displace), low-cost fuel linkages, and site/evacuation access. Regulated returns are a moat of sorts:
  low ceiling, high floor.
- **Renewables** — a low cost of capital, which is the decisive competitive weapon in auction bidding;
  and a pipeline with secured land and grid connectivity, both genuinely scarce.
- **Solar manufacturing** — ALMM listing plus backward integration to cell. Module-only assembly has a
  thin moat and is exposed to import pricing — say so rather than claiming otherwise.
- **Refining** — complexity (ability to process cheaper heavy crude), scale, and integration into petchem.
- **OMC marketing** — the retail outlet network, effectively impossible to replicate at scale.
- **Exchange** — network effects and regulatory position; genuinely one of the strongest moat structures
  in this file, since liquidity attracts liquidity.

### Valuation (`valuation`)

Primary multiple: **EV/EBITDA** for generation and refining, because leverage differs enormously and P/E
is distorted by capital structure. **P/B** is meaningful for asset-heavy regulated utilities.
**EV per MW** is the standard cross-check for generation assets, and **EV/EBITDA per tonne of capacity**
for refining.

For renewable IPPs, discounted-cash-flow logic applies more naturally than a trailing multiple, since
the assets are long-dated contracted cash flows — state which basis is used.

The power exchange is valued as a market infrastructure business on **P/E**, not on any energy metric.

### CB Rating substitutions (`cb-rating`)

Capital-intensive, so leverage and cash flow substitute in — the standard capital-intensive treatment.

| Component | Weight | Power-energy substitution |
|---|---|---|
| Growth | 30% | Capacity addition and generation growth (or throughput for refiners), alongside revenue |
| Profitability | 25% | EBITDA margin **and** PLF/CUF or GRM-vs-benchmark — asset utilisation is profitability here |
| PAT Quality | 15% | PAT growth adjusted for **inventory gain/loss** (refiners) and one-offs |
| Debt & Cash Flow | 20% | Net debt/EBITDA against the category norm, plus **discom receivable days** and operating cash conversion |
| Forward Outlook | 10% | Commissioning pipeline, auction wins, policy direction |

Total 100%. Note this splits PAT Quality and adds an explicit Debt & Cash Flow component, since leverage
is structural rather than incidental in this sector — an IPP at 5× net debt/EBITDA may be perfectly
healthy, and scoring it against a manufacturing threshold would be wrong.

### Extra sections (`quarterly-report`)

- **Capacity & Generation** — capacity by type, PLF/CUF, generation volumes, commissioning pipeline.
- **Fuel & Input Costs** — coal/gas sourcing and cost, pass-through status; crude and inventory effects
  for refiners.
- **Receivables & Discom Exposure** — for generators, the dues position by discom and ageing.
- **Debt & Cash Flow** — the standard capital-intensive section; leverage, maturity profile, cost of debt.
- **Regulatory & Policy** — CERC/MNRE/PNGRB developments affecting the companies in scope.
- **"Power School"** — the `school` mode is presented under this name in existing sector reports.

### Event transmission map (`event-impact`, `risks-outlook`)

| Event | Reaches results via | Exposure basis to cite |
|---|---|---|
| Crude price move | GRM, inventory gain/loss, marketing margin | throughput, inventory position, retail volume |
| Fuel pricing restraint (political) | marketing margin | retail fuel volume share |
| Coal price or availability change | variable cost, PLF | fuel mix, linkage vs imported share, pass-through status |
| Merchant tariff move | realisation on uncontracted power | merchant % of capacity |
| ALMM listing change | addressable market for modules | share of revenue from ALMM-gated projects |
| Solar module import duty (BCD) change | domestic manufacturer pricing power, IPP capex | domestic vs imported module sourcing |
| SECI / state auction result | future tariff and pipeline | pipeline MW, bid win rate |
| CERC tariff order | regulated return, recovery | regulated share of capacity |
| Discom payment scheme or default | receivables, cash flow | dues by discom, ageing |
| RPO enforcement change | renewable demand | renewable capacity share |

## 7. Where to look (sourcing)

**Tier 1** — quarterly investor presentations, which disclose plant-level PLF, capacity, PPA mix and (for
refiners) the GRM breakdown including inventory effects. Earnings-call commentary on merchant tariffs and
fuel pass-through carries real signal.

**Tier 2 — sector authorities**: **CEA** (generation, PLF and capacity data at national and plant level —
the authoritative benchmark for whether a company's PLF is good), **CERC** (tariff orders), **MNRE** and
the **ALMM list**, **SECI** (auction results and tariffs), **PNGRB** (gas), **PPAC** (petroleum planning —
consumption and pricing data), and **IEX** published data for market clearing prices.

CEA's national PLF and capacity data give the right denominator for market-share and utilisation claims;
a company's PLF means little without the national or regional average alongside it.

## 8. Company colour palette

| Company | Main | Soft tint |
|---|---|---|
| Adani Power | #c84b2f | #fef3f0 |
| Tata Power | #1e3a5f | #eff6ff |
| JSW Energy | #7f1d1d | #fef2f2 |
| NTPC | #166534 | #f0fdf4 |
| ACME Solar | #ea580c | #fff7ed |
| Emmvee Solar | #ca8a04 | #fefce8 |
| ONGC | #be123c | #fff1f2 |
| Oil India | #9d174d | #fdf2f8 |
| Reliance Industries | #1d4ed8 | #eff6ff |
| IOC | #dc2626 | #fef2f2 |
| BPCL | #b8911e | #fdf5e0 |
| HPCL | #0e7490 | #ecfeff |
| IEX | #7c3aed | #f5f3ff |

## 9. Sector-specific CSS

```css
.cat-tag{display:inline-block;padding:2px 10px;border-radius:12px;font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;}
.cat-thermal{background:#fef2f2;color:#7f1d1d;}.cat-renewable{background:#f0fdf4;color:#166534;}
.cat-solarmfg{background:#fefce8;color:#ca8a04;}.cat-utility{background:#eff6ff;color:#1e3a5f;}
.cat-upstream{background:#fff1f2;color:#be123c;}.cat-omc{background:#fff7ed;color:#c2410c;}
.cat-exchange{background:#f5f3ff;color:#7c3aed;}
.cat-section-title{font-family:'Playfair Display',serif;font-size:1.15rem;font-weight:700;padding:10px 16px;border-radius:8px;margin:20px 0 14px;display:flex;align-items:center;gap:10px;}

/* capacity / plant block */
.cap-card{background:var(--surface);border:1px solid var(--border);border-left:4px solid var(--co-color,#181511);border-radius:var(--radius);padding:16px 18px;box-shadow:var(--shadow);}
.cap-row{display:grid;grid-template-columns:1.3fr auto auto;gap:10px;font-size:11.5px;padding:6px 0;border-bottom:1px dashed var(--border);}
.cap-row:last-child{border-bottom:none;}
.ppa-pill{font-size:10px;font-weight:700;padding:2px 8px;border-radius:10px;}
.ppa-tied{background:#dbeafe;color:#1d4ed8;}.ppa-merchant{background:#fff7ed;color:#c2410c;}

/* GRM / inventory-effect callout */
.grm-note{background:#fff7ed;border:1px solid #fdba74;border-left:4px solid var(--warn);border-radius:8px;padding:12px 14px;font-size:11.5px;line-height:1.65;margin-top:12px;}
```

## 10. Mode applicability

All 15 modes apply. Notes:

- **`segments`** — capacity by fuel type and by state for generators; product slate and refining vs
  petchem vs marketing for integrated energy. Both are well disclosed.
- **`financials`** — the inventory gain/loss separation for refiners is mandatory, not optional.
- **`valuation`** — EV/EBITDA primary, EV per MW as cross-check for generation, P/E for the exchange.
  P/E alone mis-prices a leveraged IPP.
- **`cb-rating`** — uses the five-component split above with an explicit Debt & Cash Flow weight; do not
  apply a manufacturing leverage threshold to an IPP.
- **`school`** — presented as "Power School" in existing reports.
- **`event-impact`** — the most policy-sensitive sector in this repo. Crude, ALMM, import duty, tariff
  orders and discom health all move earnings directly.
- **Cross-sector work** — all universal metrics apply: Revenue, EBITDA%, PAT, Mkt Cap, P/E, EV/EBITDA and
  Net Debt are meaningful. But **flag leverage context** when this sector appears in a cross-sector table:
  an IPP at 5× net debt/EBITDA is normal infrastructure gearing, not distress, and a naive ranking on Net
  Debt will misrepresent it. PLF, CUF, GRM and merchant share are sector-specific and stay out.
