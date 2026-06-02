---
name: issues
description: Create, update, plan, and implement GitHub issues for a repository project. Use when Codex is asked to create GitHub issues, break work into sub-issues, implement an issue, write issue implementation instructions, or sync/update GitHub issue bodies.
---

# Issues

## Project

Before creating or updating issues, read the repo's `AGENTS.md` and locate the
GitHub project for the repo. Treat the project as defined only when `AGENTS.md`
provides a GitHub Project URL or enough owner/project information to identify
it. All created issues should be added to this project.

If the project is missing or ambiguous, DO NOT create issues. Inform the user
that no GitHub project is clearly defined and ask them to add or clarify it in
`AGENTS.md`.

If the GitHub project is defined but the available tools cannot add issues to
that project, DO NOT create issues unless the user explicitly approves creating
them without project linkage.

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

## Create Issues

Use `references/create.md` for creating issues.

## Implementing Issues

Use `references/implement.md` for implementing issues.

## Providing Instructions For Issues

Use `references/instructions.md` for providing instructions for issues.

## Updating Issues

Use `references/update.md` for updating issues.
