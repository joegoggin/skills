---
name: issues-instructions
description: Write local implementation instruction files for GitHub issues without implementing them. Use when Codex is asked to provide implementation instructions for a GitHub issue, create a local issue instruction file, prepare issue-specific implementation steps, or generate instruction files for multiple GitHub issues or sub-issues.
---

# Issue Instructions

## Workflow

Read `references/instructions.md` before writing instruction files.

Read the GitHub issue for context. If the issue is a sub-issue, read the main
issue for parent context. Prefer existing `just` commands for setup, checks,
tests, and builds.

Create local instruction files only; do not implement the plan. If the user asks
to implement an issue instead, use `$issues-implement`. If the user asks to
implement one numbered step from an existing instruction file, use
`$issues-step`.

If a matching instruction file already exists, leave it unchanged and tell the
user that instructions already exist for that issue.
