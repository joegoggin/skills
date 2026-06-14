---
name: issues-update
description: Update or sync existing GitHub issue bodies. Use when Codex is asked to update issue body text, sync issue bodies with current plans, normalize main or sub-issue bodies, refresh stale GitHub issues, or convert old issue step checklists into expected-result issue body structure.
---

# Update GitHub Issues

## Workflow

Read `references/update.md` before updating GitHub issue bodies.
When normalizing main or sub-issue bodies, also read the sibling
`../issues-create/references/create.md` reference for the canonical issue body
structures.

Before updating GitHub issues, read the repo's `AGENTS.md` and locate the
GitHub project for the repo when project status, priority, labels, or issue
relationships are relevant.

Do not create issues as part of an update unless the user explicitly asks to
create issues. If issue creation is needed, use `$issues-create`.

When syncing bodies, keep local `issues/issue-*.md` files unchanged unless the
user explicitly asks to update local instruction files.

Use these project field values when they are relevant to the requested update:

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
