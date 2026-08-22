# Output & Delivery Conventions

**This is the only file in the skill that names paths or tools.** Everything under `modes/` and
`sectors/` describes *what* to produce and deliberately says nothing about *where it goes* — so porting
this skill to another environment means editing this file alone, not fifteen mode files.

---

## Current target: Claude Code, in the `cauvery-business` repo

**Always save to:** `reports/staging/<Scope>_<Mode>_<Period>.html`

**Surface it with:** `SendUserFile`, so the artifact opens rather than sitting unnoticed on disk.

### Staging is not optional

`reports/published/` is the **published** collection — reports the author has verified and stands
behind. Generated output never lands there directly. It goes to `reports/staging/`, the author reviews
it, and **the author decides** whether it graduates.

This exists because generated analysis is exactly the kind of work that looks finished before it is.
Every figure needs a human check against the filings before it carries the author's name, and a report
that reaches subscribers unverified is a materially different risk from one used for private analysis.
Writing straight to the published folder would collapse that distinction silently.

So: **never write to `reports/published/`, and never move a file into it.** Promotion is the author's
action, not the skill's. If asked to "publish" or "finalise" a report, say what the promotion step is
and let them run it:

```bash
mv reports/staging/<file>.html reports/published/
```

## Filename convention

Match the existing report collection so files sort and scan together:

```
<Scope>_<Mode>_<Period>.html
```

- **Scope** — the company, the pair, or the sector/theme.
  `HDFCLife` · `HCL_TCS` · `Cement_Companies` · `All_Top_pvt_Banking`
- **Mode** — `Dashboard`, `Financials`, `Charts`, `SWOT`, `Verdict`, `BusinessProfile`, `Moats`, and so
  on. A full multi-section report is just `Dashboard` or `Report`.
- **Period** — `Q1FY27`, `Q4FY26`, `FY26`. Omit for analyses that aren't period-anchored (a moat thesis,
  a sector school).

Examples that match the existing collection:
`HDFCLife_Dashboard_Q1FY27.html` · `Cement_Companies_Dashboard_Q4FY26.html` ·
`HCL_TCS_Q1FY27_Analysis.html` · `Insurance_Metrics_School.html`

## When *not* to produce a file

**Producing no file is the default for questions** — see the router's Step 0, which decides this before
any mode loads. The rule is repeated here because this is where delivery lives:

If someone asks a question — "what's HDFC Life's VNB margin?", "what is embedded value?", "how did SBI
do?" — answer in chat with the same sourcing discipline. Forcing an HTML artifact onto a one-line
question wastes their time and buries the answer inside a file they have to open.

Build the file when the request is for something to keep, share, or publish. When genuinely ambiguous,
give a short inline answer and offer the artifact.

**Learning sessions are conversations.** Someone working through what a sector's metrics mean may ask
many questions in a row; each gets a prose answer, not a file. Build the reference artifact only if they
ask for something to keep.

## After delivering

Keep the accompanying chat message short — one to four sentences of the headline story. The artifact
carries the detail; restating it in chat duplicates work the reader has to do twice. Don't drop a file
silently either: a sentence of framing tells them what they're about to look at.

## Check for an existing report first

**Before analysing any company or sector, look in `reports/published/` for a report that already covers
it.** One command:

```bash
ls reports/published/ | grep -i <company or sector>
```

This is worth doing every time, for two reasons that are easy to miss:

1. **It may already exist.** Building a second artifact on a company the author already published is
   wasted work, and worse, it produces two documents that may not agree.
2. **A published report is author-verified.** Every figure in `reports/published/` has been checked
   against filings by a human before promotion. That makes it a **cross-check available nowhere else** —
   if your sourced figure disagrees with the published one for the same period, that disagreement is
   itself the finding, and worth surfacing rather than quietly resolving.

### Give the reader the link

A published report is not just a cross-check for you — it is **the thing the reader most likely wants**.
Every file in the published collection is live on the author's site at the collection's base URL plus the
filename, so a local file maps directly to a link the reader can open:

```bash
grep -i <company or sector> docs/report_dashboard_urls.txt
```

**When answering in chat about something the collection already covers, name the report and give its
link before adding your own analysis.** A reader who asked "what's the difference between X and Y" and
was handed a fresh explanation, when a published dashboard on exactly that question exists, was given
less than they had. Worse, an answer composed independently can differ from the published one in emphasis
or detail, which leaves the author's own two sources disagreeing.

**Conceptual questions are the ones this catches.** "How does this sector work", "what's the difference
between these two structures", "why does this metric matter" — these feel like pure sector-file
territory, which is exactly why the collection goes unchecked. If a published explainer covers it, lead
with it.

**What to do with what you find:**

- **Same period, same scope** — say so before building anything. Offer to summarise the existing report,
  or to build only what it lacks, rather than duplicating it.
- **Earlier period** — use it for continuity (see below), and treat its figures as a *prior-period*
  reference, not as current data.
- **Adjacent scope** — a sector report covering the company, or a peer report — read it for the author's
  framing and section choices even if you build something different.

**The cross-check is one-directional.** A published report is good evidence that a figure was verified;
it is not a substitute for sourcing the current period yourself. Never copy a number from it into a new
report — see below.

## Prior-report continuity

When regenerating an existing report for a new period, read the previous file from
`reports/published/` first — the **published** collection, since those are the versions the author
verified and stands behind. Prefer a published prior over a staged one; a staged draft may contain
figures nobody has checked yet, and inheriting its structure risks inheriting its unreviewed choices.
Take from it: company scope, section selection, layout choice, chart types, and any sector-specific
sections the author added.

Take **no figures from it.** Every number is re-sourced live for the current period. Inheriting numbers
from a prior artifact is precisely how a stale ratio propagates quarter after quarter.

## Porting to another environment

Only this file changes. Substitute the save location and the file-delivery mechanism:

| Environment | Save location | Delivery |
|---|---|---|
| Claude Code (current) | `reports/staging/` (never the published folder) | `SendUserFile` |
| claude.ai | `/mnt/user-data/outputs/` | `present_files` |
| ChatGPT / Gemini | the environment's file output | that platform's download/attachment affordance |
| No filesystem | — | emit the HTML inline in the response |

If no file-delivery affordance exists at all, state the saved path plainly so the reader can find it.
