# Technical Sub-Issue Specs

Read this reference before drafting phase sub-issues. Publish each spec as the
GitHub sub-issue body, with the canonical `P{phase}S{step}: {title}` issue title.
The standalone example includes a title heading; omit that duplicate heading
from the GitHub body.

## Format

Use this section order, scaling detail to the task:

1. **Goal and scope:** Intended outcome, included work, and relevant exclusions.
2. **Context and dependencies:** Parent phase, prerequisite issues, consumers,
   and existing integration points. Include relevant dependency decisions here.
3. **File changes:** Table of paths, change types, and responsibilities. Identify
   existing files verified through inspection and proposed new files explicitly.
4. **Interfaces and behavior:** Relevant signatures, types, data shapes, defaults,
   validation, error contracts, and integration behavior, grouped by component.
5. **Database changes:** Schema, constraints, and necessary migration or rollout
   details. Omit when inapplicable.
6. **Implementation sequence:** Short ordered implementation tasks, without
   progress checkboxes, full implementation code, or line-specific diffs.
7. **Acceptance criteria:** Checkboxes describing observable completion.
8. **Verification:** Focused automated scenarios and useful manual checks; group
   by test file when useful and include verified repository commands.

Ground existing paths, symbols, packages, and commands in repository inspection.
Distinguish proposed additions from existing integration points. For work that
depends on earlier planned issues, identify contracts as planned and link the
prerequisites rather than claiming they already exist. Use issue references once
available; replace temporary phase/step references with created issue links.

Specify public or cross-component contracts needed to implement the task, while
leaving routine internal coding choices open. Use short signature or payload
examples, not complete implementations. For tasks without new interfaces,
describe affected behavior without inventing APIs to fill the template. Omit
other inapplicable sections instead of filling them with boilerplate.

Resolve material scope and contract unknowns during planning. Clearly label
proposed checks when test tooling does not yet exist; do not invent executable
commands. Include rollout details only where they affect implementation. Avoid
repeating requirements in separate behavior, integration-flow, and deployment
sections, or adding empty open-question sections.

## Example

This example assumes a TypeScript/PostgreSQL repository with the stated existing
infrastructure and `just` recipes. Paths, symbols, and issue numbers are
illustrative, not defaults to impose on other projects.

````markdown
# P4S2: Persist notification preferences

## Goal and scope

Allow authenticated users to save notification preferences that persist
across sessions.

Included:

- Preference types, validation, and defaults.
- Database persistence.
- Authenticated read and update endpoints.

Excluded:

- Settings UI.
- Sending or scheduling notifications.
- Organization-wide preferences.

## Context and dependencies

Parent: #84 — Phase 4: Notification settings.
Depends on: #85 — P4S1: Establish authenticated settings access.

The settings UI and delivery service consume these interfaces in later
sub-issues.

Reuse these verified existing integration points:

- `src/auth/require-user.ts`: session authentication through `requireUser`.
- `src/db/index.ts`: PostgreSQL access through `db`.
- `src/api/errors.ts`: `ValidationError` and centralized error responses.
- `src/api/types.ts`: `ApiRequest` and `ApiResponse<T>`.

No new third-party dependencies are required.

## File changes

| File | Change | Responsibility |
| --- | --- | --- |
| `src/notifications/preferences.ts` | Create (proposed) | Types, defaults, and validation. |
| `src/notifications/preferences-repository.ts` | Create (proposed) | Reads and atomic upserts. |
| `src/api/me/notification-preferences.ts` | Create (proposed) | GET and PUT handlers. |
| `src/api/routes.ts` | Modify (existing) | Register both endpoints. |
| `db/migrations/0042_notification_preferences.sql` | Create (proposed) | Table and constraints. |
| `tests/notifications/preferences.test.ts` | Create (proposed) | Domain validation tests. |
| `tests/notifications/preferences-repository.test.ts` | Create (proposed) | Persistence and concurrency tests. |
| `tests/api/notification-preferences.test.ts` | Create (proposed) | HTTP and authentication tests. |

## Interfaces and behavior

### Domain — `src/notifications/preferences.ts`

Proposed exports:

```ts
export type DigestFrequency = "immediate" | "daily" | "weekly";

export interface NotificationPreferences {
  emailEnabled: boolean;
  digestFrequency: DigestFrequency;
}

export const DEFAULT_NOTIFICATION_PREFERENCES:
  Readonly<NotificationPreferences> = {
    emailEnabled: false,
    digestFrequency: "weekly",
  };

export function parseNotificationPreferences(
  input: unknown,
): NotificationPreferences;
```

Validation requires exactly both fields and performs no type coercion.
Reject missing fields, unknown fields, null values, arrays, and invalid
types or frequencies using the existing `ValidationError`.

Disabling email preserves the selected digest frequency.

### Persistence — `src/notifications/preferences-repository.ts`

Proposed exports using the domain type above:

```ts
export function getNotificationPreferences(
  userId: string,
): Promise<NotificationPreferences>;

export function saveNotificationPreferences(
  userId: string,
  preferences: NotificationPreferences,
): Promise<NotificationPreferences>;
```

`getNotificationPreferences`:

- Returns saved values or a fresh copy of the defaults.
- Does not insert a record when returning defaults.
- Propagates database errors rather than substituting defaults.

`saveNotificationPreferences`:

- Accepts validated preferences.
- Atomically upserts both fields using parameterized queries.
- Returns saved values and propagates database errors.
- Prevents duplicate records and partially updated field pairs.
- Uses last-committed-update wins for concurrent saves.

### HTTP — `src/api/me/notification-preferences.ts`

Proposed handlers using the existing API types and new domain type:

```ts
export function getPreferences(
  request: ApiRequest,
): Promise<ApiResponse<NotificationPreferences>>;

export function putPreferences(
  request: ApiRequest,
): Promise<ApiResponse<NotificationPreferences>>;
```

| Endpoint | Input | Success |
| --- | --- | --- |
| `GET /api/me/notification-preferences` | Authenticated session | 200 with saved preferences or defaults. |
| `PUT /api/me/notification-preferences` | Session and complete preferences | 200 with saved preferences. |

Example PUT request and successful response:

```json
{
  "emailEnabled": true,
  "digestFrequency": "daily"
}
```

Both handlers authenticate through `requireUser` before accessing preferences.
User identity comes exclusively from the session; a `userId` body field is
rejected as an unknown field.

PUT validates the request before calling the repository. Partial updates
are not supported. Successful responses include `Cache-Control: no-store`.

Use the existing error envelope:

- `400`: malformed JSON or invalid preference fields.
- `401`: missing or invalid session.
- `415`: unsupported request content type.
- `500`: database failure.

Invalid requests must not modify persisted preferences.

## Database changes

Create `notification_preferences`:

| Column | Type | Constraints |
| --- | --- | --- |
| `user_id` | UUID | Primary key; references `users(id)` with delete cascade. |
| `email_enabled` | Boolean | Not null. |
| `digest_frequency` | Text | Not null; restricted to `immediate`, `daily`, or `weekly`. |

The primary key supports lookups and enforces one record per user.
Writes supply both preference fields; database defaults are unnecessary.

Apply the migration before deploying the endpoints. Existing users require
no backfill because absent records resolve to application defaults.
An application rollback can retain the table and saved data.

## Implementation sequence

1. Add domain types, defaults, validation, and domain tests.
2. Add the migration and implement repository reads and atomic upserts.
3. Add persistence tests using the existing PostgreSQL test fixtures.
4. Implement and register both authenticated HTTP handlers.
5. Add endpoint tests and run the repository checks.

## Acceptance criteria

- [ ] A first read returns defaults without inserting a record.
- [ ] Saved preferences survive subsequent reads and new sessions.
- [ ] Each user can read and update only their own preferences.
- [ ] Invalid updates leave existing preferences unchanged.
- [ ] Disabling email preserves the selected digest frequency.
- [ ] Concurrent saves leave one complete preference record.
- [ ] Database failures produce errors instead of defaults or success.
- [ ] Deleting a user removes their preference record.

## Verification

### Domain tests

File: `tests/notifications/preferences.test.ts`

- Accept both boolean values and every supported frequency.
- Reject missing, unknown, null, and incorrectly typed fields.
- Reject arrays, scalar inputs, and coerced values such as `"true"`.

### Persistence tests

File: `tests/notifications/preferences-repository.test.ts`

- Verify default reads do not insert rows.
- Verify first save, replacement, and isolation between two users.
- Verify concurrent saves produce one complete submitted field pair.
- Verify database constraints and user-deletion cascade.
- Verify query failures propagate.

### HTTP tests

File: `tests/api/notification-preferences.test.ts`

- Verify successful GET and PUT contracts and cache headers.
- Verify authentication and each documented error response.
- Verify a supplied `userId` is rejected.
- Verify invalid updates preserve saved values.
- Verify a new session retrieves the same user's saved preferences.

### Repository checks

Run the existing repository recipes:

```sh
just test
just lint
just typecheck
```

Manual check: save non-default preferences, sign out, sign back in,
and confirm those values remain.
````
