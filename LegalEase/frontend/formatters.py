import html
import os
import re
from io import BytesIO

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt
from fpdf import FPDF

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(BASE_DIR, "..", "Image", "Logo.png")
FOOTER_TEXT = "LegalEase Inc. | contact@legalease.com | All Rights Reserved."


def sanitize_text(text: str) -> str:
    """Remove typographic quotes, markdown symbols and odd characters."""
    replacements = {
        "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
        "\u2013": "-", "\u2014": "-", "\u2022": "-", "\u2026": "...",
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace("**", "")
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    return text.strip()


def is_heading(line: str) -> bool:
    line = line.strip()
    if not line:
        return False
    if re.match(r"^\d+\.\s", line) and len(line) < 80:
        return True
    if line.endswith(":") and len(line) < 60:
        return True
    return line.isupper() and len(line) < 80


def is_bullet(line: str) -> bool:
    return line.strip().startswith(("- ", "* "))


def split_terms(terms: str):
    return [t.strip() for t in terms.split(";") if t.strip()]


# ---------- HTML preview ----------
def format_html_preview(text: str) -> str:
    parts = []
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        safe = html.escape(line)
        if is_heading(line):
            parts.append(f"<h4 style='margin:18px 0 6px 0;'>{safe}</h4>")
        elif is_bullet(line):
            parts.append(f"<p style='margin:2px 0 2px 20px;'>&bull; {html.escape(line[2:])}</p>")
        else:
            parts.append(f"<p style='margin:6px 0;'>{safe}</p>")
    return "\n".join(parts)


# ---------- DOCX ----------
def format_docx(text: str, doc_type: str, terms: str = "") -> bytes:
    doc = Document()

    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)

    if os.path.exists(LOGO_PATH):
        doc.add_picture(LOGO_PATH, width=Inches(1.8))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run(doc_type.upper())
    run.bold = True
    run.font.size = Pt(16)

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        p = doc.add_paragraph()
        if is_heading(line):
            p.add_run(line).bold = True
        elif is_bullet(line):
            p.add_run("\u2022 " + line[2:])
            p.paragraph_format.left_indent = Inches(0.3)
        else:
            p.add_run(line)

    items = split_terms(terms)
    if items:
        doc.add_paragraph().add_run("Summary of Terms").bold = True
        table = doc.add_table(rows=1, cols=2)
        table.style = "Table Grid"
        table.rows[0].cells[0].text = "No."
        table.rows[0].cells[1].text = "Term"
        for i, item in enumerate(items, 1):
            row = table.add_row().cells
            row[0].text = str(i)
            row[1].text = item

    footer = doc.sections[0].footer.paragraphs[0]
    footer.text = FOOTER_TEXT
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER

    buffer = BytesIO()
    doc.save(buffer)
    return buffer.getvalue()


# ---------- PDF ----------
class LegalPDF(FPDF):
    def header(self):
        if os.path.exists(LOGO_PATH):
            self.image(LOGO_PATH, x=(210 - 40) / 2, y=8, w=40)
        self.ln(28)

    def footer(self):
        self.set_y(-15)
        self.set_font("Times", "I", 9)
        self.cell(0, 10, FOOTER_TEXT, 0, 0, "C")


def _latin(s: str) -> str:
    """FPDF's built-in fonts only understand latin-1."""
    return s.encode("latin-1", "replace").decode("latin-1")


def format_pdf(text: str, doc_type: str) -> bytes:
    pdf = LegalPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    pdf.set_font("Times", "B", 16)
    pdf.multi_cell(0, 10, _latin(doc_type), 0, "C")
    pdf.ln(4)

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if is_heading(line):
            pdf.ln(2)
            pdf.set_font("Times", "B", 12)
            pdf.multi_cell(0, 7, _latin(line))
        elif is_bullet(line):
            pdf.set_font("Times", "", 12)
            pdf.set_x(pdf.l_margin + 8)
            pdf.multi_cell(0, 6, _latin("- " + line[2:]))
        else:
            pdf.set_font("Times", "", 12)
            pdf.multi_cell(0, 6, _latin(line))

    out = pdf.output(dest="S")
    return out.encode("latin-1") if isinstance(out, str) else bytes(out)
