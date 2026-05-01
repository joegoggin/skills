# Providing Instruction For Issues

When asked to provide instructions for implementing an issue you should do the
following:

- Read the issue for context
    - If issue is a sub-issue read the main issue for context 
- Come up with a plan to implement the issues
    - This plan should always default to using `just` commands if they exist
- Write the plan to a file called `issue-*.md` where `*` is the issue number
    - If asked to create instructions for multiple issues or for the sub-issues
      of a main issue ensure the each individual issue has there own file
    - DO NOT include multiple issues in one file
    - If file matching the pattern for an issue already exists DO NOT recreate a
      plan for that issue
    - These files should be stored in the `issues` directory
- Include detailed code examples for each step
- Include steps for manually testing the changes
- DO NOT implement the plan 
