---
name: merge-conflict
description: Resolve an existing Git merge conflict interactively. Use when Codex finds unmerged files, conflict markers, or is asked to explain and resolve merge conflicts one conflict at a time.
---

# Merge Conflict

## Merge Conflict Resolution Process

When asked to help resolve merge conflicts, follow this interactive process:

1. Identify all conflicted files first using `git status --short` and
   `git diff --name-only --diff-filter=U`.
2. Work through conflicts one at a time (do not resolve all at once in a single response).
3. For each conflict:
   - Explain what each side of the conflict is doing.
   - Account for non-text conflicts such as add/add, delete/modify, and rename
     conflicts.
   - Propose a specific fix with a diff-style snippet.
   - Ask the user to accept or reject the proposed change.
4. Wait for user confirmation before applying each conflict resolution.
5. If accepted, apply the change and continue. If rejected, do not skip the
   conflict; ask what should be preserved or propose an alternative resolution.
6. After all conflicts are addressed:
   - Verify no merge markers remain (`<<<<<<<`, `=======`, `>>>>>>>`) in project files.
   - Verify no files remain in any unmerged state.
   - Stage resolved files.
   - Run relevant checks/build commands when possible and report results.
7. After conflict resolution is complete, ask with this prompt:

   ```text
   Would you like me to:

   1) commit and push
   2) create/update PR
   3) all of the above
   ```

   When creating or updating a PR, include a summary of the merge resolution.
