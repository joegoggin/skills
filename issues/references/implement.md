# Implementing Issues

When asked to implement an issue, do the following:

## Contents

- Implementation workflow
- Implementation record format

## Implementation Workflow

- Read the issue for context.
  - If the issue is a sub-issue, read the main issue for context.
- If `issues/issue-<number>.md` exists and does not start with `## Changes`,
  read it before implementing and follow its instructions.
- If `issues/issue-<number>.md` exists and starts with `## Changes`, treat it as
  an existing implementation record, not an instruction plan. Leave it unchanged
  unless the user explicitly asks to update it.
- Update the status of the issue to `In Progress`.
- Implement the task.
- If an instruction file exists, update only the relevant checkboxes in its
  `### Progress` sections as steps are completed. Preserve the existing file
  structure and do not rewrite it into the implementation record format.
- If `issues/issue-<number>.md` does not exist, create it after implementation
  using the implementation record format below.
- Run relevant checks or tests when possible.
- Leave the issue status as `In Progress` after implementation. The user will
  manually move the issue to `Done` after review.
- Describe what changed and provide steps to test.

## Implementation record format

Create missing implementation records as `issues/issue-<number>.md`, where
`<number>` is the GitHub issue number. This file records the completed changes;
it is not an instruction plan. Do not add a `## Steps` section.

Use this structure:

`````markdown
## Changes

### Lines Changed

  +1,285
  -0

### Files

#### New

- `path/to/file1.rs`

#### Modified

- `path/to/file2.rs`

#### New File: `path/to/file1.rs`

Summarize what the new file adds and how it fits into the implementation.

##### Functions

###### `function_name(arg)`

Source line: `path/to/file1.rs:12`

Explain what the function does.

- arg (type) - Describe the parameter.

```rust
fn function_name(arg: Type) {
    // Focused implemented code snippet.
}
```

#### Modified File: `path/to/file2.rs`

Summarize what changed in the existing file.

##### New Tests

###### `test name`

Source line: `path/to/file2.rs:45`

###### Assertions

- Describe the expected behavior verified by the test.

###### Why

Explain why this test matters for the issue.

```rust
#[test]
fn test_name() {
    // Focused implemented test snippet.
}
```
`````

- Populate `### Lines Changed` from the implementation diff. Use
  `git diff --numstat` or an equivalent command for tracked files.
- Format added and removed line counts with comma thousands separators, such as
  `20,234` instead of `20234`. Prefix added counts with `+` and removed counts
  with `-`.
- Include untracked implementation files by counting each line as added and
  generating a new-file diff with `git diff --no-index /dev/null <path>` or an
  equivalent command.
- Include only files changed for the issue implementation. Exclude the
  `issues/issue-<number>.md` implementation record itself from the listed files
  and line counts.
- Under `### Files`, group implementation files by change status with these
  headings when relevant: `#### New`, `#### Modified`, `#### Deleted`, and
  `#### Renamed`. Omit empty status groups.
- In each status group, list every matching implementation file once in path
  order. For renamed files, list ``- `old/path` -> `new/path` ``.
- Add one matching file-detail section for each listed file:
  - ``#### New File: `path/to/file` ``
  - ``#### Modified File: `path/to/file` ``
  - ``#### Deleted File: `path/to/file` ``
  - ``#### Renamed File: `old/path` -> `new/path` ``
- Start each file-detail section with a concise summary of what changed and how
  the file contributes to the issue implementation.
- For code files, include symbol-group headings such as `##### Functions`,
  `##### Types`, `##### Constants`, or another precise heading when useful for
  review.
- For each important function, method, type, constant, or other symbol, include:
  a heading with the symbol name, a source line formatted like
  `Source line: path/to/file.rs:12`, a short explanation, relevant parameters
  or fields, and a focused code block showing the implemented code.
- For test files, use `##### New Tests` or `##### Modified Tests` when tests
  changed. For each important test, include the test name, source line,
  `###### Assertions`, `###### Why`, and a focused code block.
- For non-code files, generated files, lockfiles, dependency metadata, and
  deleted files, use a shorter prose summary and omit symbol-level detail unless
  it is useful for review.
- Do not include per-file `### Diff` sections by default. Add diffs only when
  the user explicitly asks for them.
