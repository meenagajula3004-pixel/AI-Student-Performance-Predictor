from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER

import matplotlib.pyplot as plt
import time



# ================= SECTION HEADING =================

heading_style = ParagraphStyle(
    "heading_style",
    fontSize=14,
    alignment=TA_CENTER,
    textColor=colors.white,
    leading=18
)


def section_title(text):

    table = Table(
        [
            [
                Paragraph(
                    text,
                    heading_style
                )
            ]
        ],
        colWidths=[410]
    )

    table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0,0),
                    (-1,-1),
                    colors.HexColor("#7C3AED")
                ),

                (
                    "ALIGN",
                    (0,0),
                    (-1,-1),
                    "CENTER"
                ),

                (
                    "VALIGN",
                    (0,0),
                    (-1,-1),
                    "MIDDLE"
                ),

                (
                    "LEFTPADDING",
                    (0,0),
                    (-1,-1),
                    12
                ),

                (
                    "RIGHTPADDING",
                    (0,0),
                    (-1,-1),
                    12
                ),

                (
                    "TOPPADDING",
                    (0,0),
                    (-1,-1),
                    8
                ),

                (
                    "BOTTOMPADDING",
                    (0,0),
                    (-1,-1),
                    8
                ),
            ]
        )
    )

    return table

# ================= CHART =================


def create_chart(previous, score):

    labels = [
        "Previous Score",
        "AI Prediction"
    ]

    values = [
        previous,
        score
    ]


    plt.figure(figsize=(6,3))

    plt.bar(
        labels,
        values
    )

    plt.ylim(
        0,
        100
    )

    plt.title(
        "Performance Analysis"
    )


    path = "performance_chart.png"


    plt.savefig(
        path,
        bbox_inches="tight"
    )


    plt.close()


    return path





# ================= CREATE PDF =================


def create_report(
    name,
    education,
    board,
    previous,
    cgpa,
    score,
    performance,
    suggestions
):

    file_name = (
        f"{name}_AI_Performance_Report_{int(time.time())}.pdf"
    )


    doc = SimpleDocTemplate(
        file_name,
        pagesize=A4,
        rightMargin=70,
        leftMargin=70,
        topMargin=50,
        bottomMargin=50
    )


    styles = getSampleStyleSheet()

    normal = styles["Normal"]



    content = []



    # ================= HEADER =================


    title_style = ParagraphStyle(
    "title_style",
    fontName="Helvetica-Bold",
    fontSize=16,
    alignment=TA_CENTER,
    textColor=colors.white,
    leading=22,
    spaceBefore=0,
    spaceAfter=0
    )


    header = Table(
        [
            [
                Paragraph(
                    "AI Student Performance Dashboard",
                    title_style
                )
            ]
        ],
        colWidths=[410]
    )


    header.setStyle(
        TableStyle(
            [

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,-1),
                    colors.HexColor("#2563EB")
                ),

                (
                    "ALIGN",
                    (0,0),
                    (-1,-1),
                    "CENTER"
                ),

                (
                    "VALIGN",
                    (0,0),
                    (-1,-1),
                    "MIDDLE"
                ),

                (
                    "LEFTPADDING",
                    (0,0),
                    (-1,-1),
                    20
                ),

                (
                    "RIGHTPADDING",
                    (0,0),
                    (-1,-1),
                    20
                ),

                ("TOPPADDING",(0,0),(-1,-1),12),
                ("BOTTOMPADDING",(0,0),(-1,-1),12),

            ]
        )
    )


    content.append(header)

    content.append(
        Spacer(1,20)
    )



    # ================= RESULT =================


    content.append(
        section_title(
            "AI Prediction Result"
        )
    )


    content.append(
        Spacer(1,10)
    )



    result_table = Table(
        [
            [
                "Predicted Score",
                f"{score:.2f}%"
            ],

            [
                "Performance",
                performance
            ]

        ],
        colWidths=[160,250]
    )



    result_table.setStyle(
        TableStyle(
            [

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,-1),
                    colors.HexColor("#DCFCE7")
                ),

                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    0.5,
                    colors.grey
                ),

                (
                    "PADDING",
                    (0,0),
                    (-1,-1),
                    12
                )

            ]
        )
    )


    content.append(result_table)


    content.append(
        Spacer(1,20)
    )



    # ================= GRAPH =================


    content.append(
        section_title(
            "Performance Analysis"
        )
    )


    content.append(
        Spacer(1,10)
    )


    chart = create_chart(
        previous,
        score
    )


    content.append(
        Image(
            chart,
            width=350,
            height=200
        )
    )


    content.append(
        Spacer(1,20)
    )



    # ================= SUGGESTIONS =================


    content.append(
        section_title(
            "Personalized AI Suggestions"
        )
    )


    content.append(
        Spacer(1,10)
    )


    for item in suggestions:

        content.append(
            Paragraph(
                "• " + item,
                normal
            )
        )

        content.append(
            Spacer(1,5)
        )



    content.append(
        Spacer(1,20)
    )



    # ================= ML EXPLANATION =================


    content.append(
        section_title(
            "Machine Learning Explanation"
        )
    )


    content.append(
        Spacer(1,10)
    )



    content.append(
        Paragraph(
            """
            This system uses Random Forest Regression algorithm.
            It analyzes academic score, study hours,
            practice hours, sleep pattern and mobile usage
            to predict student performance.
            """,
            normal
        )
    )


    content.append(
        Spacer(1,20)
    )



    content.append(
        Paragraph(
            "Generated by AI Student Predictor System",
            normal
        )
    )



    doc.build(
        content
    )


    return file_name