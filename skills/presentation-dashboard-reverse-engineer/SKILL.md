---
name: presentation-dashboard-reverse-engineer
description: "Reverse engineer any executive presentation slide, dashboard screenshot, or reporting visual into editable Microsoft PowerPoint (PPTX) and Google Slides. Provides exact step-by-step layout recreation, native VBA macros, Google Apps Script (GAS) automations, and programmatic python-pptx scripts to reconstruct charts, KPI blocks, and card layouts from images."
argument-hint: "Recreate this dashboard slide in PowerPoint | Turn this image into a Google Slides presentation"
allowed-tools: Read, Write, Bash
license: MIT
metadata:
  tags:
    - powerpoint
    - pptx
    - google-slides
    - apps-script
    - vba-macros
    - dashboard
    - reverse-engineering
    - python-pptx
---

# Presentation & Dashboard Slide Reverse Engineering

Use this skill whenever the user provides an image or screenshot of a **presentation slide, dashboard, KPI card layout, or executive briefing** and wants to:
1. **Deconstruct the visual layout** (grid, spatial alignment, hierarchy, fonts, color tokens).
2. **Recreate it natively in Microsoft PowerPoint (PPTX)** via step-by-step UI instructions or automated **VBA macros**.
3. **Recreate it in Google Slides** via step-by-step UI or automated **Google Apps Script (GAS)**.
4. **Generate automated python-pptx code** to build an identical, editable presentation file with native shapes, tables, and charts.

---

## The 4-Step Reverse Engineering Protocol

### Step 1: Spatial & Visual Decomposition
Examine the screenshot and catalog all elements:
- **Slide Dimensions & Aspect Ratio:** Standard 16:9 widescreen (13.333" x 7.5" / 1920x1080) vs. 4:3 legacy.
- **Visual Grid & Containers:**
  - Header / Title block (Title, subtitle, date/tag badges).
  - KPI Hero Metrics (large bold numbers, delta percentages `+12.4%`, trend arrows).
  - Chart containers (Bar, Line, Donut, Stacked Area, Waterfall).
  - Comparison cards / side-by-side columns.
  - Footnotes & source citations.
- **Palette & Typography Extraction:**
  - Background color (e.g., `#0F172A` Slate Dark, `#FFFFFF` Clean White, `#F8FAFC` Off-White).
  - Primary, Secondary, and Accent colors (e.g., Brand Blue `#2563EB`, Success Green `#10B981`, Danger Red `#EF4444`).
  - Font pairings (e.g., Sans-serif Inter/Segoe UI/Calibri for corporate modern; Roboto/Arial for Google Slides).

---

### Step 2: Step-by-Step UI Rebuild Guide (Manual Creation)
Provide explicit, friction-free instructions for both PowerPoint and Google Slides:
1. **Slide Setup:** Slide size, background fill color, guides layout (View > Guides).
2. **Container Construction:** Drawing cards using rounded rectangles (`Radio de esquina: 8-12px`, sin contorno / soft border `#E2E8F0`, subtle shadow).
3. **Typography & Hierarchy:** Exact font sizes (Title: 24-28pt Bold, KPI Value: 36-44pt Extra Bold, KPI Label: 11-12pt Medium Muted `#64748B`).
4. **Chart Insertion:** Native chart type, series mapping, legend position, and data label formatting.

---

### Step 3: Automation via Scripts (Choose Based on User Platform)

#### Option A: Google Slides (Google Apps Script - GAS)
Provide ready-to-run Google Apps Script code to create the dashboard slide instantly inside Google Drive:
```javascript
function createDashboardSlide() {
  const presentation = SlidesApp.getActivePresentation();
  const slide = presentation.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  
  // Set background
  slide.getBackground().setSolidFill('#0F172A');
  
  // Add Header
  const titleBox = slide.insertTextBox('Executive Dashboard - Performance Overview', 36, 24, 648, 40);
  titleBox.getText().getTextStyle().setForegroundColor('#FFFFFF').setFontSize(22).setBold(true);
  
  // Build KPI Cards dynamically
  const kpis = [
    { title: 'Total Revenue', value: '$2.45M', delta: '+14.2% YoY', x: 36, y: 80, w: 195, h: 100 },
    { title: 'Active Users', value: '184.2K', delta: '+8.6% MoM', x: 247, y: 80, w: 195, h: 100 },
    { title: 'Churn Rate', value: '1.8%', delta: '-0.3%', x: 458, y: 80, w: 195, h: 100 }
  ];
  
  kpis.forEach(k => {
    const card = slide.insertShape(SlidesApp.ShapeType.ROUNDED_RECTANGLE, k.x, k.y, k.w, k.h);
    card.getFill().setSolidFill('#1E293B');
    card.getBorder().getLineFill().setSolidFill('#334155');
    
    const text = card.getText();
    text.setText(`${k.title}\n${k.value}\n${k.delta}`);
    text.getParagraph(0).getTextStyle().setForegroundColor('#94A3B8').setFontSize(11);
    text.getParagraph(1).getTextStyle().setForegroundColor('#FFFFFF').setFontSize(22).setBold(true);
    text.getParagraph(2).getTextStyle().setForegroundColor('#10B981').setFontSize(10).setBold(true);
  });
}
```

#### Option B: Microsoft PowerPoint VBA Macro
Provide the VBA macro that builds the dashboard slide directly inside PowerPoint:
```vba
Sub BuildDashboardSlide()
    Dim sld As Slide
    Dim shp As Shape
    Dim kpiBox As Shape
    
    Set sld = ActivePresentation.Slides.Add(ActivePresentation.Slides.Count + 1, ppLayoutBlank)
    sld.Background.Fill.Solid
    sld.Background.Fill.ForeColor.RGB = RGB(15, 23, 42) ' Slate 900
    
    ' Title
    Set shp = sld.Shapes.AddTextbox(msoTextOrientationHorizontal, 36, 24, 600, 40)
    With shp.TextFrame.TextRange
        .Text = "Executive Dashboard - Performance Overview"
        .Font.Size = 22
        .Font.Bold = msoTrue
        .Font.Color.RGB = RGB(255, 255, 255)
    End With
    
    ' KPI Card Sample
    Set kpiBox = sld.Shapes.AddShape(msoShapeRoundedRectangle, 36, 80, 200, 100)
    With kpiBox
        .Fill.Solid
        .Fill.ForeColor.RGB = RGB(30, 41, 59)
        .Line.ForeColor.RGB = RGB(51, 65, 85)
        .TextFrame.TextRange.Text = "Total Revenue" & vbCrLf & "$2.45M" & vbCrLf & "+14.2% YoY"
        .TextFrame.TextRange.Lines(1).Font.Size = 11
        .TextFrame.TextRange.Lines(1).Font.Color.RGB = RGB(148, 163, 184)
        .TextFrame.TextRange.Lines(2).Font.Size = 24
        .TextFrame.TextRange.Lines(2).Font.Bold = msoTrue
        .TextFrame.TextRange.Lines(2).Font.Color.RGB = RGB(255, 255, 255)
        .TextFrame.TextRange.Lines(3).Font.Size = 10
        .TextFrame.TextRange.Lines(3).Font.Color.RGB = RGB(16, 185, 129)
    End With
End Sub
```

---

### Step 4: Python Programmatic Generation (`python-pptx`)
Generate a ready-to-execute Python script using `python-pptx` to produce the final `.pptx` file locally with exact positioning in inches (`Inches(x)` / `Pt(y)`), native charts (`CategoryChartData`, `XL_CHART_TYPE`), and editable shapes.
