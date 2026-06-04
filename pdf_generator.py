from io import BytesIO

from reportlab.platypus import (
SimpleDocTemplate,
Paragraph,
Spacer,
PageBreak
)

from reportlab.lib.styles import (
getSampleStyleSheet,
ParagraphStyle
)

from reportlab.lib import colors

def create_pdf(
month,
top_geos,
high_potential_geos,
top_strategies,
key_updates
):

```
buffer = BytesIO()

doc = SimpleDocTemplate(
    buffer,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "CustomTitle",
    parent=styles["Title"],
    textColor=colors.HexColor("#4F6DF5"),
    fontSize=36,
    leading=38
)

section_style = ParagraphStyle(
    "SectionStyle",
    parent=styles["Heading1"],
    textColor=colors.HexColor("#4F6DF5")
)

elements = []

# ====================================
# PAGE 1
# ====================================

elements.append(
    Paragraph(
        "Search<br/>Insights",
        title_style
    )
)

elements.append(
    Spacer(1, 20)
)

elements.append(
    Paragraph(
        month,
        styles["Heading2"]
    )
)

elements.append(
    Spacer(1, 500)
)

elements.append(PageBreak())

# ====================================
# PAGE 2
# ====================================

elements.append(
    Paragraph(
        "Content",
        section_style
    )
)

elements.append(
    Spacer(1, 20)
)

elements.append(
    Paragraph(
        "Top Performing Themes",
        styles["Heading2"]
    )
)

for i in range(1, 6):

    elements.append(
        Paragraph(
            f"{i}. Coming Soon",
            styles["BodyText"]
        )
    )

elements.append(
    Spacer(1, 40)
)

elements.append(
    Paragraph(
        "Theme Distribution Chart (Coming Soon)",
        styles["Heading2"]
    )
)

elements.append(PageBreak())

# ====================================
# PAGE 3
# ====================================

elements.append(
    Paragraph(
        "Media Buying",
        section_style
    )
)

elements.append(
    Spacer(1, 20)
)

elements.append(
    Paragraph(
        "Top Performing Geos",
        styles["Heading2"]
    )
)

for geo in top_geos:

    elements.append(
        Paragraph(
            f"• {geo}",
            styles["BodyText"]
        )
    )

elements.append(
    Spacer(1, 20)
)

elements.append(
    Paragraph(
        "High Potential Geos",
        styles["Heading2"]
    )
)

for geo in high_potential_geos:

    elements.append(
        Paragraph(
            f"• {geo}",
            styles["BodyText"]
        )
    )

elements.append(
    Spacer(1, 20)
)

elements.append(
    Paragraph(
        "Top Performing Media Buying Strategies",
        styles["Heading2"]
    )
)

for strategy in top_strategies:

    elements.append(
        Paragraph(
            f"• {strategy}",
            styles["BodyText"]
        )
    )

elements.append(PageBreak())

# ====================================
# PAGE 4
# ====================================

elements.append(
    Paragraph(
        "Key Updates",
        section_style
    )
)

elements.append(
    Spacer(1, 20)
)

for line in key_updates.split("\n"):

    if line.strip():

        elements.append(
            Paragraph(
                line,
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

doc.build(elements)

buffer.seek(0)

return buffer
```
