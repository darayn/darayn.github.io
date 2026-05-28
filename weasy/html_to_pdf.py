#!/usr/bin/env python3
"""
Convert an HTML file to PDF using WeasyPrint.

Usage:
    python html_to_pdf.py resume.html
    python html_to_pdf.py resume.html output.pdf

Install dependency:
    pip install weasyprint
"""

import sys
from pathlib import Path


def convert(input_path: str, output_path: str | None = None) -> None:
    try:
        from weasyprint import HTML, CSS
    except ImportError:
        print("WeasyPrint not found. Install it with:  pip install weasyprint")
        sys.exit(1)

    src = Path(input_path).resolve()
    if not src.exists():
        print(f"File not found: {src}")
        sys.exit(1)

    if output_path is None:
        dest = src.with_suffix(".pdf")
    else:
        dest = Path(output_path).resolve()

    HTML(filename=str(src)).write_pdf(
        str(dest),
        stylesheets=[CSS(string="@page { size: A4; margin: 0; }")]
    )
    print(f"✓  Saved → {dest}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) >= 3 else None
    convert(inp, out)
