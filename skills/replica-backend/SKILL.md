---
name: replica-backend
description: >
  Builds backend services, database migrations, domain use cases, authentication,
  and idempotent payment webhooks following clean architecture principles. Step 5 of the Replica suite.
  Trigger: When implementing backend logic, database migrations, auth, Stripe payments, or API endpoints for an app clone.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# replica-backend

> **PHILOSOPHY: BUSINESS LOGIC INDEPENDENT OF FRAMEWORKS.**
> Controllers and server actions should be thin adapters.
> The core domain logic and database operations must reside in decoupled Use Cases and Repositories.

Reads `replica/architecture.md` and `replica/schema.sql`.
Writes backend migrations, domain use cases, and keeps `replica/backend.md` updated.

---

## 1. Security & Clean-Room Rules

1. **Official APIs & User-Managed Keys:** Only call official third-party APIs (Stripe, Google Calendar, Resend) using the user's own developer keys. Never reverse-engineer or proxy through the original app's private endpoints.
2. **Environment Variable Hygiene:** Never hardcode secrets. Always document required keys in `.env.example`:
   ```bash
   DATABASE_URL=postgresql://...
   STRIPE_SECRET_KEY=sk_test_...
   STRIPE_WEBHOOK_SECRET=whsec_...
   RESEND_API_KEY=re_...
   ```
3. **Test Mode First:** Implement and test all financial transactions with Stripe Test Mode before switching to production.

---

## 2. Core Backend Pillars

### A. Authentication & Session Management
- **Protocol:** HTTP-only, secure, `SameSite=Lax` session cookies.
- **Provider:** Supabase Auth, Auth.js, or Clerk.
- **Multi-Tenancy & Authorization:** Every database query must filter by tenant (`org_id` or `user_id`). Test negative cases: a user must never be able to read or mutate another tenant's records.
- **Account Deletion:** Implement a full cascade deletion use case (`DeleteUserAccountUseCase`) to comply with GDPR and app store requirements.

### B. Database Migrations
- Checked into VCS (e.g. `drizzle/migrations/` or `prisma/migrations/`).
- Idempotent and reversible where possible.
- Seed data scripts with realistic entities for local testing.

### C. Idempotent Payment Webhooks (Stripe)
- **Signature verification:** Validate `stripe.webhooks.constructEvent()` with raw body.
- **Idempotency table:** Track processed event IDs (`stripe_event_id`) in the database. Discard duplicate webhook deliveries cleanly:
  ```typescript
  export async function handleStripeWebhook(event: Stripe.Event, db: Database) {
    const existing = await db.query.processedEvents.findFirst({
      where: eq(processedEvents.id, event.id),
    });
    if (existing) return { status: "already_processed" };

    switch (event.type) {
      case "checkout.session.completed":
        await activateSubscription(event.data.object);
        break;
      case "customer.subscription.deleted":
        await cancelSubscription(event.data.object);
        break;
    }

    await db.insert(processedEvents).values({ id: event.id, processedAt: new Date() });
    return { status: "success" };
  }
  ```
- **Single Source of Truth:** Subscription status lives in your database, updated strictly via signed webhooks. Never trust the frontend client for subscription state.

### D. Transactional Email & Background Jobs
- Transactional templates (confirmation, password reset, reminders) handled via Resend or Postmark.
- Scheduled jobs (slot reminders, expired session cleanup) via standard cron handlers (Vercel Cron, Trigger.dev, or BullMQ).

---

## Deliverables Checklist
- [ ] Database migrations applied and verified.
- [ ] Zod validation schemas guarding all API and Server Action boundaries.
- [ ] Authentication flows (sign up, sign in, password reset, sign out) functional.
- [ ] Multi-tenant isolation verified (tenant A cannot access tenant B data).
- [ ] Stripe checkout and webhook listeners verified with test cards.
- [ ] `.env.example` created with all necessary environment variables.
- [ ] Ready for handoff to `/replica-test`.
