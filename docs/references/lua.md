# Lua Documentation

All public and private Lua modules, helpers, methods, and tests should use
EmmyLua-style documentation comments following these conventions.

## Module-Level Docs

Use `---` comments at the top of each Lua file. Start with a concise summary,
then add a blank `---` line and a short extended description of the module's
responsibility.

```lua
--- Project layout discovery for Rust/Leptos applications.
---
--- Resolves configured source and style paths from the current Neovim buffer,
--- working directory, or expanded file path.
```

## Function and Method Docs

Use `---` prose comments immediately above every `local function`,
`function M.name`, and table method. Start with a short behavior summary, add
extended context only when it clarifies side effects or control flow, then list
typed annotations.

```lua
--- Resolves project paths from the current Neovim context.
---
--- Searches candidate roots for either a nested `web` layout or a direct web
--- root layout. Returns a warning string when required paths cannot be found.
---
---@param required string[]|nil Path keys that must exist for a layout to match.
---@return table|nil paths Resolved project paths when a layout is found.
---@return string|nil err User-facing warning when required paths cannot be located.
---
function M.resolve(required)
```

Use a blank `---` separator before annotation blocks and another before the
function body. Omit `---@param` and `---@return` lines when they do not apply.

## Type Annotations

Use EmmyLua annotations for non-obvious values and signatures:

- `---@type table<string, string>` for typed maps.
- `---@type table<string, "directory"|"file">` for map values with literal
  options.
- `---@param name string|nil` for nilable parameters.
- `---@param lines string[]` and `---@return table[] layouts` for arrays.
- `---@param fn fun()` for callbacks.
- Multiple `---@return` lines for multi-value returns.

Return annotations should name the returned value and describe it:

```lua
---@return boolean exists Whether the path exists.
---@return string|nil err Error message when the operation fails.
```

## Local Tables and Constants

Add `---@type` above module-level tables when the key or value shape is useful
to future readers or Lua language tooling. Do not add type comments for values
whose shape is obvious from nearby code.

```lua
---@type table<string, string>
local PATH_LABELS = {
    components_dir = "src/components",
}
```

## Test Docs

Document each named test block with `---` comments. Start the summary with
`Verifies`, then include `# Example Under Test` and `# Assertions` sections.
Use bullets for the meaningful assertions the test makes.

```lua
--- Verifies filesystem helpers for missing, existing, and ensured paths.
---
--- # Example Under Test
---
--- A temporary nested directory and files are created through the filesystem
--- helper module.
---
--- # Assertions
---
--- - Missing files report non-existence and read as an empty line list.
--- - Nested directories are created on demand.
--- - Written files exist and read back with the same lines.
---
test("filesystem helpers read write and ensure paths", function()
```

## Formatting Rules

- Use `---` documentation comments, not `--`, for docs consumed by tooling.
- Keep summaries concise, present tense, and behavior-focused.
- End summaries and bullet descriptions with periods.
- Document private helpers with the same style as public module functions.
- Prefer one short extended-description paragraph over long implementation
  narration.
- Do not document obvious local variables or restate code mechanics.
