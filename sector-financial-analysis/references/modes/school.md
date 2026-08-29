# Mode: School — Teaching How to Read a Sector's Numbers

A teaching mode. It can run standalone as pure education, but it becomes much stronger grounded in a real
company's actual figures — concrete numbers teach faster than invented placeholders, and a reader who has
just worked through a real balance sheet remembers the metric.

Read the loaded sector file in full before writing: it holds the metric definitions, the sector's
explanatory analogy, and the benchmarks. It is the canonical source, so every explanation stays
consistent with how the same metric is described in every other artifact.

## Step 1 — Match depth to the ask

- **A single concept question** ("what does this metric actually measure?") → answer directly in chat:
  one or two paragraphs, the sector's analogy, one small worked example. Don't force an HTML artifact
  onto a one-term question.
- **A full reference guide** — someone wanting the whole metric system, studying the sector, or asking
  for a cheat-sheet → build the artifact.
- **Personalised** — where a company is named or already under discussion, pull its real disclosed
  figures into the worked examples instead of generic ones.

## Step 2 — Structure the full artifact

**Teach the sector, then supply the reference — in that order.** A metric card explains what a number
means; it cannot explain why anyone measures that number rather than another. A reader who has only the
cards can look things up but cannot reason, and will misread the first company that doesn't fit the
template.

So the artifact has two layers, and the narrative layer comes first.

### Layer 1 — the understanding arc

Six steps, each answering the question the previous one raises. **This is the sector file's own sections
1 to 5 turned into a path**, so it needs no new research — only sequencing.

1. **What does this sector actually sell, and to whom?** One or two paragraphs, no metrics yet. A reader
   who cannot say what the business does has nothing to hang a ratio on.

2. **Why is it split into these categories?** — *the highest-value step, and the one most often skipped.*
   Every sector file opens by insisting on classification before analysis, because **the categories are
   measured on different bases and a metric that is central to one is meaningless in another**. Make that
   concrete with the sector's own example: a bank has no EBITDA, a trust is not scored on PAT, an
   asset-light logistics platform and an integrator do not share a margin band. **A reader who takes only
   one thing away should take this.**

3. **How does each category make money?** The revenue chain, stated plainly — what is sold, what it
   costs, where the margin sits, and which part is fixed versus variable. Every metric in step 4 should
   be traceable to a link in this chain.

4. **So which numbers matter, and why those?** Now introduce the metrics — **derived from step 3, not
   listed**. "Why this sector uses X rather than profit" teaches more than a definition of X ever does.
   Where the sector file carries an analogy table, this is where it earns its place.

5. **What does good look like?** Benchmarks, always **by category**, with the reason behind the band. A
   number is neither good nor bad in isolation, and a reader who learns a threshold without its reason
   will apply it to the wrong category.

6. **What goes wrong, and what is the tell?** The sector's failure modes and the early signal for each —
   the receivable that lengthens, the collection efficiency that dips, the pledge that rises. **This is
   what separates a reader who can use the numbers from one who can only recite them.**

### Layer 2 — the reference

Built to be jumped into, not read through, because that is how it is used after the first pass:

- **Metric cards**, grouped by category and each self-contained: short code, full name, one-line analogy,
  plain-English "what it is" and formula, and **a worked example using a named company's real disclosed
  figures**, ending with what the result means *for that company*.
- **A "what to watch" quick-reference** by category.
- **Regulatory quick-reference** where the sector has rules a reader needs, with as-at dates.
- **A "read a company in 60 seconds" checklist** — five yes/no questions per category.

### Teaching a single category

When the ask is one category rather than a whole sector — quick commerce, gold-loan NBFCs, transmission
InvITs — run the same arc scoped to it, and **keep step 2**. Its value inverts but does not disappear:
instead of why the sector splits, it becomes **why this category is not like its neighbours**, which is
exactly what a reader focused on one category most needs and is least likely to be told.

## Step 3 — Pedagogy

- **Never introduce a metric before the business that produces it.** This is the arc's whole point. Where
  a sector books its costs today and earns its profit over decades, its headline metric only makes sense
  once the reader knows that; met earlier, it is a definition to memorise rather than something to
  understand.
- **Define a term before using it elsewhere.** Don't explain metric B using metric A if A comes later.
- Prefer one concrete worked example to an abstract formula.
- Keep each metric card standalone — readers jump straight to the metric confusing them, and shouldn't
  need the preceding cards to make sense of it.
- Teach interpretation, not conclusions. The goal is a reader who can judge the numbers themselves, not
  one who defers to this artifact.
- **Say what the metric cannot tell you.** Every metric has a blind spot — occupancy says nothing about
  tenant concentration, a headline yield says nothing about how much of it is capital returning. Naming
  the limit is what stops a reader over-reading a single number, and it is the difference between
  teaching a metric and teaching judgement.

## Step 4 — Optional self-check block

Pitch questions at the arc, not at recall. "What is the formula for X" tests memory; **"this company's
margin fell while volumes rose — what would you check first, and why?"** tests whether the reader can
use the sector. The most useful question in any sector is a **classification** one: give a company and
ask which category it belongs to and which metric therefore does *not* apply.


Where someone is learning rather than referencing — and especially for a subscriber-facing artifact —
add a self-check section. Keep it genuinely useful rather than decorative:

- **Interpretation questions**, not definition recall. "Company X's margin fell while volumes rose —
  which of these best explains it?" teaches; "what does this acronym stand for?" doesn't.
- **Read-the-numbers exercises** — show a small real disclosed table and ask what it implies.
- 4–6 questions, multiple choice, graded inline in the artifact with a one-line explanation on reveal —
  the explanation is where the learning happens, so never reveal a bare right/wrong.
- Draw on the same real figures used in the worked examples, so the quiz reinforces rather than
  introducing new material.

Include it when the audience is learning; skip it for a reference cheat-sheet someone will scan.

## Scope behaviour

**Standalone** — pure sector education, generic worked examples drawn from real disclosed figures.
**Personalised** — one company's numbers throughout.
**Cross-sector** — teach each sector's metrics in its own section. Explaining why sectors are measured
differently is itself a valuable lesson; merging their metrics into one list is not.

## Deliver

Follow `output-conventions.md`. For a quick concept question, answer in chat — no file needed.

## When the concept isn't in the sector file

The sector file is the canonical source, but it will not always have the concept being asked about —
particularly **policy and structural concepts** rather than metrics. A trade preference, a subsidy
scheme, a licensing regime or a tariff tier can drive a company's economics more than any ratio, and
none of them look like a metric, so they are the ones most likely to be missing.

When that happens:

1. **Check the published collection.** A report that analyses the concept in context is a better source
   than general knowledge, and it is the author's own verified work.
2. **Teach it from there**, citing the report and linking it.
3. **Say that the sector file does not yet define it.** That is a real finding: it means every future
   artifact in that sector will also miss the concept, and it should be folded in rather than
   rediscovered each time.

**Do not quietly fall back to general knowledge.** An explanation with no source behind it is
indistinguishable, to the reader, from one grounded in the collection — and the sector-file gap goes
unrecorded either way.

## The questions a reader actually asks

The published collection carries **over a thousand pre-written reader questions** across its reports.
They are worth studying as a group, because they reveal what a reader wants to know — which is rarely
"define this metric" alone.

**Store the shape, never the question.** A question like *"what drove this company's 858 bps margin
expansion?"* is specific to one company and one quarter; the figure and the name belong in the artifact,
never in a reference file. **What is durable is the shape**, which instantiates against whatever company
and period is being analysed. Six recur:

| Shape | Instantiates as | What it needs |
|---|---|---|
| **Definitional** | "What is *&lt;metric or policy&gt;*?" | The sector file's definition and analogy. The most common single type |
| **Event / why-it-moved** | "What drove *&lt;this move&gt;*?" | Decomposition — volume vs price vs mix vs one-off |
| **Structural / mechanism** | "How does *&lt;X&gt;* actually help or hurt *&lt;this company&gt;*?" | The transmission from the thing to a P&L line |
| **Judgment** | "Is *&lt;this figure&gt;* good or a risk?" | Both readings, then which the evidence supports — **never a buy/sell/hold** |
| **Structural or cyclical** | "Is *&lt;this margin move&gt;* structural or cyclical?" | Recurs constantly. Answer it directly; it is the question behind most others |
| **Company-specific exposure** | "Why does *&lt;X&gt;* matter for *&lt;this company&gt;* but not its peers?" | The exposure basis — a footprint, a mix, a contract others don't have |

**The last shape is the most valuable and the most often missed.** It only works when the sector file
defines the thing being asked about; otherwise the answer falls back to a report or, worse, to general
knowledge. If a question of that shape can't be answered from the sector file, that is the gap to record
— see *When the concept isn't in the sector file* above.

**Judgment questions get both sides.** The corpus phrases them as genuine tensions — "efficient capital
or under-deployed?", "moat eroding or resilient?", "a governance positive or a liquidity risk?" — and
answers by weighing rather than asserting. Keep that framing; a question with a foregone answer teaches
nothing.

## Durable understanding here, point-in-time from the report

**School teaches the sector and the business. It does not teach a quarter.**

| | Source | Why |
|---|---|---|
| **Durable** — what the business does, why it splits into categories, why these metrics, what good looks like, how it fails | **the sector file** | True across companies and across periods. This is what makes a reader able to analyse the *next* quarter, not just read this one |
| **Point-in-time** — this company's figures, this quarter's move, this event | **sourced live, or from a published report** | Changes every period. Baking it into a reference file is how a stale number outlives the quarter it described |

**Use point-in-time material freely — as illustration, not as content.** A worked example on a real
company's disclosed figures teaches faster than an abstract formula, and a published report analysing a
specific quarter is the author's own verified work. Cite it and link it.

**The test for what belongs where**: would this still be true next quarter, and for a different company
in the same category? If yes it is sector knowledge and belongs in the sector file. If no, it is
illustration — source it, date it, and attribute it.

**Where a question is genuinely about one quarter** — why this margin moved, what drove this number —
**the report is the right answer**, and school's job is to give the reader the framework to interpret it.
