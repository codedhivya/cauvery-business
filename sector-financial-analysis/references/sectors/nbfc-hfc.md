# Sector: NBFCs & Housing Finance (India)

Covers non-banking financial companies, housing finance companies, infrastructure and sector-specific
financiers, and emerging financial-services platforms.

**This sector is separate from `banking.md` and must not be analysed with it.** The lending mechanics
look similar and the metric names overlap, but the funding side is completely different: **NBFCs cannot
take deposits from the public in the way banks do.** They fund themselves by borrowing — bank lines,
NCDs, commercial paper, ECBs, securitisation. There is no CASA, no deposit franchise, and no
low-cost-funding moat. That single difference drives most of what follows.

## 1. Category taxonomy

| Category | What it is | Examples |
|---|---|---|
| **Diversified NBFC** | Multi-product retail and SME lending | Bajaj Finance, Cholamandalam Investment |
| **Asset-backed / Vehicle finance** | Commercial vehicle, equipment, used-asset lending; higher yield, higher credit cost | Shriram Finance |
| **Gold loan NBFC** | Lending against gold collateral; short tenor, high yield, collateral-backed | Muthoot Finance |
| **Housing Finance (HFC)** | Home loans — prime, affordable, or self-employed segments | LIC Housing Finance, PNB Housing, Can Fin Homes, Bajaj Housing Finance |
| **Affordable Housing Finance** | Smaller-ticket, higher-yield, often self-employed borrowers | Aavas, Aadhar Housing, Home First, Shelter |
| **Infrastructure / Sectoral financier** | Lending to a defined sector, often government-linked | PFC, REC, IREDA |
| **NBFC-MFI (microfinance)** | Small, unsecured, joint-liability group loans to low-income borrowers. **A separate RBI licence category**, not a small NBFC | CreditAccess Grameen, Spandana Sphoorty, Fusion |
| **Financial services platform** | Emerging diversified financial platforms | Jio Financial Services |

Compare within a category by default. An affordable HFC's 13% yield and a prime HFC's 9% are not the
same metric doing the same job — the first is compensation for a riskier borrower, not superior pricing.

## 2. How companies in this sector make money

An NBFC borrows wholesale and lends retail. The gap is the **spread**, and unlike a bank it is fully
exposed to funding-market conditions — there is no sticky current-account balance cushioning the cost of
funds.

Three consequences follow, and they define how the sector is analysed:

1. **Cost of funds is the swing factor.** When credit markets tighten or rates rise, an NBFC's funding
   cost moves quickly while its loan book reprices slowly. Banks partially absorb this through CASA;
   NBFCs cannot.
2. **Credit rating is existential, not cosmetic.** A downgrade raises borrowing cost across the entire
   liability book and can close funding lines outright. Rating is a business input here in a way it is
   not for a bank.
3. **Asset–liability management (ALM) is a survival metric.** Borrowing short to lend long — a housing
   loan runs 15+ years, funded by 3-year NCDs — creates refinancing risk. ALM mismatch is what has
   historically killed NBFCs, not credit losses alone.

The four axes:

| Axis | Question | Core metrics |
|---|---|---|
| **Growth** | Is the book expanding? | AUM growth, disbursements |
| **Spread** | How profitable is the lending? | Yield, cost of funds, spread, NIM |
| **Asset quality** | How much goes bad? | GNPA, NNPA, credit cost, PCR, stage-wise provisioning |
| **Funding & capital** | Can it keep funding itself? | Borrowing mix, CRAR, credit rating, ALM |

## 3. Metric definitions

- **AUM (Assets Under Management)** — the headline size metric, and the sector's equivalent of a bank's
  advances. Note it may include **off-book AUM** (assets securitised or under co-lending arrangements)
  that no longer sit on the balance sheet but still earn fees. Always check whether a stated AUM is
  on-book, off-book or combined — the three are frequently blurred.
- **Disbursements** — new loans originated in the period. The leading indicator; AUM is the lagging
  stock, disbursement is the flow.
- **Yield on advances (%)** — what the book earns. Varies enormously by category: prime housing single
  digits, gold and vehicle finance mid-to-high teens.
- **Cost of funds (%)** — what borrowing costs. **The metric to watch most closely in a rate cycle.**
- **Spread** = yield − cost of funds. The cleanest measure of lending profitability for an NBFC, and more
  directly meaningful than NIM here because the asset and liability sides are both market-priced.
- **NIM** — reported by most, but read spread alongside it; NIM is affected by leverage and asset mix in
  ways spread is not.
- **GNPA / NNPA / PCR** — as in banking. Many NBFCs also report **Stage 1/2/3 assets** under Ind AS,
  where **Stage 2 (significant increase in credit risk, not yet impaired) is the early-warning bucket** —
  more informative than GNPA, and frequently overlooked.
- **Credit cost (%)** — provisions as % of average AUM. What asset quality actually costs earnings.

### Microfinance (NBFC-MFI) — a different vocabulary

**Do not read an MFI on GNPA alone.** Loans are small, unsecured and repaid weekly or fortnightly, so
stress shows in the ageing buckets long before it reaches a 90-day NPA. The corpus uses:

- **PAR 30 / PAR 60 / PAR 90 (Portfolio at Risk)** — share of portfolio overdue past each ageing bucket.
  **The primary asset-quality metric**, and the early-warning one; PAR 30 turns first.
- **Collection efficiency (%)** — current collections against dues. The weekly-cycle health check; a fall
  here precedes a PAR rise by a quarter or less.
- **GLP (Gross Loan Portfolio)** — the MFI's term for AUM.
- **Credit cost** — structurally higher and **far lumpier** than in secured lending. Judge across a
  cycle, never on one quarter.
- **Borrower count, ticket size, loans per borrower** — rising loans per borrower is an over-indebtedness
  signal, and the sector's repeated failure mode.
- **District and state concentration** — MFI stress is geographic and correlated. A book concentrated in
  a few districts is exposed to one flood, one crop failure, one local political intervention.
- **Write-offs** — read with PAR. Aggressive write-off flatters PAR; state them together.

**Regulatory frame**: RBI microfinance rules cap lending against assessed household income and total
indebtedness, and set a qualifying-asset share. **MFIN** publishes industry portfolio and PAR data — a
real Tier-2 source for the denominator. Confirm current thresholds at source.

**The failure mode to name**: microfinance crises are not gradual. Collection efficiency drops, PAR 30
spikes, credit cost follows a quarter later. State geographic concentration whenever asset quality looks
benign.
- **Borrowing mix** — bank borrowings vs NCDs vs commercial paper vs ECBs vs deposits (where a
  deposit-taking NBFC is permitted). **Heavy short-term CP reliance is a red flag** for refinancing risk.
- **ALM position** — cumulative mismatch by maturity bucket. Disclosed in the annual report and worth
  finding for any leveraged lender.
- **CRAR / Tier-1** — capital adequacy. RBI minimums differ from bank requirements; see §5.
- **Securitisation / direct assignment / co-lending** — moving assets off-book to free capital and earn
  fee income. Watch whether growth is genuine origination or balance-sheet management.
- **Credit rating** — the external rating on borrowing programmes. State it; it is a business input.

## 4. Benchmarks — what good looks like

Indicative and category-dependent; verify against the company's own history.

| Metric | Healthy |
|---|---|
| AUM growth | 15–25% for retail NBFCs; slower for infra financiers |
| Spread | >4% retail NBFC; 2–3% prime housing; 5%+ gold and vehicle finance |
| NIM | 6–8% diversified retail; 3–4% prime HFC |
| Cost of funds | falling or stable relative to peers; direction matters more than level |
| GNPA | <2% prime housing; <4% vehicle and affordable segments |
| Credit cost | <1.5% retail; higher is normal for used-vehicle and unsecured books |
| PCR | >50–60% |
| CRAR | comfortably above the regulatory minimum; >20% is typical and conservative |
| Short-term borrowing (CP) share | <15% of borrowings — higher is refinancing risk |
| Credit rating | AAA/AA+ for large NBFCs; a downgrade is a material event |

**What to watch, by category:**

- **Diversified NBFC** — Is AUM growth holding without loosening underwriting? Is the unsecured share
  rising faster than provisions? Is cost of funds stable?
- **Vehicle / asset-backed** — Is credit cost within guidance? How is the used-asset book performing? Is
  collection efficiency holding?
- **Gold loan** — What is the LTV position, and how exposed is it to a gold price fall? Is auction
  volume rising (a stress signal)?
- **Prime HFC** — Is spread compressing under bank competition? Banks can undercut on home loans because
  their funding is cheaper — this is the structural pressure on prime housing finance.
- **Affordable HFC** — Is the yield premium being preserved? Is GNPA stable in the self-employed book?
- **Infra financier (PFC/REC/IREDA)** — What is exposure to state discoms and their payment record? Is
  the renewable book growing? These are government-linked and their asset quality is policy-sensitive.

## 5. Regulatory quick reference

| Requirement | Level |
|---|---|
| Regulator | **RBI** — NBFCs and HFCs (HFC supervision moved from NHB to RBI) |
| Scale-based regulation | Base / Middle / Upper / Top layer — obligations rise with size; know which layer applies |
| Minimum CRAR (NBFC-ICC) | 15%, with Tier-1 minimum |
| HFC capital requirement | as prescribed under RBI's HFC directions |
| Liquidity Coverage Ratio | applicable to larger NBFCs |
| NPA recognition | 90-day norm, aligned with banks |
| Deposit acceptance | only for NBFCs specifically authorised; most are non-deposit-taking |

RBI scale-based regulation and risk-weight changes are the recurring policy events here. Verify current
levels against the applicable RBI circular rather than carrying a figure forward.

## 6. Per-mode specifics

### Headline KPIs by category (`dashboard`)

| Category | KPIs |
|---|---|
| Diversified NBFC | AUM, AUM growth, NIM/spread, GNPA, credit cost, PAT, CRAR |
| Vehicle / asset-backed | AUM, disbursements, yield, GNPA, credit cost, PAT, collection efficiency |
| Gold loan | AUM, gold tonnage held, LTV, yield, GNPA, PAT |
| HFC (prime) | AUM, disbursements, spread, GNPA, PAT, CRAR |
| HFC (affordable) | AUM, disbursements, yield, spread, GNPA, PAT |
| Infra / sectoral financier | Loan book, disbursements, sanctions, NIM, GNPA, PAT, CRAR |

### Table columns by category (`financials`)

- **All categories** — Period, AUM, YoY, Disbursements, Yield, Cost of funds, Spread, NII, PAT, YoY
- **Asset quality table** — GNPA%, NNPA%, PCR, credit cost, and **Stage 1/2/3 split where disclosed**
- **Funding table** — borrowing mix by instrument, average cost, credit rating, short-term share, and ALM
  position where available. **This table is what distinguishes NBFC analysis from bank analysis** and
  should not be dropped.

### Chart reference lines (`charts`)

| Metric | Line | Label |
|---|---|---|
| CRAR | 15% | "RBI minimum (NBFC-ICC)" |
| Short-term borrowing share | 15% | "Refinancing-risk threshold" — industry norm, label as such |
| Credit cost | 1.5% | "Typical retail credit cost" — norm, not a rule |
| GNPA | peer median | no regulatory line exists; use the category median and say so |

### Profile coverage by category (`business-profile`)

Cover for every company: **product mix and AUM split**, **borrowing mix and credit rating**, branch and
distribution footprint, geographic concentration, digital origination share, and **promoter/parent
backing** — for an NBFC, a strong parent materially affects funding access and cost, which is why
bank-promoted and corporate-backed NBFCs borrow cheaper than standalone ones.

- **HFC** — prime vs affordable positioning, average ticket size, salaried vs self-employed mix, LTV.
- **Infra financier** — sector exposure (power generation, transmission, renewable), borrower profile
  (state utilities vs private), government shareholding.
- **Gold loan** — branch network, gold tonnage, auction policy.

### Moat candidates by category (`moats`)

- **Parent or promoter backing** — the closest thing to a funding moat available here. A strong parent
  lowers cost of funds structurally, and cost of funds is the competitive weapon in lending.
- **Underwriting track record through a full cycle** — visible only in credit cost across a downturn, and
  genuinely hard to replicate because it requires having survived one.
- **Distribution reach in under-served geographies** — affordable HFCs and gold-loan NBFCs lend where
  banks do not go; that branch network is slow and expensive to build.
- **Collateral and collection infrastructure** — gold-loan auction capability, vehicle repossession
  networks. Unglamorous and hard to copy.
- **Scale-driven cost advantage** in opex-to-AUM.
- **Be sceptical** of "digital origination" as a moat — every lender claims it, and it only counts if it
  shows in cost-to-income or credit cost. Also be sceptical of AUM growth alone: growth is easy to buy by
  loosening underwriting, and the bill arrives two years later.

### Valuation (`valuation`)

Primary multiple: **P/BV**, as for banks — the balance sheet is the business. **P/E** as secondary.
Use **P/ABV** (adjusted book value, net of unprovided NPAs) where asset quality is weak. Never
EV/EBITDA. High-growth retail NBFCs have historically traded at large premiums to book; state the
premium against the company's own history rather than treating a high multiple as automatically
expensive.

### CB Rating substitutions (`cb-rating`)

Financial sector: **leverage is the business model, so Debt/Leverage is never a component.** But unlike
banks, funding is the differentiator here and gets explicit weight.

| Component | Weight | NBFC-HFC substitution |
|---|---|---|
| Growth | 30% | AUM growth and disbursement growth |
| Profitability | 25% | Spread and NIM — spread leads, since it isolates lending economics |
| Asset Quality | 25% | GNPA trend, credit cost, PCR, Stage 2 movement — replaces PAT Quality, as for banks |
| Funding & Capital | 20% | Cost of funds direction, borrowing mix and short-term reliance, credit rating, CRAR headroom — replaces generic Forward Outlook, because funding access *is* the outlook for a borrower-funded lender |

Total 100%.

### Extra sections (`quarterly-report`)

- **Asset Quality & Funding** — recurs as an explicit section in existing reports, and rightly: it pairs
  the two things that sink NBFCs.
- **Borrowing Profile** — instrument mix, average cost, maturity ladder, credit rating.
- **AUM Composition** — by product, geography and on-book vs off-book.
- **Peer Comparison** — recurs in existing reports.

### Event transmission map (`event-impact`, `risks-outlook`)

| Event | Reaches results via | Exposure basis to cite |
|---|---|---|
| RBI repo / policy rate change | cost of funds first, lending yield later | borrowing mix, share repricing within 12 months |
| Credit rating downgrade | borrowing cost across the whole liability book, funding access | rating, share of market borrowings |
| Bond-market or CP-market tightening | refinancing risk | short-term borrowing share, ALM gap |
| RBI risk-weight change (unsecured, consumer) | capital consumption, growth capacity | unsecured share of AUM, CRAR headroom |
| Scale-based regulation reclassification | compliance cost, governance requirements | current layer |
| Gold price fall | LTV breach, auction volumes | gold-loan AUM, average LTV |
| Discom payment scheme or default | asset quality at infra financiers | discom exposure share |
| Bank competition in home loans | spread compression at prime HFCs | prime share of AUM |
| Securitisation / co-lending rule change | off-book growth, fee income | off-book AUM share |

## 7. Where to look (sourcing)

**Tier 1** — quarterly investor presentations, which disclose AUM composition, disbursements, borrowing
mix, cost of funds and Stage 1/2/3 asset splits. **The ALM maturity ladder usually appears only in the
annual report** — worth retrieving for any leveraged lender.

**Tier 2 — sector authorities**: **RBI** (regulations, scale-based framework, sectoral credit data,
Financial Stability Report), **NHB** for housing-finance market data, and **CRISIL / ICRA / CARE**, whose
role here is unusually important — the rating is a business input, not just an opinion, so rating actions
and rationale documents are genuinely informative about funding cost and asset quality.

## 8. Company colour palette

| Company | Main | Soft tint |
|---|---|---|
| Bajaj Finance | #1d4ed8 | #eff6ff |
| Shriram Finance | #ea580c | #fff7ed |
| Cholamandalam Investment | #166534 | #f0fdf4 |
| Muthoot Finance | #b8911e | #fdf5e0 |
| Bajaj Housing Finance | #4338ca | #eef2ff |
| LIC Housing Finance | #1e3a5f | #eff6ff |
| PNB Housing Finance | #a16207 | #fefce8 |
| Can Fin Homes | #0e7490 | #ecfeff |
| Aavas Financiers | #7c3aed | #f5f3ff |
| Aadhar Housing Finance | #9d174d | #fdf2f8 |
| Home First Finance | #0d9488 | #f0fdfa |
| PFC | #7f1d1d | #fef2f2 |
| REC | #be123c | #fff1f2 |
| IREDA | #15803d | #f0fdf4 |
| Jio Financial Services | #334155 | #f1f5f9 |

## 9. Sector-specific CSS

```css
.cat-tag{display:inline-block;padding:2px 10px;border-radius:12px;font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;}
.cat-nbfc{background:#eff6ff;color:#1d4ed8;}.cat-vehicle{background:#fff7ed;color:#c2410c;}
.cat-gold{background:#fdf5e0;color:#b8911e;}.cat-hfc{background:#f0fdf4;color:#166534;}
.cat-affordable{background:#f5f3ff;color:#7c3aed;}.cat-infra{background:#fef2f2;color:#7f1d1d;}
.cat-section-title{font-family:'Playfair Display',serif;font-size:1.15rem;font-weight:700;padding:10px 16px;border-radius:8px;margin:20px 0 14px;display:flex;align-items:center;gap:10px;}

/* borrowing mix / funding profile */
.fund-card{background:var(--surface);border:1px solid var(--border);border-left:4px solid var(--co-color,#181511);border-radius:var(--radius);padding:16px 18px;box-shadow:var(--shadow);}
.fund-row{display:grid;grid-template-columns:118px 1fr 56px;align-items:center;gap:10px;font-size:11.5px;margin-bottom:6px;}
.fund-bar-wrap{background:var(--surface2);border-radius:4px;height:14px;overflow:hidden;}
.fund-bar{height:100%;border-radius:4px;background:var(--co-color,#181511);}
.rating-pill{font-family:'IBM Plex Mono',monospace;font-size:10.5px;font-weight:700;padding:2px 9px;border-radius:4px;}
.rt-aaa{background:#dcfce7;color:#15803d;}.rt-aa{background:#dbeafe;color:#1d4ed8;}
.rt-a{background:#fef9c3;color:#a16207;}.rt-below{background:#fee2e2;color:#b91c1c;}

/* spread walk: yield - cost of funds */
.spread-row{display:grid;grid-template-columns:1fr auto auto auto;gap:10px;font-size:11.5px;padding:7px 0;border-bottom:1px dashed var(--border);}
.spread-row:last-child{border-bottom:none;}
```

## 10. Mode applicability

All 15 modes apply. Notes:

- **`segments`** — AUM composition by product and geography, plus on-book vs off-book, is the meaningful
  cut.
- **`financials`** — the funding table is not optional; it is what separates NBFC analysis from banking.
- **`valuation`** — P/BV primary, P/ABV where asset quality is weak. Never EV/EBITDA.
- **`cb-rating`** — Asset Quality replaces PAT Quality (as in banking), and **Funding & Capital replaces
  Forward Outlook**, because for a borrower-funded lender, continued funding access *is* the outlook.
- **`risks-outlook`** — ALM mismatch and refinancing risk deserve explicit treatment. Historically these,
  not credit losses alone, are what have killed NBFCs.
- **Cross-sector work** — NBFCs have **no meaningful EBITDA**, and "Revenue" is interest income rather
  than sales. Those cells read **"n/a — not comparable for this sector"**. **Net Debt is meaningless and
  actively misleading**: borrowings are the raw material of a lender, so a naive Net Debt ranking would
  place every NBFC at the bottom of a cross-sector table. Flag this explicitly wherever this sector
  appears alongside operating companies.
