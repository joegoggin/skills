---
name: debug
description: Diagnose bugs from user-reported symptoms, diagnostics, compiler errors, test failures, runtime logs, or combinations of symptoms and logs. Use when Codex should inspect the repo, identify the root cause, propose a concrete diff, and ask before applying the fix.
---

# Debug

## Overview

Use this skill to turn a bug report, diagnostic output, or both into a grounded
root-cause explanation and a proposed code change. Do not edit files until the
user accepts the proposed fix.

## Workflow

1. **Capture the inputs** - Separate user-observed symptoms from machine output
   such as compiler diagnostics, test failures, stack traces, console errors,
   screenshots, or logs.
2. **Inspect before diagnosing** - Check `git status --short`, then read the
   referenced files, nearby call sites, relevant tests, styles, routes, configs,
   or recent diffs. Prefer `rg` for searches.
3. **Localize the failure** - Reproduce or narrow the issue when practical with
   focused, non-destructive commands. If reproduction is expensive or blocked,
   state that and continue with the strongest evidence available.
4. **Find the root cause** - Explain the smallest code path or configuration
   choice that accounts for the symptom, diagnostic, or both. Do not propose a
   change that only silences the visible error unless it addresses the cause.
5. **Propose one fix** - Show the minimal fix as a diff and include the focused
   verification command that should pass after applying it.
6. **Ask before mutating** - Ask the user whether to apply the diff. Wait for
   confirmation before editing files or running formatters that rewrite files.
7. **Apply and verify if accepted** - Make the accepted change, run focused
   checks, and report what changed and what passed. If rejected, do not apply
   the change; ask for direction or propose an alternative.

## Input Patterns

- **Symptom only**: For reports like "`Sign In` is red but should be blue",
  inspect UI components, styles, tokens, theme overrides, state classes, and
  recent changes before assuming the fix.
- **Diagnostics only**: For logs or compiler output, parse file paths, line
  numbers, symbol names, suggested names, stack frames, and repeated root
  messages first. Inspect the referenced code before proposing edits.
- **Combined symptom and diagnostics**: Prefer explanations that account for
  both the observed behavior and the machine output. If they appear unrelated,
  say so and handle the higher-confidence issue first.

## Proposed Fix Format

Present each proposed fix like this:

```markdown
**Root cause:** [brief explanation tied to inspected evidence]

**Proposed fix:**

\`\`\`diff
- old code
+ new code
\`\`\`

**Verify with:** `command`

Do you want me to apply this fix?
```

## Guardrails

- Preserve user work. Never revert unrelated changes, and call out when the fix
  touches a file that already has uncommitted changes.
- Keep fixes small and directly tied to the diagnosed issue.
- Avoid speculative rewrites, broad refactors, dependency upgrades, or formatting
  churn unless they are required for the fix.
- When multiple independent issues are present, handle them one at a time.
- If there is no confident fix, explain the missing evidence and propose the
  next diagnostic command instead of inventing a diff.
