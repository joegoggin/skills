# Updating Issues

When asked to update issue plans, do the following:

- Review recent changes for context.
- Treat `issues/issue-<number>.md` files that start with `## Changes` as
  implementation records, not issue plans or issue-body drafts.
- Use implementation records only as context when checking whether plans or
  GitHub issues are stale. Do not normalize implementation records or sync them
  to GitHub issue bodies.
- Compare them to existing `issue-*.md` files and address any inconsistencies
  caused by the changes if needed.
  - What to look for:
    - Project structure changes.
    - Code style or convention changes.
    - Variable name changes.
- Compare the updated `issue-*.md` to the existing GitHub issue to ensure they still
  match each other.
- When updating or syncing issue bodies, normalize main issues and sub-issues to
  the structures defined in `references/create.md`.
  - Main issues should include goal, optional dependencies, ordered sub-issue
    issue-number references, and manual tests.
  - Sub-issues should include goal, summary, optional examples, optional
    third-party packages, optional references, instruction-style steps, and
    instruction-style tests.
  - Preserve useful existing content by moving it into the matching section.
- Update the GitHub issue only when the local plan and remote issue are out of
  sync.
- DO NOT implement the plan.
