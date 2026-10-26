---
name: replica-diff
description: >
  Scores functional feature parity and structural layout alignment between the clone and the target app
  using Python stdlib tools (parity.py and imgdiff.py). Step 7 of the Replica suite.
  Trigger: When checking parity percentage, comparing layout differences, or evaluating shippability.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# replica-diff

> **PHILOSOPHY: FUNCTIONAL VALUE OVER PIXEL OBSESSION.**
> Parity means the user can achieve their goals smoothly.
> The layout diff verifies structural hierarchy and orientation, while deliberately ignoring color to allow complete rebranding.

Reads `replica/features.csv`, `replica/screens/`, and `replica/clone-screens/`.
Writes `replica/parity.md` and visual diff artifacts.

Tools in `tools/`:
```bash
python tools/parity.py replica/features.csv
python tools/imgdiff.py replica/screens/S01.png replica/clone-screens/S01.png --out replica/diffs/S01.png
```

---

## 1. Feature Parity Scoring (`parity.py`)

Run the parity scorer against the feature matrix:
```bash
python tools/parity.py replica/features.csv
```

### Weighting Algorithm:
- **`must` features:** Weight 3. Must be 100% completed (`yes`). Any incomplete must-have blocks deployment.
- **`should` features:** Weight 2.
- **`could` features:** Weight 1.
- `partial` completions count as 50% score.
- Intentionally excluded rows marked `skip` do not penalize your score.
- Custom innovative features you added are tracked separately.

---

## 2. Layout Structure Diffing (`imgdiff.py`)

Compares UI hierarchy without penalizing new brand colors or fonts:

```bash
python tools/imgdiff.py replica/screens/S02.png replica/clone-screens/S02.png --out diff-S02.png
```

### How `imgdiff.py` Works:
1. Converts both screenshots into grayscale edge maps (Sobel/Laplacian gradient).
2. Evaluates structural boundaries: button placements, column grids, card boundaries, navigation hierarchy.
3. Completely ignores color hue differences, allowing your custom design tokens and dark/light themes to pass.
4. Generates a highlighted diff image pinpointing displaced or missing UI blocks.

---

## 3. Shipping Criteria

To proceed to `/replica-entrepreneur` and release:
- **Must-haves:** 100% completed.
- **Overall weighted feature parity:** >= 85%.
- **Core loop layout similarity:** >= 80% structural alignment.
- Zero open S1/S2 issues in `replica/bugs.md`.

---

## Deliverables Checklist
- [ ] `replica/features.csv` updated with all implemented screens and features.
- [ ] `replica/parity.md` generated with formal score breakdown.
- [ ] Visual diffs generated in `replica/diffs/` for core screens.
- [ ] Shippability status confirmed (100% must-haves satisfied).
- [ ] Ready for handoff to `/replica-entrepreneur`.
