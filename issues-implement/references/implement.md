# Implementing Issues

When asked to implement an issue, do the following:

## Contents

- Implementation workflow
- Implementation record format

## Implementation Workflow

- Read the issue for context.
  - If the issue is a sub-issue, read the main issue for context.
- If `issues/issue-<number>.md` exists and is not an implementation record,
  read it before implementing and follow its instructions.
- If `issues/issue-<number>.md` exists and is an implementation record, leave it
  unchanged unless the user explicitly asks to update it. Treat the file as an
  implementation record when its first content after an optional leading
  `# {issue title}` heading is `## Changes`.
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
`<number>` is the GitHub issue number. Start each implementation record with
`# {GitHub issue title}`. This file records the completed changes; it is not an
instruction plan. Do not add a `## Steps` section.

Use this structure:

`````markdown
# P3S1: Add nested render tree support

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

##### Models and Types

###### `ModelName`

Source line: `path/to/file1.rs:8`

Explain what the model represents and how it is used.

- field_name (type) - Describe the field.

```rust
struct ModelName {
    field_name: Type,
}
```

##### Functions

###### `function_name(arg)`

Source line: `path/to/file1.rs:12`

Explain what the function does.

- arg (type) - Describe the parameter.

```rust
fn function_name(arg: Type) {
    // Full implemented function body when concise.
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
    // Full implemented test body when concise.
}
```

## Tests

Record the verification performed and any checks intentionally skipped.

- `<test command>` - Passed.
- `<lint command>` - Passed.
- Manual: Verified one expected behavior.

### Useful commands

```sh
<test command>
<lint command>
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
- For code files, include symbol-group headings such as `##### Models and
  Types`, `##### Functions`, `##### Constants`, or another precise heading when
  useful for review.
- Include every new model, class, struct, enum, interface, schema, data transfer
  object, ORM model, or other domain type introduced by the implementation.
  Include changed model or type definitions when their public shape, validation,
  relationships, or variants changed. For each one,
  include a heading with the symbol name, a source line formatted like
  `Source line: path/to/file.rs:12`, a short explanation, relevant fields or
  variants, and a code block showing the complete definition when concise. For
  long definitions, include the declaration and focused excerpts of changed or
  review-relevant fields, validation, relationships, or variants with source
  line references.
- For each important function, method, constant, or other symbol, include: a
  heading with the symbol name, a source line formatted like
  `Source line: path/to/file.rs:12`, a short explanation, relevant parameters,
  and a code block showing the full implemented function or method body when
  concise. For long bodies, include the complete signature and focused excerpts
  of the changed or review-relevant logic with source line references.
- For test files, use `##### New Tests` or `##### Modified Tests` when tests
  changed. For each important test, include the test name, source line,
  `###### Assertions`, `###### Why`, and a code block showing the full test
  function body when concise. For long fixture-heavy or table-driven tests,
  include the setup and assertions needed to understand the behavior.
- In `## Tests`, include a brief verification summary plus result bullets for
  automated and manual checks. For checks that were not run, write `Not run`
  with the reason instead of leaving unchecked todo items.
- After the verification list, include `### Useful commands` with a fenced `sh`
  block when one or more command-backed verification items have stable commands.
- In `### Useful commands`, include only commands that directly correspond to
  command-backed verification items, and list them in the same order.
- For non-code files, generated files, lockfiles, dependency metadata, and
  deleted files, use a shorter prose summary and omit symbol-level detail unless
  it is useful for review.
- Do not include per-file `### Diff` sections by default. Add diffs only when
  the user explicitly asks for them.
