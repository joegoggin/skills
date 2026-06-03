# Providing Instructions For Issues

When asked to provide instructions for implementing an issue, do the
following:

## Contents

- Instruction workflow
- Instruction file format

## Instruction Workflow

- Read the issue for context.
  - If the issue is a sub-issue, read the main issue for context.
- Create a plan to implement the issue.
  - Prefer existing `just` commands for setup, checks, tests, and builds.
- Write the plan to `issues/issue-*.md`, where `*` is the issue number.
  - If asked to create instructions for multiple issues or sub-issues of a main
    issue, ensure each issue has its own file.
  - DO NOT include multiple issues in one file.
  - If a matching file already exists for an issue, leave it unchanged and tell
    the user that instructions already exist for that issue.
- Start each instruction file with `# {GitHub issue title}`.
- Use the exact instruction-file structure below.
- DO NOT implement the plan.

## Instruction file format

Use this top-level section order:

```markdown
# P3S1: Add nested render tree support

## Goal

Describe the implementation goal for this issue.

## Summary

Summarize the issue context, parent/sub-issue relationship, scope boundaries,
and notable existing code state.

## Examples

Provide short code, JSON, command, or UI examples when they add context.

## 3rd-party packages

- [Package name](https://example.com): Explain what the package does and why
  this issue needs it.

## References

- Parent issue: #1
- Related issue: #2
- Relevant local file: `src/example.rs`
- [External reference](https://example.com)

## Steps

### Progress

- [ ] Step 1 - Complete one small task.
- [ ] Step 2 - Complete another small task.

### Step 1

#### Description

Complete one small task.

#### file: `src/example.rs`

Include the code diff or snippet needed for this file.

### Step 2

#### Description

Complete another small task.

#### file: `src/another-example.rs`

Include the code diff or snippet needed for this file.

## Tests

Verify the implementation with a brief summary of the relevant automated and
manual checks.

- [ ] Run `just test`.
- [ ] Run `just lint`.
- [ ] Verify one expected behavior manually.

### Useful commands

```sh
just test
just lint
```
```

- Always start with exactly one `# {GitHub issue title}` heading.
- Always include `## Goal`, `## Summary`, `## Steps`, and `## Tests`.
- Include `## Examples`, `## 3rd-party packages`, and `## References` only
  when they are relevant.
- Keep the top-level section order exactly as shown when optional sections are
  present, with the title heading before `## Goal`.
- In `## Steps`, always include `### Progress` first.
- In `### Progress`, use one checkbox per top-level implementation step in this
  exact format: `- [ ] Step N - Short imperative task.`
- Add one matching `### Step N` section for every progress checkbox.
- Keep each numbered step focused on one small task.
- In every `### Step N` section, add a blank line after the heading, then add
  `#### Description`.
- In each `#### Description` subsection, describe exactly what to do in that
  step, including relevant commands and important scope exclusions when needed.
- After the description, add one ``#### file: `path/to/file` `` subsection for
  each file that needs an add or change in that step.
- Under each ``#### file: `path/to/file` `` subsection, include the code diff or
  code snippet needed to complete that file change.
- Include all code needed to complete the step. Do not include full files unless
  the full file is genuinely needed; include only the surrounding context needed
  to make the add or change safely.
- Keep follow-up work out of the issue instructions when the source issue or
  parent issue assigns that work to separate issues.
- In `## Tests`, include a brief verification summary plus a `- [ ]` checklist
  of automated and manual tests.
- After the test checklist, include `### Useful commands` with a fenced `sh`
  block when one or more checklist items have stable commands.
- In `### Useful commands`, include only commands that directly correspond to
  checklist items, and list them in the same order as the matching checklist
  items.
- When a useful command uses `rg`, make the matching checklist item start with
  `Confirm` and include the meaningful searched terms from the `rg` pattern in
  human-readable form. For example:
  - Checklist: `- [ ] Confirm \`crates/leptatui/src/prelude.rs\` still does not contain \`pub use leptos::prelude::*\`, \`pub use ratatui::*\`, or \`pub use crossterm::*\`.`
  - Command: `rg "pub use (leptos::prelude|ratatui|crossterm)::\\*" crates/leptatui/src`
  - Checklist: `- [ ] Confirm no \`Component\`, \`RenderCtx\`, node builder, \`TuiStyle\`, or counter example was added in this issue.`
  - Command: `rg "Component|RenderCtx|TuiStyle|counter" crates/leptatui/src crates/leptatui/examples`
- Do not add commands for descriptive/manual checklist items or checks that
  require temporary code changes instead of a stable reusable command.
