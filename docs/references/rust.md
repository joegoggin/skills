# Rust Documentation

All public and private items must have rustdoc comments following these
conventions.

## Contents

- Module-level docs
- Item docs
- Enum variant docs
- Function and method docs
- Test function docs
- Handler/controller methods
- Cross-references
- Formatting rules

## Module-Level Docs

Use `//!` comments at the top of the file. Start with a one-line summary,
then provide extended context. When the module contains submodules, include
a `# Modules` section:

```rust
//! Email delivery for the GigLog API.
//!
//! This module provides email sending capabilities through the
//! [Resend](https://resend.com) API. It is split into a low-level client and
//! higher-level sender abstractions that compose emails for specific features.
//!
//! # Modules
//!
//! - [`client`] — Core HTTP client for the Resend API.
//! - [`senders`] — Specialized email sender implementations.
```

## Item Docs (Structs, Enums, Traits)

Use `///` comments. Start with a concise summary. Each field gets its own
`///` comment:

```rust
/// HTTP client for sending emails through the Resend API.
///
/// Wraps a [`reqwest::Client`] with Resend API credentials and provides
/// a single [`send_email`](Self::send_email) method for delivering messages.
pub struct EmailClient {
    /// Underlying HTTP client used for API requests.
    client: Client,
    /// Resend API key for authentication.
    api_key: String,
}
```

## Enum Variant Docs

When documenting enums, each variant must have its own `///` comment.

- Unit variants: describe the meaning, behavior, or state represented.
- Tuple variants: describe what each payload value represents.
- Struct variants: include `///` docs for variant fields when applicable.
- Variant summaries end with a period.

```rust
/// Message emitted by the route list screen.
pub enum RouteListMsg {
    /// Executes the route at the provided index.
    RunRoute(usize),
    /// Opens the editor for the route at the provided index.
    EditRoute(usize),
    /// Persists updated route-list UI state.
    StateChanged(RouteListState),
}
```

## Function and Method Docs

Use `///` comments with formal sections in this order:

1. **Summary line** — starts with a verb (Creates, Sends, Returns, Validates, etc.)
2. **Extended description** (optional) — additional behavior or side effects
3. **`# Arguments`** — bulleted list of parameters
4. **`# Returns`** — description of the return value
5. **`# Errors`** — error variants and when they occur

Only include sections that apply (skip `# Errors` for infallible functions,
skip `# Arguments` for zero-parameter methods, etc.):

```rust
/// Sends a plain-text email to a single recipient via the Resend API.
///
/// # Arguments
///
/// * `to` — Recipient email address.
/// * `subject` — Email subject line.
/// * `body` — Plain-text email body.
///
/// # Returns
///
/// An empty [`ApiResult`] on success.
///
/// # Errors
///
/// Returns [`ApiErrorResponse::InternalServerError`] if the HTTP request
/// to the Resend API fails.
pub async fn send_email(&self, to: &str, subject: &str, body: &str) -> ApiResult<()> {
```

## Test Function Docs

Use `///` rustdoc comments on every `#[test]` function. Place the rustdoc
block immediately above `#[test]`.

Use this structure:

1. **Summary line** — starts with `Verifies` and describes the behavior under
   test.
2. **`# Example Under Test`** — shows the concrete inputs, fixtures, commands,
   paths, config snippets, or setup being exercised.
3. **`# Assertions`** — lists each meaningful assertion the test makes,
   including parse or load success when an `unwrap` is part of the behavior
   being proven.
4. **`# Why`** — optional; include only for non-obvious regression intent,
   precedence rules, accumulated errors, user-facing contracts, or other
   behavior that future readers may not infer from the test name.

Use fenced code blocks in examples:

- `toml` for TOML config snippets.
- `text` for CLI commands, paths, stdout/stderr snippets, and non-language
  examples.

Test docs must describe only the current assertions and behavior in the test.
Do not mention removed assertions, obsolete product names, or behavior the test
does not currently check.

````rust
/// Verifies CLI validation diagnostics include config field names.
///
/// # Example Under Test
///
/// ```toml
/// [services.api]
/// command = []
/// ```
///
/// ```text
/// goggin-rs-process-watch run --config bad.toml
/// ```
///
/// # Assertions
///
/// - The command exits with failure.
/// - Standard error contains `invalid config:`.
/// - Standard error contains `services.api.command`.
///
/// # Why
///
/// Empty command arrays should be reported with the full user-facing config
/// field path.
#[test]
fn run_reports_validation_field_names() {
    // Test body omitted.
}
````

## Handler/Controller Methods

Include the HTTP method and route path in the extended description:

```rust
/// Registers a new user account.
///
/// Mapped to `POST /sign-up`. Creates the user, generates an email
/// verification code, and sends a confirmation email.
```

## Cross-References

Use rustdoc link syntax for types, methods, and modules:

- Types: `` [`TypeName`] ``
- Methods on self: `` [`method_name`](Self::method_name) ``
- Modules: `` [`module_name`] ``

## Formatting Rules

- All summaries and bullet descriptions end with a period.
- Argument bullets use an em-dash separator: ``* `param` — Description.``
- Return descriptions start with "A" or "An" followed by the type
  (e.g., "An empty [`ApiResult`] on success.").
- Error descriptions start with "Returns [`ErrorVariant`] if...".
- Private functions receive the same documentation as public ones.
