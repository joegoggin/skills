---
name: issues
description: 'Route GitHub issue workflows to narrower skills. Use when Codex is asked to create GitHub issues, break work into sub-issues, write issue implementation instructions, implement a GitHub issue, implement one numbered instruction step such as `$issues #18 step 6`, update or sync GitHub issue bodies, or manage project-backed issue workflows.'
---

# Issues

Use this skill as a lightweight router. Select the narrow issue skill that
matches the user's request, read that skill, and follow its instructions. Do not
load every issue workflow.

## Workflow routing

- Use `$issues-create` to create GitHub issues, create main issues, break work
  into sub-issues, or add new issues to a repo project.
- Use `$issues-update` to update, sync, or normalize existing GitHub issue
  bodies.
- Use `$issues-instructions` to write local `issues/issue-<number>.md`
  implementation instruction files without implementing.
- Use `$issues-implement` to implement a whole GitHub issue and create or update
  the local implementation record.
- Use `$issues-step` to implement exactly one numbered step from a local
  instruction file, such as `$issues #18 step 6`.

## Shared project rules

Before creating or updating GitHub issues, read the repo's `AGENTS.md` and
locate the GitHub project for the repo. Treat the project as defined only when
`AGENTS.md` provides a GitHub Project URL or enough owner/project information to
identify it. All created issues should be added to this project.

If the project is missing or ambiguous, do not create issues. Inform the user
that no GitHub project is clearly defined and ask them to add or clarify it in
`AGENTS.md`.

If the GitHub project is defined but the available tools cannot add issues to
that project, do not create issues unless the user explicitly approves creating
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
