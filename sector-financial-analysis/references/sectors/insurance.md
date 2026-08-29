# Sector: Insurance (India)

Covers Indian life insurers, standalone health insurers (SAHI), general/non-life insurers, and TPAs.
Named examples: LIC, ICICI Prudential Life, HDFC Life, SBI Life, Axis Max Life, Star Health, Niva Bupa,
ICICI Lombard, Medi Assist.

## 1. Category taxonomy

Classify every company before applying any metric — the four categories are measured on genuinely
different bases and mixing them produces nonsense.

| Category | What it is | Examples |
|---|---|---|
| **Life** | Long-duration savings and protection contracts | LIC, HDFC Life, ICICI Prudential Life, SBI Life, Axis Max Life |
| **Health (SAHI)** | Standalone health insurers — health and personal accident only, cannot write other lines | Star Health, Niva Bupa |
| **General** | Non-life: motor, health, property, crop, liability | ICICI Lombard, and the multi-line non-life insurers |
| **TPA** | **Not an insurer.** Earns a service fee for processing claims on behalf of insurers/employers; zero premium income | Medi Assist |

## 2. Why insurers are valued differently

Manufacturing companies are judged mainly on current profits. Insurers are judged on future
profitability (VNB), capital strength (Solvency), customer retention (Persistency), and underwriting
quality (Combined Ratio). Use this analogy table in any explanatory output:

| Manufacturing term | Insurance equivalent | Why the same |
|---|---|---|
| Revenue / Sales | GWP / GDPI / Total Premium | Money coming in |
| Future order profitability | VNB (Value of New Business) | Value of business written today, earned over years |
| Gross margin % | VNB Margin | Profit per ₹100 of premium written |
| Net worth / book value | Embedded Value (EV) | Worth today plus locked-in future profits |
| ROE | RoEV / EVOP | Return on capital deployed |
| Raw material cost | Claims | The cost the insurer cannot avoid |
| Operating ratio | Combined Ratio / CISR | Below 100% = profitable; above = underwriting loss |
| Repeat business | Persistency | % of customers renewing |
| Capital adequacy (CRAR) | Solvency Ratio | Buffer for unexpected claims |

### The analogy

A manufacturer that books its costs today and earns its profit over decades. Premium is not revenue in any ordinary sense — much of it is a liability for claims not yet made — which is why current profit says so little and the value of business written says so much.

## 3. Metric definitions

### Life

- **GWP / Total Premium** — total premium collected. Not profit; claims, commissions and bonuses come out of it.
- **APE (Annualised Premium Equivalent)** = Regular Annual Premium + 10% × Single Premium. Standardises
  new-business volume across insurers with different premium mixes.
- **VNB (Value of New Business)** = present value of all future profits from policies sold in the period.
  The single most important life profitability metric — more informative than PAT.
- **VNB Margin** = VNB ÷ APE. Profit locked in per ₹100 of new business.
- **Embedded Value (EV / IEV)** = Adjusted Net Worth + PV of future profits from in-force policies. The
  true economic net worth; valued via P/EV the way banks are valued via P/B.
- **RoEV** = operating profit ÷ average EV. The sector's equivalent of ROE.
- **Persistency** — % still paying at the 13th month (year-1 renewal) or 61st month (year-5). Low
  persistency signals revenue leakage and possible mis-selling.
- **Solvency Ratio** = Available Solvency Margin ÷ Required Solvency Margin.

### Health / General

- **Combined Ratio** = (Claims + all expenses) ÷ Net Premium Earned. Below 100% = underwriting profit.
  The single most watched health/general metric.
- **CISR (Combined Insurance Service Ratio)** — the IFRS-17 / Ind AS 117 equivalent of Combined Ratio.
  Same interpretation.
- **Loss / Claims Ratio** = Claims Incurred ÷ Net Premium Earned. Too low can mean claim denials; too
  high erodes profitability.
- **Expense Ratio** = operating + acquisition costs ÷ Net Premium Earned.
- **GDPI** — Gross Direct Premium Income, the general-insurance revenue line pre-reinsurance.
- Health and general insurers have **no Embedded Value** — no surrender value, no locked multi-decade
  profit stream. Investment income supplements underwriting when Combined Ratio exceeds 100%.

### TPA

Analysed like a services company: Revenue, EBITDA margin, PAT — never Combined Ratio or VNB. Key
metrics: Premiums Administered, market share, claims processed. Flag any shift to a platform fee on
total premium flow rather than per-claim — a structurally higher-margin revenue line.

## 4. Benchmarks — what good looks like

| Metric | Healthy |
|---|---|
| VNB Margin | >25% strong; <20% a watch item. Sector context: SBI Life ~27–28%, Axis Max ~25%, ICICI Pru ~25–27%, HDFC Life ~24–25%, LIC ~21–23% and rising |
| RoEV | >15–17% |
| Persistency (13th month) | >80–85% |
| Persistency (61st month) | >50% |
| Solvency Ratio | IRDAI minimum 150% for all insurers; >180–200% comfortable |
| Combined Ratio | <100% = underwriting profit; general insurers trending toward/below 103% is the practical bar |
| EV growth | >15%/yr |
| APE growth | >10% |
| GWP growth (health) | >15% |

**What to watch, by category** — for verdict and school outputs:

- **Life** — APE growing >10%? VNB margin expanding? EV growing >15%? RoEV >15–17%? 13th-month persistency >80%?
- **Health** — GWP growing >15%? Combined/CISR below 100%? Loss ratio improving YoY? Solvency >200%? Market share growing?
- **General** — GDPI above industry average? Combined Ratio trending to/below 103%? Investment yield >8%? Underwriting improving QoQ?
- **TPA** — revenue growth >20%? EBITDA margin stable/improving? Reported vs adjusted PAT diverging? Market share widening?

### What goes wrong, and the tell

**Business written at a margin that does not survive contact with reality.** The tells: persistency falling in the later years, which means the profit assumed at sale is not being earned; a solvency ratio drifting toward the floor; and a mix shifting toward products that flatter headline premium but carry thin margin. For non-life, a combined ratio drifting above 100 while investment income covers the gap — underwriting losses funded by markets are a bet, not a business.

## 5. IRDAI regulatory quick reference

| Rule | Life | Health (SAHI) / General |
|---|---|---|
| Minimum Solvency Ratio | 150% | 150% |
| Minimum central govt securities | 25% of investible funds | 30% |
| Minimum approved securities | 50% | 55% |
| Maximum equity exposure | 15% (non-ULIP funds) | 20% |

## 6. Per-mode specifics

### Headline KPIs by category (`dashboard`)

| Category | KPIs |
|---|---|
| Life | PAT, VNB, VNB Margin, APE, Solvency, AUM/EV |
| Health | PAT, GWP, Combined Ratio (or CISR), Loss Ratio, Solvency |
| General | PAT, GDPI, Combined Ratio, Solvency, ROE |
| TPA | Revenue, PAT (reported vs adjusted where they diverge), EBITDA margin, market share |

### Table columns by category (`financials`)

- **Life** — GWP/Total Premium, YoY, APE, VNB, VNB Margin, PAT, Embedded Value, Solvency
- **Health** — Period, GWP, YoY, Combined Ratio (or CISR), Loss Ratio, Expense Ratio, Underwriting P/L, PAT, market share
- **General** — Period, GDPI, YoY, Net Earned Premium, Combined Ratio, Claims Ratio, PAT, ROE, Solvency
- **TPA** — Period, Revenue, YoY, EBITDA, EBITDA%, PAT (reported), PAT (adjusted — show both where they diverge, and footnote why), Premiums Administered

### Chart reference lines (`charts`)

| Metric | Line | Label |
|---|---|---|
| Combined Ratio / CISR | 100% | "Breakeven" — bars green-tinted below, red above |
| Solvency Ratio | 150% | "IRDAI Minimum 150%" — horizontal bar chart reads best |

### Profile coverage by category (`business-profile`)

- **Life** — promoter/JV, revenue pillars (new business, renewal, group, investment income), distribution mix (bancassurance vs agency vs digital, with %), product mix by APE (ULIP / Non-Par savings / Protection / Annuity / PAR) as segment bars, any strategic pivot underway.
- **Health** — SAHI constraint, distribution mix, product mix (retail vs group vs personal accident), network hospital count, differentiators (claim settlement speed, NPS).
- **General** — lines of business, how profit is generated (underwriting result **plus** investment income — state explicitly that Combined Ratio >100% doesn't necessarily mean unprofitable), distribution, investment portfolio mix.
- **TPA** — state plainly it is **not an insurer**; the claims-processing service-fee model, client base, differentiating tech, share of premiums administered.

### Moat candidates by category (`moats`)

- **Life** — bank/agent distribution scale that can't be rebuilt quickly (cite branch/agent counts), EV as locked-in decades of future profit, brand and government backing (LIC), product-mix quality (annuity/protection leadership), independent actuarial EV validation as a governance-trust moat.
- **Health** — hospital network breadth, claims-data depth enabling better actuarial pricing, digital CX or global-parent actuarial IP, specialist vs generalist agents.
- **General** — line-of-business diversification, investment-income engine size, solvency cushion enabling growth without capital raises.
- **TPA** — data/AI network effects raising insurer switching costs, market-share-driven data moat, platform stickiness.

### Valuation (`valuation`)

Primary multiple: **P/EV** for life insurers — the life insurer's "P/E". **P/B** for general insurers and
TPAs; P/E as secondary. Health insurers are commonly valued on P/B or price/GWP. Never apply P/EV to a
health, general or TPA business — they have no embedded value.

### CB Rating substitutions (`cb-rating`)

Financial-sector rules apply: leverage is the business model, not a risk flag, so Debt/Leverage is never
a component.

| Component | Weight | Insurance substitution |
|---|---|---|
| Growth | 30% | APE growth (life) / GWP growth (health, general) / revenue growth (TPA) |
| Profitability | 25% | VNB Margin (life) / Combined Ratio inverted (health, general) / EBITDA margin (TPA) |
| PAT Quality | 25% | PAT growth adjusted for one-offs; for life, EV/RoEV movement carries more signal than PAT |
| Capital & Outlook | 20% | Solvency headroom above 150%, plus guidance and persistency trend |

Total 100%. **Capital adequacy substitutes for the generic Forward Outlook component** because solvency
is the binding constraint on an insurer's ability to grow.

### Extra sections (`quarterly-report`)

**Investments & Returns** — an IRDAI regulatory recap (`.reg-card`) plus per-company `.inv-card`
portfolio breakdowns: AUM, yield, asset allocation, equity sensitivity. Flag the market-sensitivity
caveat where relevant — an equity correction can swing EV or MTM investment income sharply in a single
quarter, and where that happened it must be called out rather than left to distort a trend silently.

### Event transmission map (`event-impact`, `risks-outlook`)

| Event | Reaches results via | Exposure basis to cite |
|---|---|---|
| GST change on premiums (e.g. term-insurance exemption) | pricing, demand, product mix | protection share of APE |
| IRDAI solvency norm change | capital headroom, growth capacity | current solvency vs 150% |
| IRDAI open-architecture bancassurance rules | distribution access | bancassurance % of APE |
| Surrender-value / commission regulation | margins, agent economics | product mix, commission ratio |
| Equity market correction | EV, MTM investment income | equity % of investment book |
| Interest-rate move | guaranteed-product margins, bond MTM | non-par guaranteed share of APE |
| Catastrophe / health-claims spike | loss ratio, combined ratio | reinsurance cover, geographic concentration |

## 7. Where to look (sourcing)

**Tier 1** — company investor presentations and BSE/NSE filings; life insurers publish detailed VNB/EV
disclosures quarterly. Search `"<company> investor presentation Q<n> FY<yy> filetype:pdf"`.

**Tier 2 — sector authorities**: **IRDAI** (circulars, the annual handbook, monthly new-business premium
data — the authoritative source for market share), Swiss Re sigma for global/industry context,
CRISIL/ICRA/CARE for ratings, Prime Database and exchange filings for shareholding.

Life insurers' EV figures are usually **independently validated by an actuarial firm** — worth naming
when citing EV, as it materially raises the figure's credibility.

## 8. Company colour palette

**The companies named here are illustrative as at authoring, not the current universe.** Anything listed since belongs in the analysis too — see "Establish the universe before ranking anything" in `source-hierarchy.md`.

| Company | Main | Soft tint |
|---|---|---|
| LIC | #1d4ed8 | #eff6ff |
| ICICI Prudential Life | #c84b2f | #fef3f0 |
| Axis Max Life | #166534 | #f0fdf4 |
| HDFC Life | #be123c | #fff1f2 |
| SBI Life | #1e3a5f | #eff6ff |
| Star Health | #7c3aed | #f5f3ff |
| Niva Bupa | #d97706 | #fffbeb |
| ICICI Lombard | #7f1d1d | #fef2f2 |
| Medi Assist | #0e7490 | #ecfeff |

## 9. Sector-specific CSS

```css
/* category tags */
.cat-tag{display:inline-block;padding:2px 10px;border-radius:12px;font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;}
.cat-life{background:#dbeafe;color:#1d4ed8;}.cat-health{background:#dcfce7;color:#15803d;}
.cat-general{background:#fee2e2;color:#7f1d1d;}.cat-tpa{background:#fce7f3;color:#9d174d;}
.cat-section-title{font-family:'Playfair Display',serif;font-size:1.15rem;font-weight:700;padding:10px 16px;border-radius:8px;margin:20px 0 14px;display:flex;align-items:center;gap:10px;}

/* Investments & Returns section */
.reg-card{background:var(--gold-soft);border:1px solid var(--gold);border-radius:var(--radius);padding:14px 16px;margin-bottom:16px;font-size:11.5px;}
.reg-card h4{font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:var(--gold);margin-bottom:8px;}
.inv-card{background:var(--surface);border:1px solid var(--border);border-left:4px solid var(--co-color,#181511);border-radius:var(--radius);padding:16px 18px;box-shadow:var(--shadow);}
```

Category accent bands: Life bg `#eff6ff` border `#1d4ed8`; Health bg `#f0fdf4` border `#15803d`;
General bg `#fef2f2` border `#7f1d1d`; TPA bg `#fdf2f8` border `#9d174d`.

## 10. Mode applicability

All 15 modes apply. Notes:

- **`valuation`** — P/EV for life only; see above.
- **`segments`** — product mix by APE (life) or retail/group/PA split (health) is the meaningful cut;
  geography rarely is.
- **`cb-rating`** — uses the financial-sector substitution table above; never Debt/Leverage.
- **Cross-sector work** — insurers have **no meaningful EBITDA and no comparable "Revenue" line**.
  In any cross-sector table those cells read **"n/a — not comparable for this sector"**. This is the
  single most likely place for an insurer to be silently misrepresented.
