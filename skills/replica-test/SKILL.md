---
name: replica-test
description: >
  Validates application clone functionality, executing Playwright E2E test suites with Page Object Models,
  accessibility scans with Axe, and systematic bug classification. Step 6 of the Replica suite.
  Trigger: When writing E2E tests, verifying clone flows, running QA audits, or testing for regression bugs.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# replica-test

> **PHILOSOPHY: TESTING WITHOUT SHORTCUTS.**
> Flaky tests and CSS-class-based selectors are an anti-pattern.
> Build resilient test suites using semantic accessibility selectors, Page Object Models, and automated accessibility scans.

Reads user flows in `replica/recon.md`.
Writes `replica/test-plan.md`, `replica/bugs.md`, and test specs under `e2e/`.

---

## 1. Testing Pyramid Strategy

1. **Domain Unit Tests:** Test domain entity invariants and validation rules in isolation (fast, zero I/O).
2. **Integration Tests:** Test database repositories and API handlers against test containers or an isolated test DB.
3. **End-to-End Tests (Playwright):** Test full user journeys through the browser against a local development server with seeded data.

---

## 2. Playwright Standards & Page Object Model (POM)

Following the [Gentleman Playwright Standard](file:///D:/Gentleman-Ecosystem/Gentleman-Skills/curated/playwright/SKILL.md):

- **Semantic Selectors Only:** Use `getByRole()`, `getByLabel()`, `getByText()`. Never select by CSS classes or internal implementation details (`.btn-primary` or `#slot-3`).
- **Encapsulate page interactions in POM classes:**

```typescript
// e2e/pages/booking.page.ts
import { Page, Locator, expect } from "@playwright/test";

export class BookingPage {
  readonly page: Page;
  readonly slotButtons: Locator;
  readonly confirmButton: Locator;
  readonly nameInput: Locator;
  readonly emailInput: Locator;

  constructor(page: Page) {
    this.page = page;
    this.slotButtons = page.getByRole("radio");
    this.confirmButton = page.getByRole("button", { name: /confirm booking/i });
    this.nameInput = page.getByLabel(/your name/i);
    this.emailInput = page.getByLabel(/email address/i);
  }

  async goto(slug: string) {
    await this.page.goto(`/${slug}`);
  }

  async selectFirstAvailableSlot() {
    await this.slotButtons.first().click();
  }

  async fillGuestDetails(name: string, email: string) {
    await this.nameInput.fill(name);
    await this.emailInput.fill(email);
  }

  async submit() {
    await this.confirmButton.click();
  }
}
```

---

## 3. Test Matrix (Per Flow)

For each flow (`F01`, `F02`, ...) define:
- **Happy Path (`-H`):** The standard user journey completing with success.
- **Edge Cases (`-E`):**
  - Timezone conversion across daylight saving boundaries.
  - Slot collision (slot claimed in another tab before submission).
  - Double submit prevention (rapid double click).
  - Network disconnection / slow response.
- **Negative Cases (`-N`):**
  - Invalid email or missing required fields.
  - Payment failure (Stripe declined card `4000 0000 0000 0002`).
  - Unauthorized access to another user's private dashboard.

---

## 4. Accessibility Testing (Axe-Core)

Embed automated accessibility assertions into critical test paths:

```typescript
import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";
import { BookingPage } from "./pages/booking.page";

test("booking page should have no detectable a11y violations", async ({ page }) => {
  const bookingPage = new BookingPage(page);
  await bookingPage.goto("team-standup");

  const accessibilityScanResults = await new AxeBuilder({ page }).analyze();
  expect(accessibilityScanResults.violations).toEqual([]);
});
```

---

## 5. Bug Severity Classification

Log any defect in `replica/bugs.md` using strict severity tiers:
- **S1 (Blocker):** Data loss, payment calculation error, security vulnerability, broken core loop. Deployment blocked.
- **S2 (High):** Major edge-case failure, broken secondary flow, no workaround. Deployment blocked.
- **S3 (Medium):** Minor functional quirk, cosmetic alignment issue, fallback available.
- **S4 (Low):** Minor typo or polish suggestion.

---

## Deliverables Checklist
- [ ] `replica/test-plan.md` created covering all flows and edge cases.
- [ ] Playwright E2E specs automated under `e2e/`.
- [ ] Accessibility scans pass with zero violations.
- [ ] Zero open S1 or S2 bugs in `replica/bugs.md`.
- [ ] Ready for handoff to `/replica-diff`.
