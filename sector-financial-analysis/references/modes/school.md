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

1. **The sector's analogy table** — lead with it. The fastest way to make an unfamiliar metric
   intuitive is to anchor it to something the reader already understands.
2. **A "what to watch" quick-reference** by category, from the sector file.
3. **Metric cards**, grouped by category, each self-contained:
   - a short colour tag with the metric's short code
   - full name, plus a one-line analogy subtitle
   - "What it is" / "Formula" — 2–3 sentences of plain English, no unexplained jargon
   - **a worked example box** using a named company's real disclosed figures, walking through the
     calculation step by step and ending with what the result means *for that company*
4. **Regulatory quick-reference** where the sector has rules a reader needs (capital minimums,
   investment limits).
5. **A closing "read a company in 60 seconds" checklist** — 5 yes/no questions per category, optionally
   answered for a specific company.

## Step 3 — Pedagogy

- **Define a term before using it elsewhere.** Don't explain metric B using metric A if A comes later.
- Prefer one concrete worked example to an abstract formula.
- Keep each metric card standalone — readers jump straight to the metric confusing them, and shouldn't
  need the preceding cards to make sense of it.
- Teach interpretation, not conclusions. The goal is a reader who can judge the numbers themselves, not
  one who defers to this artifact.

## Step 4 — Optional self-check block

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
