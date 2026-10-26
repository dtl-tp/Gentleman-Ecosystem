---
name: replica-design
description: >
  Reconstructs a clean-room design system from reference screenshots into semantic tokens,
  an 8px spatial grid, and WCAG-compliant color contrast using contrast.py. Step 3 of the Replica suite.
  Trigger: When extracting design tokens, building a design system, or checking color contrast for an app clone.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# replica-design

> **PHILOSOPHY: TOKENS OVER ARBITRARY VALUES.**
> Hard-coded pixel values and random hex colors in components are an architectural crime.
> Every color, spacing, and font size must map to a semantic design token.

Reads `replica/screens/` and `replica/recon.md`.
Writes `replica/design/tokens.json` and updates `replica/design/primitives.md`.

Tool in `tools/`:
```bash
python tools/contrast.py replica/design/tokens.json
```

---

## 1. Clean-Room Styling Principles

1. **Tokens, never pixels:** No inline hex codes (`#1a73e8`) or magic numbers (`margin: 17px`) in UI code.
2. **Open Assets Only:** Use open-source font families (Inter, Geist, Roboto, Plus Jakarta Sans) and standard icon sets (Lucide, Heroicons). Never scrape or embed the original's custom SVGs, brand illustrations, or proprietary fonts.
3. **Semantic Color Roles:** Colors are defined by purpose, not hue name:
   - `primary`, `primary-foreground`
   - `muted`, `muted-foreground`
   - `destructive`, `destructive-foreground`
   - `surface`, `surface-raised`, `border`

---

## 2. Spatial System (The 8px Grid)

Strict mathematical scale based on multiples of 4px and 8px:

| Token | Pixels | Rem (16px base) | Use Case |
| :--- | :--- | :--- | :--- |
| `space-1` | 4px | 0.25rem | Icon gaps, tight padding |
| `space-2` | 8px | 0.5rem | Button padding Y, chip spacing |
| `space-3` | 12px | 0.75rem | Compact form controls |
| `space-4` | 16px | 1.0rem | Standard card padding, input padding X |
| `space-6` | 24px | 1.5rem | Section gaps, modal padding |
| `space-8` | 32px | 2.0rem | Major layout gutters |
| `space-12`| 48px | 3.0rem | Hero vertical padding |

---

## 3. WCAG 2.1 AA Accessibility Validation

Contrast is verified mathematically with `tools/contrast.py`:
- **Normal text:** Minimum contrast ratio of **4.5:1** against the background.
- **Large text (>= 18pt or bold >= 14pt):** Minimum contrast ratio of **3.0:1**.
- **Interactive UI components & borders:** Minimum ratio of **3.0:1**.

```bash
# Execute contrast linter on token configuration
python tools/contrast.py replica/design/tokens.json
```

---

## 4. Output: `tokens.json` Structure

```json
{
  "color": {
    "background": "#ffffff",
    "foreground": "#0f172a",
    "primary": "#2563eb",
    "primary-foreground": "#ffffff",
    "muted": "#f1f5f9",
    "muted-foreground": "#64748b",
    "border": "#e2e8f0",
    "destructive": "#ef4444"
  },
  "typography": {
    "font-family": "Inter, system-ui, sans-serif",
    "scale": {
      "xs": "0.75rem",
      "sm": "0.875rem",
      "base": "1.0rem",
      "lg": "1.125rem",
      "xl": "1.25rem",
      "2xl": "1.5rem",
      "3xl": "1.875rem"
    }
  },
  "radii": {
    "sm": "4px",
    "md": "8px",
    "lg": "12px",
    "full": "9999px"
  }
}
```

---

## Deliverables Checklist
- [ ] `replica/design/tokens.json` created with full color, spacing, and typography scales.
- [ ] Contrast verified clean (exit code 0 from `tools/contrast.py`).
- [ ] Tailwind v4 `@theme` or CSS variables config generated.
- [ ] Component inventory mapped to primitive tokens.
- [ ] Ready for handoff to `/replica-build`.
