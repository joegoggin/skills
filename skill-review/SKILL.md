---
name: skill-review
description: Review current-branch skill changes for trigger quality, SKILL.md structure, bundled resource usefulness, validation gaps, stale UI metadata, typos, and unnecessary context bloat. Use when Codex is asked to review a skill, skill folder, skill diff, or recent changes to Codex skills, and present proposed fixes interactively one issue at a time.
---

# Skill Review

## What to Review

Unless told otherwise, assume you are reviewing skill-related changes on the
current branch. Inspect `git status`, staged, unstaged, and untracked changes,
and the branch diff against its base branch when one can be determined.

If the user names a skill path, skill folder, PR, diff, or narrower scope, use
that scope and state it before presenting findings.

Load `$skill-creator` when available before judging skill design. Use its
current standards as the source of truth for skill naming, frontmatter,
progressive disclosure, bundled resources, UI metadata, and validation.

## What to Check

- **Trigger quality** - Ensure the frontmatter description clearly says what
  the skill does and when to use it, including concrete trigger contexts.
- **Required structure** - Verify `SKILL.md` exists, YAML frontmatter has only
  `name` and `description`, the folder name matches the skill name, and names
  use lowercase letters, digits, and hyphens.
- **Instruction quality** - Flag vague workflows, missing sequencing, stale
  assumptions, duplicated guidance, or instructions that leave important
  decisions unresolved for the next agent.
- **Context discipline** - Remove unnecessary background, obvious advice,
  oversized examples, copied reference material, and unused sections that make
  the skill expensive to load.
- **Progressive disclosure** - Move details into `references/` when they are
  lengthy or conditional, and ensure `SKILL.md` tells Codex exactly when to
  read each reference.
- **Bundled resources** - Check that `scripts/`, `references/`, and `assets/`
  are present only when useful, named clearly, referenced from `SKILL.md` when
  needed, and free of placeholder files.
- **Validation and testing** - Identify missing `quick_validate.py` runs,
  untested scripts, and complex skills that need realistic forward-testing.
- **UI metadata** - If `agents/openai.yaml` exists, ensure its display name,
  short description, and default prompt still match the skill.
- **Spelling and docs** - Fix typos and stale documentation inside skill files.

## Process

1. **Prioritize high-impact findings** - Start with issues that affect
   triggering, correctness, safety, validation, or whether another Codex
   instance can reliably use the skill.
2. **Step through issues one at a time** - Do not provide all feedback in a
   single response.
3. **For each issue found:**
   - Provide a clear title and description.
   - Explain why it matters for skill behavior or maintainability.
   - Show the proposed diff or focused file change.
   - Name the validation or checks to run after applying it.
   - Ask the user whether to accept or reject the change.
4. **Wait for user confirmation** before moving to the next issue.
5. **After the user responds:**
   - If accepted: Apply the change, run relevant checks when feasible, and move
     to the next issue.
   - If rejected: Skip the change and move to the next issue.
6. **Continue until all meaningful skill issues have been addressed.**
7. **If no issues are found:** Say that clearly and mention any residual
   validation gaps or areas not checked.
8. **After all accepted fixes are resolved:** Ask the user if they want to:
   - Commit the changes.
   - Push to the remote branch.
   - Create or update a PR with a summary of the accepted fixes.

## Example Format

For each issue, present it like this:

```
**Issue 1: Trigger description misses the main use case**

The frontmatter description says what the skill does, but it does not list the
user requests that should trigger it. Because frontmatter is the only trigger
surface loaded before the skill fires, this can make the skill hard to invoke
implicitly.

**Proposed fix:**

\`\`\`diff
- description: Review skills for quality.
+ description: Review Codex skills for trigger quality, SKILL.md structure,
+ bundled resource usefulness, validation gaps, and stale metadata. Use when
+ Codex is asked to review a skill, skill folder, skill diff, or recent changes
+ to Codex skills.
\`\`\`

**Checks:** Run `quick_validate.py <path/to/skill>`.

Do you want to accept this change?
```
