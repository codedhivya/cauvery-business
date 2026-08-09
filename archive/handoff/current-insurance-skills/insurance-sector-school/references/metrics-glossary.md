# Indian Insurance Sector — Metrics Glossary & Manufacturing Analogy

Use this as the canonical definitions source so every skill explains metrics the same way.
When writing for a general/retail audience, lean on the manufacturing analogy — it's the fastest
way to make an unfamiliar reader grasp why insurers are valued differently from normal companies.

## Manufacturing ↔ Insurance Analogy Table

| Manufacturing Term | Insurance Equivalent | Why Same? |
|---|---|---|
| Revenue / Sales | GWP / GDPI / Total Premium | Premium = money coming in |
| Future Order Profitability | VNB (Value of New Business) | Value of business written today, paid over years |
| Gross Margin % | VNB Margin | Profit per ₹100 of premium written |
| Net Worth / Book Value | Embedded Value (EV) | Worth today + locked-in future profits |
| ROE | RoEV / EVOP | Return on capital deployed |
| Raw Material Cost | Claims | The "cost" the insurer cannot avoid |
| Operating Ratio | Combined Ratio / CISR | Below 100% = profitable; above 100% = loss |
| Customer Repeat Business | Persistency | % customers renewing — stickiness |
| Capital Adequacy (CRAR) | Solvency Ratio | Safety buffer for unexpected claims |

Key framing line to reuse: "Manufacturing companies are judged mainly on current profits. Insurance
companies are judged on future profitability (VNB), capital strength (Solvency), customer retention
(Persistency), and underwriting quality (Combined Ratio)."

## Life Insurance Metrics

- **GWP / Total Premium** — total premium collected; NOT profit (claims, commissions, bonuses come out of it).
- **APE (Annualised Premium Equivalent)** = Regular Annual Premium + 10% × Single Premium. Standardises
  new-business volume across insurers with different single-vs-regular premium mixes.
- **VNB (Value of New Business)** = present value of all future profits from policies sold in the period.
  The single most important life-insurer profitability metric — more informative than PAT.
- **VNB Margin** = VNB ÷ APE. Profit locked in per ₹100 of new business. Sector context: SBI Life ~27–28%
  (best-in-class), Axis Max Life ~25%, ICICI Pru ~25–27%, HDFC Life ~24–25%, LIC ~21–23% (rising).
- **Embedded Value (EV / IEV)** = Adjusted Net Worth + PV of future profits from in-force policies. The
  true economic net worth of a life insurer — valued via P/EV the way banks are valued via P/B.
- **RoEV** = Operating profit ÷ average EV. The insurance-sector equivalent of ROE. >15–17% is strong.
- **Persistency Ratio** — % of policyholders still paying premium at the 13th month (year 1 renewal) or
  61st month (year 5 renewal). Low persistency = revenue leakage + agent mis-selling signal. Healthy
  benchmarks: 13th month >80–85%, 61st month >50%.
- **Solvency Ratio** = Available Solvency Margin ÷ Required Solvency Margin. IRDAI minimum 150% for
  ALL insurers (life, health, general, TPA-adjacent). >180–200% is a comfortable cushion.
- **P/EV** = Market Cap ÷ Embedded Value — the life insurer's "P/E".

## Health / General Insurance Metrics

- **Combined Ratio** = (Claims + All Expenses) ÷ Net Premium Earned. <100% = underwriting profit,
  >100% = underwriting loss (must be offset by investment income). The single most watched health/general metric.
- **CISR (Combined Insurance Service Ratio)** — IFRS-17 equivalent of Combined Ratio (used by insurers
  reporting under Ind AS 117 / IFRS 17, e.g. Niva Bupa). Same interpretation.
- **Loss Ratio / Claims Ratio** = Claims Incurred ÷ Net Premium Earned. The "raw material cost" of
  insurance. Too low can mean claim denials; too high erodes profitability.
- **Expense Ratio** = Operating + acquisition costs ÷ Net Premium Earned.
- **GDPI** = Gross Direct Premium Income (general insurance revenue line, pre-reinsurance).
- Health/general insurers do NOT have an Embedded Value concept — no surrender value, no locked
  multi-decade profit stream the way life insurance does. Investment income supplements underwriting
  when Combined Ratio > 100%.

## TPA (Third Party Administrator)

- NOT an insurer — earns a service fee for processing health claims on behalf of insurers/employers.
  Zero premium income. Analysed like a services/software company: Revenue, EBITDA margin, PAT — not
  Combined Ratio or VNB.
- Key TPA metrics: Premiums Administered (the book of business it processes claims for), Market Share,
  claims processed per month, and increasingly a "platform model" fee taken on total premium flow
  rather than per-claim (a structurally different, higher-margin revenue line to flag if present).

## IRDAI Regulatory Quick Reference

| Rule | Life Insurers | Health (SAHI) / General Insurers |
|---|---|---|
| Minimum Solvency Ratio | 150% | 150% |
| Minimum Central Govt Securities | 25% of investible funds | 30% (govt securities) |
| Minimum Approved Securities | 50% | 55% |
| Maximum Equity Exposure | 15% (non-ULIP funds) | 20% |

## What to Watch, By Category (quick checklist for "verdict"/"school" style outputs)

- **Life**: Is APE growing >10%? Is VNB margin expanding? Is EV growing >15%/yr? Is RoEV >15–17%?
  Is 13th-month persistency >80%?
- **Health**: Is GWP growing >15%? Is Combined/CISR Ratio below 100%? Is the loss ratio improving YoY?
  Is solvency above 200%? Is market share growing?
- **General**: Is GDPI growing above industry average? Is Combined Ratio trending toward/below 103%?
  Is investment yield above 8%? Is ROE trending up? Is underwriting improving quarter-on-quarter?
- **TPA**: Is revenue growth healthy (>20%)? Is EBITDA margin stable/improving? Does reported PAT
  diverge materially from adjusted PAT (one-off tax credits, exceptional items)? Is market share widening?

## Source Hierarchy & Attribution

When pulling numbers (web search or otherwise), prefer sources in this order, and don't silently
blend tiers — note in the output which tier a disputed or headline figure came from if precision matters.

1. **Primary — the company itself.** BSE/NSE exchange filings, the company's own investor presentation
   or press release, and earnings-call transcripts/management commentary. This is the most authoritative
   tier and should win any conflict with a lower tier. When searching, terms like
   "\<company> investor presentation Q\<n> FY\<yy> filetype:pdf" or "\<company> BSE filing" surface this
   tier better than a generic "\<company> results" query.
2. **Named data/ratings providers**, when relevant and you can name them specifically: Prime Database or
   Moneycontrol (shareholding/ownership data), CRISIL/ICRA/CARE Ratings (credit ratings), Swiss Re or
   similar (industry-level sector statistics), IRDAI circulars/handbooks (regulatory rules and sector
   aggregates). Cite the provider by name in the output rather than presenting the number as if it were
   the company's own disclosure.
3. **Named brokerage/analyst research** — Emkay, JM Financial, Nuvama, Nomura, Motilal Oswal (MOFSL),
   HDFC Securities, Nirmal Bang, ICICI Direct, and similar. Only ever attribute a view to a *specific,
   real, named firm* you can substantiate — never invent a brokerage call or a target price. Always
   frame these as third-party views, not the skill's own recommendation (see the compliance rule below).
   A consensus-estimate aggregator (e.g. a named poll like CNBC-TV18's estimate poll) belongs in this tier too.
4. **General financial news outlets** (Reuters, Bloomberg, Business Standard, Mint, Moneycontrol news
   articles, Economic Times, etc.) — reliable for context and color, but re-verify any exact figure
   (ratios, ₹ amounts, %) against a Tier-1 source before treating it as authoritative if the number will
   drive a table cell.
5. **Aggregator/blog sites and SEO content farms** — lowest priority. Usable for a quick read, but numbers
   from this tier should be cross-checked against Tier 1 before being placed in a table. In practice,
   this tier is where transcription errors and stale/rounded figures most often creep in (e.g. a
   persistency ratio quietly copied wrong from quarter to quarter) — treat an unusual or headline number
   from this tier with real suspicion until confirmed elsewhere.

**Conflict handling**: if two sources disagree on a number, don't quietly pick one. Prefer the higher
tier (especially Tier 1, the company's own filing) as authoritative, and add a short visible note in the
output flagging the discrepancy and which source you went with and why — this is more useful to the
reader than false confidence in a single number.

**Never fabricate an attribution.** If you can't identify which specific entity said something, either
don't attribute it or say "unattributed" — a made-up source is worse than no source.

**Compliance**: never issue a buy/sell/hold recommendation in the skill's own voice. Named brokerage
views can be reported factually, clearly attributed; personal or synthesized "verdict" framing must be
presented as a research/educational read of the disclosed numbers, not investment advice.

## Style Notes for All Skills

- Always show the **YoY (or QoQ) change**, not just the absolute number — a number without direction
  is not useful to an investor.
- Never invent numbers. If the user hasn't supplied a figure and it isn't something you can look up
  reliably (search the web for the specific quarter's investor presentation / exchange filing if you
  have search access), mark it "Not disclosed this period" rather than guessing.
- This is research/education content, not investment advice. Don't issue buy/sell/hold recommendations
  in your own voice — you can report what named brokerages said, clearly attributed, but don't invent
  brokerage views either.
