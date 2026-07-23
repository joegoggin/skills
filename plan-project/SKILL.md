---
name: plan-project
description: Plan a new or continuing software project from a user-provided idea prompt, turn the implementation plan into sequentially numbered phases, and create GitHub issues without implementing the project. Use when Codex is asked to create GitHub issues for an initial project plan, extend an existing phased plan with features or changes, or create phase issues with compactly named linked sub-issues using the issues-create skill. Do not use to implement code, create app files, run migrations, or start building the planned project.
---

# Plan Project

## Overview

Turn a new project idea, feature, or change into a phased implementation plan, then use `$issues-create` to create GitHub issues from that plan. Continue numbering after existing phases when the project already has a plan. Do not implement the planned work.

This skill defines the planning shape. Delegate GitHub project validation, labels, priorities, assignment, issue creation, sub-issue linking, and fallback behavior to `$issues-create`.

## Implementation Boundary

Never implement the project work as part of this skill. Do not edit application code, create project files, scaffold an app, run migrations, start services, install dependencies, or begin work on any created issue.

If the user asks to plan and implement in the same request, use this skill only to plan and create issues, then stop. Implementation requires a separate explicit request after issue creation.

For issue work, use only `$issues-create`. Do not invoke `$issues`,
`$issues-implement`, `$issues-step`, or `$issues-instructions`.

## Workflow

1. Read the user's project idea and inspect the repository if one exists.
2. Locate the repository's GitHub Project and determine the next phase number.
3. Clarify only high-impact unknowns that materially affect architecture, scope, platform, data ownership, or delivery order.
4. Draft a phased implementation plan before creating issues.
5. Convert each phase into a sequentially numbered main issue.
6. Convert each ordered phase step into a compactly named linked sub-issue under
   that phase.
7. Ensure each phase issue description lists all of its sub-issues.
8. Use `$issues-create` to create the GitHub issues, treating each phase issue as the
   main issue for that phase.
9. Stop after summarizing the created issues. Do not begin implementing any phase or sub-issue.

## Repository And Project Checks

Before creating issues, follow `$issues-create` project rules:

- Read the repo's `AGENTS.md` and locate the GitHub Project for the repo.
- If the project is missing or ambiguous, do not create issues; tell the user no GitHub Project is clearly defined and ask them to add or clarify it in `AGENTS.md`.
- If the project is defined but available tools cannot add issues to that project, do not create issues unless the user explicitly approves creating them without project linkage.

## Phase Numbering

Before drafting the plan, inspect all active and archived items in the configured GitHub Project whose content is an open or closed issue. Check those issues for main titles in the canonical form `Phase N: {short title}`, where `N` is a positive integer.

- Use one greater than the highest canonical phase number as the first new phase number.
- Start at Phase 1 when no canonical phase issue exists. Treat this as normal project planning, not as an error or a different workflow.
- Number multiple new phases consecutively from that starting number.
- Ignore child issue titles, unrelated items, and malformed phase titles. Do not renumber existing issues. Gaps and duplicate phase numbers do not change the highest-number rule.
- If the available tools cannot enumerate the project's issues, do not guess or create issues. Tell the user the next phase number cannot be determined safely.

## Planning Shape

Create phases that are independently understandable and ordered by delivery dependency. Prefer phases that produce usable milestones over phases grouped only by technical layer.

For each phase, include:

- Phase title.
- Phase goal.
- Ordered implementation steps.
- Acceptance criteria.
- Suggested label and priority.

Default the label to `Feature` and priority to `Medium` unless the project idea clearly implies another `$issues-create` label or priority.

## Issue Creation Shape

For each phase:

- Create one main phase issue summarizing the phase goal, scope, dependencies, acceptance criteria, label, and priority.
- Title the main issue as `Phase {phase_number}: {short phase title}`, for example `Phase 6: Add team collaboration`.
- Create one linked sub-issue for each implementation step.
- Do not create a separate project-wide parent issue unless the user explicitly asks for one.
- Title each phase sub-issue as `P{phase_number}S{step_number}: {short task
  title}`, for example `P3S1: Add nested render tree support`.
- Keep sub-issues small enough to implement independently, with phase context
  and a clear expected result.
- Order sub-issues in the sequence they should be implemented.
- After sub-issues exist, ensure the phase issue description lists every sub-issue with links or issue numbers.

If GitHub sub-issue relationships are unavailable through the current tools, follow `$issues-create` fallback behavior: create child issues that link back to the phase issue, list them in the phase issue description, and tell the user the sub-issue relationship must be added manually.

## Output

After issue creation, summarize:

- The phase issues created.
- The linked sub-issues created for each phase.
- Any project-linkage or sub-issue relationship limitations encountered.
- That no implementation work was performed.
