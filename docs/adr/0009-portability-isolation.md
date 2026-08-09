# ADR-0009: Confine paths and tool names to a single file

**Status**: Accepted · 2026-08-09

## Context

The skill needs to run in other agent environments later — ChatGPT, Gemini — so subscribers can use it
without a Claude account.

Almost all of it is already portable: `references/**` is plain markdown domain knowledge with no runtime
dependency. What is *not* portable is a thin shell — the YAML frontmatter format, and any reference to a
tool (`SendUserFile`) or a path (`reports/staging/`).

An early draft had every mode file ending with "save to `reports/staging/…` and call `SendUserFile`".
That would have hardcoded Claude Code into all fifteen modes, making a future port a fifteen-file edit.

## Decision

**Keep the shell out of the core.**

- Mode files and sector files contain **zero tool names and zero paths**. They describe only what to
  produce.
- All I/O collapses into `references/output-conventions.md`, which states plainly that it is the only
  file naming paths or tools.
- Porting means editing that one file.

A validation grep enforces this.

**Claude-first**: Phase 1 targets Claude Code. Export bundles for other platforms wait until the
subscriber platform is chosen and sector files stop churning — building three bundles now would mean
maintaining them through Phases 2–4 for a platform not yet selected.

## Consequences

- The rename of `cb_research_reports/` → `reports/published/` touched exactly one file inside the skill.
  That was the design working as intended, and it validated the constraint under real conditions.
- Two honest limits on any future port. **Progressive disclosure** — loading only the two files a request
  needs — is a Claude-Code-style capability; RAG-based platforms retrieve knowledge files instead, which
  is less deterministic, so the port will be functional but not identical. And those platforms **cap
  knowledge-file count and size**, with caps that change; at ~32 files a concatenating build mode may be
  required rather than one-file-per-mode.
- Mode files read slightly more abstractly, since they cannot say where output goes.
