# Architecture Decisions

Why this repo is shaped the way it is. Each record covers one decision: the situation that forced it,
what was chosen, and what it costs.

Read before reversing something that looks arbitrary — several of these are counterintuitive and were
made against specific evidence from the 98-report corpus.

## Index

| # | Decision |
|---|---|
| [0001](#0001-consolidate-nine-insurance-skills-into-one-multi-sector-skill) | Consolidate nine insurance skills into one multi-sector skill |
| [0002](#0002-mode-files-own-the-craft-sector-files-own-the-domain) | Mode files own the craft; sector files own the domain |
| [0003](#0003-derive-the-mode-set-from-the-report-corpus-not-from-the-nine-insurance-skills) | Derive the mode set from the report corpus, not from the nine insurance skills |
| [0004](#0004-support-cross-sector-comparison-constrained-to-universal-metrics) | Support cross-sector comparison, constrained to universal metrics |
| [0005](#0005-unify-cb-rating-on-one-core-method-with-per-sector-substitutions) | Unify CB Rating on one core method with per-sector substitutions |
| [0006](#0006-generated-reports-go-to-staging-promotion-is-a-human-action) | Generated reports go to staging; promotion is a human action |
| [0007](#0007-conversation-is-the-default-output-artifacts-are-the-exception) | Conversation is the default output; artifacts are the exception |
| [0008](#0008-exclude-news-digests-keep-policy-and-corporate-action-analysis) | Exclude news digests; keep policy and corporate-action analysis |
| [0009](#0009-confine-paths-and-tool-names-to-a-single-file) | Confine paths and tool names to a single file |
| [0010](#0010-inherit-structure-from-prior-reports-never-inherit-figures) | Inherit structure from prior reports; never inherit figures |
| [0011](#0011-install-the-skill-by-symlink-treat-the-packaged-skill-as-a-build-artifact) | Install the skill by symlink; treat the packaged `.skill` as a build artifact |

**The four that matter most.** ADR-0002 is the contract that makes the skill multi-sector — break it and
nothing visibly fails, the abstraction just quietly dies. ADR-0006 is the rule with real-world
consequences: generated analysis reaching subscribers unverified is the failure this repo exists to
prevent. ADR-0004 prevents the most likely silent misrepresentation — an insurer or bank shown in an
EBITDA column where the metric does not exist. ADR-0010 is why the skill never copies a number from a
previous report, however convenient that would be.

**Adding one**: keep the structure — Status, Context (with evidence), Decision (including what was
rejected), Consequences (*including the costs*). A record listing only benefits is unfinished; the value
is that a future reader can tell whether the trade-off still holds. Records are immutable once accepted —
to change a decision, add a new one and mark the old `Superseded by ADR-NNNN`.

---
## 0001. Consolidate nine insurance skills into one multi-sector skill

**Status**: Accepted · 2026-08-09

### Context

Nine separate Claude skills existed for Indian insurance analysis — dashboard, financials, charts,
business profile, SWOT, moats, verdict, school, and a composite quarterly report. Each carried its own
`SKILL.md` plus a `references/` folder containing two files: `design-system.md` and
`metrics-glossary.md`.

Those two files were **byte-identical across all nine folders** (verified by md5). Eighteen copies of two
files.

The plan was to extend the same treatment to other sectors — banking, pharma, and more. That does not
scale on two axes:

- **Metadata cost.** A skill's name and description sit in context permanently, used or not. Nine skills
  × N sectors is a lot of always-loaded text for work that is mostly not happening.
- **Trigger collision.** "Give me a SWOT" would have to disambiguate between `insurance-swot-analysis`,
  `banking-swot-analysis`, `pharma-swot-analysis` and so on. Every new sector makes every existing
  trigger less precise.

At three sectors this becomes 27 skills.

### Decision

**One skill, `sector-financial-analysis`, covering every sector.** Sectors are reference files inside it,
not separate skills. The skill count is one today and stays one after thirteen more sectors are added.

A two-skill split was considered — a light "toolkit" for single-slice queries plus a separate "full
report" skill for the heavy composite. Rejected: it doubles the always-loaded metadata per sector, which
is precisely the cost being removed, in order to solve a mode-disambiguation problem the router resolves
with one table lookup. The composite report's weight is a loaded-on-demand concern, not a metadata one.

### Consequences

- Adding a sector means writing one file. No new skill, no new description competing for triggers.
- Per request, roughly two reference files load: one sector, one mode. Cost is independent of how many
  sectors exist.
- The router must correctly detect sector and mode. That routing logic is now a single point of failure
  where previously the skill-selection mechanism handled it — mitigated by keeping the router small
  (~166 lines) and explicit.
- One description must carry the trigger phrases of all fifteen modes. It is necessarily long, and had
  to be compressed to fit the 1024-character limit (see the description in `SKILL.md`).
- Eighteen duplicate reference files were deleted, replaced by one copy each.

---

## 0002. Mode files own the craft; sector files own the domain

**Status**: Accepted · 2026-08-09

### Context

Having decided on one skill for all sectors (ADR-0001), the question became
how to divide its content so that adding a sector stays cheap.

The naive split — one folder per sector, each containing its own dashboard/SWOT/charts instructions —
reproduces the original duplication problem inside a single skill. Fifteen sectors × fifteen modes is 225
files, most of them near-identical.

An audit of the 98 existing reports showed why a better split exists: **the structure of these artifacts
is the same across sectors, and only the metric names differ.** The KPI strip is company×metric cards
whether the report is about insurance (`LIC FY26 PAT`), cement (`UltraTech Q4 Revenue`) or hotels
(`IHCL Q4 PAT`). SWOT markup is identical in pharma, cement and banking reports. Shared CSS classes
appear across the corpus at high rates — `card` 84%, `kpi` 75%, `panel` 65%, `badge` 61%.

### Decision

Split by **craft vs domain**, not by sector:

- **`references/modes/*.md` own the craft.** How to lay out a SWOT grid, what distinguishes a moat from
  a strength, when a table needs a footnote, where a chart reference line goes. These files must name
  **zero** sector-specific metrics.
- **`references/sectors/*.md` own the domain.** Category taxonomy, metric definitions, benchmarks,
  colour palette, regulator rules, and a per-mode specifics section that the mode files delegate into.

Concretely: `modes/dashboard.md` says "show the headline KPIs for this company's category, per the sector
file's *Headline KPIs by category* table." `insurance.md` supplies Life → PAT/VNB/VNB Margin/APE/Solvency.
`banking.md` supplies NII/NIM/GNPA/CASA/CRAR.

Each sector file must provide nine delegation targets: headline KPIs, table columns, chart reference
lines, profile coverage, moat candidates, valuation multiple, CB Rating substitutions, extra sections,
and an event transmission map.

### Consequences

- **Adding a sector is a one-file job.** Insurance and banking were built deliberately as opposite ends
  of the metric spectrum — VNB and Combined Ratio share nothing with NIM and GNPA — and both are served
  by the fifteen mode files *without modification*. That is the evidence the abstraction holds.
- The contract is invisible when broken. Putting `VNB` into `modes/swot.md` breaks nothing today; it
  quietly kills the abstraction, and every future sector inherits insurance's vocabulary. This is
  enforced by a grep in the validation suite and stated in `AGENTS.md`.
- Mode files must be written more abstractly than a single-sector skill would need, which makes them
  slightly harder to read in isolation.
- A sector needing something genuinely new must declare it as an *extra section* or a *substitution* in
  its own file rather than editing a mode. If a mode edit seems necessary, that is a signal the sector
  file is incomplete.

---

## 0003. Derive the mode set from the report corpus, not from the nine insurance skills

**Status**: Accepted · 2026-08-09

### Context

The obvious way to build the consolidated skill was to convert each of the nine insurance skills into one
mode file — a mechanical one-to-one migration.

Before doing that, the 98 reports in `reports/published/` were audited to check whether those nine
actually covered the work. They did not. Insurance is only 3 of 98 reports; normalising on it would have
encoded one small sector's habits as the shape of everything.

Of the 68 multi-tab reports, the nine insurance modes did recur strongly — Dashboard 100%, Charts 89%,
Analyst 70%, SWOT 58%, Financials 55%, Business Profile 50%, Moats 44%, Verdict 44%, School 42%. The
abstraction was sound. But several recurring report sections had no corresponding mode.

### Decision

Six modes were added beyond the insurance nine, each justified by frequency in the corpus:

| Mode | Reports | Why insurance missed it |
|---|---|---|
| `valuation` | 35 | Insurance hides valuation as one column inside Verdict, because P/EV is its only meaningful multiple. Most sectors give it a full tab — it appears in **more reports than Moats (30) or Verdict (30)**. |
| `analyst-ratings` | 47 | Its own discipline: only real, named, substantiable firms. Was a tab inside the insurance composite, never a standalone concern. |
| `segments` | 24 | Insurance folds this into business-profile as "product mix". Most sectors need a standalone revenue-by-segment/geography cut. |
| `risks-outlook` | 24 | Distinct from SWOT's Threats quadrant — that is structural, this is live and near-term. |
| `cb-rating` | 15 | The house scoring framework. See ADR-0005. |
| `event-impact` | 77 | Policy and corporate-action analysis. See ADR-0008. |

Two candidates were rejected: *Peer Comparison* (9 reports) folds into `verdict`/`dashboard`, which
already compare across companies; *Management/Governance* (3) folds into `business-profile`.

Final count: **fifteen modes**.

### Consequences

- The mode set reflects fifteen sectors' worth of practice rather than one sector's. Normalising on
  insurance would have deleted a top-five mode (`valuation`) outright.
- Three other corpus findings were folded in at the same time: **layout is a separate axis** from mode
  (27 reports are single-page scroll, 46 tabbed — both are now first-class); the **AI assist panel** is
  the house default rather than an exception (85 of 98 reports carry it, against the insurance skill's
  instruction to add it "only if the user specifically wants" it); and ten CSS classes the skills
  referenced were never defined anywhere, so every run improvised them.
- More modes means a longer skill description and more surface area to keep sector-free.
- The audit is recorded in [ROADMAP.md](../ROADMAP.md) so it need not be re-derived.

---

## 0004. Support cross-sector comparison, constrained to universal metrics

**Status**: Accepted · 2026-08-09

### Context

Five of the 98 reports compare companies across sectors — `CB_Company_Ranker`, `CB_Sector_Ranker`,
`MultiSector_Dashboard`, `CB_MultiCo_Dashboard`, `Cross_Sector_IEX_IndiGo_Fractal_Airtel`.

The concern raised was that cross-sector comparison is inherently confusing and might be better dropped.
That concern is well-founded but aims at the wrong target. Inspecting those five reports showed they were
**already disciplined**: comparison tables use only universal metrics (Revenue, EBITDA%, PAT, growth,
Mkt Cap, P/E), and `Cross_Sector_IEX_IndiGo_Fractal_Airtel` quarantines incomparable metrics into a
separate "Sector Metrics" tab.

The real hazard is narrower and sharper: **insurers and banks have no meaningful EBITDA**, and a bank's
"Revenue" is a spread, not sales. Drop an insurer into a `Q4 EBITDA %` column and it either shows blank
or — worse — a number that looks comparable and is not.

### Decision

Keep cross-sector comparison, with four rules that make the existing convention explicit rather than
rediscovered per report:

1. **Comparison tables use only universal metrics** — Revenue, EBITDA%, PAT, growth %, Mkt Cap, P/E,
   EV/EBITDA, Net Debt.
2. **Sector-specific metrics are quarantined** to their own per-sector section. VNB never appears in a
   column beside EV/EBITDA.
3. **A sector lacking a universal metric says so.** The cell reads **"n/a — not comparable for this
   sector"** — never a blank, never a borrowed number.
4. **Every cross-sector table carries a `Sector` column**, so a reader always knows which band a row is in.

Valuation is expressed as a position within the company's *own* sector band, not as a raw cross-sector
ranking — a 15× P/E means different things in IT and cement.

Single-sector remains the default. Cross-sector applies only when the request genuinely spans sectors.

### Consequences

- The five existing cross-sector report types remain reproducible.
- The specific failure mode — an insurer silently misrepresented in an EBITDA column — is addressed
  directly rather than by avoiding the whole capability.
- Every sector file must declare, in its §10 cross-sector note, which universal metrics do *not* apply to
  it. This is the single most important line in a sector file for preventing silent misrepresentation,
  and it is easy to forget when writing one.
- Cross-sector output is deliberately less rich than single-sector output. That is the correct trade:
  the metrics that would make it richer are the ones that are not comparable.

---

## 0005. Unify CB Rating on one core method with per-sector substitutions

**Status**: Accepted · 2026-08-09

### Context

"CB Rating" / "CB Score" appears in 15 places across the corpus, with bands (`≥75 🟢 / 55–74 🟡 /
<55 🔴`), a group taxonomy (Manufacturing / Finance / Consumption / Infra / Energy), and an interactive
ranker with sort controls.

The question was whether the skill could compute these. Investigation found it could not, because the
corpus documents **four incompatible methods**:

| Source | Scale | Parameters |
|---|---|---|
| `CB_Company_Ranker` | 0–100 | Rev Growth 30% · EBITDA Margin 25% · PAT Quality 25% · FY27 Outlook 20% |
| `Q1FY27_adani_power_utilities` | 1–10 weighted | Rev 20% · EBITDA 25% · Net Profit 25% · Debt/Leverage 15% · Cash Flow 15% |
| `CB_Sector_Ranker` | 1–5 | 9 qualitative parameters including Seasonality |
| pharma dashboards | composite | company layer + Volume 8% + Sentiment 7% "live-market layers" |

Scores are hardcoded per report (`{name:'HAL', rev:7595, cb:72, sig:'Selective'}`), computed by the
author and written in. There was no single formula to inherit.

A rigid single formula was also not viable: Debt/Leverage and Cash Flow are meaningless for a bank or
insurer, where borrowing *is* the business model.

### Decision

**One canonical core, with per-sector substitutions.**

Core weights, on a 0–100 scale, taken from `CB_Company_Ranker` as the most formalised version:

| Component | Weight |
|---|---|
| Revenue Growth | 30% |
| Profitability | 25% |
| PAT Quality | 25% |
| Forward Outlook | 20% |

Each sector file declares its own substitution table, which must total 100%. Capital-intensive sectors
substitute part of Profitability for Debt/Leverage and Cash Flow (the Adani variant). **Financial sectors
never use Debt/Leverage** — banking substitutes Asset Quality for PAT Quality, since for a bank asset
quality *is* profit quality; insurance substitutes capital adequacy, since solvency is the binding
constraint on growth.

Any rendered score must state the parameter set used.

### Consequences

- Scores become comparable across reports and quarters, which a proprietary rating requires to mean
  anything. Four methods on three different scales made cross-report comparison meaningless.
- Both existing formulas are preserved rather than one being discarded.
- Every new sector file must supply a substitution table, and a validation check confirms it totals 100%.
- Scores computed under the new method will not match historically published scores. Those were computed
  by hand under whichever variant applied at the time.
- The banking presentation retains its established name, **"CB Earnings-Quality Rating"**, which carries
  meaning: how much of reported profit is core and repeatable versus provision release or one-offs.

---

## 0006. Generated reports go to staging; promotion is a human action

**Status**: Accepted · 2026-08-09

### Context

The first report generated by the skill was written directly into the published collection. That was
wrong, and the correction became a structural rule rather than a preference.

`reports/published/` is a local mirror of <https://elangocauvery.github.io/CB-Finance/> — reports that
have been verified and are shown to subscribers. Generated analysis is not that, however finished it
looks.

The specific risk: these reports are dense with figures that a reader has no independent way to check,
and they go to subscribers who will not check them. Generated output looks finished before it is.

### Decision

**Two-stage pipeline with a human gate:**

```
skill generates  →  reports/staging/  →  author verifies  →  reports/published/
```

The skill **never writes to `reports/published/` and never moves a file into it**, even when asked to
"publish" or "finalise". Asked to publish, it states the `mv` command and lets the author run it.

`reports/staging/` is tracked in git rather than ignored, so draft history is visible.

This is stated in three places because it is the rule most costly to break: the router's non-negotiables,
`output-conventions.md`, and `AGENTS.md`.

### Consequences

- Verification is structural rather than a matter of discipline. Skipping it requires a deliberate `mv`.
- Both staged reports demonstrate why the gate exists. The private banks comparison is missing slippage
  ratio and credit cost for all five banks; the life insurance verdict's P/EV multiples come from a
  single low-tier source and drive the scorecard's Valuation lens. Neither should reach a subscriber
  unverified.
- An extra manual step before publishing.
- A `PreToolUse` hook enforcing this mechanically was considered and declined for now. Without it, the
  rule is documented rather than enforced — `git status` before committing is the backstop.

---

## 0007. Conversation is the default output; artifacts are the exception

**Status**: Accepted · 2026-08-09

### Context

The skill was built around producing HTML artifacts, because that is what the 98 reports are. But a large
part of its intended use is learning — asking "what is NII?", "what's the difference between GNPA and
NNPA?", "how did SBI do?" — where a generated file is the wrong answer.

The rule to answer conversationally did exist, but only in `output-conventions.md`, which loads *last*,
and in per-mode asides phrased as soft judgement ("use judgement", "often enough"). Meanwhile every mode
file ends with a Deliver step pointing at file output. The gradient pushed toward building a file for
every request.

The failure this produces is specific: a one-line answer buried inside an HTML file the reader has to
open, when they asked a question in a conversation.

### Decision

**Depth is a routing axis, decided before anything loads** — Step 0 in the router, ahead of sector, mode
and scope.

- **Answer in chat** for questions: concept explanations, single figures, quick reads, anything
  exploratory. **This is the default.** The same sourcing discipline applies — real figures, real
  attribution, no fabrication — delivered as prose.
- **Build the artifact** when the person wants something to keep, share, publish or return to.
- **When ambiguous, answer in chat and offer the artifact.** That costs one sentence; the reverse wastes
  the reader's time.
- Honour explicit overrides in both directions — "just tell me" / "give me a report".

Stated explicitly: a learning session is a conversation, and twenty questions should not produce twenty
files.

### Consequences

- The skill is usable for learning, which is half its purpose.
- Routing has four axes rather than three, and depth must be judged before the mode is known — a request
  can map to `school` at either depth.
- Sourcing discipline does not relax in chat mode. An unsourceable figure returns "not disclosed" in
  conversation too, which matters more there because there is no footnote to catch it.
- Misrouting is cheap and self-correcting in either direction: the reader says "actually build it" or
  "just tell me".

---

## 0008. Exclude news digests; keep policy and corporate-action analysis

**Status**: Accepted · 2026-08-09

### Context

Some reports are event-driven rather than results-driven. The audit found event content is far more
pervasive than it first appears: **77 of 96 reports (80%)** carry policy/regulatory or corporate-action
material — aluminium tariffs, steel safeguard duty, telecom AGR, banking open offers, battery stake
sales.

The split matters. Only **two** are standalone event reports (`Q1FY27_Analysis_USGenericTariff`,
`Vedanta_Demerger_Dashboard`). Roughly 75 carry event content as a *section inside* a quarterly report —
telecom's "Key Policy Catalyst", steel's "Safeguard Duty Protection".

Two further reports are news digests (`Market_breaking_news_*`, "SectorWire") — headline roundups of what
happened in the market.

### Decision

**Keep event analysis. Exclude news digests.**

`event-impact.md` covers two event classes:
- **Policy or regulatory events** — tariffs, duties, circulars, tax changes, price caps
- **Corporate actions** — demergers, mergers, buybacks, stake sales, open offers, IPO listings

It serves double duty: a standalone report type, and the discipline invoked whenever event content
appears inside another mode.

**The dividing line**: an event qualifies only if it can be tied to **named companies with a stated
exposure basis**. "What happened in the market this week" is journalism, not company evaluation, and the
mode file says so explicitly so the router does not drift into it.

The six-step spine is lifted from the tariff report: establish the event factually from a primary source
(separating confirmed from proposed from speculated) → trace the transmission mechanism to a P&L line →
name exposed companies with a stated exposure basis → quantify where disclosed and **refuse where not** →
second-order effects including who gains → what to watch next.

### Consequences

- Steps 1 and 3–6 are pure method, identical for a tariff, a rate cut or a demerger. Only step 2 —
  transmission mechanism — is domain knowledge, so each sector file carries an **event transmission map**
  linking common events to the metric they hit and the exposure basis to cite.
- The two news-digest reports are not reproducible by the skill. That is deliberate.
- The tariff report's own framing sets the standard for honesty here: its heading reads *"IMMEDIATE
  IMPACT — there isn't one, yet"*. Manufacturing an impact estimate to fill the section is the main
  failure mode of event analysis, and readers act on those numbers.

---

## 0009. Confine paths and tool names to a single file

**Status**: Accepted · 2026-08-09

### Context

The skill needs to run in other agent environments later — ChatGPT, Gemini — so subscribers can use it
without a Claude account.

Almost all of it is already portable: `references/**` is plain markdown domain knowledge with no runtime
dependency. What is *not* portable is a thin shell — the YAML frontmatter format, and any reference to a
tool (`SendUserFile`) or a path (`reports/staging/`).

An early draft had every mode file ending with "save to `reports/staging/…` and call `SendUserFile`".
That would have hardcoded Claude Code into all fifteen modes, making a future port a fifteen-file edit.

### Decision

**Keep the shell out of the core.**

- Mode files and sector files contain **zero tool names and zero paths**. They describe only what to
  produce.
- All I/O collapses into `references/output-conventions.md`, which states plainly that it is the only
  file naming paths or tools.
- Porting means editing that one file.

A validation grep enforces this.

**Claude-first**: Phase 1 targets Claude Code. Export bundles for other platforms wait until the
subscriber platform is chosen and sector files stop churning — building three bundles now would mean
maintaining them through Phases 2–4 for a platform not yet selected.

### Consequences

- The rename of `cb_research_reports/` → `reports/published/` touched exactly one file inside the skill.
  That was the design working as intended, and it validated the constraint under real conditions.
- Two honest limits on any future port. **Progressive disclosure** — loading only the two files a request
  needs — is a Claude-Code-style capability; RAG-based platforms retrieve knowledge files instead, which
  is less deterministic, so the port will be functional but not identical. And those platforms **cap
  knowledge-file count and size**, with caps that change; at ~32 files a concatenating build mode may be
  required rather than one-file-per-mode.
- Mode files read slightly more abstractly, since they cannot say where output goes.

---

## 0010. Inherit structure from prior reports; never inherit figures

**Status**: Accepted · 2026-08-09

### Context

The established workflow was to fork the previous quarter's report for a sector and update the numbers.
That has a genuine advantage — the prior artifact is complete and proven, its company scope and layout
already tuned over several quarters.

It also has a measurable cost, visible throughout the corpus audit. Forking propagates defects and never
propagates fixes:

- Tab markup diverged into two conventions (`tab-btn` in 49 files, `tab` in others)
- A footer appears in **19%** of reports
- An explicit `Source:` line appears in **42%**
- The `.fnote` caveat block — which flags one-off tax credits, MTM swings and basis changes — appears in
  **1 of 98**
- CB Score fragmented into four incompatible methods on three scales (ADR-0005)

None of this is carelessness; it is what forking does mechanically. The existing metrics glossary already
warned about the matching failure mode: *"a persistency ratio quietly copied wrong from quarter to
quarter."*

### Decision

**A three-way split of what the skill takes from where:**

| Layer | Source | When |
|---|---|---|
| **Durable sector knowledge** — metric definitions, benchmarks, taxonomy, palette, transmission maps | mined **once** from the reports into `sectors/*.md` | read from the sector file at runtime |
| **Point-in-time facts** — quarterly figures, ratings, valuations | sourced **live** per run | never baked into any file |
| **Continuity reference** — company scope, section selection, layout, chart types | the prior period's report, on request | only when regenerating |

**Structure and expertise are inherited; numbers never are.** When regenerating a report for a new
period, read the prior artifact for scope and layout, then re-source every figure.

Prefer a *published* prior over a staged one — a staged draft may contain figures nobody has verified.

### Consequences

- The advantage of the fork workflow is kept; the drift is not. Fix the missing `.fnote` rule once and
  all report types get it.
- If the skill pulled figures from stored reports, a Q2 report would silently inherit Q1 values. This is
  the exact failure the glossary warned about, and it is why the split is stated explicitly rather than
  left to judgement.
- Two things the skill does not replace, stated so expectations stay honest: **generation is
  non-deterministic** (a fork reproduces byte-for-byte, a regeneration does not), and **bespoke editorial
  angles** — "Why DMart Differs", "Budget Warfare", "Milk Chain" — come from the author, not the
  template.
- The framing: the skill guarantees the floor — structure, caveats, sourcing, scoring consistency — so
  attention goes to the insight rather than the scaffolding.

---

## 0011. Install the skill by symlink; treat the packaged `.skill` as a build artifact

**Status**: Accepted · 2026-08-10

### Context

After Phase 1 the skill existed only as source in the repo. Nothing loaded it — `~/.claude/skills/` and
`.claude/skills/` did not exist — so it could not trigger in a session at all.

This was easy to miss, because answers produced during the build *appeared* to demonstrate the skill
working. They did not: the author of the files had their content in context regardless. The skill's
correctness had been validated; its ability to trigger had never been tested.

Separately, the packaged `.skill` file (57K) sat at the repo root. It is a build artifact — regenerable
from source at any time — and committing it means a binary diff on every rebuild that git cannot
meaningfully version.

### Decision

**Install by symlink, not copy:**

```
.claude/skills/sector-financial-analysis -> ../../sector-financial-analysis
```

Git stores it as mode `120000`, a real symlink, so anyone cloning the repo gets the skill wired up.
Editing the source updates the installed skill with no second copy to drift — the same approach as
`CLAUDE.md → AGENTS.md`.

**Gitignore `*.skill`** as a build artifact; distribute via GitHub Releases when needed. One exception is
negated: archived packaged skills under `archive/` stay tracked, since a rule aimed at the new build
artifact should not silently eat historical ones.

### Consequences

- The skill is live and can be tested for triggering — the one property that could not be verified
  otherwise.
- Edits during Phases 2–4 take effect immediately, with no install step.
- It will trigger on the thirteen unbuilt sectors and then have to decline. That is handled explicitly in
  the router — *"If a request names a company from an unbuilt sector, say so plainly… don't silently
  substitute another sector's metrics"* — but whether it reads as helpful honesty or noise is only
  answerable from real use. If it over-triggers, the fix is tightening the description, not uninstalling.
- No installable build is present on GitHub until a Release is cut.
- Removal is one line and does not touch the source:
  `rm .claude/skills/sector-financial-analysis`

---
