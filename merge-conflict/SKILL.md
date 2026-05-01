---
name: merge-conflict 
description: Handle an existing merge conflict. 
---

## Merge Conflict Resolution Process

When asked to help resolve merge conflicts, follow this interactive process:

1. Identify all conflicted files first.
2. Work through conflicts one at a time (do not resolve all at once in a single response).
3. For each conflict:
   - Explain what each side of the conflict is doing.
   - Propose a specific fix with a diff-style snippet.
   - Ask the user to accept or reject the proposed change.
4. Wait for user confirmation before applying each conflict resolution.
5. If accepted, apply the change; if rejected, skip and propose the next conflict.
6. After all conflicts are addressed:
   - Verify no merge markers remain (`<<<<<<<`, `=======`, `>>>>>>>`) in project files.
   - Verify no files remain in unmerged (`UU`) state.
   - Stage resolved files.
   - Run relevant checks/build commands when possible and report results.
7. After conflict resolution is complete, ask whether to:
   - Commit the merge resolution
   - Push the branch
   - Create or update a PR summary
