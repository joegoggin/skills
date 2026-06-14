---
name: code-review
description: Review current-branch code changes for bugs, security issues, typos, stale docs, and missing tests. Use when Codex is asked to review a branch, PR, diff, or recent local changes and should present proposed fixes interactively one issue at a time.
---

# Code Review

## What to Review

Unless told otherwise, assume you are reviewing all changes on the current
branch. Inspect `git status`, staged and unstaged changes, and the branch diff
against its base branch when one can be determined.

## What to Check

- **Correctness issues** - Check for bugs, logic errors, regressions, and data
  loss risks.
- **Security issues** - Flag concrete vulnerabilities or unsafe patterns.
- **Missing tests** - Identify meaningful test gaps for changed behavior.
- **Spelling mistakes** - Check for typos in code, comments, and strings.
- **Documentation** — Ensure there is no missing or stale documentation.
  Use the `$docs` skill, if available, to determine this repo’s documentation
  conventions before adding or editing docs.

## Process

1. **Prioritize high-impact findings** - Focus on correctness, security,
   regressions, missing tests, and stale docs before cosmetic issues.
2. **Step through issues one at a time** - Do not provide all feedback in a single response
3. **For each issue found:**
   - Provide a clear description of the issue
   - Show a diff of the proposed fix
     - display this the same way you display changes to the code being made
   - Ask the user whether to accept or reject the change
4. **Wait for user confirmation** before moving to the next issue
5. **After the user responds:**
   - If accepted: Apply the change and move to the next issue
   - If rejected: Skip the change and move to the next issue
6. **Continue until all issues have been addressed**
7. **If no issues are found:** Say that clearly and mention any residual test
   gaps or areas not checked.
8. **After all issues are resolved:** Ask the user with this prompt:

   ```text
   Would you like me to:

   1) commit and push
   2) create/update PR
   3) all of the above
   ```

   - When creating or updating a PR, include a summary of all the changes made
     during the review.
   - The summary and title should reflect all the changes made on the current branch.
   - If a PR for this branch already exists, update the summary to reflect any
     new changes that might be missing.

## Example Format

For each issue, present it like this:

```
**Issue 1: [Brief title]**

[Description of the issue and why it should be changed]

**Proposed fix:**

\`\`\`diff
- old code
+ new code
\`\`\`

Do you want to accept this change?
```
