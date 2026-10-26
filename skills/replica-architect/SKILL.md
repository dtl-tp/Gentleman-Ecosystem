---
name: replica-architect
description: >
  Designs the production architecture, database schema, and domain layers for an app clone,
  enforcing Screaming / Hexagonal Architecture, The Scope Rule, Zod boundaries, and strict relational integrity.
  Step 2 of the Replica suite.
  Trigger: When designing stack, database schema, API structure, or folder layout for a cloned app.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# replica-architect

> **PHILOSOPHY: SOLID FOUNDATIONS BEFORE CODE.**
> A generic "indie hacker" flat folder structure collapses the moment complexity grows.
> We design software with strict boundaries, pure domain logic, and screaming folder structures.

Reads `replica/recon.md` and `replica/features.csv`.
Writes `replica/architecture.md` and `replica/schema.sql`.

---

## 1. Architectural Blueprint: Screaming & Hexagonal

We organize the codebase around **business capabilities (features)**, never generic technical buckets:

```
src/
├── domain/                      # PURE business logic, entities, value objects & ports
│   ├── booking/
│   │   ├── booking.entity.ts    # Invariants and state transitions
│   │   └── booking.repository.ts # Port (interface), no ORM imports
│   └── shared/
│       └── result.ts            # Result / Either pattern for error handling
├── application/                 # Use Cases / Application Services
│   └── booking/
│       ├── book-slot.use-case.ts
│       └── book-slot.dto.ts     # Zod validated input/output schemas
├── infrastructure/              # Adapters, ORM implementations, third-party clients
│   ├── database/
│   │   ├── drizzle/schema.ts    # Database tables & relations
│   │   └── repositories/        # Implements domain ports
│   ├── payments/stripe.client.ts
│   └── email/resend.client.ts
└── presentation/                # UI, API routes, Controllers & State
    ├── features/                # Follows THE SCOPE RULE
    │   ├── booking-flow/
    │   │   ├── components/      # Private to booking-flow
    │   │   ├── hooks/           # Container logic / orchestration
    │   │   └── booking-page.tsx
    │   └── shared/              # Shared across 2+ features
    │       └── components/      # Presentational primitives
    └── app/                     # Route definitions / handlers
```

---

## 2. The Scope Rule (MANDATORY)

**"Scope determines structure"**: Where a component, hook, or utility lives depends strictly on where it is consumed:

| Usage | Placement |
| :--- | :--- |
| Used by **1 feature** | `src/presentation/features/[feature]/components/` |
| Used by **2+ features** | `src/presentation/features/shared/components/` |
| Global design primitive | `src/presentation/shared/ui/` (buttons, inputs, dialogs) |

---

## 3. Strict Boundary Validation (Zod 4)

**NEVER trust external data. NEVER use `any`.**
Every API route, Server Action, and Webhook must validate incoming payloads through Zod schemas before reaching the application layer:

```typescript
import { z } from "zod";

export const CreateBookingSchema = z.object({
  eventTypeId: z.string().uuid(),
  hostId: z.string().uuid(),
  startAt: z.string().datetime({ offset: true }),
  endAt: z.string().datetime({ offset: true }),
  guestEmail: z.string().email().toLowerCase(),
  guestName: z.string().min(2).max(100),
  timezone: z.string().min(1),
  answers: z.record(z.unknown()).default({}),
});

export type CreateBookingDTO = z.infer<typeof CreateBookingSchema>;
```

---

## 4. Database Schema & Relational Integrity

Do not solve database problems in the UI. Enforce invariants directly in SQL:

- **Primary Keys:** UUID v7 or `gen_random_uuid()` for distributed, collision-resistant IDs.
- **Timestamps:** Always `timestamptz` stored in UTC.
- **Currency & Money:** Always integer cents (e.g. `1500` for $15.00) plus an ISO-4217 currency column (`USD`). Never floating-point numbers.
- **Foreign Keys:** Explicit `ON DELETE` rules (`CASCADE` vs `RESTRICT`).
- **Exclusion Constraints / Concurrency:** Overlapping bookings or slot collisions must be prevented by the database:
  ```sql
  -- Prevents double-booking the same host for overlapping time ranges
  CREATE EXTENSION IF NOT EXISTS btree_gist;
  ALTER TABLE bookings
    ADD CONSTRAINT no_overlapping_slots
    EXCLUDE USING gist (
      host_id WITH =,
      tstzrange(start_at, end_at) WITH &&
    ) WHERE (status = 'confirmed');
  ```

---

## 5. Technology Stack Defaults (Battle-Tested)

| Layer | Recommended Default | Alternative | Why |
| :--- | :--- | :--- | :--- |
| **Framework** | Next.js 15 (App Router) / React 19 or Angular 19 | Remix / SvelteKit | Strict SSR, Server Actions, modern compiler |
| **State** | Zustand 5 (with atomic selectors) / Signals | GPX-Store / Redux Toolkit | Predictable state, no unnecessary re-renders |
| **Database** | PostgreSQL (Supabase / Neon) | Turso / Cloudflare D1 | Rock-solid relational foundation, RLS, ACID |
| **ORM** | Drizzle ORM | Prisma | Type-safe, close to SQL, zero runtime overhead |
| **Validation** | Zod 4 | Valibot | Standard boundary validation |
| **Payments** | Stripe Checkout & Customer Portal | Lemon Squeezy | Security, hosted PCI compliance, easy webhooks |
| **Email** | Resend | Postmark / SES | Fast, developer-friendly, transactional delivery |

---

## Deliverables Checklist
- [ ] `replica/architecture.md` generated detailing layers, stack choices, and data flow.
- [ ] `replica/schema.sql` written with explicit constraints, foreign keys, and indexes.
- [ ] Screaming folder structure defined following the Scope Rule.
- [ ] Concurrency and idempotency strategies established for webhooks and background jobs.
- [ ] Persisted to Engram under `sdd/{app-name}/architecture`.
- [ ] Ready for handoff to `/replica-design` and `/replica-build`.
