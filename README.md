# PDFman

Upload a PDF → extract text → save it as a .md file in a local vault.

---

## Flow

`START → parse_pdf → save_markdown → END`

### Components

- FastAPI → handles file upload
- LangGraph → orchestrates workflow

### Tools:

- `parse_pdf` → extracts text from PDF
- `save_markdown` → writes Markdown file to vault

---

## Phase: 0

1. `/upload` endpoint in place for PDF ingestion
2. basic conversion of uploaded PDF to markdown format
