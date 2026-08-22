#!/usr/bin/env python3
"""
Sync reports/published/ from the CB Research site.

The published collection is a local mirror of the Pages site. When new reports
are added there the mirror falls behind — and since the skill's sector files
were built from that mirror, anything it hasn't seen is knowledge the skill
doesn't have.

By default this reads the live index at the Pages site, so no browser step is
needed. The index builds its links in JavaScript, so the report list is parsed
from the embedded `file:` entries rather than from href attributes.

    python3 scripts/sync_reports.py                 # read the live site
    python3 scripts/sync_reports.py <saved.html>    # or a saved portal page

It downloads only the files missing locally, rewrites docs/report_dashboard_urls.txt,
and reports anything it could not fetch — a 404 there is a broken link on the
site that members hit too.

Then run audit_corpus.py to find out whether the new reports introduce a
sector, metric or section the skill doesn't cover.

Exit 0 = in sync or all downloaded, 1 = something failed to download.
"""

import os
import re
import sys
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLISHED = os.path.join(ROOT, "reports", "published")
URL_LIST = os.path.join(ROOT, "docs", "report_dashboard_urls.txt")
BASE = "https://elangocauvery.github.io/CB-Finance/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Template placeholders in the page's JS, not real reports.
NOT_REPORTS = {"filename.html"}


def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def report_names(html):
    """Report filenames, from JS `file:` entries and from plain hrefs."""
    names = set(re.findall(r'file:\s*["\']([^"\']+\.html)["\']', html))
    names |= {urllib.parse.unquote(u.split("/")[-1])
              for u in re.findall(r'href="(' + re.escape(BASE) + r'[^"]+\.html)"', html)}
    return sorted(n for n in names if n not in NOT_REPORTS)


def main():
    if len(sys.argv) > 1:
        src = sys.argv[1]
        if not os.path.isfile(src):
            print(f"error: {src} not found", file=sys.stderr)
            return 2
        html = open(src, encoding="utf-8", errors="ignore").read()
        print(f"Reading saved page: {os.path.basename(src)}")
    else:
        print(f"Reading live index: {BASE}")
        try:
            html = fetch(BASE).decode("utf-8", "ignore")
        except Exception as e:
            print(f"error: could not fetch the index — {e}", file=sys.stderr)
            return 2

    names = report_names(html)
    if not names:
        print("No report links found.", file=sys.stderr)
        return 2

    os.makedirs(os.path.dirname(URL_LIST), exist_ok=True)
    with open(URL_LIST, "w") as fh:
        fh.write("\n".join(BASE + urllib.parse.quote(n) for n in names) + "\n")

    os.makedirs(PUBLISHED, exist_ok=True)
    have = {f for f in os.listdir(PUBLISHED) if f.endswith(".html")}
    missing = [n for n in names if n not in have]

    print(f"Site lists {len(names)} reports · {len(have)} already local · "
          f"{len(missing)} to fetch\n")

    if not missing:
        print("Already in sync.")
        return 0

    ok, failed = [], []
    for i, name in enumerate(missing, 1):
        try:
            data = fetch(BASE + urllib.parse.quote(name))
            with open(os.path.join(PUBLISHED, name), "wb") as fh:
                fh.write(data)
            ok.append(name)
            print(f"  [{i}/{len(missing)}] + {name}")
        except Exception as e:
            failed.append((name, str(e)))
            print(f"  [{i}/{len(missing)}] ✗ {name} — {e}")

    print(f"\nDownloaded {len(ok)}, failed {len(failed)}.")
    if failed:
        print("\nFailed — linked from the site but not present on it.")
        print("A 404 is a broken link members would also hit:")
        for name, err in failed:
            print(f"  {name}: {err}")

    print("\nNext: python3 scripts/audit_corpus.py")
    print("  — whether the new reports introduce a sector, metric or section")
    print("    the skill doesn't cover. Findings are advisory.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
