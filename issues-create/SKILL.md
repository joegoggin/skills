---
name: issues-create
description: Create project-linked GitHub issues for repository work. Use when Codex is asked to create issues, create a main issue, break work into ordered sub-issues, convert a plan into GitHub issues, or create project-backed issue tasks.
---

# Create GitHub Issues

## Workflow

Read `references/create.md` before creating issues.

Before creating issues, read the repo's `AGENTS.md` and locate the GitHub
project for the repo. Treat the project as defined only when `AGENTS.md`
provides a GitHub Project URL or enough owner/project information to identify
it.

If the project is missing or ambiguous, do not create issues. Inform the user
that no GitHub project is clearly defined and ask them to add or clarify it in
`AGENTS.md`.

If the GitHub project is defined but the available tools cannot add issues to
that project, do not create issues unless the user explicitly approves creating
them without project linkage.

Use these project field values when creating issues:

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
