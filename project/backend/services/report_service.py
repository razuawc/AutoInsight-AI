from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from typing import Optional
import csv
from io import StringIO


class ReportService:
    @staticmethod
    def generate_pdf_report(data: dict, output_path: str) -> str:
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        story.append(Paragraph("AI Workflow Automation Hub - Report", styles["Title"]))
        story.append(Spacer(1, 0.25 * inch))

        story.append(Paragraph(f"Generated: {data.get('generated_at', 'N/A')}", styles["Normal"]))
        story.append(Spacer(1, 0.25 * inch))

        story.append(Paragraph("Executive Summary", styles["Heading2"]))
        story.append(Paragraph(data.get("summary", "No summary available."), styles["Normal"]))
        story.append(Spacer(1, 0.25 * inch))

        story.append(Paragraph("Key Insights", styles["Heading2"]))
        for insight in data.get("insights", []):
            story.append(Paragraph(f"- {insight}", styles["Normal"]))

        story.append(Spacer(1, 0.25 * inch))
        story.append(Paragraph("Recommendations", styles["Heading2"]))
        for rec in data.get("recommendations", []):
            story.append(Paragraph(f"- {rec}", styles["Normal"]))

        if data.get("metrics"):
            story.append(Spacer(1, 0.25 * inch))
            story.append(Paragraph("Metrics", styles["Heading2"]))
            table_data = [[k, str(v)] for k, v in data["metrics"].items()]
            table = Table([["Metric", "Value"]] + table_data)
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]))
            story.append(table)

        doc.build(story)
        return output_path

    @staticmethod
    def generate_csv(data: list[dict], headers: list[str]) -> str:
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow({h: row.get(h, "") for h in headers})
        return output.getvalue()
