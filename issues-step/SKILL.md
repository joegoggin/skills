---
name: issues-step
description: 'Implement exactly one numbered step from a local issue instruction file. Use when Codex is asked for `$issues #18 step 6`, `issue 18 step 6`, `implement step 6 for #18`, or any request to complete one specific step from a local issue instruction file.'
---

# Issue Instruction Step

## Workflow

Read `references/step.md` before implementing the selected step.

Read only the matching local `issues/issue-<number>.md` instruction file unless
the selected step explicitly instructs otherwise. Do not read the GitHub issue,
parent issue, `AGENTS.md`, project metadata, other instruction steps, or
unrelated local context.

Implement only the selected step. Do not implement adjacent steps, inferred
prerequisites, cleanup, or tests outside the selected step unless that step
explicitly includes them.

When the selected step is complete, update only its matching progress checkbox
and report the exact verification performed.
