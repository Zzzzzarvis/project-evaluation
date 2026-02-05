from pathlib import Path
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas


def markdown_to_pdf(md_path: Path, pdf_path: Path) -> None:
    md_path = Path(md_path)
    pdf_path = Path(pdf_path)
    text = md_path.read_text(encoding="utf-8")

    c = canvas.Canvas(str(pdf_path), pagesize=LETTER)
    width, height = LETTER
    x = 72
    y = height - 72
    line_height = 14

    for line in text.splitlines():
        if y < 72:
            c.showPage()
            y = height - 72
        c.drawString(x, y, line)
        y -= line_height

    c.save()
