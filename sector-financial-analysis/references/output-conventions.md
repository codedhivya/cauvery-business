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
