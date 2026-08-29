---
name: sector-financial-analysis
description: 'Builds research-grade HTML for Indian listed companies across sectors: KPI dashboards, financial tables, charts, business profiles, segment breakdowns, valuation multiples, SWOT, moats, risks & outlook, brokerage ratings, CB scores and rankers, metric explainers, full quarterly reports, and policy-event or corporate-action impact analysis. Use whenever the user names an Indian company or sector and wants a dashboard, snapshot, "the numbers", results, financials, a chart, how a company makes money, its business model, segments, valuation, a SWOT, its moat, risks or outlook, analyst views, a CB score or ranking, a verdict or "which is better", sector jargon explained (VNB, NIM, GNPA, TCV, ARPU), or a full report — also when a tariff, demerger or buyback needs impact assessed. Trigger on implicit asks like "how did SBI do". Covers all 18 sectors: banking, NBFC, insurance, capital markets, IT, pharma, auto, consumer, capital goods, power, metals, cement, chemicals, realty, REITs, logistics, telecom, new-age.'
---

# Sector Financial Analysis

Produces research artifacts on Indian listed companies. One skill covering every sector, because the
*craft* of building a SWOT or a KPI dashboard is the same everywhere — only the metrics change.

Route every request through four questions: **what depth**, **which sector(s)**, **which mode**, **what
scope**. Then load only the files those answers point to.

---

## Step 0 — Detect the depth: conversation or artifact?

Decide this **first**, because it changes how much work the rest of the request needs.

**Answer in chat — no file — when the person is asking a question.** Concept questions ("what is NII?",
"what's the difference between GNPA and NNPA?", "why do insurers use VNB instead of profit?"), a single
figure ("what was HDFC Life's VNB margin?"), a quick read ("how did SBI do?"), or anything exploratory.
This is the **default**. Apply the same sourcing discipline — real figures, real attribution, no
fabrication — just deliver it as prose.

**Build the artifact when the person wants something to keep, share, publish or return to.** Signals:
"build", "generate", "create a report/dashboard", "compare X and Y" at length, "I want to send this to
someone", or an explicit request for a file.

When genuinely ambiguous, **answer in chat first and offer the artifact**. That costs the reader one
sentence; the reverse — burying a one-line answer inside a generated HTML file they have to open — wastes
their time and hides the answer.

**A "full report" is the most expensive thing this skill does.** `quarterly-report` composes a dozen
sections, each needing its own live sourcing, and takes many minutes. Before building one, **state the
sections you are about to build and confirm** — one line, e.g. *"Full report = dashboard, financials,
charts, business profile, segments, valuation, SWOT, moats, risks, analyst views, verdict, CB rating.
Build all, or a subset?"* Skip the confirmation only if the person already named the sections.

**Prefer the smallest artifact that answers the question.** A `dashboard` is a fraction of the cost of a
full report and is usually what "how did X do" actually wants. Offer to add sections rather than
building every section by default.

**Either way — chat or artifact — check the published collection first.** If a published report already
covers the company, sector or comparison being asked about, it is the author's own verified work and it
outranks anything you would compose from the sector file alone. **Lead with what that report says, cite
it by name, and give the reader its link.** Then add what it does not cover. See
`references/output-conventions.md` for where the collection lives.

This matters most for the questions that feel purely conceptual — "what's the difference between X and
Y", "how does this sector work". Those are exactly the questions a published explainer already answers,
and answering them from the sector file alone silently discards the author's work and can contradict it.

Honour explicit overrides in either direction: "just tell me", "no file", "don't build anything" means
chat; "give me a report on this" means build it.

A learning session is a conversation. Someone working through what a sector's metrics mean should be
able to ask twenty questions without generating twenty files — use `school`'s teaching material to
answer inline, and build the reference artifact only if they ask for something to keep.

## Step 1 — Detect the sector

Identify each company's sector and load `references/sectors/<sector>.md`.

| Sector | Recognise by |
|---|---|
| `insurance` | LIC, ICICI Prudential Life, HDFC Life, SBI Life, Axis Max Life, Star Health, Niva Bupa, ICICI Lombard, Medi Assist; VNB, Combined Ratio, solvency, premium |
| `banking` | SBI, HDFC Bank, ICICI Bank, Axis, Kotak, BoB, PNB, Canara, IndusInd, AU SFB; NIM, GNPA, CASA, advances, deposits |
| `consumer` | DMart, V2 Retail, Aditya Birla Fashion, Page, United Spirits, Radico, United Breweries, Sula, IHCL, EIH, Chalet, Lemon Tree, KPR Mill, sugar and dairy names; SSSG, footfall, RevPAR, occupancy, cane crush, yarn |
| `capital-goods` | BHEL, HAL, RVNL, IRFC, Dixon, Kaynes, Syrma, Amber, Polycab, MTAR, INOX India, Shakti Pumps, ABB, Siemens Energy, Hitachi Energy, CG Power, Voltamp; order book, book-to-bill, execution, EMS, defence, railways |
| `power-energy` | Adani Power, Tata Power, JSW Energy, NTPC, ACME Solar, Emmvee, ONGC, Reliance, IOC/BPCL/HPCL, IEX, Coal India; PLF, PPA, merchant tariff, ALMM, cell/module, GRM, crude, e-auction vs FSA |
| `pharma-health` | Sun Pharma, Dr Reddy's, Cipla, Lupin, Divi's, Aurobindo, Zydus, Torrent, Mankind, Alkem, Laurus, Gland, Sai Life, hospitals and diagnostics; USFDA, ANDA, Para IV, ARPOB, occupancy |
| `nbfc-hfc` | Bajaj Finance, Shriram, Muthoot, Cholamandalam, LIC Housing, PNB Housing, Can Fin, Aavas, Aadhar, Home First, PFC, REC, IREDA, Jio Financial, CreditAccess Grameen, Spandana; AUM, GLP, PAR 30, collection efficiency, cost of funds, spread, disbursements. **Not banking** — no CASA, borrowing-funded |
| `capital-markets` | BSE, MCX, CDSL, NSDL, CAMS, KFintech, Angel One, Groww, HDFC/ICICI Pru/SBI/UTI/ABSL AMC, mutual funds; QAAUM, SIP, demat accounts, ADTO, take rate, TER |
| `it-services` | TCS, Infosys, HCLTech, Wipro, Tech Mahindra, LTIMindtree, Persistent, Coforge, Mphasis, InfoEdge, Fractal; TCV, utilisation, attrition, constant currency, BFSI mix |
| `auto` | Hero, Bajaj Auto, TVS, Eicher, Ather, Maruti, M&M, Tata Motors, Uno Minda, Endurance, Craftsman, Pricol, Lumax, Belrise, Exide, Amara Raja, tyres; volumes, realisation, OEM vs replacement, EV penetration |
| `metals` | Tata Steel, JSW Steel, SAIL, Jindal, Shyam Metallics, Hindalco, NALCO, Vedanta, Hindustan Zinc; EBITDA/tonne, captive ore & coal, LME, realisation |
| `cement` | UltraTech, Ambuja, ACC, Shree, Ramco, JSW Cement, Dalmia, JK Cement; EBITDA/tonne, clinker vs grinding, lead distance, pet coke, regional mix |
| `chemicals` | SRF, Aarti, Deepak Nitrite, Vinati, Balaji Amines, Alkyl Amines, Galaxy, Finolex, Supreme, Astral, Asian Paints, Berger, Coromandel, Chambal, plastic and metal recyclers; specialty vs commodity vs fertiliser vs pipes vs paints vs recycling (EPR, scrap spread) |
| `infra-realty` | DLF, Prestige, Oberoi Realty, Sobha, Brigade, Godrej Properties, Anant Raj, Adani Ports, JSW Infrastructure, Gujarat Pipavav; pre-sales, collections, launches, cargo, concession tenure |
| `reit-invit` | Embassy, Mindspace, Brookfield India, Nexus Select, IndiGrid, PowerGrid InvIT, IRB InvIT, Cube Highways; DPU, distribution yield, NDCF, LTV, availability. **An asset class, not an industry** — a trust, not an operating company. Load the underlying asset's sector file too if its drivers matter |
| `logistics` | Shadowfax, Delhivery, Blue Dart, VRL Logistics, TCI Express, Container Corporation; orders/shipments, revenue per shipment, pincodes, density, **asset-light vs asset-heavy** — the two are not comparable on margin |
| `telecom` | Bharti Airtel, Vodafone Idea, Indus Towers, Tata Communications, Bharti Hexacom; ARPU, subscribers, churn, spectrum and AGR dues |
| `new-age` | Eternal (Zomato/Blinkit), Swiggy, Meesho, Nykaa, Urban Company; GOV/NOV, AOV, take rate, contribution margin, dark stores, cash runway. **Pre-profit platforms — not judged on PAT** |

Sectors not yet built have no file. **If a request names a company from an unbuilt sector, say so
plainly** — offer to work from general principles without sector-specific benchmarks, or to add that
sector file. Don't silently substitute another sector's metrics; that is how a bank ends up scored on
insurance benchmarks.

If the sector genuinely can't be identified, **ask — don't guess.**

**Multiple sectors**: load every relevant sector file. Cross-sector work is supported but constrained —
see Step 3.

## Step 2 — Detect the mode

Load `references/modes/<mode>.md`.

| Mode | Triggers on |
|---|---|
| `dashboard` | dashboard, snapshot, overview, at a glance, "the numbers", how did X do |
| `financials` | financials, results, P&L, detailed numbers, line items, breakdown |
| `charts` | chart, graph, plot, visualise, trend, show me visually |
| `business-profile` | business model, how do they make money, products, distribution, tell me about, management, governance |
| `segments` | segments, product mix, revenue split, by geography, business lines |
| `valuation` | valuation, multiples, P/E, P/B, EV/EBITDA, expensive, cheap, what's it worth |
| `swot` | SWOT, strengths and weaknesses, pros and cons, bull and bear case |
| `moats` | moat, competitive advantage, USP, why is it hard to compete with, durability |
| `risks-outlook` | risks, outlook, guidance, what could go wrong, headwinds |
| `analyst-ratings` | analyst views, brokerage, target price, ratings, what do analysts say |
| `verdict` | which is better, who wins, verdict, scorecard, ranking, best in sector |
| `cb-rating` | CB score, CB rating, ranker, rank these companies |
| `school` | what is <metric>, explain, teach me, I'm new to this, how do I read this |
| `quarterly-report` | full report, complete dashboard, everything on Q<n>, the whole picture |
| `event-impact` | a tariff/duty/circular/policy change, demerger, merger, buyback, stake sale — and its effect on named companies |

**Several modes at once** is normal — "compare X and Y with charts and a verdict" loads three. When the
request is broadly "everything", use `quarterly-report`, which composes the rest.

**Not this skill**: market-news digests and headline roundups. `event-impact` requires an event tied to
*named companies with a stated exposure basis*; "what happened in the market this week" is journalism,
not company evaluation.

## Step 3 — Detect the scope

| Scope | Behaviour |
|---|---|
| **Single company** | No peer comparison unless asked. Go deeper instead of wider. |
| **Pair** | Parallel structure throughout so the two read across cleanly. |
| **Sector sweep** | Group by the sector file's categories; add cross-company summaries. |
| **Cross-sector** | Constrained — see below. |

### Cross-sector guardrails

Comparing across sectors is supported but is where analysis most easily goes wrong, because the same
word means different things in different industries.

- **Comparison tables use only universal metrics** — Revenue, EBITDA%, PAT, growth %, Mkt Cap, P/E,
  EV/EBITDA, Net Debt.
- **Sector-specific metrics stay quarantined** in their own per-sector section. VNB never appears in a
  column beside EV/EBITDA.
- **Every cross-sector table carries a `Sector` column.**
- **Where a sector genuinely lacks a universal metric, say so.** Banks and insurers have no meaningful
  EBITDA, and borrowings are their raw material rather than leverage. Those cells read
  **"n/a — not comparable for this sector"** — never a blank, and never a number borrowed from a
  different concept. A figure that looks comparable but isn't does more damage than an honest gap.
- Single-sector is the default. Go cross-sector only when the request genuinely spans sectors.

## Step 4 — Answer or build

**First, check whether a report already exists.** Before analysing any company or sector, look for prior
coverage in the published collection — see `references/output-conventions.md`. An existing report may
already answer the request, and because published reports are author-verified, one covering the same
period is a cross-check on your figures that no external source provides.


If Step 0 said **conversation**, answer in chat now. Read the sector file for the facts and, for teaching
questions, `modes/school.md` for how to explain them — then stop. Don't write a file, and don't pad a
two-sentence answer into an essay to justify having loaded a reference.

If Step 0 said **artifact**, continue. Always in play, whatever the mode:

- **`references/design-system.md`** — all HTML, CSS and Chart.js patterns. Read before writing markup.
- **`references/source-hierarchy.md`** — where numbers may come from, how to attribute them, and the
  compliance rules. Read before sourcing anything.
- **`references/output-conventions.md`** — where the artifact goes and how it's delivered. The only
  file naming paths or tools.

Then follow the loaded mode file, taking every metric, benchmark, threshold and category from the loaded
sector file.

## Non-negotiables

These come from `source-hierarchy.md` and apply to every mode. They exist because these artifacts are
dense with numbers that a reader has no independent way to check.

- **Never fabricate a figure.** Unavailable data is marked "Not disclosed", not estimated. A report with
  honest gaps is worth more than one with confident inventions.
- **Never invent an attribution** — no imagined brokerage, rating, target price or quote. If no real
  named view can be sourced, omit the section.
- **Never issue buy/sell/hold in this skill's own voice.** Report real named brokerage views as theirs;
  frame any verdict as a research read of disclosed fundamentals.
- **Prefer company filings over aggregators**, and where sources conflict, flag the discrepancy visibly
  rather than silently picking one.
- **Every artifact carries** an explicit `Source:` line with dates, the data as-of date, and the
  research/educational disclaimer.
- **Attach the caveat.** Where a figure carries a one-off, a basis change, or a restatement, footnote it.
  This is the most-skipped element and the one most likely to mislead a trusting reader.
- **Output is a draft until a human says otherwise.** Everything this skill generates goes to the staging
  location in `output-conventions.md`, never into the published collection. Promotion is the author's
  decision after verifying the figures — the skill never makes it.

## Regenerating an existing report

When updating a report for a new period, read the prior artifact for **company scope, section selection,
layout, chart types and custom sections** — then re-source every number. Inherit the structure; never
inherit the figures. A ratio carried forward from a previous artifact is exactly how a stale number
survives unnoticed across quarters.

## Adding a sector

Copy `references/sectors/_template.md` to `references/sectors/<sector>.md` and fill it in — that is the
whole job. **No mode file should need editing.** If a new sector seems to require changing a mode, it
almost certainly needs a substitution declared in its own sector file instead; `insurance.md` and
`banking.md` sit at opposite ends of the metric spectrum and both run on the unmodified modes.

Then add a row to the Step 1 table above.
