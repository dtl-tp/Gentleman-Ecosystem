---
name: replica-brand
description: >
  Rebrands an application clone to establish a distinct, legally sound identity.
  Performs trademark screening, color palette generation, voice definition, and executes sweep.py
  to purge all residual trademarks, domains, and brand colors from the codebase. Step 9 of the Replica suite.
  Trigger: When choosing an app name, rebranding, checking trademarks, or executing sweep.py code sanitation.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# replica-brand

> **PHILOSOPHY: OWNERSHIP AND INTEGRITY.**
> Nothing launches under the original app's identity.
> A clean-room clone becomes your product only when it possesses a unique brand, its own voice, and zero residual traces of the competitor.

Reads `replica/fixes.md`.
Writes `replica/brand.md` and `replica/brand.json`.

Tool in `tools/`:
```bash
python tools/sweep.py . --avoid "OriginalApp,Original LLC" --domains original.com --colors "#006bff"
python tools/sweep.py . --config replica/brand.json
```

---

## 1. Naming & Trademark Screening

1. **Candidate Generation:** Develop 15-20 candidates based on your positioning angle (Descriptive, Compound, Metaphor, Evocative).
2. **Distinctiveness Filter:**
   - **No confusing similarity:** Reject names sounding similar to the incumbent or category leaders. No lazy "-ly" or "-ify" knockoffs.
   - Easy to spell, memorable, no negative connotations in major languages.
3. **Screening Matrix (To be verified by the user):**
   - **US Trademark:** USPTO TESS (Class 9 software, Class 42 SaaS).
   - **EU Trademark:** EUIPO eSearch / TMview.
   - **Global:** WIPO Global Brand Database.
   - **Domain:** WHOIS availability on `.com` or modern TLDs (`.io`, `.app`, `.dev`).
   - **Social & Package Handles:** GitHub, X, npm, App Store, Google Play.

---

## 2. Visual Identity & Brand Voice

- **Palette Generation:** Establish a distinct 8-color semantic palette. If the original uses blue, explore warm ochres, forest greens, or vibrant purples. Never mirror the competitor's exact primary hue.
- **Voice Guide:** 3 core tonal attributes (e.g. *Direct, Technical, Reliable*).
- **Logo Brief:** Minimalist vector geometry and typography specification for designers.

---

## 3. Codebase Brand Sweeper (`sweep.py`)

Run the automated sweeper to audit every file in the repository:
```bash
python tools/sweep.py . --config replica/brand.json
```

### What `sweep.py` Scans:
- File and directory names.
- Source code, comments, string literals, and identifiers (e.g. `CalendlyButton` or `calendly_sync`).
- Hex color codes (matching short-form and full-form hex values).
- Domains and URLs.

> [!CAUTION]
> `sweep.py` exits with code `1` if any reference to the original brand is detected.
> **All matches must be eliminated before proceeding to deployment.**

---

## 4. Output: `replica/brand.json`

```json
{
  "name": "SyncPulse",
  "avoid": [
    "Calendly",
    "Calendly LLC",
    "Calendly Inc"
  ],
  "domains": [
    "calendly.com"
  ],
  "colors": [
    "#006bff",
    "#0ae8f0"
  ]
}
```

---

## Deliverables Checklist
- [ ] Unique name selected and screened against trademark registers.
- [ ] `replica/brand.md` compiled with palette, logo brief, and voice guidelines.
- [ ] `replica/brand.json` written with forbidden names, domains, and hex codes.
- [ ] `tools/sweep.py` executed and exiting cleanly with code `0`.
- [ ] Ready for handoff to `/replica-launch`.
