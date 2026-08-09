# ADR-0007: Conversation is the default output; artifacts are the exception

**Status**: Accepted · 2026-08-09

## Context

The skill was built around producing HTML artifacts, because that is what the 98 reports are. But a large
part of its intended use is learning — asking "what is NII?", "what's the difference between GNPA and
NNPA?", "how did SBI do?" — where a generated file is the wrong answer.

The rule to answer conversationally did exist, but only in `output-conventions.md`, which loads *last*,
and in per-mode asides phrased as soft judgement ("use judgement", "often enough"). Meanwhile every mode
file ends with a Deliver step pointing at file output. The gradient pushed toward building a file for
every request.

The failure this produces is specific: a one-line answer buried inside an HTML file the reader has to
open, when they asked a question in a conversation.

## Decision

**Depth is a routing axis, decided before anything loads** — Step 0 in the router, ahead of sector, mode
and scope.

- **Answer in chat** for questions: concept explanations, single figures, quick reads, anything
  exploratory. **This is the default.** The same sourcing discipline applies — real figures, real
  attribution, no fabrication — delivered as prose.
- **Build the artifact** when the person wants something to keep, share, publish or return to.
- **When ambiguous, answer in chat and offer the artifact.** That costs one sentence; the reverse wastes
  the reader's time.
- Honour explicit overrides in both directions — "just tell me" / "give me a report".

Stated explicitly: a learning session is a conversation, and twenty questions should not produce twenty
files.

## Consequences

- The skill is usable for learning, which is half its purpose.
- Routing has four axes rather than three, and depth must be judged before the mode is known — a request
  can map to `school` at either depth.
- Sourcing discipline does not relax in chat mode. An unsourceable figure returns "not disclosed" in
  conversation too, which matters more there because there is no footnote to catch it.
- Misrouting is cheap and self-correcting in either direction: the reader says "actually build it" or
  "just tell me".
