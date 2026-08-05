from reportlab.pdfgen import canvas


def create_report(
    name,
    score,
    performance,
    suggestions
):

    file = "student_report.pdf"

    pdf = canvas.Canvas(file)

    pdf.drawString(
        100,
        750,
        "AI Student Performance Report"
    )

    pdf.drawString(
        100,
        700,
        f"Student Name: {name}"
    )

    pdf.drawString(
        100,
        650,
        f"Predicted Score: {score:.2f}%"
    )

    pdf.drawString(
        100,
        600,
        f"Performance: {performance}"
    )


    pdf.drawString(
        100,
        550,
        "AI Suggestions:"
    )


    y = 520

    for suggestion in suggestions:

        pdf.drawString(
            120,
            y,
            suggestion
        )

        y -= 30


    pdf.save()


    return file