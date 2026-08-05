from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

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

    file_name = "student_report.pdf"

    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    content = []

    # ================= TITLE =================
    content.append(Paragraph(
        "<b><font size=18 color='blue'>AI Student Performance Report</font></b>",
        styles["Title"]
    ))

    content.append(Spacer(1, 20))

    # ================= STUDENT DETAILS =================
    content.append(Paragraph("<b>👤 Student Details</b>", styles["Heading2"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph(f"Name: {name}", styles["Normal"]))
    content.append(Paragraph(f"Education: {education}", styles["Normal"]))
    content.append(Paragraph(f"Board / University: {board}", styles["Normal"]))

    if cgpa:
        content.append(Paragraph(f"CGPA: {cgpa}", styles["Normal"]))

    content.append(Paragraph(f"Previous Score: {previous:.2f}%", styles["Normal"]))

    content.append(Spacer(1, 15))

    # ================= RESULT =================
    content.append(Paragraph("<b>📊 Prediction Result</b>", styles["Heading2"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph(f"Predicted Score: {score:.2f}%", styles["Normal"]))
    content.append(Paragraph(f"Performance: {performance}", styles["Normal"]))

    content.append(Spacer(1, 15))

    # ================= SUGGESTIONS =================
    content.append(Paragraph("<b>🤖 AI Suggestions</b>", styles["Heading2"]))
    content.append(Spacer(1, 10))

    for s in suggestions:
        content.append(Paragraph(f"• {s}", styles["Normal"]))

    content.append(Spacer(1, 20))

    # ================= FOOTER =================
    content.append(Paragraph(
        "<font size=10 color='grey'>Generated using AI Student Predictor</font>",
        styles["Normal"]
    ))

    # ================= BUILD =================
    doc.build(content)

    return file_name