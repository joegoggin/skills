---
name: code-review
description: Review changes on current branch.
---

# Code Review 

## What to Review

Unless told otherwise you should always assume you are reviewing all the changes
on the current branch.

## What to Check

- **Spelling mistakes** - Check for typos in code, comments, and strings
- **Code quality issues** - Bugs, logic errors, and other problems
- **Security issues** - Ensure the app is secure. Security is a top priority.
- **Documentation** — Ensure there is no missing or stale documentation.
  Use the `$docs` skill, if available, to determine this repo’s documentation 
  conventions before adding or editing docs.

## Process

1. **Step through issues one at a time** - Do not provide all feedback in a single response
2. **For each issue found:**
   - Provide a clear description of the issue
   - Show a diff of the proposed fix
     - display this the same way you display changes to the code being made
   - Ask the user whether to accept or reject the change
3. **Wait for user confirmation** before moving to the next issue
4. **After the user responds:**
   - If accepted: Apply the change and move to the next issue
   - If rejected: Skip the change and move to the next issue
5. **Continue until all issues have been addressed**
6. **After all issues are resolved:** Ask the user if they want to:
   - Commit the changes
   - Push to the remote branch
   - Create a PR with a summary of all the changes made during the review
     - The summary and title should reflect all the changes made on the current branch
     - If a PR for this branch already exists, update the summary to reflect
       any new changes that might be missing

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



