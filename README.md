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

## Phase: 1

1. added `/summarize` endpoint to perform basic summary

### cURL Commands

```bash
curl -X POST "http://127.0.0.1:8000/upload" \
  -F "files=@/path/to/book1.pdf" \
  -F "files=@/path/to/book2.pdf"
```

```bash
curl -X POST "http://127.0.0.1:8000/summarize" \
  -H "Content-Type: application/json" \
  -d '{
    "filenames": [
      "book1.pdf",
      "book2.pdf"
    ]
  }'
```
