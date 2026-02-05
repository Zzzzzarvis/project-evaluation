from pathlib import Path
from scripts.markdown_to_pdf import markdown_to_pdf


def test_markdown_to_pdf(tmp_path):
    md = tmp_path / "in.md"
    pdf = tmp_path / "out.pdf"
    md.write_text("# Title\n\nHello")
    markdown_to_pdf(md, pdf)
    assert pdf.exists() and pdf.stat().st_size > 0
