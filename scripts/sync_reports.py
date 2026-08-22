#!/usr/bin/env python3
"""
Sync reports/published/ from the CB Research member portal.

The published collection is a local mirror of the Pages site. When new reports
are added there, the mirror falls behind — and the skill's sector files are
built from that mirror, so anything it hasn't seen is knowledge the skill
doesn't have.

This does three things in one pass:
  1. extracts every report URL from a saved copy of the member portal page
  2. downloads only the files missing locally (existing ones are left alone)
  3. reports what arrived, and what could not be fetched

Then run audit_corpus.py to find out whether the new reports introduce
anything the skill lacks.

    # save the member portal page from your browser, then:
    python3 scripts/sync_reports.py ~/Downloads/"CB Research — Member Portal.html"
    python3 scripts/audit_corpus.py

Exit 0 = nothing new or all downloaded, 1 = something failed to download.
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


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    portal = sys.argv[1]
    if not os.path.isfile(portal):
        print(f"error: {portal} not found", file=sys.stderr)
        return 2

    html = open(portal, encoding="utf-8", errors="ignore").read()
    urls = sorted(set(re.findall(
        r'href="(' + re.escape(BASE) + r'[^"]+\.html)"', html)))
    if not urls:
        print("No report links found. Is that the member portal page?", file=sys.stderr)
        return 2

    os.makedirs(os.path.dirname(URL_LIST), exist_ok=True)
    with open(URL_LIST, "w") as fh:
        fh.write("\n".join(urls) + "\n")

    os.makedirs(PUBLISHED, exist_ok=True)
    have = {f for f in os.listdir(PUBLISHED) if f.endswith(".html")}
    wanted = {urllib.parse.unquote(u.split("/")[-1]): u for u in urls}
    missing = {n: u for n, u in wanted.items() if n not in have}

    print(f"Portal lists {len(urls)} reports · {len(have)} already local · "
          f"{len(missing)} to fetch\n")

    if not missing:
        print("Already in sync. Nothing to download.")
        return 0

    ok, failed = [], []
    for i, (name, url) in enumerate(sorted(missing.items()), 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            with open(os.path.join(PUBLISHED, name), "wb") as fh:
                fh.write(data)
            ok.append(name)
            print(f"  [{i}/{len(missing)}] + {name}")
        except Exception as e:
            failed.append((name, str(e)))
            print(f"  [{i}/{len(missing)}] ✗ {name} — {e}")

    print(f"\nDownloaded {len(ok)}, failed {len(failed)}.")
    if failed:
        print("\nFailed — these are linked from the portal but not on the site.")
        print("A 404 means a broken link members would also hit:")
        for name, err in failed:
            print(f"  {name}: {err}")

    print("\nNext: python3 scripts/audit_corpus.py")
    print("  — tells you whether the new reports introduce a sector, metric or")
    print("    section the skill doesn't yet cover. Findings are advisory.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
