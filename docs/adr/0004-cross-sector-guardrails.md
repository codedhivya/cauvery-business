# ADR-0004: Support cross-sector comparison, constrained to universal metrics

**Status**: Accepted · 2026-08-09

## Context

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

## Decision

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

## Consequences

- The five existing cross-sector report types remain reproducible.
- The specific failure mode — an insurer silently misrepresented in an EBITDA column — is addressed
  directly rather than by avoiding the whole capability.
- Every sector file must declare, in its §10 cross-sector note, which universal metrics do *not* apply to
  it. This is the single most important line in a sector file for preventing silent misrepresentation,
  and it is easy to forget when writing one.
- Cross-sector output is deliberately less rich than single-sector output. That is the correct trade:
  the metrics that would make it richer are the ones that are not comparable.
