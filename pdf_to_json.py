from __future__ import annotations

import json
from pathlib import Path

from pypdf import PdfReader


ROOT_DIR = Path(__file__).resolve().parent
PAPERS_DIR = ROOT_DIR / "papers"
OUTPUT_DIR = ROOT_DIR / "papers_json"


def pdf_to_json_dict(pdf_path: Path) -> dict:
    """Convert a single PDF to a JSON-serializable dict.

    The dict includes per-page text and a concatenated full_text field so that
    every piece of text extracted from the PDF is represented in the JSON.
    """

    reader = PdfReader(str(pdf_path))

    pages = []
    full_text_parts: list[str] = []

    for index, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception:
            # If extraction fails for a page, still keep an entry so that
            # page positions are preserved.
            text = ""

        pages.append(
            {
                "page_number": index,
                "text": text,
            }
        )
        full_text_parts.append(text)

    # Concatenate all page texts to provide a convenient full_text field.
    full_text = "\n\n".join(full_text_parts)

    data: dict = {
        "source_pdf": pdf_path.name,
        "relative_pdf_path": str(pdf_path.relative_to(ROOT_DIR)),
        "num_pages": len(pages),
        "pages": pages,
        "full_text": full_text,
    }

    return data


def convert_all_papers() -> None:
    """Convert all PDFs in PAPERS_DIR to JSON files in OUTPUT_DIR."""

    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted(PAPERS_DIR.glob("*.pdf"))

    if not pdf_files:
        print(f"No PDF files found in {PAPERS_DIR}")
        return

    for pdf_path in pdf_files:
        print(f"Processing {pdf_path} ...")
        json_data = pdf_to_json_dict(pdf_path)

        output_name = pdf_path.stem + ".json"
        output_path = OUTPUT_DIR / output_name

        with output_path.open("w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

        print(f"  -> Wrote {output_path}")


if __name__ == "__main__":
    convert_all_papers()
