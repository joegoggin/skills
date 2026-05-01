---
name: docs
description: Apply repository documentation conventions. Use when Codex is adding, editing, or checking docs, comments, or docstrings and needs language-specific documentation rules from this skill's references.
---

# Documentation Conventions

Documentation conventions may differ by language. Check the `references`
directory and load only the file that matches the language being documented.

- Rust: `references/rust.md`

## What to Ignore

- Config files (`*.json`, `*.toml`, `*.yml`, etc.)
- Style files (`*.css`, `*.scss`, etc.)

## No Convention Found

If no convention exists for a language, do not add or edit documentation for
that language. Inform the user that no documentation convention is configured
and ask whether to proceed without one.
