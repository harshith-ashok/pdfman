import fitz


def parse_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = []

    for page in doc:
        text.append(page.get_text())

    doc.close()
    return "\n".join(text)
