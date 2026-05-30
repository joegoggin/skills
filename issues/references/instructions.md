# Providing Instructions For Issues

When asked to provide instructions for implementing an issue, do the
following:

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
- Use the exact instruction-file structure below.
- DO NOT implement the plan.

## Instruction file format

Use this top-level section order:

```markdown
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

Complete one small task.

Add concise implementation details here.

### Step 2

Complete another small task.

Add concise implementation details here.

## Tests

Describe how to verify the implementation.

- [ ] Run the relevant automated check.
- [ ] Verify one expected behavior manually.
```

- Always include `## Goal`, `## Summary`, `## Steps`, and `## Tests`.
- Include `## Examples`, `## 3rd-party packages`, and `## References` only
  when they are relevant.
- Keep the top-level section order exactly as shown when optional sections are
  present.
- In `## Steps`, always include `### Progress` first.
- In `### Progress`, use one checkbox per top-level implementation step in this
  exact format: `- [ ] Step N - Short imperative task.`
- Add one matching `### Step N` section for every progress checkbox.
- Keep each numbered step focused on one small task.
- Use the numbered step sections for details, file paths, commands, concise
  examples, and important scope exclusions.
- Include code examples only when they add useful context. Keep them short and
  avoid full implementation examples unless the issue specifically needs an
  exact shape or contract.
- Keep follow-up work out of the issue instructions when the source issue or
  parent issue assigns that work to separate issues.
- In `## Tests`, include a brief verification summary plus a `- [ ]` checklist
  of automated and manual tests. Add useful command examples after the checklist
  when relevant.
