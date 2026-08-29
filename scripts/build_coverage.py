#!/usr/bin/env python3
"""
Generate docs/COVERAGE.md — every sector, category and company the skill knows.

Derived from the sector files, never hand-maintained. A hand-written coverage
list drifts the moment a sector file changes, and a stale one is worse than
none: it is the document people check before asking whether something is
covered.

    python3 scripts/build_coverage.py           # write docs/COVERAGE.md
    python3 scripts/build_coverage.py --check   # fail if it is out of date

--check is for CI and for the sync workflow: exit 1 means a sector file moved
and the coverage page was not regenerated.
"""

import os
import re
import sys
import collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTORS = os.path.join(ROOT, "sector-financial-analysis", "references", "sectors")
PUBLISHED = os.path.join(ROOT, "reports", "published")
OUT = os.path.join(ROOT, "docs", "COVERAGE.md")

# Categories that legitimately name no company — a plant type or a division of
# a company named elsewhere, not a distinct listed entity.
NAMELESS_OK = {
    "Grinding-only / split unit", "Commercial / lease developer", "Wireline / enterprise",
    "Hyperlocal / last-mile", "Contract logistics & warehousing",
}


def taxonomy(path):
    """(category, examples) pairs from a sector file's section 1.

    Some files open section 1 with a comparison table rather than the taxonomy
    (reit-invit contrasts REIT against InvIT first), so an explicit
    sub-category block wins where one exists. Column counts differ between
    files, so examples are taken from the LAST cell rather than a fixed index.
    """
    body = open(path).read()
    m = re.search(r"^## 1\..*?(?=^## 2\.)", body, re.S | re.M)
    if not m:
        return []
    block = m.group(0)
    sub = re.search(r"^### Sub-categories.*", block, re.S | re.M)
    if sub:
        block = sub.group(0)
    out = []
    for line in block.splitlines():
        if not line.startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not cells[0].startswith("**"):
            continue
        cat = cells[0].strip("*").strip()
        ex = cells[-1]
        # strip markdown emphasis for readability
        ex = re.sub(r"\*\*(.*?)\*\*", r"\1", ex).strip()
        out.append((cat, ex))
    return out


def report_counts():
    """Reports per sector, using the audit's own classifier so the two agree."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "ac", os.path.join(ROOT, "scripts", "audit_corpus.py"))
    ac = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ac)
    counts = collections.Counter()
    if os.path.isdir(PUBLISHED):
        for f in os.listdir(PUBLISHED):
            if f.endswith(".html"):
                counts[ac.classify(f)] += 1
    return counts


def render():
    files = sorted(f for f in os.listdir(SECTORS)
                   if f.endswith(".md") and f != "_template.md")
    counts = report_counts()
    total_reports = sum(v for k, v in counts.items() if k and not k.startswith("_"))

    L = []
    L.append("# Coverage")
    L.append("")
    L.append("Every sector the skill knows, the categories inside it, and the companies named in each.")
    L.append("")
    L.append("**Generated from the sector files — do not edit by hand.**")
    L.append("")
    L.append("```bash")
    L.append("python3 scripts/build_coverage.py")
    L.append("```")
    L.append("")
    L.append("Companies listed are **illustrative, not the current universe**. Anything listed since a")
    L.append("sector file was written belongs in an analysis too — the skill sources the constituent list")
    L.append("live rather than reading it from here. A name's absence is not a statement that the company")
    L.append("is out of scope.")
    L.append("")
    L.append(f"**{len(files)} sectors · {total_reports} classified reports in the published collection.**")
    L.append("")
    L.append("| Sector | Categories | Reports |")
    L.append("|---|---:|---:|")
    for f in files:
        name = f[:-3]
        L.append(f"| [`{name}`](#{name}) | {len(taxonomy(os.path.join(SECTORS, f)))} | {counts.get(name, 0)} |")
    L.append("")
    L.append("---")
    L.append("")

    gaps = []
    for f in files:
        name = f[:-3]
        rows = taxonomy(os.path.join(SECTORS, f))
        L.append(f"## {name}")
        L.append("")
        n = counts.get(name, 0)
        L.append(f"*{n} report{'' if n == 1 else 's'} in the collection.*")
        L.append("")
        L.append("| Category | Companies |")
        L.append("|---|---|")
        for cat, ex in rows:
            proper = [w for w in re.findall(r"\b[A-Z][A-Za-z&.\-]{2,}", ex)
                      if w not in ("The", "And", "Not", "An")]
            if not proper and cat not in NAMELESS_OK:
                gaps.append((name, cat))
                ex = f"{ex} — *no company named*"
            L.append(f"| **{cat}** | {ex} |")
        L.append("")

    if gaps:
        L.append("---")
        L.append("")
        L.append("## Categories with no company named")
        L.append("")
        L.append("Each is a category the skill can describe but cannot point at. Usually it means the")
        L.append("collection carries no report on that category — a gap in the corpus rather than in the")
        L.append("skill. Fill one from a report, never from general knowledge.")
        L.append("")
        for sec, cat in gaps:
            L.append(f"- **{sec}** — {cat}")
        L.append("")

    L.append("---")
    L.append("")
    L.append("Research and educational content only — **not investment advice**.")
    return "\n".join(L) + "\n"


def main():
    text = render()
    check = "--check" in sys.argv
    if check:
        if not os.path.exists(OUT):
            print("docs/COVERAGE.md missing — run: python3 scripts/build_coverage.py",
                  file=sys.stderr)
            return 1
        if open(OUT).read() != text:
            print("docs/COVERAGE.md is out of date — run: python3 scripts/build_coverage.py",
                  file=sys.stderr)
            return 1
        print("docs/COVERAGE.md is current.")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        fh.write(text)
    n = text.count("\n| **")
    print(f"Wrote docs/COVERAGE.md — {n} categories across "
          f"{len([l for l in text.splitlines() if l.startswith('## ') and l != '## Categories with no company named'])} sectors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
