# Sector: Banking (India)

Covers Indian scheduled commercial banks — public sector, private sector, and small finance banks.

## 1. Category taxonomy

| Category | What it is | Examples |
|---|---|---|
| **Public Sector (PSU)** | Government-majority banks. Large deposit franchises, lower NIMs, higher legacy asset-quality baggage, policy-lending obligations | SBI, Bank of Baroda, PNB, Canara Bank, Union Bank, Bank of Maharashtra, Indian Bank, IDBI Bank |
| **Private Sector** | Higher NIMs, stronger fee income, faster growth, generally better cost ratios | HDFC Bank, ICICI Bank, Axis Bank, Kotak Mahindra Bank, IndusInd Bank, Federal Bank |
| **Small Finance Bank (SFB)** | Niche/microfinance-derived lending. Structurally higher NIMs **and** higher credit costs; asset quality is far more cyclical | AU Small Finance Bank, Jana Small Finance Bank, Equitas, Ujjivan |
Compare within a category by default. An SFB's 9% NIM and a PSU's 3% NIM are not the same metric doing
the same job, and ranking them together is meaningless.

## 2. How a bank actually makes money

A bank borrows at one rate and lends at another. The spread is **Net Interest Income**; expressed
against assets it is **NIM**. Everything else either supplements that spread (fee income, treasury) or
erodes it (operating costs, credit losses).

This is why a bank is analysed on four axes, and why profit alone tells you very little:

| Axis | Question | Core metrics |
|---|---|---|
| **Margin** | How profitable is the spread? | NII, NIM, yield on advances, cost of funds |
| **Asset quality** | How much of the book goes bad? | GNPA, NNPA, PCR, slippage ratio, credit cost |
| **Growth** | Is the balance sheet expanding? | Advances growth, deposit growth, CASA |
| **Capital** | Can it absorb losses and keep growing? | CRAR, CET-1, LCR |

A bank can report record profit while quietly accumulating stress. Asset quality is the axis that
matters most and the one that lags.

### The analogy

A bank buys money wholesale and sells it retail. Deposits are the raw material, loans the product, and the spread between them is the gross margin — except that some of the product goes bad after it is sold, which is why provisioning sits where cost of goods would.

## 3. Metric definitions

- **NII (Net Interest Income)** = interest earned − interest expended. The core revenue line.
- **NIM (Net Interest Margin)** = NII ÷ average interest-earning assets. The spread expressed as a
  percentage. Report domestic vs whole-bank separately where a bank has overseas operations, since the
  blend obscures the domestic trend.
- **GNPA** — gross non-performing assets as % of gross advances. The headline bad-loan number.
- **NNPA** — net NPA, after provisions. The gap between GNPA and NNPA is what has been provided for.
- **PCR (Provision Coverage Ratio)** — provisions held against NPAs. Higher means less future
  earnings risk from existing bad loans.
- **Slippage ratio** — fresh NPAs added during the period as % of opening standard advances. **More
  informative than GNPA**, because GNPA can fall through write-offs and recoveries while fresh stress
  keeps forming. Always look for it.
- **Credit cost** — provisions as % of average advances. What asset quality actually costs earnings.
- **CASA ratio** — current and savings deposits ÷ total deposits. Low-cost, sticky funding; a high CASA
  is a structural funding advantage, not merely a good quarter.
- **Advances / Deposits growth** — balance-sheet expansion. Watch the credit-deposit ratio: advances
  growing much faster than deposits is not sustainable and eventually forces up funding costs.
- **CRAR (Capital Adequacy Ratio)** — total capital ÷ risk-weighted assets, under Basel III.
- **CET-1** — the highest-quality capital tier. The binding constraint on growth in practice.
- **LCR (Liquidity Coverage Ratio)** — high-quality liquid assets against 30-day stressed outflows.
- **RoA** — the cleanest cross-bank profitability measure, since it is unaffected by leverage.
- **RoE** — return on equity. Read alongside RoA; a high RoE on a thin capital base is a different
  proposition from the same RoE on a strong one.
- **Cost-to-income** — operating efficiency.

## 4. Benchmarks — what good looks like

| Metric | Healthy |
|---|---|
| NIM | Private >3.5%; PSU ~3%; SFB 7%+ (higher credit costs offset this) |
| GNPA | <3% comfortable; <2% strong; trend matters more than level |
| NNPA | <1% strong |
| PCR | >70% comfortable; >75% conservative |
| Slippage ratio | <1.5% annualised for a mature book |
| CASA | >40% strong; >45% a genuine funding moat |
| RoA | >1% good; >1.5% excellent |
| RoE | >15% |
| CRAR | Regulatory minimum 11.5% including capital conservation buffer; >15% comfortable |
| CET-1 | >12% comfortable |
| LCR | Regulatory minimum 100%; banks typically run well above |
| Cost-to-income | <45% efficient; PSU banks structurally higher |

**What to watch, by category:**

- **PSU** — Is GNPA still improving or has it plateaued? Is NIM holding as deposits reprice? Is credit growth funded by deposits? Is CET-1 sufficient without government capital?
- **Private** — Is deposit growth keeping pace with advances? Is CASA eroding as depositors chase term rates? Is fee income growing? Is unsecured lending share rising faster than provisions?
- **SFB** — Is the microfinance book showing stress? Is slippage rising? Is the deposit franchise maturing away from bulk funding? Is credit cost within guidance?

### What goes wrong, and the tell

**Growth without the funding or the provisioning to support it.** The tells, in order of how early they appear: loan growth running well ahead of deposit growth (the funding is being bought, not gathered); a rising credit-deposit ratio; falling provision coverage while gross NPAs look stable; and restructured or Stage 2 assets climbing before anything reaches NPA. A bank that grows fastest in a boom is usually the one that provisions most in the bust.

## 5. RBI regulatory quick reference

| Requirement | Level |
|---|---|
| Minimum CRAR (Basel III, incl. CCB) | 11.5% |
| Minimum CET-1 (incl. CCB) | 8% |
| LCR | ≥100% |
| Priority Sector Lending | 40% of adjusted net bank credit (higher for SFBs) |
| CRR / SLR | As prevailing — check the current RBI policy statement rather than assuming |

Regulatory levels change with RBI policy. Verify against the current circular rather than carrying a
figure forward.

## 6. Per-mode specifics

### Headline KPIs by category (`dashboard`)

| Category | KPIs |
|---|---|
| PSU | PAT, NII, NIM, GNPA, PCR, CRAR, advances growth |
| Private | PAT, NII, NIM, GNPA, CASA, RoA, advances growth |
| SFB | PAT, NII, NIM, GNPA, credit cost, CRAR, AUM growth |

### Table columns by category (`financials`)

- **All categories** — Period, NII, YoY, NIM, Operating Profit, Provisions, PAT, YoY, GNPA%, NNPA%, PCR, CRAR
- **Balance sheet table** — Advances, YoY, Deposits, YoY, CASA%, Credit-Deposit ratio
- **Asset quality table** — Opening GNPA, slippages, recoveries/upgrades, write-offs, closing GNPA, credit cost

The asset-quality movement table matters: it separates genuine improvement from write-off-driven
cosmetic improvement, and that distinction is invisible in the headline GNPA number.

### Chart reference lines (`charts`)

| Metric | Line | Label |
|---|---|---|
| CRAR | 11.5% | "RBI Minimum (incl. CCB)" |
| CET-1 | 8% | "RBI Minimum CET-1" |
| LCR | 100% | "RBI Minimum LCR" |
| GNPA | peer median | no fixed regulatory line — use the peer median and label it as such |

Standard chart set, mirroring the established banking reports: NII vs Net Profit (quarterly), GNPA &
NNPA trend, Provision Coverage, Deposits vs Advances, NIM (domestic vs whole bank), RoA & RoE, CRAR.

### Profile coverage by category (`business-profile`)

- **PSU** — ownership and government stake, branch and ATM network, loan-book mix (corporate / retail / agri / MSME), deposit franchise, digital progress, any government capital-infusion history.
- **Private** — promoter/institutional shareholding, branch and digital mix, loan-book composition with emphasis on unsecured share, fee-income streams, subsidiaries (AMC, insurance, broking) and their contribution.
- **SFB** — origin (microfinance NBFC conversion, typically), geographic concentration, secured vs unsecured mix, deposit franchise maturity, transition path toward universal banking where applicable.

Cover management and board here too — leadership changes at banks are materially predictive, and RBI
approval of MD/CEO terms is itself information.

### Moat candidates by category (`moats`)

- **Deposit franchise** — a high CASA built over decades is the strongest moat in banking. It cannot be bought quickly: it needs branches, trust and time. Cite CASA % and its stability through rate cycles.
- **Branch network in under-banked geographies** — expensive and slow to replicate.
- **Underwriting track record through a full credit cycle** — visible only in slippage across a downturn.
- **Technology and cost structure** — a structurally lower cost-to-income compounds into pricing power.
- **Subsidiary ecosystem** — captive distribution for insurance/AMC products.
- Be sceptical of "digital" as a moat unless it shows up in cost-to-income or acquisition cost. Every bank claims it.

### Valuation (`valuation`)

Primary multiple: **P/BV** — banks are valued on book value, since the balance sheet *is* the business.
Use **P/ABV** (adjusted book value, net of unprovided NPAs) where asset quality is weak, as reported book
overstates the equity. P/E secondary. Never use EV/EBITDA — see below.

### CB Rating substitutions (`cb-rating`)

Financial-sector rules: **leverage is the business model, not a risk flag**, so Debt/Leverage is never a
component.

| Component | Weight | Banking substitution |
|---|---|---|
| Growth | 30% | Advances growth and deposit growth (both — advances growth alone rewards unfunded expansion) |
| Profitability | 25% | NIM and RoA |
| Asset Quality | 25% | GNPA trend, slippage ratio, PCR — replaces generic PAT Quality, since asset quality *is* profit quality for a bank |
| Capital & Outlook | 20% | CET-1 headroom above minimum, plus guidance |

Total 100%.

### Extra sections (`quarterly-report`)

Banking reports in this house consistently carry these beyond the standard mode set:

- **Asset Quality** — its own section, not folded into Financials. GNPA/NNPA levels, the movement table
  (opening → slippages → recoveries/upgrades → write-offs → closing), PCR and credit cost. It earns
  separate billing because it is the axis that sinks banks and the one that lags earnings.
- **Loan Book Composition** — mix by segment (retail / corporate / MSME / agri) and secured vs unsecured.
- **Margins & Returns** — the NIM walk, yield on advances vs cost of funds, RoA and RoE together.
- **Capital & Efficiency** — CRAR/CET-1 headroom alongside cost-to-income.

The established banking tab set is: Dashboard · Financials · Charts · Business Analysis · School ·
Rankings · CB Rating · AI assist panel.

### CB Rating naming (`cb-rating`)

In banking this is presented as the **"CB Earnings-Quality Rating"**, not simply "CB Rating". The name
carries the meaning: it asks how much of reported profit is core and repeatable versus how much came from
falling provisions, treasury gains or one-offs. A bank posting 23% PAT growth on 8% NII growth is a
different proposition from one posting 16% on 12.7% — the rating exists to make that visible.

Pair it with the standing house disclaimer (see `source-hierarchy.md`).

### Event transmission map (`event-impact`, `risks-outlook`)

| Event | Reaches results via | Exposure basis to cite |
|---|---|---|
| RBI repo rate cut | NIM compression — EBLR-linked loans reprice immediately, deposits reprice slowly | % of book on external benchmark (EBLR) vs MCLR/fixed |
| RBI repo rate hike | NIM expansion near-term, then deposit-cost catch-up | same |
| Deposit rate competition | cost of funds up, NIM down | CASA %, share of bulk deposits |
| Risk-weight change on unsecured lending | capital consumption, growth capacity | unsecured share of advances, CET-1 headroom |
| Revised NPA/provisioning norms | credit cost, reported PAT | stressed/restructured book, PCR |
| Priority-sector lending change | yield mix, PSLC purchase cost | PSL shortfall |
| CRR change | lendable liquidity | CASA and liquidity position |
| Bank merger / amalgamation | integration cost, network overlap | relative size, branch overlap |
| Sectoral stress (MFI, real estate) | slippage, credit cost | that sector's share of advances |

## 7. Where to look (sourcing)

**Tier 1** — quarterly results presentations and BSE/NSE filings. Bank investor presentations are
unusually detailed: asset-quality movement, sectoral exposure, and NIM walk are typically disclosed.
Search `"<bank> investor presentation Q<n> FY<yy> filetype:pdf"`.

**Tier 2 — sector authorities**: **RBI** is the primary authority — the Financial Stability Report,
Trend and Progress of Banking in India, sectoral deployment of credit data, and policy statements.
Also CRISIL/ICRA/CARE for ratings, and IBA for industry aggregates.

RBI publishes system-level credit and deposit growth, which is the right benchmark for judging whether a
bank is gaining or losing share — a bank growing advances 12% when the system grew 14% is losing ground,
and the headline number alone won't say so.

## 8. Company colour palette

**The companies named here are illustrative as at authoring, not the current universe.** Anything listed since belongs in the analysis too — see "Establish the universe before ranking anything" in `source-hierarchy.md`.

| Bank | Main | Soft tint |
|---|---|---|
| SBI | #1e3a5f | #eff6ff |
| HDFC Bank | #be123c | #fff1f2 |
| ICICI Bank | #c84b2f | #fef3f0 |
| Axis Bank | #7f1d1d | #fef2f2 |
| Kotak Mahindra Bank | #dc2626 | #fef2f2 |
| Bank of Baroda | #ea580c | #fff7ed |
| Punjab National Bank | #a16207 | #fefce8 |
| Canara Bank | #0e7490 | #ecfeff |
| IndusInd Bank | #7c3aed | #f5f3ff |
| Bank of Maharashtra | #166534 | #f0fdf4 |
| IDBI Bank | #4338ca | #eef2ff |
| AU Small Finance Bank | #d97706 | #fffbeb |

## 9. Sector-specific CSS

```css
.cat-tag{display:inline-block;padding:2px 10px;border-radius:12px;font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;}
.cat-psu{background:#dbeafe;color:#1d4ed8;}.cat-private{background:#fee2e2;color:#7f1d1d;}
.cat-sfb{background:#fffbeb;color:#a16207;}
.cat-section-title{font-family:'Playfair Display',serif;font-size:1.15rem;font-weight:700;padding:10px 16px;border-radius:8px;margin:20px 0 14px;display:flex;align-items:center;gap:10px;}

/* asset-quality movement block */
.aq-card{background:var(--surface);border:1px solid var(--border);border-left:4px solid var(--co-color,#181511);border-radius:var(--radius);padding:16px 18px;box-shadow:var(--shadow);}
```

Category accent bands: PSU bg `#eff6ff` border `#1d4ed8`; Private bg `#fef2f2` border `#7f1d1d`;
SFB bg `#fffbeb` border `#a16207`.

## 10. Mode applicability

All 15 modes apply. Notes:

- **`segments`** — loan-book composition (retail / corporate / MSME / agri, and secured vs unsecured) is
  the meaningful cut, plus geography for banks with regional concentration.
- **`valuation`** — P/BV primary, P/ABV where asset quality is weak. Never EV/EBITDA.
- **`cb-rating`** — Asset Quality replaces PAT Quality; never Debt/Leverage.
- **`risks-outlook`** — asset-quality risk deserves its own treatment; it is the axis that sinks banks.
- **Cross-sector work** — banks have **no meaningful EBITDA, and "Revenue" is not comparable** to a
  manufacturer's (NII is a spread, not sales). Those cells read **"n/a — not comparable for this
  sector"**. Net Debt is likewise meaningless: borrowings are raw material for a bank, not leverage.
