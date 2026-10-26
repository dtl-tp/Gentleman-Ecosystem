---
name: replica-recon
description: >
  Reverse-engineers any target application into a functional recon map: screen inventory, user flows,
  component catalog, inferred domain data model, and a feature matrix from public docs, pricing pages,
  store listings, and clean-room exploration. Step 1 of the Replica suite.
  Trigger: When asked to reverse engineer an app, clone an app, map user flows, or inspect a competitor's feature set.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# replica-recon

> **PHILOSOPHY: CONCEPTS > CODE.**
> You cannot build what you do not understand. A shallow recon leads to fragile architecture and messy code.
> Map the business logic and user journeys before writing a single line of code.

Everything in the Replica suite builds from what this skill produces. Output lives in the project's `replica/` directory and is proactively persisted into **Engram** for cross-session continuity.

```
replica/recon.md        # The complete functional recon map
replica/features.csv    # The weighted feature matrix (must / should / could)
replica/screens/        # Reference screenshots of the original (clean-room reference only, never shipped)
```

---

## Clean-Room Rules (MANDATORY)

We rebuild **functionality, user journeys, and UX patterns**. We NEVER steal what the original app owns:

- **Public sources & personal accounts only:** Read public documentation, pricing pages, marketing walkthroughs, and click through your own legitimate test account. Never bypass paywalls, exploit sessions, or use unauthorized accounts.
- **Reading, not scraping:** No aggressive scraping loops or automated crawler abuse.
- **No private APIs or decompiled code:** Do not capture private backend endpoints or decompile source bundles. Use public documentation or infer the domain interface from UI interactions.
- **Screenshots are reference only:** Placed in `replica/screens/` strictly to analyze layout hierarchy, spacing, and state transitions. Never bundled in production assets.

---

## Execution Workflow

### Step 1: Define Scope & Core Loop
Clarify or establish three boundaries:
1. **Target application & platform:** Web, Desktop, iOS, Android.
2. **The vertical slice:** Do not attempt to clone an entire enterprise suite on day one. Isolate the **core loop** (the primary flow users pay for).
3. **Target audience:** Niche, agency, SMB, or developer-focused alternative.

### Step 2: Source Discovery
Systematically compile public sources in a table:
- **Help Center & Docs:** Feature boundaries, edge-case handling, configuration settings.
- **Pricing & Tier Gating:** Highlights which features are mission-critical.
- **Changelog / Release Notes:** Recent engineering priorities and evolving capabilities.
- **App Store / Directory Listings:** Key marketing hooks, core screenshots, initial user reviews.
- **Public Walkthroughs & Webinars:** Real user journeys step-by-step.

### Step 3: Screen Inventory
Assign stable screen IDs (`S01`, `S02`, ...):
```markdown
| ID | Screen Name | Route / Modal Trigger | Purpose | Key Components | Observed States |
```
> [!IMPORTANT]
> Capture **every state**: Empty state, loading skeleton, filled, validation error, permission denied, responsive mobile. An unrecorded empty state is an unbuilt empty state.

### Step 4: User Flows & Click Budgets
Document end-to-end flows (`F01`, `F02`, ...) with the click count on the happy path:
```markdown
F01 Guest books a meeting
  S01 Landing -> S02 Select Date/Time -> S03 Details Form -> S04 Confirmation
  Happy Path: 4 clicks
  Edge Cases: Timezone mismatch, slot taken during submission, network timeout.
```

### Step 5: Domain Model Inference
Infer entities, fields, relationships, and validation constraints with confidence ratings:
```markdown
Booking:
  - id: UUID (Primary Key)
  - event_type_id: UUID (Foreign Key -> EventType)
  - host_id: UUID (Foreign Key -> User)
  - start_at / end_at: ISO-8601 UTC
  - guest_name, guest_email: string
  - status: enum ('confirmed', 'cancelled', 'rescheduled')
  Evidence: S03 form inputs, S04 confirmation payload, API help doc.
  Confidence: High
```

### Step 6: Feature Matrix (`features.csv`)
Initialize `replica/features.csv` with columns:
`feature,area,priority,original,clone,notes`
- `priority`: `must` | `should` | `could`
- `clone`: initialize to `no` (updated during `/replica-build`)

### Step 7: Engram Persistence
Persist the recon summary and feature matrix directly to **Engram**:
- Topic key: `sdd/{app-name}/recon`
- Title: `Recon map and feature matrix for {app-name}`
- Content: Executive summary of core loop, screen counts, domain entities, and key challenges.

---

## Deliverables Checklist
- [ ] `replica/recon.md` generated with screens, flows, and inferred domain model.
- [ ] `replica/features.csv` generated with prioritized features.
- [ ] Non-clonable elements (third-party networks, licensed media, proprietary catalogs) explicitly marked as `skip`.
- [ ] Persisted to Engram under `sdd/{app-name}/recon`.
- [ ] Ready for handoff to `/replica-architect`.
