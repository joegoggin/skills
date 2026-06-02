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

Provide short code, JSON, command, or UI examples when they add context.

## 3rd-party packages

- [Package name](https://example.com): Briefly describe what the package does
  and why it is needed for this issue.

## References

- [Resource title](https://example.com)

## Steps

### Progress

- [ ] Step 1 - Complete one small task.
- [ ] Step 2 - Complete another small task.

### Step 1

#### Description

Complete one small task. Include relevant commands and important scope
exclusions when needed.

### Step 2

#### Description

Complete another small task.

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
- Keep examples short and contextual. Include code examples only when they are
  needed for clarification. Do not provide full implementation examples.
- In `## 3rd-party packages`, include the package name, link, brief
  description, and what it is used for.
- In `## Steps`, always include `### Progress` first.
- In `### Progress`, use one checkbox per top-level implementation step in this
  exact format: `- [ ] Step N - Short imperative task.`
- Add one matching `### Step N` section for every progress checkbox.
- Keep each numbered step focused on one small task.
- In every `### Step N` section, add a blank line after the heading, then add
  `#### Description`.
- In each `#### Description` subsection, describe exactly what to do in that
  step, including relevant commands and important scope exclusions when needed.
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
