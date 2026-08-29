# Sector: <NAME> (India)

> **Template.** Copy to `<sector>.md` and fill in. Keep the section numbering — the mode files delegate
> into these sections by name, so renaming or dropping one breaks that contract silently.
>
> Read `insurance.md` and `banking.md` as worked examples. They deliberately sit at opposite ends of the
> spectrum: insurance is measured on future profit and embedded value, banking on spread and asset
> quality, and both are served by the same 15 mode files without modification. If a new sector seems to
> need a mode changed, first check whether it actually needs a substitution declared here instead.
>
> Delete these quoted instruction blocks as you fill each section in.

## 1. Category taxonomy


**The Examples column must name real companies, not describe them.** "listed hospital chains"
names nobody — a reader cannot look it up and it cannot seed a peer set. Take the names from a
report, never from general knowledge. If the collection genuinely has no report on a category,
leave it and record it in `KNOWN_GAPS` in `scripts/build_coverage.py`; `verify_skill.py` fails on
an unrecorded one.
> The sub-types within this sector that are measured on genuinely different bases. Two or four is
> typical. If every company here is measured identically, say so — a single category is a legitimate
> answer and better than an invented split.

| Category | What it is |
|---|---|
| | |

> State whether cross-category comparison is meaningful. Where it isn't, say so plainly — this is what
> stops a reader ranking two companies on a metric that means different things for each.

## 2. How companies in this sector make money

> Two or three paragraphs a newcomer could follow. What is the core economic engine, and what does an
> investor actually watch? This section does most of the work in `school` and `business-profile` outputs,
> so write it for someone who has never analysed this sector.
>
> An analogy table helps where the sector's metrics are unintuitive (insurance uses a manufacturing
> analogy). Skip it where metrics are self-explanatory — a forced analogy teaches worse than none.

### The analogy

One paragraph anchoring this sector to something a reader already understands, and stating the
consequence for how it is measured. **The single most useful teaching device in the file** — `school`
leads with it. Avoid a generic simile; the analogy has to earn its place by explaining why the
sector's headline metric is what it is.

## 3. Metric definitions

> Every metric this sector's reports use, defined in plain English with its formula. Say what the metric
> is *for*, not just what it computes — a reader who knows the formula but not the purpose can't
> interpret the number.
>
> Flag any metric that is commonly misread, and any that does **not** apply here (insurance has no
> EBITDA; health insurers have no embedded value). Those absences matter as much as the definitions.

## 4. Benchmarks — what good looks like

| Metric | Healthy |
|---|---|
| | |

> Ground these in real disclosed figures from this sector's companies rather than generic rules of
> thumb. Where the *trend* matters more than the level, say so — several sectors are like this and a
> static threshold misleads.
>
> **Give margin benchmarks per category, never one band for the whole sector.** This is the most common
> defect in a sector file, and it was found in two of the first ten. A single "sector norm" makes a
> structurally thin business look broken and a structurally rich one look excellent, when both are
> performing normally for what they are. `capital-goods.md` originally quoted one EMS band of 4–8%; real
> data ranged from 3% (box-build assembly) to 15.6% (industrial and semiconductor) — the band described
> one sub-category and was applied to all of them.
>
> The test: **if two companies in this sector could both be performing well while their margins differ by
> more than a few points, the benchmark must be split** — and §1's taxonomy probably needs splitting too,
> since a single benchmark across a heterogeneous category usually means the category itself is too
> coarse.

**What to watch, by category:**

> Four or five yes/no questions per category. Feeds `verdict`, `swot` and `school`.

### What goes wrong, and the tell

The sector's characteristic failure mode, and the **early signals in order of when they appear**. A
reader who knows the metrics but not the failure mode can recite the numbers without judging them.
State the tell as something observable in a disclosure, not as a sentiment.

## 5. Regulatory quick reference

| Requirement | Level |
|---|---|
| | |

> Name the regulator(s). Include only rules that actually move the analysis. Add a line reminding the
> reader to verify current levels rather than carrying a figure forward — regulatory thresholds change.
> Omit this section entirely for lightly-regulated sectors rather than padding it.

## 6. Per-mode specifics

> These are the delegation targets the mode files reach into. Each must exist for that mode to work
> properly in this sector.

### Headline KPIs by category (`dashboard`)

| Category | KPIs |
|---|---|
| | |

### Table columns by category (`financials`)

> The column set per category, plus any secondary tables this sector needs (banking needs an
> asset-quality movement table; a capital-intensive sector may need debt and cash flow).

### Chart reference lines (`charts`)

| Metric | Line | Label |
|---|---|---|
| | | |

> Thresholds with real meaning — a regulatory minimum, a breakeven, an industry norm. Every line needs a
> label saying what it represents. Where no meaningful threshold exists, say so rather than inventing
> one; a peer median labelled as such is an honest alternative.

### Profile coverage by category (`business-profile`)

> What a profile must cover for each category to be genuinely informative here.

### Moat candidates by category (`moats`)

> Where durable advantage actually comes from in this sector, and what evidence substantiates each.
> Include a note on which claimed moats are usually weak here — every sector has a fashionable
> non-moat, and naming it protects the analysis.

### Valuation (`valuation`)

> The primary multiple investors in this sector actually use, and why. Secondary multiples. Explicitly
> name any multiple that must **not** be used and the reason.

### CB Rating substitutions (`cb-rating`)

| Component | Weight | Substitution |
|---|---|---|
| Growth | 30% | |
| Profitability | 25% | |
| PAT Quality | 25% | |
| Forward Outlook | 20% | |

> **Must total 100%.** Substitute only where the generic component is genuinely meaningless or misleading
> here; keep the core weights otherwise. Financial sectors must never use Debt/Leverage, since borrowing
> is the business model rather than a risk.
>
> **The four rows above are the default, not a limit.** A sector may split or add a component where the
> economics demand it, provided the total is still 100%. Worked precedents already in the repo:
> - `banking.md` — Asset Quality replaces PAT Quality (for a bank, asset quality *is* profit quality)
> - `insurance.md` — capital adequacy replaces Forward Outlook (solvency is the binding growth constraint)
> - `pharma-health.md` — Regulatory & Outlook replaces Forward Outlook (a USFDA import alert can remove a
>   site's revenue outright, so regulatory standing *is* the outlook)
> - `power-energy.md` — **five components**: PAT Quality drops to 15%, an explicit Debt & Cash Flow
>   component takes 20%, Outlook 10%. An IPP at 5× net debt/EBITDA is normal infrastructure gearing, and
>   scoring it against a manufacturing threshold would be wrong
> - `capital-goods.md` — order inflow and book-to-bill substitute into Growth; cash conversion and debtor
>   days into PAT Quality

### Extra sections (`quarterly-report`)

> Sections specific to this sector that carry real analytical weight — insurance has Investments &
> Returns; capital-intensive sectors have Debt & Cash Flow; export sectors have Exports & JVs; cement
> has Geographic Mix. Name each and say what it contains.

### Event transmission map (`event-impact`, `risks-outlook`)

| Event | Reaches results via | Exposure basis to cite |
|---|---|---|
| | | |

> The recurring policy and market events for this sector, the mechanism by which each reaches results,
> and the specific disclosure that quantifies a company's exposure. This is the only genuinely
> sector-specific step in event analysis, so it carries real weight — the mode supplies the method and
> depends on this table for the mechanism.

## 7. Where to look (sourcing)

**Tier 1** —

> The Tier-1 route for this sector and the search phrasing that surfaces it. Note anything this
> sector's companies disclose unusually well or unusually poorly.

**Tier 2 — sector authorities**:

> The regulator and data bodies specific to this sector, named. Note where an authority publishes
> industry aggregates that give the right benchmark for market-share judgements.

## 8. Company colour palette

**The companies named here are illustrative as at authoring, not the current universe.** Anything listed since belongs in the analysis too — see "Establish the universe before ranking anything" in `source-hierarchy.md`.

| Company | Main | Soft tint |
|---|---|---|
| | | |

> Visually distinct hues, each with a ~10% soft tint. Add new companies here as they appear so the next
> report reuses the same colour rather than re-rolling.

## 9. Sector-specific CSS

```css
/* category tags and any classes only this sector needs */
```

> Only classes genuinely specific to this sector. Anything used across sectors belongs in
> `design-system.md` instead — check there first before adding here.

## 10. Mode applicability

> Which of the 15 modes apply, any that should be skipped, any renames (cement uses "Cement School").
>
> **Always end with the cross-sector note**: which universal metrics (Revenue, EBITDA%, PAT, growth,
> Mkt Cap, P/E, EV/EBITDA, Net Debt) do **not** apply to this sector, so a cross-sector table renders
> "n/a — not comparable for this sector" instead of a misleading figure. This is the single most
> important line in the file for preventing silent misrepresentation.
