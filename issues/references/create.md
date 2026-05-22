# Create Issues

When creating issues on GitHub for this project you should use the following
conventions:

- Give all new issues a status of `Todo`.
- If a priority is not provided, set the priority to `Medium` by default.
- Create a main issue with a summary of the full task that needs to be completed.
- Break up the full task into small tasks and add those as sub-issues when
  GitHub sub-issues are available.
- If the available tooling cannot create sub-issue relationships, create child
  issues that link back to the main issue and tell the user that the sub-issue
  relationship must be added manually.
- Give each sub-issue a summary of the small task and the same priority as the
  main issue.
- Order sub-issues in the sequence they should be implemented.
- Split sub-issues into smaller checklist steps.
- Assign all issues to the authenticated GitHub user. If the user cannot be
  determined, ask who should be assigned.

## Main issue body

Use this structure for main issues:

```markdown
## Goal

Describe the main goal for the issue.

## Dependencies

List links to issues that must be finished before this issue can start.

## Sub-Issues

1. #1
2. #2
3. #3

## Tests

Describe how to manually test that the full issue implementation is correct.
```

- Omit `## Dependencies` when there are no dependencies.
- Populate `## Sub-Issues` with an ordered list of GitHub issue-number
  references in the sequence the sub-issues should be implemented.
- Include manual test instructions that validate the completed main issue, not
  only individual sub-issues.

## Sub-issue body

Use this structure for sub-issues:

```markdown
## Goal

Describe the main goal for the sub-issue.

## Summary

Summarize the task.

## Examples

Provide short code examples when they add context.

## 3rd-party packages

- [Package name](https://example.com): Briefly describe what the package does
  and why it is needed for this issue.

## References

- [Resource title](https://example.com)

## Steps

- [ ] Complete one small task.
  - [ ] Complete a needed sub-step.
- [ ] Complete another small task.

## Tests

Describe how to manually test that the sub-issue implementation is correct.

- [ ] Verify one expected behavior.
- [ ] Verify another expected behavior.
```

- Omit `## Examples`, `## 3rd-party packages`, and `## References` when they
  are not relevant.
- Keep examples short and contextual. Do not provide full implementation
  examples.
- In `## 3rd-party packages`, include the package name, link, brief
  description, and what it is used for.
- Keep each `## Steps` checklist item to one small task. Use indented task-list
  sub-steps only when a step needs more detail.
- Use GitHub task-list syntax (`- [ ]`) for all checklist items.
