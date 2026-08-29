#!/usr/bin/env python3
"""
Generate docs/COVERAGE.md and docs/COVERAGE.html — every sector, category and
company the skill knows.

Derived from the sector files, never hand-maintained. A hand-written coverage
list drifts the moment a sector file changes, and a stale one is worse than
none: it is the document people check before asking whether something is
covered.

    python3 scripts/build_coverage.py           # write both files
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
OUT_HTML = os.path.join(ROOT, "docs", "COVERAGE.html")

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


def to_html(md):
    """Render the coverage markdown as a single self-contained page.

    Deliberately minimal: this is a reference table people scan, so the job is
    legibility — readable measure, tabular figures, and a table that scrolls in
    its own container rather than pushing the page sideways on a phone.
    """
    import html as _h

    def inline(s):
        s = _h.escape(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"`([^`]+?)`", r"<code>\1</code>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    body, rows, in_code = [], [], False
    def flush():
        if not rows:
            return
        head, align, *data = rows
        body.append('<div class="tw"><table>')
        body.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>")
        body.append("<tbody>")
        for r in data:
            body.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
        body.append("</tbody></table></div>")
        rows.clear()

    for line in md.splitlines():
        if line.startswith("```"):
            flush()
            body.append("<pre><code>" if not in_code else "</code></pre>")
            in_code = not in_code
            continue
        if in_code:
            body.append(_h.escape(line))
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells):
                rows.append(cells)
            elif len(rows) == 1:
                rows.append(cells)
            continue
        flush()
        if m := re.match(r"^(#{1,3}) (.+)$", line):
            lvl = len(m.group(1))
            txt = m.group(2)
            slug = re.sub(r"[^a-z0-9]+", "-", txt.lower()).strip("-")
            body.append(f'<h{lvl} id="{slug}">{inline(txt)}</h{lvl}>')
        elif line.startswith("- "):
            body.append(f"<li>{inline(line[2:])}</li>")
        elif line.strip() == "---":
            body.append("<hr>")
        elif line.strip():
            body.append(f"<p>{inline(line)}</p>")
    flush()

    html_body = "\n".join(body)
    html_body = re.sub(r"(?:<li>.*?</li>\n?)+", lambda m: "<ul>" + m.group(0) + "</ul>", html_body)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Coverage &mdash; CB Research</title>
<style>
  :root {{
    --bg:#fbfaf8; --surface:#fff; --ink:#1c1a17; --muted:#6b6560;
    --line:#e6e1da; --accent:#8a5a2b; --accent-soft:#f6efe6;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:not([data-theme="light"]) {{
      --bg:#16150f; --surface:#1e1c16; --ink:#ece7dd; --muted:#9c948a;
      --line:#332f27; --accent:#d9a066; --accent-soft:#241f18;
    }}
  }}
  * {{ box-sizing:border-box; }}
  body {{
    margin:0; background:var(--bg); color:var(--ink);
    font:16px/1.65 ui-serif, Georgia, "Times New Roman", serif;
    padding:56px 24px 96px;
  }}
  main {{ max-width:60rem; margin:0 auto; }}
  h1 {{ font-size:2.1rem; line-height:1.15; margin:0 0 .4em; letter-spacing:-.015em; text-wrap:balance; }}
  h2 {{
    font-size:1.28rem; margin:2.8em 0 .5em; padding-bottom:.28em;
    border-bottom:1px solid var(--line); letter-spacing:-.01em;
    font-family:ui-monospace, SFMono-Regular, Menlo, monospace; color:var(--accent);
  }}
  h3 {{ font-size:1.02rem; margin:2em 0 .4em; }}
  p, li {{ color:var(--ink); max-width:65ch; }}
  em {{ color:var(--muted); }}
  ul {{ padding-left:1.15rem; }}
  li {{ margin:.2em 0; }}
  hr {{ border:0; border-top:1px solid var(--line); margin:3em 0; }}
  code {{
    font:0.86em/1.4 ui-monospace, SFMono-Regular, Menlo, monospace;
    background:var(--accent-soft); padding:.12em .38em; border-radius:3px;
  }}
  pre {{
    background:var(--surface); border:1px solid var(--line); border-radius:6px;
    padding:12px 14px; overflow-x:auto;
  }}
  pre code {{ background:none; padding:0; }}
  .tw {{ overflow-x:auto; margin:1.1em 0; }}
  table {{ border-collapse:collapse; width:100%; font-size:.92rem; font-variant-numeric:tabular-nums; }}
  th, td {{ text-align:left; padding:.5em .7em; border-bottom:1px solid var(--line); vertical-align:top; }}
  th {{
    font:600 .72rem/1.3 ui-sans-serif, system-ui, sans-serif;
    text-transform:uppercase; letter-spacing:.07em; color:var(--muted);
    border-bottom:1px solid var(--line); white-space:nowrap;
  }}
  tbody tr:last-child td {{ border-bottom:none; }}
  td:first-child {{ white-space:nowrap; }}
  a {{ color:var(--accent); text-decoration:none; border-bottom:1px solid transparent; }}
  a:hover, a:focus-visible {{ border-bottom-color:var(--accent); }}
  a:focus-visible {{ outline:2px solid var(--accent); outline-offset:3px; }}
</style>
</head>
<body>
<main>
{html_body}
</main>
</body>
</html>
"""


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
        if not os.path.exists(OUT_HTML) or open(OUT_HTML).read() != to_html(text):
            print("docs/COVERAGE.html is out of date — run: python3 scripts/build_coverage.py",
                  file=sys.stderr)
            return 1
        if open(OUT).read() != text:
            print("docs/COVERAGE.md is out of date — run: python3 scripts/build_coverage.py",
                  file=sys.stderr)
            return 1
        print("docs/COVERAGE.md and docs/COVERAGE.html are current.")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        fh.write(text)
    with open(OUT_HTML, "w") as fh:
        fh.write(to_html(text))
    n = text.count("\n| **")
    print(f"Wrote docs/COVERAGE.md — {n} categories across "
          f"{len([l for l in text.splitlines() if l.startswith('## ') and l != '## Categories with no company named'])} sectors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
