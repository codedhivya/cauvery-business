#!/usr/bin/env python3
"""
Flatten the published report collection into one greppable text file.

The reports are large, bilingual HTML with charts, scripts and nested markup.
Answering "what does the collection already say about X" meant stripping several
of them at read time — expensive, and repeated for every question. This builds
that once:

    python3 scripts/build_corpus_index.py

    docs/corpus-index.txt     one line per fragment, each prefixed by its report

Then a lookup is a single grep:

    grep -i 'kleros' docs/corpus-index.txt
    grep -i 'mundra' docs/corpus-index.txt | cut -d'|' -f1 | sort -u   # which reports

**The index is DERIVED, and it is a FINDING AID rather than a source.** It tells
you which report carries a fact; the report itself is what you read and cite.
Never edit it, and never quote it as the source of a figure — a fragment here has
lost its table, its footnote and its as-of date. Regenerate after every sync.

Two things about this collection make a naive strip fail, both found by testing
rather than by reading the markup:

1. **Most reports build their content in JavaScript.** Several are 80-94% script
   by bytes, with tables, rankings and Q&A panels held in data arrays. Dropping
   <script> indexes only the page shell — a report can look indexed and carry
   almost none of its own numbers. So string literals inside <script> are
   harvested too, after the same cleaning as the DOM text.
2. **The reports are bilingual.** Removing Tamil characters mid-line leaves the
   Tamil sentence behind as mangled punctuation and stray figures, which greps as
   a duplicate hit. A line that contains Tamil is therefore dropped whole, since
   it is a translation of the adjacent English. Pass --keep-tamil to index it.
"""

import argparse
import collections
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLISHED = os.path.join(ROOT, "reports", "published")
INDEX = os.path.join(ROOT, "docs", "corpus-index.txt")

# Contents are markup or behaviour, not prose. <script> is handled separately —
# see harvest_scripts — because this collection keeps its data there.
DROP_ELEMENTS = re.compile(r"<(style|svg|noscript|template)\b.*?</\1\s*>", re.S | re.I)
SCRIPTS = re.compile(r"<script\b[^>]*>(.*?)</script\s*>", re.S | re.I)
COMMENTS = re.compile(r"<!--.*?-->", re.S)

# Block-level boundaries become line breaks, so a grep hit lands on its own row
# rather than in the middle of a 40KB paragraph. <span> is included because the
# bilingual pattern is <span class="lang-en">…</span><span class="lang-ta">…</span>
# — without the split, English and Tamil share a line.
BLOCK_BOUNDARY = re.compile(
    r"</?(div|p|tr|li|ul|ol|h[1-6]|section|article|header|footer|nav|table|"
    r"thead|tbody|br|hr|option|button|span)\b[^>]*>",
    re.I,
)

# Table cells are joined into their row rather than split onto separate lines.
# A cell is often a bare entity — <td>Mundra</td> is six characters and would be
# dropped by the minimum-length floor, losing exactly the name someone greps for.
# Kept as a row it reads "Mundra · Gujarat · 4,620 MW · ..." and carries context.
CELL_BOUNDARY = re.compile(r"</(td|th)\s*>", re.I)

TAG = re.compile(r"<[^>]+>")
TAMIL = re.compile(r"[஀-௿]")
WS = re.compile(r"[ \t\xa0]+")

# Shorter than this and a line is almost always chrome — a nav label, a lone icon,
# a table header. The threshold is low on purpose: "P/E (TTM) 30.16x" is 16 chars
# and is exactly the kind of fact worth finding.
MIN_LINE = 12

# Long prose gets wrapped so grep output stays readable in a terminal.
WRAP_AT = 400

# A report this thin almost certainly failed to parse rather than being short.
THIN_REPORT = 20

# JS string literals that are code rather than content: selectors, classes, URLs,
# colours, format strings, single identifiers.
CODE_LITERAL = re.compile(
    r"^(?:[\w.#-]+|#[0-9a-fA-F]{3,8}|\W+)$"          # one token, colour, punctuation
    r"|^(?:https?:|mailto:|data:|/|\./|\.\./)"        # urls and paths
    r"|[{}$<>]=|=>|function\s*\(|\bvar\b|\bconst\b",  # code fragments
)
ESCAPES = [("\\n", " "), ("\\t", " "), ("\\r", " "),
           ('\\"', '"'), ("\\'", "'"), ("\\`", "`"), ("\\\\", "\\")]
UNICODE_ESCAPE = re.compile(r"\\u([0-9a-fA-F]{4})")

# Chart and animation config objects share the {key: value} shape with data rows
# but carry no facts.
CONFIG_KEYS = re.compile(
    r"\b(behavior|duration|easing|responsive|maintainAspectRatio|borderWidth|"
    r"backgroundColor|borderColor|tension|padding|display|beginAtZero|fontSize|"
    r"scales|legend|tooltip|gridLines|animation)\b")


def clean_line(line, keep_tamil):
    """Normalise one candidate line, or return None to drop it."""
    if not keep_tamil and len(TAMIL.findall(line)) >= 2:
        # A translation of the adjacent English line. Dropping it whole avoids the
        # mangled residue that stripping the characters alone would leave.
        return None
    line = WS.sub(" ", line).strip()
    if len(line) < MIN_LINE:
        return None
    if not re.search(r"[A-Za-z0-9]", line):
        return None
    return line


def wrap(line):
    """Split an over-long line at sentence, then word, boundaries."""
    if len(line) <= WRAP_AT:
        return [line]
    out, current = [], ""
    for piece in re.split(r"(?<=[.;·])\s+", line):
        while len(piece) > WRAP_AT:
            cut = piece.rfind(" ", 0, WRAP_AT)
            cut = cut if cut > WRAP_AT // 2 else WRAP_AT
            out.append(piece[:cut].strip())
            piece = piece[cut:].strip()
        if not piece:
            continue
        if len(current) + len(piece) + 1 > WRAP_AT:
            if current:
                out.append(current)
            current = piece
        else:
            current = f"{current} {piece}".strip()
    if current:
        out.append(current)
    return out


def strip_markup(text):
    """HTML fragment -> text with block tags turned into line breaks."""
    text = CELL_BOUNDARY.sub(" \u00b7 ", text)
    text = BLOCK_BOUNDARY.sub("\n", text)
    text = TAG.sub(" ", text)
    text = html.unescape(text)
    # Tidy separators left where a cell was empty or the row ended.
    return re.sub(r"(?:\s*\u00b7\s*)+", " \u00b7 ", text)


def _unescape_js(s):
    for a, b in ESCAPES:
        s = s.replace(a, b)
    return UNICODE_ESCAPE.sub(lambda m: chr(int(m.group(1), 16)), s)


def harvest_scripts(raw):
    """Content held in JS data: string literals, and flat data objects.

    Most reports in this collection render their tables, rankings and Q&A panels
    from JavaScript. Without this, those reports index only their page shell.

    Objects are harvested as well as strings because the numbers live unquoted:
    a row reading {bank:'ICICI Bank', usd:17.88, share:'14-18%'} yields the bank
    name from the strings alone, and the figure only from the object. The upper
    length bound is generous — a single answer string in a Q&A array runs well
    past a thousand characters, and wrapping handles the length later.
    """
    out = []
    for block in SCRIPTS.findall(raw):
        for _, literal in re.findall(r"([\"'`])((?:[^\"'`\\]|\\.){8,4000}?)\1", block):
            literal = _unescape_js(literal)
            if CODE_LITERAL.search(literal.strip()):
                continue
            if not re.search(r"[A-Za-z]{3}", literal):
                continue
            out.extend(strip_markup(literal).split("\n"))

        # Flat {key: value} rows — the data tables behind the rendered page.
        for obj in re.findall(r"\{[^{}]{20,2000}\}", block):
            if obj.count(":") < 2 or not re.search(r"[A-Za-z]{3}", obj):
                continue
            if CONFIG_KEYS.search(obj):
                continue
            flat = re.sub(r"[\"'`]", " ", _unescape_js(obj).strip("{}"))
            flat = re.sub(r"\s+", " ", flat).strip()
            if len(flat) >= 25:
                out.extend(strip_markup(flat).split("\n"))
    return out


def flatten(raw, keep_tamil=False):
    """One report's HTML -> clean text lines, DOM first then script content."""
    body = COMMENTS.sub(" ", DROP_ELEMENTS.sub(" ", raw))
    body = SCRIPTS.sub(" ", body)
    candidates = strip_markup(body).split("\n") + harvest_scripts(raw)

    lines, seen = [], set()
    for candidate in candidates:
        line = clean_line(candidate, keep_tamil)
        if line is None:
            continue
        # Exact duplicates are dropped per report, not merely consecutive ones:
        # JS template strings and repeated bilingual pills recur far apart, and a
        # finding aid gains nothing from the second copy.
        for piece in wrap(line):
            if piece in seen:
                continue
            seen.add(piece)
            lines.append(piece)
    return lines


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--keep-tamil", action="store_true",
                    help="index the Tamil text too (roughly doubles the index)")
    ap.add_argument("--out", default=INDEX, help="index path")
    args = ap.parse_args()

    if not os.path.isdir(PUBLISHED):
        print(f"No published collection at {PUBLISHED}", file=sys.stderr)
        return 1
    reports = sorted(f for f in os.listdir(PUBLISHED) if f.endswith(".html"))
    if not reports:
        print("No reports to index. Run scripts/sync_reports.py first.", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    counts = collections.Counter()

    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write("# DERIVED — generated by scripts/build_corpus_index.py. Do not edit.\n")
        fh.write("# A FINDING AID, not a source: it says which report carries a fact.\n")
        fh.write("# Read and cite the report itself — a fragment here has lost its\n")
        fh.write("# table, its footnote and its as-of date. Stale after every sync.\n")
        fh.write("# Format: <report.html> | <text>\n")
        fh.write(f"# {len(reports)} reports"
                 f"{' · Tamil kept' if args.keep_tamil else ' · Tamil dropped'}\n")
        for name in reports:
            with open(os.path.join(PUBLISHED, name), encoding="utf-8",
                      errors="replace") as src:
                raw = src.read()
            for line in flatten(raw, args.keep_tamil):
                fh.write(f"{name} | {line}\n")
                counts[name] += 1

    size = os.path.getsize(args.out)
    print(f"Indexed {len(reports)} reports -> {os.path.relpath(args.out, ROOT)}")
    print(f"  {sum(counts.values()):,} lines · {size / 1_048_576:.1f} MB")

    # A report that parsed to almost nothing looks like success in the totals.
    empty = [r for r in reports if counts[r] == 0]
    thin = [(r, counts[r]) for r in reports if 0 < counts[r] < THIN_REPORT]
    if empty:
        print(f"\n  WARNING — {len(empty)} report(s) produced no lines:", file=sys.stderr)
        for r in empty:
            print(f"    {r}", file=sys.stderr)
    if thin:
        print(f"\n  {len(thin)} report(s) under {THIN_REPORT} lines — check the parse:")
        for r, n in sorted(thin, key=lambda x: x[1]):
            print(f"    {n:4}  {r}")

    print("\nLook something up:")
    print("  grep -i '<term>' docs/corpus-index.txt")
    print("  grep -i '<term>' docs/corpus-index.txt | cut -d'|' -f1 | sort -u")
    return 1 if empty else 0


if __name__ == "__main__":
    sys.exit(main())
