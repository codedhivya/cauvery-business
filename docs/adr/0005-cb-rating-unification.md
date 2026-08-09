# ADR-0005: Unify CB Rating on one core method with per-sector substitutions

**Status**: Accepted · 2026-08-09

## Context

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

## Decision

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

## Consequences

- Scores become comparable across reports and quarters, which a proprietary rating requires to mean
  anything. Four methods on three different scales made cross-report comparison meaningless.
- Both existing formulas are preserved rather than one being discarded.
- Every new sector file must supply a substitution table, and a validation check confirms it totals 100%.
- Scores computed under the new method will not match historically published scores. Those were computed
  by hand under whichever variant applied at the time.
- The banking presentation retains its established name, **"CB Earnings-Quality Rating"**, which carries
  meaning: how much of reported profit is core and repeatable versus provision release or one-offs.
