---
name: replica-build
description: >
  Rebuilds application screens clean-room style from recon maps and design tokens,
  enforcing Container-Presentational separation, React 19 compiler patterns or Angular Signals,
  and comprehensive state handling. Step 4 of the Replica suite.
  Trigger: When building UI screens, implementing clean-room features, or executing the vertical slice of an app.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# replica-build

> **PHILOSOPHY: CLEAN SEPARATION OF CONCERNS.**
> A component that fetches data, manages complex domain state, and renders markup all in one place is unmaintainable.
> Separate Containers (orchestration & state) from Presentational components (pure UI).

Reads `replica/recon.md`, `replica/architecture.md`, `replica/design/tokens.json`.
Updates `replica/features.csv` (the `clone` column) and logs progress to `replica/build-log.md`.

---

## 1. Clean-Room Implementation Rules

1. **Clean-room authorship:** Write every line of code from scratch based on the recon map and specifications. Never copy/paste HTML, CSS, JavaScript, or SVGs from the target app.
2. **Distinct copy:** Write all labels, placeholders, empty states, and micro-copy with your own voice. Matching functional behavior is parity; copying wording is infringement.
3. **Strict tokens:** Use only semantic tokens defined during `/replica-design`. No ad-hoc inline styles.

---

## 2. Component Architecture: Container / Presentational Pattern

Every screen must separate logic from rendering:

```typescript
// 1. PRESENTATIONAL COMPONENT: Pure, predictable, receives props, renders UI
// File: src/presentation/features/booking/components/slot-picker.tsx
import { Slot } from "@/domain/booking/booking.types";

interface SlotPickerProps {
  slots: readonly Slot[];
  selectedSlotId: string | null;
  onSelectSlot: (slotId: string) => void;
  isLoading?: boolean;
}

export function SlotPicker({ slots, selectedSlotId, onSelectSlot, isLoading }: SlotPickerProps) {
  if (isLoading) return <SlotPickerSkeleton />;
  if (slots.length === 0) return <EmptyState message="No available time slots." />;

  return (
    <div className="grid grid-cols-3 gap-2" role="radiogroup" aria-label="Available slots">
      {slots.map((slot) => (
        <button
          key={slot.id}
          type="button"
          role="radio"
          aria-checked={selectedSlotId === slot.id}
          onClick={() => onSelectSlot(slot.id)}
          className="rounded-md border p-3 text-sm font-medium focus-visible:outline-2"
        >
          {slot.formattedTime}
        </button>
      ))}
    </div>
  );
}

// 2. CONTAINER COMPONENT: Hooks, state, API calls, event handlers
// File: src/presentation/features/booking/booking-container.tsx
export function BookingContainer({ eventTypeId }: { eventTypeId: string }) {
  const { slots, selectedSlotId, selectSlot, isLoading, error } = useBookingSlots(eventTypeId);

  if (error) return <ErrorMessage message="Failed to load slots." />;

  return (
    <SlotPicker
      slots={slots}
      selectedSlotId={selectedSlotId}
      onSelectSlot={selectSlot}
      isLoading={isLoading}
    />
  );
}
```

---

## 3. Framework Standards

### For React 19:
- **React Compiler optimization:** **DO NOT** use `useMemo` or `useCallback` manually. Let the compiler handle memoization automatically.
- **Named imports only:** Always `import { useState, useEffect } from "react";`. Never `import React from "react";`.
- **Server Actions & Mutations:** Validate input with Zod before executing business use cases.

### For Angular 19:
- **Standalone components & Zoneless:** Always `standalone: true`.
- **Signals-first:** Use `signal()`, `computed()`, and `effect()`.
- **Dependency Injection:** Use modern `inject(Service)` instead of constructor injection.

---

## 4. Build Sequence

### Step 1: App Shell & Routing
Generate the layout (nav, header, sidebar, footer), theme providers, and route stubs for all screens in the inventory.

### Step 2: The Vertical Slice
Build the core happy-path loop end-to-end first. For a booking app:
1. Public booking page renders slots.
2. Form submits details.
3. Confirmation screen confirms booking.
4. Dashboard lists the new booking.

### Step 3: Screen-by-Screen Execution
Follow the screen priority from `architecture.md`. For each screen:
1. Inspect its row in `replica/recon.md`.
2. Build container and presentational components using design tokens.
3. **Implement all states:** `empty`, `loading` (skeletons), `filled`, `error`, `responsive` (390px mobile to 1440px desktop).
4. Save a screenshot to `replica/clone-screens/Sxx.png` for parity checking.
5. Update `replica/features.csv` with `yes` or `partial`.
6. Commit using conventional commits: `feat(ui): implement S02 slot picker`.

---

## Definition of Done (Per Screen)
- [ ] Every state from recon (empty, loading skeleton, error, filled) is implemented.
- [ ] Responsive across mobile (390px) and desktop (1440px).
- [ ] Full keyboard navigation and visible focus rings.
- [ ] No console errors or accessibility violations.
- [ ] `features.csv` updated with status.
- [ ] Screenshot captured in `replica/clone-screens/` for `/replica-diff`.
