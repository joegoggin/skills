---
name: refactor-review
description: Suggest current-branch refactors for maintainability, readability, duplication reduction, architecture fit, naming, dead code removal, testability, and oversized-file decomposition. Use when Codex is asked to refactor, improve structure, simplify code, reduce duplication, split large files, or propose cleanup changes, and should present proposed refactors interactively one at a time.
---

# Refactor Review

## What to Inspect

Unless told otherwise, assume you are refactoring changes on the current branch.
Inspect `git status`, staged and unstaged changes, and the branch diff against
its base branch when one can be determined.

If the user names files, directories, a PR, or a repo-wide scope, use that scope
instead and state it before presenting refactors.

When assessing oversized files, inspect the complete in-scope files and nearby
module structure, not only changed lines. Exclude generated, vendored, and build
output files unless the user explicitly includes them.

## What to Look For

- **Duplication** - Consolidate repeated logic, constants, types, fixtures, or
  setup when the shared shape is clear.
- **Complexity** - Simplify deeply nested conditionals, long functions, broad
  switch statements, and tangled control flow.
- **Naming and clarity** - Improve names, function boundaries, and local
  structure when it makes intent easier to read.
- **Cohesion and module boundaries** - Move logic closer to its owner or split
  unrelated responsibilities when the repo already has a clear pattern.
- **Oversized files** - Look for files whose mixed responsibilities, navigation
  difficulty, or divergence from nearby repository conventions justify a logical
  split. Use contextual evidence rather than a fixed line-count threshold, and
  do not flag a large file that remains cohesive and easy to maintain.
- **Dead code** - Remove unreachable, unused, or obsolete code when confidence
  is high.
- **Testability** - Extract pure helpers, isolate side effects, or clarify
  seams only when doing so preserves behavior and makes tests easier to write.
- **Docs and comments** - Update, remove, or tighten comments and docs affected
  by the refactor. Use the `$docs` skill, if available, when editing docs.

## Refactor Rules

1. **Preserve behavior** - Refactors should not intentionally change runtime
   behavior, public contracts, data shape, or error handling unless the user
   explicitly asks for that broader change.
2. **Prefer existing patterns** - Follow the repo's current structure,
   naming, dependencies, and helper APIs before adding a new abstraction.
3. **Keep the payoff concrete** - Do not suggest speculative rewrites,
   aesthetic churn, or architecture changes without a clear maintenance win.
4. **Separate bugs from refactors** - Mention correctness, security, or test
   problems only when they block or materially affect the refactor. If the user
   asked for review, use `$code-review` instead.
5. **Minimize blast radius** - Favor small, verifiable changes that can be
   accepted or rejected independently.
6. **Split by responsibility** - Recommend decomposing an oversized file only
   when each proposed file has a distinct, durable role and the resulting
   structure follows repository conventions.

## Process

1. **Prioritize useful refactors** - Start with high-impact, low-risk
   maintainability improvements before cosmetic cleanup.
2. **Step through refactors one at a time** - Do not provide all proposed
   refactors in a single response.
3. **For each refactor found:**
   - Provide a brief title.
   - Explain why the refactor is worthwhile.
   - List every file that would be affected.
   - For an oversized-file refactor, explain the contextual evidence that the
     file should be split and show an annotated tree of the complete proposed
     file structure. Give each file a short responsibility description. Do not
     provide a diff or focused code example for this refactor category.
   - For every other refactor, include a file tree when files would be added,
     removed, renamed, or moved, then show a diff or focused code example of the
     proposed change.
   - State the behavior-preservation assumption.
   - Name the tests or checks to run after applying it.
   - Ask the user whether to accept or reject the refactor.
4. **Wait for user confirmation** before moving to the next refactor.
5. **After the user responds:**
   - If accepted: Apply the change, run the relevant checks when feasible, and
     move to the next refactor.
   - If rejected: Skip the change and move to the next refactor.
6. **Continue until all worthwhile refactors have been addressed.**
7. **If no refactors are worth doing:** Say that clearly and mention any areas
   intentionally left alone.
8. **After all accepted refactors are resolved:** Ask the user with this prompt:

   ```text
   Would you like me to:

   1) commit and push
   2) create/update PR
   3) all of the above
   ```

   - When creating or updating a PR, include a summary of the accepted refactors.
   - The summary and title should reflect all accepted refactors.
   - If a PR for this branch already exists, update the summary to include any
     new accepted refactors that are missing.

## Example Format

For each refactor, present it like this:

```
**Refactor 1: Extract shared validation helper**

This removes duplicated validation logic from two request handlers while
preserving the existing error messages and control flow.

**Files affected:**
- `src/users/create.ts`
- `src/users/update.ts`
- `src/users/validation.ts`

**File tree change:**

\`\`\`text
src/users/
|-- create.ts
|-- update.ts
`-- validation.ts  # new shared helper
\`\`\`

**Proposed change:**

\`\`\`diff
- if (!email || !email.includes("@")) {
-   return badRequest("Invalid email")
- }
+ const emailError = validateEmail(email)
+ if (emailError) return badRequest(emailError)
\`\`\`

**Behavior preservation:** The same invalid email message is returned for the
same inputs; only the duplicated check moves into a helper.

**Checks:** Run `npm test -- users` or the closest relevant test target.

Do you want to accept this refactor?
```

For an oversized-file refactor, replace the proposed diff with:

```
**Proposed file structure:**

\`\`\`text
src/orders/
|-- service.ts        # Preserve the public API and coordinate the workflow
|-- validation.ts     # Validate order input and domain preconditions
|-- pricing.ts        # Calculate totals, discounts, and taxes
|-- repository.ts     # Read and persist orders
`-- notifications.ts  # Dispatch order-status notifications
\`\`\`
```
