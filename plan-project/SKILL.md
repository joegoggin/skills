---
name: plan-project
description: Plan a new software project from a user-provided idea prompt, turn the implementation plan into ordered phases, and create GitHub issues for the plan without implementing the project. Use when Codex is asked to create GitHub issues for a new project plan, convert a project idea into phased implementation issues, or create phase issues with linked step sub-issues using the issues skill. Do not use to implement code, create app files, run migrations, or start building the planned project.
---

# Plan Project

## Overview

Turn a project idea into a phased implementation plan, then use `$issues` to create GitHub issues from that plan. Do not implement the planned project.

This skill defines the planning shape. Delegate GitHub project validation, labels, priorities, assignment, issue creation, sub-issue linking, and fallback behavior to `$issues`.

## Implementation Boundary

Never implement the project work as part of this skill. Do not edit application code, create project files, scaffold an app, run migrations, start services, install dependencies, or begin work on any created issue.

If the user asks to plan and implement in the same request, use this skill only to plan and create issues, then stop. Implementation requires a separate explicit request after issue creation.

## Workflow

1. Read the user's project idea and inspect the repository if one exists.
2. Clarify only high-impact unknowns that materially affect architecture, scope, platform, data ownership, or delivery order.
3. Draft a phased implementation plan before creating issues.
4. Convert each phase into a main issue.
5. Convert each ordered phase step into a linked sub-issue under that phase.
6. Ensure each phase issue description lists all of its step sub-issues.
7. Use `$issues` to create the GitHub issues, treating each phase issue as the
   main issue for that phase.
8. Stop after summarizing the created issues. Do not begin implementing any phase or sub-issue.

## Repository And Project Checks

Before creating issues, follow `$issues` project rules:

- Read the repo's `AGENTS.md` and locate the GitHub Project for the repo.
- If the project is missing or ambiguous, do not create issues; tell the user no GitHub Project is clearly defined and ask them to add or clarify it in `AGENTS.md`.
- If the project is defined but available tools cannot add issues to that project, do not create issues unless the user explicitly approves creating them without project linkage.

## Planning Shape

Create phases that are independently understandable and ordered by delivery dependency. Prefer phases that produce usable milestones over phases grouped only by technical layer.

For each phase, include:

- Phase title.
- Phase goal.
- Ordered implementation steps.
- Acceptance criteria.
- Suggested label and priority.

Default the label to `Feature` and priority to `Medium` unless the project idea clearly implies another `$issues` label or priority.

## Issue Creation Shape

For each phase:

- Create one main phase issue summarizing the phase goal, scope, dependencies, acceptance criteria, label, and priority.
- Create one linked sub-issue for each implementation step.
- Do not create a separate project-wide parent issue unless the user explicitly asks for one.
- Keep sub-issues small enough to implement independently, with checklist steps and phase context.
- Order sub-issues in the sequence they should be implemented.
- After sub-issues exist, ensure the phase issue description lists every sub-issue with links or issue numbers.

If GitHub sub-issue relationships are unavailable through the current tools, follow `$issues` fallback behavior: create child issues that link back to the phase issue, list them in the phase issue description, and tell the user the sub-issue relationship must be added manually.

## Output

After issue creation, summarize:

- The phase issues created.
- The linked step sub-issues created for each phase.
- Any project-linkage or sub-issue relationship limitations encountered.
- That no implementation work was performed.
