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
- Run `$docs` with no additional input so current-branch and untracked changes
  are documented according to the configured documentation conventions.
- Treat documentation changes produced by `$docs` as part of the issue
  implementation and include them in any implementation record created below.
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

### File: `path/to/file1.rs`

#### Lines: `1-4`

 4
 0

Added the nested render tree data structures and traversal helpers used by the
new rendering path.

#### Line: `20`

 1
 1

Changed the parent lookup to preserve child ordering during nested render tree
construction.

#### Lines: `32-44`

 13
 0

Updated render tree construction to attach child nodes instead of flattening
them into the parent list.

### File: `path/to/file2.rs`

#### Lines: `42-47`

 6
 0

Changed the render assertions to verify nested children and preserve coverage
for existing flat render output.

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

- Populate `## Changes` from the implementation diff. Use `git diff`,
  `git diff --stat`, `git diff --numstat`, or equivalent commands for tracked
  files.
- Include untracked implementation files by counting each line as added and
  generating a new-file diff with `git diff --no-index /dev/null <path>` or an
  equivalent command.
- Include only files changed for the issue implementation. Exclude the
  `issues/issue-<number>.md` implementation record itself from the listed files
  and line counts.
- Under `## Changes`, create one ``### File: `path/to/file` `` section for each
  implementation file in path order. For renamed files, use
  ``### File: `old/path` -> `new/path` ``. For deleted files, use the deleted
  path.
- Within each file section, create one line block for each tight contiguous
  changed range. Use ``#### Line: `136` `` for a single changed line and
  ``#### Lines: `107-110` `` for a multi-line range.
- Use diff hunks as the default source for line blocks. Do not combine
  non-contiguous changes into one broad range when untouched code sits between
  them. Merge only overlapping or immediately contiguous changed ranges where
  the resulting range does not hide unrelated untouched code.
- Use the changed line range from the post-change file when available. For
  deleted files, use the removed file's line range. For new files, use ranges
  from the new file. If a binary file or generated artifact has no useful line
  range, write ``#### Lines: `not applicable` ``.
- In each line block, write ` <added line count>` and ` <removed line count>`
  for that block only, not for the whole file. Use `0` when a block has no
  additions or removals. Format large counts with comma thousands separators,
  such as `20,234`.
- After the counts, explain the change in prose. Focus on what changed, why it
  matters for the issue, and any important behavior or compatibility effect.
  Do not replace this with model, type, function, or symbol inventories.
- For non-code files, generated files, lockfiles, dependency metadata, binary
  files, and deleted files, use the same file/chunk format with a shorter prose
  explanation.
- In `## Tests`, include a brief verification summary plus result bullets for
  automated and manual checks. For checks that were not run, write `Not run`
  with the reason instead of leaving unchecked todo items.
- After the verification list, include `### Useful commands` with a fenced `sh`
  block when one or more command-backed verification items have stable commands.
- In `### Useful commands`, include only commands that directly correspond to
  command-backed verification items, and list them in the same order.
- Do not include per-file `### Diff` sections by default. Add diffs only when
  the user explicitly asks for them.
