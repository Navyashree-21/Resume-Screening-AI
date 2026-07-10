from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


class PDFReport:

    @staticmethod
    def generate(result, filename):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>Resume Screening AI Report</b>",
                styles["Heading1"]
            )
        )

        story.append(Spacer(1,20))

        story.append(
            Paragraph(
                f"<b>Overall Score:</b> {result['overall_score']}/100",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Decision:</b> {result['decision']}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1,20))

        story.append(
            Paragraph(
                "<b>Skill Analysis</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                result["skill"]["reason"],
                styles["Normal"]
            )
        )

        story.append(Spacer(1,15))

        story.append(
            Paragraph(
                "<b>Education</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                result["education"]["reason"],
                styles["Normal"]
            )
        )

        story.append(Spacer(1,15))

        story.append(
            Paragraph(
                "<b>Experience</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                result["experience"]["reason"],
                styles["Normal"]
            )
        )

        story.append(Spacer(1,15))

        story.append(
            Paragraph(
                "<b>Salary Prediction</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                result["salary"]["reason"],
                styles["Normal"]
            )
        )

        story.append(Spacer(1,15))

        story.append(
            Paragraph(
                "<b>ATS Matching</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                result["jd_match"]["reason"],
                styles["Normal"]
            )
        )

        if "improvement" in result:

            story.append(Spacer(1,15))

            story.append(
                Paragraph(
                    "<b>Resume Improvements</b>",
                    styles["Heading2"]
                )
            )

            for item in result["improvement"]["resume_improvements"]:

                story.append(
                    Paragraph(
                        f"• {item}",
                        styles["Normal"]
                    )
                )

        doc.build(story)