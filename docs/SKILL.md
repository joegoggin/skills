---
name: docs
description: Apply repository documentation conventions. Use when Codex is adding, editing, checking, auditing, or refreshing docs, comments, or docstrings; when the user invokes `$docs` with no additional input, update missing, stale, misleading, or convention-mismatched documentation in current-branch and untracked workspace changes using this skill's references.
---

# Documentation Conventions

## Default Invocation

When the user provides only `$docs` with no additional input, update
documentation in current-branch and untracked workspace changes so changed
supported-language files match the configured conventions.

Identify current-branch changes by comparing the current branch to the
merge-base with its upstream branch. If no upstream exists, compare against the
merge-base with the default branch. Include tracked staged and unstaged changes,
plus untracked files that are not ignored by Git. Do not include ignored files
unless the user explicitly asks to include them.

Check changed supported-language files for missing, stale, misleading, or
convention-mismatched documentation. Update or remove documentation so it
accurately describes the current code and follows the configured convention.
Report the files changed and any changed files skipped because no convention is
configured.

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
that language by default. During a bare `$docs` invocation, skip unsupported
languages and report them instead of asking whether to proceed.

When the user explicitly asks to add, edit, refresh, or apply documentation in
an unsupported language, inform the user that no documentation convention is
configured and ask whether to proceed without one.
