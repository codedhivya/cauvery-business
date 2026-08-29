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
    "Grinding-only / split unit", "Commercial / lease developer",
    "Hyperlocal / last-mile", "Contract logistics & warehousing",
    "REIT — Hospitality", "InvIT — Logistics & warehousing",
}

# Words that mark a fragment as a description of a company type rather than a
# company. "listed hospital chains" and "the branded-foods majors" name nobody:
# a reader cannot look them up, and they cannot seed a peer set.
# Deliberately case-SENSITIVE. These words appear inside real company names
# ("Nexus Select Trust", "Container Corporation"), so only the lowercase form
# marks a description.
_DESC = re.compile(
    r"\b(majors?|players?|businesses|operators?|chains?|makers?|manufacturers?|"
    r"producers?|entrants?|arms?|similar|firms?|mills?|spinners?|utilities|"
    r"companies|providers?|platforms?|insurers?|trusts?|recyclers?|units?|"
    r"the commodity portion|and the|and listed|of the above)\b")


# Gaps that have been reviewed and accepted: the collection carries no report
# on these, so there is no company to name without inventing one. Anything NOT
# on this list failing the name test is a regression — see --strict.
KNOWN_GAPS = {
    ("chemicals", "Commodity chemicals"),
    ("pharma-health", "Diagnostics"),
    ("reit-invit", "InvIT — Pipelines / energy"),
    ("reit-invit", "InvIT — Private placement"),
}


def named_companies(ex):
    """The fragments of an examples cell that actually name a company."""
    out = []
    for frag in re.split(r"[;,]|\band\b", ex):
        frag = frag.strip(" .")
        if not frag or not frag[0].isupper() or _DESC.search(frag):
            continue
        out.append(frag)
    return out


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
    sub = bool(sub)
    out, ex_col = [], None
    for line in block.splitlines():
        if not line.startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        # Locate the Examples column from the header. Not every taxonomy has one
        # — reit-invit's sub-category table ends in a note, and rendering a note
        # as a company list is worse than rendering nothing.
        if ex_col is None and not cells[0].startswith("**"):
            for i, c in enumerate(cells):
                if c.lower().startswith("example"):
                    ex_col = i
            if ex_col is None:
                ex_col = -1          # header seen, no Examples column
            continue
        if not cells[0].startswith("**"):
            continue
        cat = cells[0].strip("*").strip()
        # Some taxonomies group first (reit-invit: Vehicle | Sub-category | ... ).
        # Name the row for the sub-category, qualified by its group, or every
        # row in the group renders under the same heading.
        if sub and len(cells) > 2 and ex_col not in (1, None):
            cat = f"{cat} — {cells[1].strip('*').strip()}"
        ex = "" if ex_col in (None, -1) or ex_col >= len(cells) else cells[ex_col]
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
            named = named_companies(ex)
            if named:
                # Show only the names. The descriptive remainder ("and the
                # integrated sugar mills") reads as a company here and is not one.
                cell = ", ".join(named)
            elif cat in NAMELESS_OK:
                cell = "*no separate listed company — see the sector file*"
            else:
                gaps.append((name, cat))
                cell = "*none named — see below*"
            L.append(f"| **{cat}** | {cell} |")
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


def unnamed(gaps=None):
    """(sector, category) pairs whose Examples column names no company."""
    out = []
    for f in sorted(os.listdir(SECTORS)):
        if not f.endswith(".md") or f == "_template.md":
            continue
        for cat, ex in taxonomy(os.path.join(SECTORS, f)):
            if cat in NAMELESS_OK:
                continue
            if not named_companies(ex):
                out.append((f[:-3], cat))
    return out


def main():
    if "--strict" in sys.argv:
        new = [g for g in unnamed() if g not in KNOWN_GAPS]
        if new:
            print("Categories naming no company, not in KNOWN_GAPS:", file=sys.stderr)
            for sec, cat in new:
                print(f"  {sec} — {cat}", file=sys.stderr)
            print("\nAn Examples column must name companies, not describe them.",
                  file=sys.stderr)
            print("Fill it from a report, or record it in KNOWN_GAPS with a reason.",
                  file=sys.stderr)
            return 1
        stale = [g for g in KNOWN_GAPS if g not in unnamed()]
        if stale:
            print("KNOWN_GAPS entries that are now filled — remove them:", file=sys.stderr)
            for sec, cat in stale:
                print(f"  {sec} — {cat}", file=sys.stderr)
            return 1
        print(f"All Examples columns name companies ({len(KNOWN_GAPS)} accepted gaps).")
        return 0

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
