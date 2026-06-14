---
name: issues-implement
description: 'Implement a whole GitHub issue for a repository project. Use when Codex is asked to implement an entire issue #N, work through all remaining steps in an issue instruction file, update issue progress while implementing a whole issue, or create an implementation record after completing an issue. Do not use for one exact numbered instruction step such as `$issues #18 step 6`; use `$issues-step`.'
---

# Implement GitHub Issues

## Workflow

Read `references/implement.md` before implementing a whole issue.

Do not use this skill for an exact numbered instruction step such as
`$issues #18 step 6`; use `$issues-step` instead.

Before changing GitHub issue project status, read the repo's `AGENTS.md` and
locate the GitHub project for the repo when project metadata is available. Use
the project status value `In Progress` while implementation is underway and
leave the issue in that status after implementation for user review.

Use these project field values when they are relevant:

### Labels

- Feature
- Bug
- DevOps
- Documentation
- Refactor
- Testing
- Update

### Status

- Todo
- In Progress
- Done

### Priority

- Low
- Medium
- High
- Urgent
