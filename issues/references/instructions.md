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
- Include detailed code examples for each step.
- Include steps for manually testing the changes.
- DO NOT implement the plan.
