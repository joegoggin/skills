# Updating Issues

When asked to update or sync GitHub issue bodies, do the following:

- Review recent changes for context.
- Do not edit, create, normalize, or rewrite local `issues/issue-*.md` files
  unless the user explicitly asks to update local instruction files.
- Treat `issues/issue-<number>.md` files as implementation records, not issue
  plans or issue-body drafts, when their first content after an optional leading
  `# {issue title}` heading is `## Changes`.
- Use implementation records only as context when checking whether plans or
  GitHub issues are stale. Do not normalize implementation records or sync them
  to GitHub issue bodies.
- Read local `issues/issue-*.md` files only as context when they are directly
  relevant to the requested GitHub issue update.
- When updating or syncing GitHub issue bodies, normalize main issues and sub-issues to
  the structures defined in `references/create.md`.
  - Main issues should include goal, optional dependencies, ordered sub-issue
    issue-number references, and manual tests.
  - Sub-issues should include goal, summary, optional examples, optional
    third-party packages, optional references, expected result, and tests.
  - Preserve useful existing content by moving it into the matching section.
  - When an existing sub-issue has `## Steps`, convert useful step content into
    done-state expectations under `## Expected Result` instead of preserving the
    step checklist structure.
- Update the GitHub issue only when the remote issue body is out of sync.
- DO NOT implement the plan.
