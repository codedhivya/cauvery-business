---
name: corpus-sync
description: Syncs the CB Research published collection and folds new knowledge into the sector-financial-analysis skill. Runs the whole loop — pull new reports from the live site or a saved portal page, classify them, mine each new report for sectors, metrics, sections and CSS the skill lacks, apply what belongs, and verify. Use whenever the user says reports have been published, asks to sync or refresh the corpus, mentions a new portal page or a moved site, asks whether the skill covers a newly published company, or asks to update the skill from the reports. Also use for a periodic check that the mirror and the skill are current.
---

# Corpus Sync

Keeps two things in step: the local mirror of the published collection, and the sector knowledge in
`sector-financial-analysis`. When reports are published and neither is updated, the skill silently lacks
what the author already knows.

**The loop is: pull → classify → mine → apply → verify → baseline.** Steps 1, 2 and 6 are mechanical.
**Steps 3 and 4 are the work** — the scripts flag *that* something is new, never *what it means*.

---

## Step 1 — Pull

```bash
python3 scripts/sync_reports.py
```

Reads the live index and downloads only what is missing. If the user has saved a portal page, pass it —
a saved page is authoritative about its own base URL, which matters because **the collection has moved
host before**:

```bash
python3 scripts/sync_reports.py <path to saved page>
```

**If every download fails at once, the site has moved** — check the base URL the script reports against
the hrefs in the page. That failure looks like a dead site and is not one.

**A 404 on a few files is different**: those are broken links on the site itself, which members hit too.
Report them to the user; they are fixable only at the source.

## Step 2 — Classify

```bash
python3 scripts/audit_corpus.py
```

Anything landing in **`unclassified`** is usually a keyword gap, not a missing sector. Check the report's
own header for the sector it claims before concluding otherwise. Extend `SECTOR_KEYWORDS` in the script
for a keyword gap.

**Two traps, both seen in practice:**

- **Order carries meaning.** First match wins, so a multi-sector dashboard must be matched before the
  single-sector lists — otherwise one company name in the filename claims a report covering four
  unrelated sectors.
- **Substrings over-match.** A bare keyword can capture an unrelated filename. Prefer a distinctive
  fragment.

**A genuinely new sector is rare and is the user's call** — see *Adding a sector* below.

## Step 3 — Mine each new report

**This is the step that cannot be automated, and the one that carries the value.** The scripts compare
strings; they cannot tell whether a new metric deserves a definition or was a one-off.

For each new report, read it and ask:

1. **Does its taxonomy match the sector file's?** Lift the taxonomy from **how the report compares its
   subjects**, not from how they could plausibly be sorted. A sector file organised on the wrong axis
   passes every structural check and still loses the insight.
2. **Does it name a business model the sector file doesn't?** A sector built from its largest reports
   will have skipped whatever a single distinct report covers.
3. **Are its metrics defined?** Ignore incidental mentions; add what the sector genuinely needs.
4. **Does it use a section no mode covers?** If it appears across several sectors it is mode-level
   craft; if it is bespoke editorial, leave it to the author.
5. **Does it teach something worth a `school` entry, or an explainer?**
6. **Are its CSS classes defined?** Cross-sector ones belong in `design-system.md`.

**Categories naming no real company** are flagged by `audit_corpus.py`. Fill them from a report —
**never from general knowledge**, which is a lower bar than everything else in the file.

## Step 4 — Apply

Edit the sector files, mode files or `design-system.md`. Two rules that are easy to break here:

- **Never copy a figure into a reference file.** Sector files hold durable facts — definitions,
  benchmarks, regulator rules, palettes. A company number or a period literal in `references/` is a
  stale figure waiting to be served. Regulator rules *are* allowed and should carry an **as-at date**.
- **No sector metric may enter a mode file.** That contract is what keeps adding a sector a one-file job.

Ask the user when the judgment is genuinely theirs: a new sector, a taxonomy that contradicts the
existing one, or a metric that may be a deliberate one-off. **Do not ask about things the corpus already
settles** — check first.

## Step 5 — Verify

```bash
python3 scripts/verify_skill.py
```

Must pass before baselining. It checks the structural contracts, per-sector completeness, that each
sector still carries its defining insight, and that every refusal survives.

## Step 6 — Baseline

```bash
python3 scripts/audit_corpus.py --accept
```

Only after the findings have actually been reviewed. Baselining unreviewed reports marks work as done
that was never done, and the next run will not flag it again.

---

## Adding a sector

Rare, and the user decides. Justified when a report describes a business the existing files cannot
analyse — not merely a company they do not name.

1. Copy `references/sectors/_template.md`
2. Fill it from the report: taxonomy, metrics, benchmarks, regulator, per-mode specifics, palette
3. Add a row to the router's sector table in `SKILL.md`, and extend the description's sector list
   — **the description has a 1024-character limit and is usually near it**
4. Add keywords to `SECTOR_KEYWORDS`
5. Update the sector-count checks in `verify_skill.py` and add a content check for its defining insight
6. Update the counts in `AGENTS.md`, `README.md` and `MAINTENANCE.md`

**No mode file should change.** If a sector seems to need one edited, it needs a substitution declared in
its own file instead.

## Reporting back

Tell the user: how many reports arrived, what was folded in and where, what was **deliberately left**
and why, and anything needing their decision. **Findings left unapplied are worth more said than
silently dropped** — especially a gap in the corpus itself, like a category with no report behind it.
