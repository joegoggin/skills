---
name: docs
description: Apply configured Rust and Lua documentation conventions. Use when Codex is adding, editing, checking, auditing, or refreshing documentation, comments, or docstrings in Rust or Lua files; when the user invokes `$docs` with no additional input, update applicable documentation in current-branch and untracked workspace changes. Do not use for documentation work limited to other file types.
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
Report the files changed.

Documentation conventions may differ by language. Check the `references`
directory and load only the file that matches the language being documented.

- Rust: `references/rust.md`
- Lua: `references/lua.md`

## Editing Documentation

When the user asks to add, edit, refresh, or apply documentation fixes, modify
documentation according to this skill only for file types with configured
conventions. For other file types, continue under ordinary repository and user
instructions without applying this skill.

## What to Ignore

- Config files (`*.json`, `*.toml`, `*.yml`, etc.)
- Style files (`*.css`, `*.scss`, etc.)

## Unsupported File Types

When no matching convention exists, treat the file type as outside this skill's
scope. Do not inspect it through this skill, apply documentation rules, warn,
report, prompt for confirmation, or block the task. During a bare `$docs`
invocation, silently skip unsupported file types. During an explicit
documentation request, continue using ordinary repository and user instructions.
