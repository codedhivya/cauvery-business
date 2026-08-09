#!/usr/bin/env python3
"""
Detect drift between the published report corpus and the skill.

Reports written by hand — by a colleague, or before the skill existed — often carry
knowledge the skill doesn't have yet: a sector with no file, a metric no sector file
defines, a section type no mode covers. Left unnoticed, that knowledge stays stranded
in static HTML, which is the exact problem the skill was built to solve.

This script compares reports/published/ against the skill and reports what's new.

    python3 scripts/audit_corpus.py            # show drift
    python3 scripts/audit_corpus.py --accept   # baseline the current corpus as reviewed
    python3 scripts/audit_corpus.py --all      # re-audit everything, ignoring the baseline

Exit codes: 0 = no action needed, 1 = drift found (usable in CI).

Findings are advisory, not prescriptive. A new metric may deserve a sector-file entry,
or may be a one-off the author chose deliberately. A human decides.
"""

import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLISHED = os.path.join(ROOT, "reports", "published")
SECTORS_DIR = os.path.join(ROOT, "sector-financial-analysis", "references", "sectors")
MODES_DIR = os.path.join(ROOT, "sector-financial-analysis", "references", "modes")
DESIGN = os.path.join(ROOT, "sector-financial-analysis", "references", "design-system.md")
MANIFEST = os.path.join(ROOT, "docs", "corpus-manifest.json")

# Sector keyword map — mirrors the taxonomy in ROADMAP.md. Extend when adding a sector.
SECTOR_KEYWORDS = {
    "banking": ["bank", "sbi", "psu", "sfb", "idbi", "bom_ib"],
    "nbfc-hfc": ["nbfc", "hfc", "pfc", "rec", "ireda", "jio_financial"],
    "insurance": ["insurance", "lic", "life_insurance", "hdfc_icici"],
    "capital-markets": ["bse", "mcx", "cdsl", "broking", "angelone", "groww", "amc", "edelweiss", "ipo"],
    "it-services": ["it_services", "tcs", "hcl", "infoedge", "fractal"],
    "pharma-health": ["pharma", "drreddys", "medtech", "hospital", "gland", "generic"],
    "auto": ["2w", "tvsmotor", "bajajauto", "auto_spares", "tyre", "battery", "pv_sector"],
    "metals": ["steel", "aluminium", "vedanta", "nalco", "hindalco"],
    "cement": ["cement", "ultratech"],
    "chemicals": ["chemical", "himadri", "pvc", "paint", "fertilizer", "recycling"],
    "power-energy": ["power", "solar", "acme", "emmvee", "oilgas", "omc", "ril", "adani_power", "iex"],
    "capital-goods": ["bhel", "defence", "railway", "mtar", "inox", "ems", "cables", "polycab",
                      "shaily", "shaktipumps", "pacedigitek"],
    "consumer": ["dmart", "fmcg", "alcobev", "sugar", "dairy", "textile", "nitinspinners",
                 "v2retail", "abfashion", "gold", "amusement", "hotel", "india-hotels"],
    "infra-realty": ["realestate", "ports", "reit", "invit"],
    "telecom": ["telecom", "airtel"],
    "_cross-sector": ["multisector", "multico", "ranker", "cross_sector", "newage",
                      "powerproxy", "india_pv"],
    "_excluded": ["market_breaking"],
}

# Finance terms worth noticing if a sector file doesn't define them.
METRIC_RE = re.compile(
    r"\b(VNB|APE|GWP|GDPI|CISR|RoEV|EVOP|NII|NIM|GNPA|NNPA|PCR|CASA|CRAR|CET-?1|LCR|NSFR|"
    r"EBITDA|EBIT|PAT|PBT|ROE|ROA|ROCE|RoNW|EPS|P/E|P/B|P/BV|P/EV|EV/EBITDA|DPU|NAV|AUM|"
    r"ARPU|MAU|DAU|GMV|SSSG|ASP|OPM|NPM|WACC|IRR|DSCR|FFO|NOI|CAGR|YoY|QoQ|"
    r"Combined Ratio|Loss Ratio|Expense Ratio|Solvency|Persistency|Embedded Value|"
    r"Slippage|Credit Cost|Cost of Funds|Yield on Advances|Book Value|Order Book|"
    r"Capacity Utilisation|Realisation|Blended Realisation|Same Store Sales|Occupancy|"
    r"Load Factor|Utilisation|Churn|Subscriber|Tonnage|Volume Growth)\b",
    re.I,
)

SECTION_RE = re.compile(
    r'class="(?:tab-btn|tab|section-title|sec-hdr|nav-tab|tablink)[^"]*"[^>]*>([^<]{3,44})<'
)

# Section names that map to an existing mode — anything else is a candidate gap.
KNOWN_SECTIONS = {
    "dashboard", "overview", "snapshot", "summary", "kpi", "at a glance",
    "financial", "results", "p&l", "revenue table", "income", "per-bank financials",
    "chart", "graph", "visual", "trend", "comparative charts",
    "business profile", "business analysis", "companies", "company", "business model", "profile",
    "segment", "geographic", "geography", "product mix",
    "valuation",
    "swot",
    "moat", "usp",
    "risk", "outlook", "guidance",
    "analyst", "brokerage", "rating consensus",
    "verdict", "scorecard", "ranker", "ranking", "winner", "compare", "comparison", "peer",
    "preference", "conclusion",
    "cb rating", "cb score", "cbf", "earnings-quality",
    "school", "learn", "glossary",
    "assist", "socrates",
    "demerger", "merger", "ipo", "buyback", "listed entities", "tariff", "policy", "impact",
    "management", "board", "governance",
    "asset quality", "loan book", "margins", "capital", "investments", "debt", "cash flow",
    "metrics editor", "seasonality", "reasoning",
}

STOP = {"YOY", "QOQ", "CAGR", "PAT", "EBITDA", "ROE", "ROA"}  # universal; not sector-specific


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def strip_html(raw):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"&[a-z#0-9]+;", " ", t)
    return " ".join(t.split())


def classify(filename):
    low = filename.lower()
    for sector, keys in SECTOR_KEYWORDS.items():
        if any(k in low for k in keys):
            return sector
    return None


def load_manifest():
    if os.path.exists(MANIFEST):
        with open(MANIFEST) as fh:
            return json.load(fh)
    return {"audited": {}}


def skill_corpus():
    """Everything the skill currently knows, as one lowercase blob per area."""
    sectors = {}
    for f in sorted(os.listdir(SECTORS_DIR)):
        if f.endswith(".md"):
            sectors[f[:-3]] = open(os.path.join(SECTORS_DIR, f)).read().lower()
    modes = "".join(
        open(os.path.join(MODES_DIR, f)).read().lower()
        for f in sorted(os.listdir(MODES_DIR)) if f.endswith(".md")
    )
    design = open(DESIGN).read()
    css = set(re.findall(r"\.([a-zA-Z][a-zA-Z0-9-]*)\s*(?=[,{:])", design))
    for blob in sectors.values():
        css |= set(re.findall(r"\.([a-zA-Z][a-zA-Z0-9-]*)\s*(?=[,{:])", blob))
    return sectors, modes, css


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--accept", action="store_true",
                    help="record the current corpus as reviewed")
    ap.add_argument("--all", action="store_true",
                    help="audit every report, ignoring the baseline")
    args = ap.parse_args()

    if not os.path.isdir(PUBLISHED):
        print(f"error: {PUBLISHED} not found", file=sys.stderr)
        return 2

    manifest = load_manifest()
    audited = {} if args.all else manifest.get("audited", {})
    sectors, modes, known_css = skill_corpus()
    built = {s for s in sectors if not s.startswith("_")}

    files = sorted(f for f in os.listdir(PUBLISHED) if f.endswith(".html"))
    new, changed = [], []
    for f in files:
        digest = md5(os.path.join(PUBLISHED, f))
        if f not in audited:
            new.append((f, digest))
        elif audited[f] != digest:
            changed.append((f, digest))

    if args.accept:
        manifest["audited"] = {f: md5(os.path.join(PUBLISHED, f)) for f in files}
        os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
        with open(MANIFEST, "w") as fh:
            json.dump(manifest, fh, indent=2, sort_keys=True)
            fh.write("\n")
        print(f"Baselined {len(files)} reports as reviewed.")
        return 0

    print(f"Corpus: {len(files)} reports · {len(new)} new · {len(changed)} changed\n")
    if not new and not changed:
        print("No drift. The skill is current with the corpus.")
        return 0

    unknown_sector = defaultdict(list)
    unseen_metrics = Counter()
    unseen_sections = Counter()
    unseen_css = Counter()
    metric_where = defaultdict(set)

    for f, _ in new + changed:
        raw = open(os.path.join(PUBLISHED, f), encoding="utf-8", errors="ignore").read()
        text = strip_html(raw)
        sector = classify(f)

        if sector is None:
            unknown_sector["unclassified"].append(f)
        elif sector.startswith("_"):
            pass  # cross-sector or deliberately excluded
        elif sector not in built:
            unknown_sector[sector].append(f)

        blob = sectors.get(sector, "") if sector else ""
        for m in set(x.upper() for x in METRIC_RE.findall(text)):
            if m in STOP:
                continue
            if m.lower() not in blob and m.lower() not in modes:
                unseen_metrics[m] += 1
                metric_where[m].add(f)

        for s in set(SECTION_RE.findall(raw)):
            s = re.sub(r"[^\x00-\x7F]", "", re.sub(r"&[a-z#0-9]+;", " ", s)).strip()
            if not s or "${" in s:
                continue
            if not any(k in s.lower() for k in KNOWN_SECTIONS):
                unseen_sections[s] += 1

        classes = set()
        for c in re.findall(r'class="([^"]+)"', raw):
            classes.update(c.split())
        for c in classes - known_css:
            if not re.match(r"^[a-z][a-z0-9-]{1,24}$", c):
                continue
            unseen_css[c] += 1

    if new:
        print("NEW REPORTS")
        for f, _ in new:
            print(f"   + {f}  [{classify(f) or 'unclassified'}]")
        print()
    if changed:
        print("CHANGED REPORTS")
        for f, _ in changed:
            print(f"   ~ {f}")
        print()

    action = False

    if unknown_sector:
        action = True
        print("⚠ SECTOR NOT BUILT — these reports belong to a sector with no file")
        for sector, fs in sorted(unknown_sector.items()):
            print(f"   {sector}: {', '.join(fs[:4])}{' …' if len(fs) > 4 else ''}")
        print("   → add references/sectors/<sector>.md (see ROADMAP.md)\n")

    if unseen_metrics:
        action = True
        print("⚠ METRICS NOT DEFINED in the matching sector file")
        for m, c in unseen_metrics.most_common(20):
            where = sorted(metric_where[m])[:2]
            print(f"   {m:22} in {', '.join(w[:34] for w in where)}")
        print("   → add to the sector file's Metric definitions, or ignore if incidental\n")

    if unseen_sections:
        action = True
        print("⚠ SECTIONS NOT COVERED by any mode")
        for s, c in unseen_sections.most_common(15):
            print(f"   {c:2}×  {s}")
        print("   → declare as a sector Extra section, or consider a new mode if it recurs\n")

    if unseen_css:
        action = True
        print("⚠ CSS CLASSES not in design-system.md or a sector file")
        top = ", ".join(f"{c}({n})" for c, n in unseen_css.most_common(14))
        print(f"   {top}")
        print("   → add to design-system.md if cross-sector, else the sector file\n")

    if not action:
        print("Reports are new but introduce nothing the skill lacks.")

    print("Findings are advisory. Review, fold in what belongs, then:")
    print("   python3 scripts/audit_corpus.py --accept")
    return 1 if action else 0


if __name__ == "__main__":
    sys.exit(main())
