# ADR-0011: Install the skill by symlink; treat the packaged `.skill` as a build artifact

**Status**: Accepted · 2026-08-10

## Context

After Phase 1 the skill existed only as source in the repo. Nothing loaded it — `~/.claude/skills/` and
`.claude/skills/` did not exist — so it could not trigger in a session at all.

This was easy to miss, because answers produced during the build *appeared* to demonstrate the skill
working. They did not: the author of the files had their content in context regardless. The skill's
correctness had been validated; its ability to trigger had never been tested.

Separately, the packaged `.skill` file (57K) sat at the repo root. It is a build artifact — regenerable
from source at any time — and committing it means a binary diff on every rebuild that git cannot
meaningfully version.

## Decision

**Install by symlink, not copy:**

```
.claude/skills/sector-financial-analysis -> ../../sector-financial-analysis
```

Git stores it as mode `120000`, a real symlink, so anyone cloning the repo gets the skill wired up.
Editing the source updates the installed skill with no second copy to drift — the same approach as
`CLAUDE.md → AGENTS.md`.

**Gitignore `*.skill`** as a build artifact; distribute via GitHub Releases when needed. One exception is
negated: archived packaged skills under `archive/` stay tracked, since a rule aimed at the new build
artifact should not silently eat historical ones.

## Consequences

- The skill is live and can be tested for triggering — the one property that could not be verified
  otherwise.
- Edits during Phases 2–4 take effect immediately, with no install step.
- It will trigger on the thirteen unbuilt sectors and then have to decline. That is handled explicitly in
  the router — *"If a request names a company from an unbuilt sector, say so plainly… don't silently
  substitute another sector's metrics"* — but whether it reads as helpful honesty or noise is only
  answerable from real use. If it over-triggers, the fix is tightening the description, not uninstalling.
- No installable build is present on GitHub until a Release is cut.
- Removal is one line and does not touch the source:
  `rm .claude/skills/sector-financial-analysis`
