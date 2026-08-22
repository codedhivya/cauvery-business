# Architecture Decision Records

Why this repo is shaped the way it is. Each record covers one decision: the situation that forced it,
what was chosen, and what it costs.

Read these before reversing something that looks arbitrary — several of these decisions are
counterintuitive and were made against specific evidence from the 98-report corpus.

| # | Decision | Status |
|---|---|---|
| [0001](0001-one-skill-not-nine.md) | Consolidate nine insurance skills into one multi-sector skill | Accepted |
| [0002](0002-mode-sector-split.md) | Mode files own the craft; sector files own the domain | Accepted |
| [0003](0003-modes-derived-from-corpus.md) | Derive the mode set from the corpus, not the nine skills | Accepted |
| [0004](0004-cross-sector-guardrails.md) | Support cross-sector comparison, constrained to universal metrics | Accepted |
| [0005](0005-cb-rating-unification.md) | Unify CB Rating on one core with per-sector substitutions | Accepted |
| [0006](0006-staging-gate.md) | Generated reports go to staging; promotion is a human action | Accepted |
| [0007](0007-conversation-is-the-default.md) | Conversation is the default output; artifacts are the exception | Accepted |
| [0008](0008-exclude-news-digests.md) | Exclude news digests; keep policy and corporate-action analysis | Accepted |
| [0009](0009-portability-isolation.md) | Confine paths and tool names to a single file | Accepted |
| [0010](0010-inherit-structure-never-figures.md) | Inherit structure from prior reports; never inherit figures | Accepted |
| [0011](0011-install-by-symlink.md) | Install the skill by symlink; `.skill` is a build artifact | Accepted |
| [0012](0012-reit-invit-is-an-asset-class.md) | REITs/InvITs get their own file — an asset class, not an industry | Accepted |

## The four that matter most

If you read only some of these:

- **[0002](0002-mode-sector-split.md)** is the contract that makes the skill multi-sector. Break it and
  nothing visibly fails — the abstraction just quietly dies.
- **[0006](0006-staging-gate.md)** is the rule with real-world consequences. Generated analysis reaching
  subscribers unverified is the failure this repo is built to prevent.
- **[0004](0004-cross-sector-guardrails.md)** prevents the most likely silent misrepresentation: an
  insurer or bank shown in an EBITDA column where the metric does not exist.
- **[0010](0010-inherit-structure-never-figures.md)** is why the skill never copies a number from a
  previous report, however convenient that would be.

## Writing a new one

Copy the structure: **Status**, **Context** (what forced the decision, with evidence), **Decision** (what
was chosen, and what was rejected), **Consequences** (what follows, *including the costs*).

A record that lists only benefits is not finished. The value of an ADR is that a future reader can tell
whether the trade-off still holds.

Records are immutable once accepted. To change a decision, add a new record and mark the old one
`Superseded by ADR-NNNN`.
