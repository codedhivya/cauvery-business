# Sector: New-Age Platforms (India)

Covers quick commerce, food delivery, e-commerce marketplaces and services platforms — the listed
internet-first businesses.

**These are the only companies in this repo where losing money can be the correct strategy.** A platform
deliberately spends ahead of revenue to buy scale, because density and habit compound. So the ordinary
questions — is margin improving, is PAT growing — are the wrong first questions. The right ones are
**do the unit economics work, and is there enough cash to reach the point where they do.**

Judge them on contribution margin per order and runway, not on reported profit.

## 1. Category taxonomy

| Category | What it is | Examples |
|---|---|---|
| **Quick commerce** | 10–30 minute delivery from dark stores. Capital-hungry, density-driven | Blinkit (Eternal), Instamart (Swiggy) |
| **Food delivery** | Restaurant aggregation and delivery; the more mature model | Zomato (Eternal), Swiggy |
| **E-commerce marketplace** | Third-party sellers, platform takes a cut | Meesho, Nykaa |
| **Services marketplace** | Matches consumers with service professionals | Urban Company |
| **Omni-channel retail** | Store-led retail with a digital layer — **profitable and arguably `consumer`** | Trent |

**Boundary note**: `Trent` appears in existing new-age reports but behaves like a `consumer` retailer —
profitable, store-led, judged on SSSG and revenue per sq ft. Analyse it with `consumer.md`'s framing and
note why it is grouped here. Genuine new-age names are pre-profit or newly profitable platforms whose
economics turn on order volume rather than store throughput.

## 2. How companies in this sector make money

A platform sits between demand and supply and takes a cut. The chain is:

**orders × average order value = GOV** → **GOV × take rate = revenue** → **revenue − variable cost per
order = contribution** → **contribution − fixed costs = EBITDA**

Each link is a lever, and they behave differently:

- **Orders** grow with users and with frequency. Frequency is the harder and more valuable one — a user
  ordering four times a month is worth far more than four users ordering once.
- **AOV** grows with basket size and mix. Quick commerce AOV is structurally lower than food delivery.
- **Take rate** is the monetisation dial. Raising it too fast pushes supply-side partners away, which is
  why platforms move it slowly and why a sudden jump deserves scrutiny.
- **Contribution margin per order** is where the business is won. It nets delivery cost, discounts and
  payment charges against revenue per order. **Positive and rising contribution margin is the signal that
  the model works**; everything above it is fixed-cost leverage that scale will eventually cover.

**Quick commerce is the capital-intensive variant.** Each dark store is upfront capex plus a maturity
curve — typically loss-making for its first several months, then contribution-positive. So a company
opening stores fast will show worsening blended economics while the underlying store performance
improves. **Always ask for mature-store versus new-store economics**; the blended number conceals both.

**The two dangers to read for.** First, growth bought with discounts — GOV rising while contribution
margin falls means the platform is buying orders. Second, **adjusted EBITDA doing too much work**: these
companies typically exclude ESOP cost and other items, and the gap between reported and adjusted can be
the difference between a profit and a loss.

### The analogy

A business buying customers now on the argument that they will be profitable later. The question is never current profit — it is whether each new customer costs less than they eventually bring in, and whether the cash lasts long enough to find out.

## 3. Metric definitions

- **GOV (Gross Order Value)** — total value of orders placed, before discounts. The headline scale
  metric.
- **NOV (Net Order Value)** — GOV net of discounts and cancellations. **Closer to economic reality than
  GOV**, and the gap between the two is the discount intensity.
- **GMV** — used interchangeably with GOV by some platforms; state which definition the company uses,
  since they are not always the same.
- **AOV (Average Order Value)** = GOV ÷ orders.
- **Orders** and **order frequency per user** — volume and habit.
- **MTU (Monthly Transacting Users)** — the active user base actually spending.
- **Take rate (%)** = revenue ÷ GOV. The monetisation rate.
- **Contribution margin (per order and %)** — revenue per order less variable costs (delivery, discount,
  payment gateway). **The single most important metric in this file.** Report it per segment; quick
  commerce and food delivery have very different curves.
- **Adjusted EBITDA** — as reported by the company, **with the adjustments itemised**. ESOP cost is the
  usual exclusion. Show reported alongside adjusted.
- **Dark stores** — count, net additions, average age, and **mature vs new split**. Throughput per store.
- **Cash burn (₹ cr/quarter)** and **runway (quarters or months)** at current burn. For a pre-profit
  platform this is a survival metric, not a footnote.
- **Cash and equivalents** — the denominator of runway.
- **Segment-wise revenue and contribution** — Eternal-type companies run several distinct businesses
  (food delivery, quick commerce, B2B supplies, going-out) with different maturity. A consolidated number
  is close to meaningless.
- **Path to profitability** — management's stated timeline and the milestones it depends on. Treat it as
  guidance, and track it against prior guidance.

## 4. Benchmarks — what good looks like

Indicative; this sector is in transition and levels move fast. Verify against the company's own trend
rather than treating any figure as fixed.

| Metric | Healthy |
|---|---|
| GOV growth | 20%+ YoY for a scaling platform |
| Take rate | rising slowly; a sharp jump risks supply-side churn |
| Contribution margin (food delivery, mature) | positive and expanding; high single digit % of GOV |
| Contribution margin (quick commerce) | positive at store level once mature; blended lags during expansion |
| Adjusted EBITDA margin | improving trend matters more than the level |
| Reported vs adjusted EBITDA gap | narrowing; a widening gap deserves explanation |
| Dark store maturity | new stores contribution-positive within a few quarters |
| Runway | >8 quarters at current burn; <4 is a financing event waiting to happen |
| Order frequency | rising — the clearest signal of genuine habit |

**What to watch:**

- **Is contribution margin positive and rising** — separately for each segment, not blended?
- **Is GOV growth accompanied by improving contribution**, or bought with discounts? Check the GOV-to-NOV
  gap.
- **How many dark stores are mature versus new**, and what do mature-store economics look like?
- **What exactly is excluded from adjusted EBITDA**, and is the gap narrowing?
- **What is the runway**, and does the path-to-profitability timeline fit inside it?
- **Is order frequency rising**, or is growth coming entirely from new-user acquisition — which is more
  expensive and less durable?
- **Is a competitor funding a price war?** In a two-player market, one player's capital raise is the
  other's margin problem.

### What goes wrong, and the tell

**Growth that stops paying for itself.** The tells: order growth slowing while discounting rises, meaning demand is being bought; contribution margin flat or negative at scale, which suggests the unit economics do not improve with volume; cash runway shortening against the burn rate; and a profitability milestone that keeps moving out by a quarter each quarter.

## 5. Regulatory quick reference

Lightly regulated relative to financials, but several live exposures:

| Area | Body / issue |
|---|---|
| E-commerce policy, FDI in multi-brand retail | DPIIT — inventory vs marketplace model rules |
| Gig worker classification and social security | Labour codes; state-level rules — a structural cost risk for delivery fleets |
| Food safety | FSSAI — restaurant partners and dark-store handling |
| Consumer protection | CCPA — dark patterns, deceptive pricing rules |
| Competition | CCI — deep-discounting and preferential-treatment complaints have been filed against platforms |
| Data protection | DPDP Act |
| Quick commerce zoning | local licensing for dark stores in residential areas |

**Gig-worker regulation is the most consequential open risk.** Reclassifying delivery partners as
employees would change the variable-cost structure that contribution margin depends on.

## 6. Per-mode specifics

### Headline KPIs by category (`dashboard`)

| Category | KPIs |
|---|---|
| Quick commerce | GOV, orders, AOV, dark stores (mature/new), contribution margin, adjusted EBITDA, cash burn |
| Food delivery | GOV, orders, AOV, MTU, take rate, contribution margin, adjusted EBITDA |
| E-commerce marketplace | GMV, orders, AOV, take rate, contribution margin, adjusted EBITDA, MTU |
| Services marketplace | GMV, transactions, take rate, provider base, contribution margin, adjusted EBITDA |
| Omni-channel retail | use `consumer.md` — SSSG, store count, revenue per sq ft |

### Table columns by category (`financials`)

- **All** — Period, GOV/GMV, YoY, Orders, AOV, Take rate, Revenue, **Contribution margin**,
  **Adjusted EBITDA**, **Reported EBITDA**, PAT
- **Segment table — mandatory.** Revenue and contribution by segment (food delivery / quick commerce /
  B2B / other). These companies run unlike businesses under one listing, and a consolidated line hides
  which one is working.
- **Cash & runway table** — cash balance, quarterly burn, runway in quarters. Not optional for a
  pre-profit platform.
- **Adjustment reconciliation** — a `.fnote` itemising what separates reported from adjusted EBITDA.

### Chart reference lines (`charts`)

| Metric | Line | Label |
|---|---|---|
| Contribution margin | 0% | "Contribution breakeven" — the line that decides whether the model works |
| Adjusted EBITDA margin | 0% | "EBITDA breakeven" |
| Runway | 4 quarters | "Financing-risk threshold" |
| GOV growth | 20% | "Scaling benchmark" — industry norm, label as such |

**Plot contribution margin by segment, never blended**, and plot GOV alongside contribution — the
relationship between them is the entire investment question in this sector.

### Profile coverage by category (`business-profile`)

Cover: the segment portfolio and what each does, **dark-store or fulfilment footprint** with maturity
split, user base and frequency, supply-side base (restaurants, sellers, service professionals), take-rate
policy, competitive position in a typically two- or three-player market, cash position and funding
history, and management's stated path to profitability with its prior track record.

Existing reports carry **Unit Economics**, **Cash & Runway**, **Distribution & Reach** and
**"Why Profit? Why Loss?"** — that last one is a genuinely good section and worth keeping: it forces an
explicit account of what is driving the result rather than describing it.

### Moat candidates by category (`moats`)

- **Network effects and density.** In quick commerce, more orders per dark store lowers cost per order,
  which funds better service, which wins more orders. **Density is the real moat**, and it is
  geographic — a platform can be dominant in one city and subscale in another. Cite orders per store.
- **Habit and frequency.** A user ordering weekly is expensive for a competitor to dislodge. Frequency
  data is the evidence; app downloads are not.
- **Supply-side lock-in** — restaurant or seller relationships, exclusive listings, integrated logistics.
- **Fulfilment infrastructure** — a dark-store network in prime urban locations is capital and time, and
  the good locations are finite.
- **Be sceptical of GMV scale as a moat.** GMV bought with discounts is rented, not owned, and unwinds
  the moment the discount stops. The test is whether contribution margin holds while GMV grows.
- **Be equally sceptical of "first mover"** in a market where a well-funded competitor can replicate the
  model — several of these categories have seen exactly that.

### Valuation (`valuation`)

**Not P/E.** Most of these companies have no meaningful earnings, and those that do have only just
reached profitability, so a trailing multiple is either undefined or absurd.

Primary: **EV/GOV** or **EV/Revenue**, with the growth rate and contribution trajectory stated alongside
— a multiple without those is meaningless here. **EV/EBITDA** becomes usable once adjusted EBITDA is
durably positive, and should be stated on the *reported* basis with the adjustment gap noted.

Sum-of-the-parts is often the honest approach for multi-segment platforms, valuing a mature food-delivery
business differently from a scaling quick-commerce one. Where a company is pre-profit, say plainly that
valuation rests on a path-to-profitability assumption and name the assumption.

### CB Rating substitutions (`cb-rating`)

Pre-profit platforms: profit-based components are replaced by unit economics and funding, because scoring
a deliberately loss-making business on PAT measures its strategy, not its performance.

| Component | Weight | New-age substitution |
|---|---|---|
| Growth | 30% | **GOV/GMV growth and order growth**, with order frequency where disclosed — not revenue, which moves with take-rate changes |
| Unit Economics | 25% | **Contribution margin level and direction, by segment** — replaces Profitability, because margin on a scaling platform is a function of stage, not quality |
| Earnings Quality | 25% | **Reported vs adjusted EBITDA gap** and its direction; discount intensity (GOV-to-NOV gap) — is growth bought or earned? |
| Funding & Outlook | 20% | **Cash runway**, burn trend, path-to-profitability credibility against prior guidance |

Total 100%. **Do not score a pre-profit platform on PAT.** A company burning cash to build density may be
executing well; one burning cash with flat contribution margin is not, and only the unit economics
distinguish them.

### Extra sections (`quarterly-report`)

- **Unit Economics** — contribution margin by segment, per-order breakdown. The centrepiece.
- **Cash & Runway** — balance, burn, quarters remaining.
- **Why Profit? Why Loss?** — an explicit account of the drivers, as existing reports do.
- **Segment Analysis** — mandatory; these are several businesses in one listing.
- **Distribution & Reach** — dark stores, cities, fulfilment footprint.
- **New Business Segments** — the newer bets and what they are costing.

### Event transmission map (`event-impact`, `risks-outlook`)

| Event | Reaches results via | Exposure basis to cite |
|---|---|---|
| Competitor capital raise | discount intensity, contribution margin | that market's share of GOV |
| Gig-worker classification ruling | variable delivery cost, contribution margin | delivery partner count, fleet cost share |
| Take-rate change | revenue and supply-side churn | current take rate, partner base |
| Quick-commerce zoning or licensing change | dark-store rollout | stores in affected cities |
| CCI proceeding on discounting or preferential listing | pricing conduct, penalty | practices under review |
| FDI or e-commerce policy change | marketplace vs inventory model | model in use |
| Fuel price move | delivery cost per order | fleet cost as % of contribution |
| Funding-market tightening | runway, ability to sustain burn | cash, quarterly burn |
| New category launch (by self or competitor) | GOV mix, near-term burn | investment committed |

## 7. Where to look (sourcing)

**Tier 1** — quarterly investor presentations and shareholder letters. This sector discloses GOV, orders,
AOV, contribution margin, dark-store counts and adjusted-EBITDA reconciliations there, and **almost none
of it appears in the press release**. Several of these companies write detailed shareholder letters that
are unusually candid about unit economics — read them.

**Tier 2** — there is no industry regulator publishing volumes, which makes this sector harder to
benchmark than most. **Redseer, Bain and similar consultancies** publish market-size and share estimates;
attribute them to the firm and treat them as estimates rather than measurements. **DPIIT** for
e-commerce policy, **CCI** for competition proceedings.

Because no authoritative third-party volume data exists, **market-share claims in this sector are usually
company-sourced or consultancy-estimated**. Say which, rather than presenting either as fact.

## 8. Company colour palette

**The companies named here are illustrative as at authoring, not the current universe.** Anything listed since belongs in the analysis too — see "Establish the universe before ranking anything" in `source-hierarchy.md`.

| Company | Main | Soft tint |
|---|---|---|
| Eternal (Zomato) | #be123c | #fff1f2 |
| Blinkit (Eternal) | #ca8a04 | #fefce8 |
| Swiggy | #ea580c | #fff7ed |
| Meesho | #7c3aed | #f5f3ff |
| Nykaa | #9d174d | #fdf2f8 |
| Urban Company | #0d9488 | #f0fdfa |
| Trent | #1e3a5f | #eff6ff |

## 9. Sector-specific CSS

```css
.cat-tag{display:inline-block;padding:2px 10px;border-radius:12px;font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;}
.cat-qcom{background:#fefce8;color:#ca8a04;}.cat-fooddel{background:#fff1f2;color:#be123c;}
.cat-marketplace{background:#f5f3ff;color:#7c3aed;}.cat-services{background:#f0fdfa;color:#0d9488;}
.cat-omni{background:#eff6ff;color:#1e3a5f;}
.cat-section-title{font-family:'Playfair Display',serif;font-size:1.15rem;font-weight:700;padding:10px 16px;border-radius:8px;margin:20px 0 14px;display:flex;align-items:center;gap:10px;}

/* unit economics — the per-order walk */
.ue-card{background:var(--surface);border:1px solid var(--border);border-left:4px solid var(--co-color,#181511);border-radius:var(--radius);padding:16px 18px;box-shadow:var(--shadow);}
.ue-row{display:grid;grid-template-columns:1.4fr auto;gap:10px;font-size:11.5px;padding:6px 0;border-bottom:1px dashed var(--border);}
.ue-row:last-child{border-bottom:none;font-weight:700;}
.ue-val{font-family:'IBM Plex Mono',monospace;font-weight:600;}
.ue-pos{color:var(--pos);}.ue-neg{color:var(--neg);}

/* runway gauge — survival metric for a pre-profit platform */
.runway-card{background:#fff7ed;border:1px solid #fdba74;border-left:4px solid var(--warn);border-radius:var(--radius);padding:14px 16px;font-size:11.5px;}
.runway-card h4{font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:var(--warn);margin-bottom:8px;}
.runway-bar-wrap{background:var(--surface2);border-radius:4px;height:16px;overflow:hidden;margin-top:6px;}
.runway-bar{height:100%;border-radius:4px;background:var(--warn);}

/* adjusted vs reported EBITDA gap */
.adj-gap{display:grid;grid-template-columns:1fr auto auto;gap:10px;font-size:11.5px;padding:6px 0;border-bottom:1px dashed var(--border);}
.adj-gap:last-child{border-bottom:none;}
.adj-pill{font-family:'IBM Plex Mono',monospace;font-size:10.5px;font-weight:700;padding:2px 8px;border-radius:4px;background:var(--surface2);}
```

## 10. Mode applicability

All 15 modes apply. Notes:

- **`segments`** — the highest-value mode here and effectively mandatory. These companies run unlike
  businesses under one listing; a consolidated number hides which is working.
- **`financials`** — the cash-and-runway table and the adjusted-vs-reported reconciliation are not
  optional for a pre-profit platform.
- **`charts`** — plot contribution margin **by segment**, never blended, and plot it against GOV. The
  relationship between the two is the investment question.
- **`valuation`** — **not P/E**. EV/GOV or EV/Revenue with growth and contribution trajectory stated.
  Say plainly when valuation rests on a path-to-profitability assumption.
- **`cb-rating`** — Unit Economics replaces Profitability and Funding & Outlook replaces Forward Outlook;
  never score a pre-profit platform on PAT.
- **`moats`** — density and frequency are real; GMV scale bought with discounts is not.
- **`school`** — this sector's vocabulary (GOV vs NOV vs GMV, take rate, contribution margin) is
  genuinely unfamiliar to most readers and worth teaching explicitly.
- **Cross-sector work** — **Revenue, Mkt Cap and EV/Revenue apply; EBITDA%, PAT and P/E frequently do
  not**, because several of these companies are pre-profit by design. Those cells read
  **"n/a — not comparable for this sector"** rather than showing a negative margin that would rank them
  bottom of a table alongside mature manufacturers. GOV, take rate, contribution margin, AOV, dark stores
  and runway are sector-specific and stay in their own section.
