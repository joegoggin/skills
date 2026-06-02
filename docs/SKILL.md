---
name: docs
description: Apply repository documentation conventions. Use when Codex is adding, editing, checking, auditing, or refreshing docs, comments, or docstrings; when the user invokes `$docs` with no additional input, audit the current repository for missing and stale documentation using this skill's references.
---

# Documentation Conventions

## Default Invocation

When the user provides only `$docs` with no additional input, inspect the
current repository for missing or stale documentation. Report findings and do
not edit files unless the user explicitly asks to add or update documentation.

Documentation conventions may differ by language. Check the `references`
directory and load only the file that matches the language being documented.

- Rust: `references/rust.md`
- Lua: `references/lua.md`

## Editing Documentation

When the user asks to add, edit, refresh, or apply documentation fixes, modify
documentation only for languages with configured conventions.

## What to Ignore

- Config files (`*.json`, `*.toml`, `*.yml`, etc.)
- Style files (`*.css`, `*.scss`, etc.)

## No Convention Found

If no convention exists for a language, do not add or edit documentation for
that language. Inform the user that no documentation convention is configured
and ask whether to proceed without one.
