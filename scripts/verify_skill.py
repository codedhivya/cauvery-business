#!/usr/bin/env python3
"""
Verify the sector-financial-analysis skill still holds together.

Run this after editing any sector file, mode file or the router. It checks two
different kinds of thing:

  STRUCTURE — the contracts that make the skill multi-sector. These fail loudly
  and mechanically: a sector metric leaking into a mode file, a CSS class with
  no definition, a CB Rating table that doesn't total 100%.

  CONTENT — that each sector file actually contains its defining answer, and
  that the skill's refusals are present. A sector file can pass every structural
  check and still be empty of the one insight that makes the sector legible.

Neither kind can be checked by reading the skill casually, which is why this
exists. What it CANNOT check is whether the router triggers unprompted — that
needs a session that didn't author the files. See the triggering test in
MAINTENANCE.md.

The check count grows with each sector added — it is derived, not fixed, so
the totals quoted in the docs go stale. The script prints its own tally.

    python3 scripts/verify_skill.py            # run everything
    python3 scripts/verify_skill.py --quiet    # only failures

Exit 0 = all pass, 1 = failures (usable in CI or a pre-commit hook).
"""

import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "sector-financial-analysis")
REFS = os.path.join(SKILL, "references")
MODES = os.path.join(REFS, "modes")
SECTORS = os.path.join(REFS, "sectors")

# Metrics that belong to exactly one sector. If any appears in a mode file the
# mode/sector contract is broken — see docs/adr/0002.
# NOT included: EV/EBITDA, P/E, EBITDA%, Net Debt — those are universal
# cross-sector metrics and legitimately appear in modes.
SECTOR_METRICS = (
    r"VNB|Combined Ratio|IRDAI|persistency|GWP|GDPI|Embedded Value|\bNIM\b|GNPA|NNPA|"
    r"\bCASA\b|CRAR|CET-1|slippage|USFDA|ARPOB|\bPLF\b|\bALMM\b|\bGRM\b|\bSSSG\b|"
    r"RevPAR|\bTCV\b|QAAUM|\bARPU\b|\bDPU\b|EBITDA per tonne|lead distance|\bAGR\b|"
    r"book-to-bill|Para IV|\bADTO\b"
)

TOOLS_AND_PATHS = r"SendUserFile|present_files|/mnt/|reports/"
HARDCODED_PERIOD = r"Q[1-4] ?FY[0-9]{2}"

# Sector files must carry all ten numbered sections in order. Titles are matched
# on the NUMBER, not the wording — sectors legitimately rename them
# ("5. RBI regulatory quick reference", "2. Why insurers are valued differently"),
# and the contract is about the ordered ten, not the exact words.
TEMPLATE_SECTION_COUNT = 10

DELEGATION_TARGETS = [
    "Headline KPIs by category", "Table columns by category", "Chart reference lines",
    "Profile coverage", "Moat candidates", "Valuation", "CB Rating substitutions",
    "Extra sections", "Event transmission map",
]

# Each sector's defining insight — the thing that makes it legible. Phrases are
# matched against whitespace-normalised lowercase text, so line wrapping is safe.
SECTOR_CONTENT = {
    "banking":         ["cannot be bought", "more informative than gnpa", "40%"],
    "insurance":       ["more informative than pat", "150%"],
    "nbfc-hfc":        ["no casa", "cost of funds", "net debt is meaningless"],
    "capital-markets": ["closing aum flatters", "not valued on a multiple"],
    "it-services":     ["delivery quality", "constant currency"],
    "pharma-health":   ["falling alos is *good*", "import alert"],
    "auto":            ["siam", "replacement"],
    "consumer":        ["single most important retail metric", "revpar"],
    "capital-goods":   ["book-to-bill", "box-build"],
    "power-energy":    ["inventory gain/loss", "merchant"],
    "metals":          ["ebitda per tonne", "captive", "volume, not revenue"],
    "cement":          ["lead distance", "regional"],
    "chemicals":       ["never draw one ebitda-margin line", "specialty", "commodity"],
    "infra-realty":    ["pre-sales", "revenue is a lagging number"],
    "logistics":       ["asset-light", "density", "operating leverage"],
    "reit-invit":      ["perpetual", "finite", "reit and invit are the primary split", "coverage"],
    "telecom":         ["agr", "spectrum"],
    "new-age":         ["contribution margin", "runway", "not p/e"],
}

# Refusals and disciplines that must survive any edit.
GUARDRAILS = [
    ("banks have no EBITDA",              "sectors/banking.md",        ["no meaningful ebitda"]),
    ("insurers have no EBITDA",           "sectors/insurance.md",      ["no meaningful ebitda"]),
    ("net debt meaningless for lenders",  "sectors/nbfc-hfc.md",       ["net debt is meaningless"]),
    ("a fund is not valued on a multiple","sectors/capital-markets.md",["not valued on a multiple"]),
    ("REIT stays out of cross-sector",    "sectors/reit-invit.md",     ["does not belong in a cross-sector"]),
    ("a trust is not scored on PAT",      "sectors/reit-invit.md",     ["do not appear"]),
    ("no buy/sell/hold in own voice",     "source-hierarchy.md",       ["never issue a buy / sell / hold"]),
    ('"Not disclosed" must be earned',    "source-hierarchy.md",       ["targeted attempt", "one query per company"]),
    ("house disclaimer recorded",         "source-hierarchy.md",       ["earnings-quality analysis only"]),
    ("universe sourced, not recalled",    "source-hierarchy.md",       ["are not the current universe"]),
    ("omit analysts if unsourceable",     "modes/analyst-ratings.md",  ["omit the section entirely"]),
    ("news digests excluded",             "modes/event-impact.md",     ["out of scope"]),
    ("prior coverage stated in output",   "output-conventions.md",     ["prior cb research coverage"]),
    ("P&L must tie, never back-solve",    "modes/financials.md",       ["never back-solve a line"]),
    ("prior period reconciled",           "output-conventions.md",     ["they must agree"]),
    ("pledge flagged as risk",            "modes/business-profile.md", ["leverage position on the company"]),
    ("optics separated from operations",  "modes/business-profile.md", ["separate the optics from the operations"]),
    ("school flags sector-file gaps",     "modes/school.md",           ["does not yet define it"]),
    ("question shapes, not questions",    "modes/school.md",           ["store the shape, never the question"]),
    ("school teaches before referencing", "modes/school.md",           ["teach the sector, then supply the reference"]),
    ("metric blind spots named",          "modes/school.md",           ["say what the metric cannot tell you"]),
    ("durable vs point-in-time split",    "modes/school.md",           ["school teaches the sector and the business. it does not teach a quarter"]),
    ("mixed reporting seasons handled",   "modes/quarterly-report.md", ["mixed reporting seasons"]),
]

# Router behaviour: depth routing and self-imposed scope limits.
ROUTER_RULES = [
    ("Step 0 decides depth first",        ["step 0 — detect the depth"]),
    ("chat is the explicit default",      ["this is the **default**"]),
    ("ambiguous -> answer then offer",    ["answer in chat first and offer"]),
    ("explicit overrides honoured",       ["just tell me"]),
    ("'build' routes to artifact",        ["build the artifact when"]),
    ("unbuilt sector -> never substitute",["don't silently substitute another sector's metrics"]),
    ("ask if sector unclear",             ["ask — don't guess"]),
    ("event needs named companies",       ["named companies with a stated exposure basis"]),
    ("output is a draft until verified",  ["never into the published collection"]),
    ("chat path checks prior coverage",   ["either way — chat or artifact — check the published"]),
    ("full report confirms scope first",  ["most expensive thing this skill does"]),
]


def norm(path):
    """Whitespace-normalised lowercase text, so line wrapping never breaks a match."""
    with open(os.path.join(REFS, path) if not os.path.isabs(path) else path) as fh:
        return " ".join(fh.read().lower().split())


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quiet", action="store_true", help="print only failures")
    args = ap.parse_args()

    failures = []
    lines = []
    ran = []

    def check(group, name, ok, detail=""):
        ran.append(name)
        if not ok:
            failures.append(f"{group}: {name}{' — ' + detail if detail else ''}")
        if not args.quiet or not ok:
            lines.append(f"  {'PASS' if ok else 'FAIL'}  {name}{'' if ok else '  ' + detail}")

    def header(t):
        if not args.quiet:
            lines.append(f"\n{t}\n" + "-" * len(t))

    mode_files = sorted(f for f in os.listdir(MODES) if f.endswith(".md"))
    sector_files = sorted(f for f in os.listdir(SECTORS)
                          if f.endswith(".md") and f != "_template.md")
    mode_blob = "".join(open(os.path.join(MODES, f)).read() for f in mode_files)
    sector_blob = "".join(open(os.path.join(SECTORS, f)).read() for f in sector_files)

    # ---- STRUCTURE -------------------------------------------------------
    header("STRUCTURE — the contracts that make the skill multi-sector")

    hits = re.findall(SECTOR_METRICS, mode_blob, re.I)
    check("structure", "no sector metric leaked into a mode file", not hits,
          f"found {sorted(set(h.lower() for h in hits))[:6]}" if hits else "")

    leak = re.findall(TOOLS_AND_PATHS, mode_blob + sector_blob)
    check("structure", "no tool name or path outside output-conventions.md", not leak,
          f"found {sorted(set(leak))}" if leak else "")

    per = re.findall(HARDCODED_PERIOD, mode_blob + sector_blob)
    check("structure", "no hardcoded period in modes or sectors", not per,
          f"found {sorted(set(per))[:4]}" if per else "")

    used = set(re.findall(r"`\.([a-zA-Z][a-zA-Z0-9-]*)`", mode_blob))
    defined = set(re.findall(r"\.([a-zA-Z][a-zA-Z0-9-]*)\s*(?=[,{:])",
                             open(os.path.join(REFS, "design-system.md")).read() + sector_blob))
    unresolved = sorted(used - defined)
    check("structure", f"all {len(used)} CSS classes used in modes resolve",
          not unresolved, f"unresolved {unresolved}" if unresolved else "")

    cov = os.path.join(ROOT, "docs", "COVERAGE.md")
    if os.path.exists(cov):
        import subprocess
        rc = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build_coverage.py"),
                             "--check"], capture_output=True).returncode
        check("structure", "docs/COVERAGE.md regenerated from the sector files", rc == 0,
              "run: python3 scripts/build_coverage.py" if rc else "")

        rc2 = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build_coverage.py"),
                              "--strict"], capture_output=True)
        check("structure", "every Examples column names companies, not descriptions",
              rc2.returncode == 0,
              rc2.stderr.decode().strip().splitlines()[-1] if rc2.returncode else "")

    skill_lines = sum(1 for _ in open(os.path.join(SKILL, "SKILL.md")))
    check("structure", f"SKILL.md under 500 lines ({skill_lines})", skill_lines < 500)

    check("structure", f"15 mode files present ({len(mode_files)})", len(mode_files) == 15)
    check("structure", f"18 sector files present ({len(sector_files)})", len(sector_files) == 18)

    # ---- PER-SECTOR COMPLETENESS ----------------------------------------
    header("PER-SECTOR — template sections, delegation targets, CB weights")

    for f in sector_files:
        raw = open(os.path.join(SECTORS, f)).read()
        flat = " ".join(raw.lower().split())
        name = f[:-3]

        present = {int(m) for m in re.findall(r"^## (\d+)\.", raw, re.M)}
        missing_s = [n for n in range(1, TEMPLATE_SECTION_COUNT + 1) if n not in present]
        missing_d = [d for d in DELEGATION_TARGETS if d not in raw]

        try:
            block = raw.split("CB Rating substitutions")[1].split("###")[0]
            weights = [int(x) for x in re.findall(r"\|\s*(\d{1,2})%\s*\|", block)]
            total = sum(weights)
        except IndexError:
            weights, total = [], 0

        teach = []
        if "### the analogy" not in flat:
            teach.append("no analogy")
        if "what goes wrong" not in flat:
            teach.append("no failure mode")

        ok = (not missing_s and not missing_d and total == 100
              and "cross-sector work" in flat and not teach)
        detail = []
        if missing_s: detail.append(f"missing sections {missing_s}")
        if missing_d: detail.append(f"targets {missing_d}")
        if total != 100: detail.append(f"CB weights {weights}={total}%")
        if "cross-sector work" not in flat: detail.append("no cross-sector note")
        if teach: detail.append("; ".join(teach))
        check("sector", f"{name:16} 10 sections · 9 targets · CB {total}% · analogy · failure mode", ok, "; ".join(detail))

    # ---- CONTENT ---------------------------------------------------------
    header("CONTENT — does each sector carry its defining insight?")

    for name, phrases in SECTOR_CONTENT.items():
        flat = norm(f"sectors/{name}.md")
        missing = [p for p in phrases if p not in flat]
        check("content", f"{name:16} carries its defining framing", not missing,
              f"missing {missing}" if missing else "")

    # ---- GUARDRAILS ------------------------------------------------------
    header("GUARDRAILS — refusals and disciplines")

    for name, path, phrases in GUARDRAILS:
        flat = norm(path)
        check("guardrail", name, any(p in flat for p in phrases))

    # ---- ROUTER ----------------------------------------------------------
    header("ROUTER — depth routing and scope limits")

    sk = " ".join(open(os.path.join(SKILL, "SKILL.md")).read().lower().split())
    for name, phrases in ROUTER_RULES:
        check("router", name, any(p in sk for p in phrases))

    # ---- REPORT ----------------------------------------------------------
    print("\n".join(lines))
    total_checks = len(lines) if not args.quiet else "?"
    print()
    if failures:
        print(f"{len(failures)} FAILURE(S):")
        for f in failures:
            print(f"  - {f}")
        print("\nSee docs/adr/ for why each contract exists.")
        return 1

    print(f"All {len(ran)} checks pass.")
    print("\nNot covered here: whether the router triggers unprompted. That needs a")
    print("session that did not author the files — see the fresh-session questions")
    print("in MAINTENANCE.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
