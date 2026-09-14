# Updating Issues

When asked to update or sync GitHub issue bodies, do the following:

- Review recent changes for context.
- Do not edit, create, normalize, or rewrite local `issues/issue-*.md` files
  unless the user explicitly asks to update local instruction files.
- Treat `issues/issue-<number>.md` files as implementation records, not issue
  plans or issue-body drafts, when their first two top-level sections after
  an optional title are `## Summary` followed by `## Changes`.
  Also recognize legacy records whose first section is `## Changes`.
- Use implementation records only as context when checking whether plans or
  GitHub issues are stale. Do not normalize implementation records or sync them
  to GitHub issue bodies.
- Read local `issues/issue-*.md` files only as context when they are directly
  relevant to the requested GitHub issue update.
- When updating or syncing GitHub issue bodies, normalize main issues using
  [the main issue format](../../issues-create/references/create.md): goal,
  optional dependencies, ordered sub-issue references, and manual tests.
- Normalize sub-issues using
  [the technical spec format](../../plan-project/references/sub-issue-spec.md),
  regardless of whether they were originally created by `$plan-project`.
  This format takes precedence over the default `$issues-create` sub-issue
  template. Read the shared reference for section order, technical detail,
  optional sections, and the example; do not maintain a separate template here.
  - Inspect relevant repository files and the parent issue before revising
    scope, file responsibilities, interfaces, dependencies, or test commands.
    Distinguish verified existing code from proposed additions and planned
    prerequisite contracts. Resolve material unknowns rather than inventing
    technical details or expanding the issue's scope.
  - Preserve useful existing content by moving it into the matching spec
    section. Convert `Expected Result` content into interface behavior and
    observable acceptance criteria; retain relevant examples and references.
  - Convert useful `Steps` content into a short numbered implementation
    sequence. Extract contracts and file responsibilities from old code or
    diffs instead of retaining full implementations or line-specific patches.
  - Preserve evidence of completed work and existing acceptance checkbox
    states where the corresponding requirements remain unchanged. Do not turn
    completed implementation steps into unchecked work or infer acceptance
    solely from an old progress checkbox.
  - Publish the spec in the existing GitHub issue body. Keep the issue title,
    phase/step identifiers, and relationships unless their update was requested.
- Update the GitHub issue only when the remote issue body is out of sync.
- DO NOT implement the plan.
