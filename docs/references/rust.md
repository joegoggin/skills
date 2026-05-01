# Rust Documentation

All public and private items must have rustdoc comments following these
conventions.

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
