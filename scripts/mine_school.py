#!/usr/bin/env python3
"""
Extract the Q&A content from published reports, grouped by sector and by source.

Three different things live in the interactive panels, and they are not
interchangeable:

  school  — teaching the sector. Durable by intent, and the richest source.
  assist  — answering about the companies in THIS report, this quarter.
            Point-in-time by intent; take the mechanism, never the instance.
  quiz    — self-check items, with options and an explanation on reveal.

Merging them buries the school content inside a much larger volume of
report-specific Q&A, which is how it went unmined in the first place.

The collection's School and Assist panels carry hundreds of written
explanations — the author teaching a sector in their own words. That is the
richest source of sector knowledge in the corpus and the easiest to overlook,
because it sits in interactive panels rather than in the tables.

    python3 scripts/mine_school.py                 # summary by sector
    python3 scripts/mine_school.py <sector>        # the pairs for one sector
    python3 scripts/mine_school.py <sector> --durable   # only the conceptual ones

**What to take from it, and what to leave.** A question naming a company, a
period or a figure is point-in-time — the report answers it, and it does not
belong in a sector file. What belongs is the *mechanism* the answer explains:
why a CDMO's revenue steps up at commercialisation, why a carbon border tariff
lands on production route rather than volume, why an input-cost rise compresses
a downstream margin before it can be passed on. Those stay true next quarter.

Three markup conventions appear in the corpus, so all three are parsed:
DOM pairs, JS data arrays, and prompt-only chips (questions with no answer).
"""

import collections
import html
import importlib.util
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLISHED = os.path.join(ROOT, "reports", "published")

# Three different things live in these panels and they are NOT interchangeable:
#
#   school  — teaching the sector. Durable by intent; the richest source.
#   assist  — answering about the companies in THIS report, this quarter.
#             Point-in-time by intent; mine the mechanism, never the instance.
#   quiz    — self-check items, with options and an explanation.
#
# Merging them buries the school content inside a much larger volume of
# report-specific Q&A, which is how it went unmined.
SOURCES = [
    ("school", re.compile(r'class="school-q"[^>]*>(.*?)</div>\s*<div class="school-a"[^>]*>(.*?)</div>', re.S)),
    ("assist", re.compile(r'class="(?:cba2?-q|assist-q|qa-q)"[^>]*>(.*?)</div>\s*<div class="(?:cba2?-a|assist-a|qa-a)"[^>]*>(.*?)</div>', re.S)),
]
JS = re.compile(r'[{,]\s*q\s*:\s*([\'"`])(.*?)\1\s*,\s*a\s*:\s*([\'"`])(.*?)\3', re.S)
# Quiz items carry options and an explanation rather than a free-text answer,
# so they need their own pattern — a q/a matcher misses them entirely.
QUIZ = re.compile(
    r'\{\s*q\s*:\s*(["\'])(.*?)\1\s*,\s*opts\s*:\s*\[(.*?)\]\s*,'
    r'\s*correct\s*:\s*(\d+)\s*,\s*explain\s*:\s*(["\'])(.*?)\5', re.S)
POINT_IN_TIME = re.compile(r'₹|\d{2,}%|Q[1-4]\s?FY|\bFY\d\d')


def _clean(s):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", s)).split())


def _classify():
    spec = importlib.util.spec_from_file_location(
        "ac", os.path.join(ROOT, "scripts", "audit_corpus.py"))
    ac = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ac)
    return ac.classify


def mine():
    classify = _classify()
    out = collections.defaultdict(list)
    for f in sorted(os.listdir(PUBLISHED)):
        if not f.endswith(".html"):
            continue
        sec = classify(f)
        if not sec or sec.startswith("_"):
            continue
        raw = open(os.path.join(PUBLISHED, f), encoding="utf-8", errors="ignore").read()
        found = []
        for kind, pat in SOURCES:
            found += [(kind, _clean(q), _clean(a)) for q, a in pat.findall(raw)]
        found += [("assist", _clean(q), _clean(a)) for _, q, _, a in JS.findall(raw)]
        for _, q, opts, correct, _, explain in QUIZ.findall(raw):
            opts = [o.strip(" '\"") for o in re.split(r'["\']\s*,\s*["\']', opts.strip(" '\""))]
            try:
                answer = opts[int(correct)]
            except (ValueError, IndexError):
                answer = "?"
            found.append(("quiz", _clean(q),
                          f"ANSWER: {_clean(answer)} — {_clean(explain)}"))
        for kind, q, a in found:
            if 12 < len(q) < 200 and len(a) > 80:
                out[sec].append((q, a, f, kind))
    return out


def main():
    data = mine()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    durable_only = "--durable" in sys.argv

    if not args:
        total = sum(len(v) for v in data.values())
        print(f"{total} Q&A pairs across {len(data)} sectors\n")
        for s, v in sorted(data.items(), key=lambda x: -len(x[1])):
            by = collections.Counter(k for *_, k in v)
            dur = sum(1 for q, _, _, _ in v if not POINT_IN_TIME.search(q))
            kinds = " ".join(f"{k}:{n}" for k, n in by.most_common())
            print(f"  {s:16} {len(v):4}   ({dur} conceptual)   {kinds}")
        print("\nRun with a sector name to read its pairs.")
        return 0

    sec = args[0]
    if sec not in data:
        print(f"No Q&A found for '{sec}'. Sectors: {', '.join(sorted(data))}", file=sys.stderr)
        return 1
    for q, a, src, kind in data[sec]:
        if durable_only and POINT_IN_TIME.search(q):
            continue
        print(f"\n[{kind}] Q: {q}\nA: {a[:900]}\n   [{src}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
