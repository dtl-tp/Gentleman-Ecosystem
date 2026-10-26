---
name: excel-chart-reverse-engineer
description: "Reverse engineer any Excel chart, graph, dashboard screenshot, or report image. Deconstructs the visual into its underlying tabular data structure, exact chart type, axis configuration, data series, and step-by-step instructions to recreate it in Microsoft Excel or programmatically via openpyxl/Python."
argument-hint: "Reverse engineer this chart screenshot | How to build this Excel graph from image"
allowed-tools: Read, Write, Bash
license: MIT
metadata:
  tags:
    - excel
    - chart
    - reverse-engineering
    - dashboard
    - openpyxl
    - dataviz
---

# Excel Chart & Dashboard Reverse Engineering

Use this skill whenever the user provides an image or screenshot of a chart, dashboard, or data visualization from Excel, Power BI, or a report, and wants to:
1. Know **how the underlying table / data model must be structured**.
2. Identify the **exact Excel chart type** and advanced sub-configurations (combo chart, secondary axis, clustered columns, stacked areas, etc.).
3. Obtain **step-by-step Excel UI instructions** (ranges, series, axis formatting, data labels) to rebuild it.
4. Optionally generate the **Python `openpyxl` / `pandas` code** to build the identical spreadsheet and native chart programmatically.

---

## 4-Step Reverse Engineering Protocol

When an image is provided, follow this systematic breakdown:

### Step 1: Visual Decomposition & Chart Classification
Inspect the screenshot and identify:
- **Primary Chart Type:** (e.g., Clustered Column, Stacked Bar, Line with Markers, Combo / Clustered Column + Line on Secondary Axis, Treemap, Waterfall, Scatter/Bubble, Gauge / Donut).
- **Number of Data Series:** Single series vs. multiple comparative series.
- **Axes Anatomy:**
  - **Horizontal / Category Axis (X):** Discrete categories, dates (daily, monthly, quarterly), or numerical intervals.
  - **Vertical / Value Axis (Y1):** Currency, percentage, raw counts, logarithmic scale, min/max bounds.
  - **Secondary Value Axis (Y2 - if present):** Identifying which series maps to the right axis (usually percentages, cumulative %, or different units like Temperature vs. Rainfall).
- **Visual Encodings & Markers:** Data labels, trendlines, target/budget reference lines, error bars, sparklines.
- **Color Palette & Legend:** Legend placement (top, bottom, right, none/inline labels).

---

### Step 2: Inferred Data Architecture (The Table Blueprint)
Design the exact table layout required in Excel.

Provide the schema in Markdown table format, indicating:
- **Columns / Headers:** Explicit names.
- **Data Types:** Date, Text, Currency, Percentage, Formula.
- **Row Grain:** What each row represents (e.g., 1 row per month, 1 row per product category).
- **Formulas / Calculated Columns:** Explicit Excel formulas (e.g., `=SUM(...)`, `=B2/C2`, `=AVERAGEIF(...)`, MoM variance `=(C2-B2)/B2`).

*Example Blueprint:*
```markdown
| Col A: Fecha / Periodo (Texto/Fecha) | Col B: Ventas Reales (€) | Col C: Objetivo Presupuesto (€) | Col D: % Cumplimiento (Fórmula: =B2/C2) |
|---|---|---|---|
| Ene-2026 | 45.200 | 40.000 | 113,0% |
| Feb-2026 | 38.900 | 42.000 | 92,6% |
```

---

### Step 3: Excel Native Rebuild Guide (UI Step-by-Step)
Give the exact, unambiguous steps in Excel:

1. **Table Selection:** Select range `A1:D13`.
2. **Chart Insertion:** `Insertar > Gráficos > [Tipo exacto de gráfico]`.
   - *If Combo Chart:* Select `Gráfico combinado > Columna agrupada - Línea en eje secundario`.
3. **Series Configuration:**
   - Click `Seleccionar datos (Select Data)`.
   - Series 1: Name = `B1`, Values = `B2:B13`.
   - Series 2: Name = `C1`, Values = `C2:C13`.
   - Series 3: Name = `D1`, Values = `D2:D13` -> Check `Eje secundario (Secondary Axis)`.
4. **Formatting & Polish:**
   - Axis Bounds: Format Axis > Minimum / Maximum.
   - Number Format on Axis / Data Labels: e.g. `#,##0 €` or `0.0%`.
   - Series Overlap / Gap Width: Adjust column width (`Superposición de series` = 0%, `Ancho del intervalo` = 120-150% for modern look).
   - Clean aesthetics: Remove harsh black gridlines, use soft gray `#E2E8F0`, delete redundant legends if direct labels exist.

---

### Step 4: Programmatic openpyxl Script (Optional or if requested)
If the user wants to generate the spreadsheet programmatically, produce the ready-to-run Python script using `openpyxl` with:
- Native chart object (`BarChart`, `LineChart`, etc.).
- Proper `Reference` ranges for data and categories.
- Styling and placement anchored cleanly to a dashboard tab.
