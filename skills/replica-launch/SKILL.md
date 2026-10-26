---
name: replica-launch
description: >
  Prepares launch marketing assets, positioning-driven landing page copy, pricing comparison matrices,
  and store listings linted against App Store and Google Play character limits using listing.py. Step 10 of the Replica suite.
  Trigger: When writing landing page copy, structuring SaaS pricing, preparing store listings, or running listing.py.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# replica-launch

> **PHILOSOPHY: HONESTY IN POSITIONING.**
> Never invent testimonials or fake user numbers. An honest launch focused on solving real pain points
> converts infinitely better than artificial hype.

Reads `replica/fixes.md`, `replica/brand.md`, `replica/brand.json`.
Writes `replica/launch/` directory assets (`landing.md`, `pricing.md`, `listing.json`, `launch-plan.md`).

Tool in `tools/`:
```bash
python tools/listing.py replica/launch/listing.json
```

---

## 1. Landing Page Architecture (`landing.md`)

Structure the landing page around your value proposition and competitor fixes:

1. **Hero Section:**
   - Headline: The core angle (what you do + for whom).
   - Subhead: Direct contrast against the incumbent's primary weakness.
   - Primary Call to Action (CTA) + interactive screenshot of the real clone.
2. **The Problem Statement:**
   - Articulate the top 2 customer frustrations identified during `/replica-entrepreneur` (in your own words; never quote review text directly as testimonials).
3. **The Solution (How It Works):**
   - 3 clear, frictionless steps derived from the core user loop.
4. **Fix-Driven Feature Breakdown:**
   - Lead with your product's unique differentiators first. Parity features follow below.
5. **Transparent Pricing Table:**
   - Clear tiers, flat billing, no hidden per-seat traps.
6. **Objection-Busting FAQ:**
   - Data import/export capabilities, privacy commitments, API access.
7. **Final CTA.**

---

## 2. Competitive Pricing Matrix (`pricing.md`)

- Compare your pricing directly against the incumbent's public pricing tiers.
- Cite the exact date and public URL of competitor pricing pages.
- Highlight billing transparency: flat pricing, simple cancellation, no per-seat friction.

---

## 3. App Store & Google Play Linter (`listing.py`)

Validate metadata before submission using `tools/listing.py`:

```bash
python tools/listing.py replica/launch/listing.json
```

### What `listing.py` Enforces:
- **Title Limits:** Apple App Store (30 chars), Google Play (30 chars).
- **Subtitle / Short Description:** Apple (30 chars), Google (80 chars).
- **Keyword Field:** Apple (100 chars, comma-separated, detects duplicate or wasted space).
- **Copycat Rule:** Scans all metadata for references to the original app's name, trademarks, or unsubstantiated claims ("#1 app in the world"), preventing store rejections.

---

## Deliverables Checklist
- [ ] `replica/launch/landing.md` completed with honest, angle-driven copy.
- [ ] `replica/launch/pricing.md` drafted with public comparison matrix.
- [ ] `replica/launch/listing.json` configured.
- [ ] `tools/listing.py` executed with zero warnings or violations.
- [ ] Ready for handoff to `/replica-deploy`.
