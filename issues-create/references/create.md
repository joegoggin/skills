# Create Issues

When creating issues on GitHub for this project you should use the following
conventions:

## Contents

- Creation conventions
- Main issue body
- Sub-issue body

## Creation Conventions

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
- Define the expected result for each sub-issue instead of adding implementation
  step checklists.
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

## Expected Result

Describe the completed state in enough detail that the implementer can
recognize what done means. Include expected behavior, outputs, UI states, data
shape, commands, or scope exclusions when they clarify the result.

Example: Running `just test` succeeds, and nested render tree nodes preserve
their parent-child ordering in the rendered output.

## Examples

Provide short code, JSON, command, or UI examples when they add context.

## 3rd-party packages

- [Package name](https://example.com): Briefly describe what the package does
  and why it is needed for this issue.

## References

- [Resource title](https://example.com)

## Tests

Verify the implementation with a brief summary of the relevant automated and
manual checks.

- [ ] Run `just test`.
- [ ] Verify one expected behavior manually.

### Useful commands

```sh
just test
```
```

- Omit `## Examples`, `## 3rd-party packages`, and `## References` when they
  are not relevant.
- Keep the top-level sub-issue section order exactly as shown when optional
  sections are present.
- Keep examples short and contextual. Include code examples only when they are
  needed for clarification. Do not provide full implementation examples.
- In `## 3rd-party packages`, include the package name, link, brief
  description, and what it is used for.
- Always include `## Expected Result`.
- In `## Expected Result`, describe the done state in detail. Include expected
  behavior, outputs, UI states, data shape, commands, and scope exclusions when
  they help define what correct completion looks like.
- Include short examples in `## Expected Result` when they clarify the expected
  done state. Do not provide full implementation examples.
- Do not include implementation progress checklists or numbered step sections
  in sub-issue bodies.
- Do not require per-file code or diff subsections in sub-issue bodies. If code
  is needed for clarification, include a short contextual example in
  `## Examples`.
- In `## Tests`, include a brief verification summary plus a `- [ ]` checklist
  of automated and manual tests.
- After the test checklist, include `### Useful commands` with a fenced `sh`
  block when one or more checklist items have stable commands.
- In `### Useful commands`, include only commands that directly correspond to
  checklist items, and list them in the same order as the matching checklist
  items.
