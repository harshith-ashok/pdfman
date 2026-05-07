# PDFman

AI-powered PDF → Obsidian knowledge extraction system.

Upload PDFs, process them through a LangGraph workflow, generate structured Obsidian-compatible notes, and store them inside a local vault.

---

## Flow

```text
START
→ parse_pdf
→ chunk_text
→ summarize_chunks
→ extract_topics
→ generate_notes
→ save_notes
→ END
```

---

## Architecture

### Components

- FastAPI → handles API endpoints and file uploads
- LangGraph → orchestrates workflow execution
- Ollama → runs local language models
- Obsidian Vault → stores generated markdown knowledge base

---

## Workflow

```text
parse_pdf
→ chunk_text
→ summarize_chunks
→ extract_topics
→ generate_notes
→ save_notes
```

---

## Packages Used

| Package                    | Responsibility                 |
| -------------------------- | ------------------------------ |
| `langgraph`                | Workflow orchestration         |
| `langchain`                | LLM abstractions               |
| `langchain-ollama`         | Local Ollama model integration |
| `langchain-text-splitters` | Intelligent document chunking  |

---

## Tools

| Tool               | Purpose                                    |
| ------------------ | ------------------------------------------ |
| `parse_pdf`        | Extracts raw text from PDFs                |
| `chunk_text`       | Splits large text into manageable chunks   |
| `summarize_chunks` | Generates chunk-level summaries            |
| `extract_topics`   | Detects important concepts/topics          |
| `generate_notes`   | Creates Obsidian-compatible markdown notes |
| `save_markdown`    | Saves notes into vault folders             |

---

# Features

- Multiple PDF upload support
- Separate upload and summarize endpoints
- Automatic topic extraction
- Obsidian-compatible markdown generation
- YAML frontmatter support
- Automatic backlinks (`[[links]]`)
- Vault folder organization per PDF
- Local LLM support through Ollama
- LangGraph workflow orchestration

---

# Vault Structure

```text
vault/
└── Unit 4 AI Notes/
    ├── Neural Networks.md
    ├── Bayesian Networks.md
    ├── Reasoning Methods.md
    └── Uncertainty.md
```

---

# Obsidian Features

Generated notes include:

- YAML frontmatter
- tags
- backlinks
- aliases
- markdown headings
- bullet points
- source metadata

Example:

```md
---
tags:
  - ai
  - reasoning
source: Unit 4 AI Notes.pdf
---

# Neural Networks

## Overview

...

## Related Notes

- [[Gradient Descent]]
- [[Backpropagation]]
```

---

# Phases

## Phase 0

### Initial PDF Processing

- `/upload` endpoint for PDF ingestion
- Basic PDF → Markdown conversion
- Local vault integration

---

## Phase 1

### Summarization Pipeline

- Added `/summarize` endpoint
- Introduced LangGraph workflow
- Added chunk-based summarization
- Added text splitting pipeline

---

## Phase 2

### Multi-File Processing

- Multiple PDF upload support
- Separate upload and summarize endpoints
- Workflow state management
- Improved FastAPI integration

---

## Phase 3

### Obsidian Knowledge Generation

- Topic extraction from summarized content
- Automatic note generation
- Obsidian-compatible markdown formatting
- YAML frontmatter generation
- Automatic backlinks between notes
- PDF-specific folder organization
- Multi-note generation from a single PDF
- Markdown output cleaning and normalization

---

# API Endpoints

## Upload PDFs

```bash
curl -X POST "http://127.0.0.1:8120/upload" \
  -F "files=@/path/to/book1.pdf" \
  -F "files=@/path/to/book2.pdf"
```

Example:

```bash
curl -X POST "http://127.0.0.1:8120/upload" \
  -F "files=@/Users/harshith/Downloads/Unit 4 AI Notes.pdf"
```

---

## Summarize PDFs

```bash
curl -X POST "http://127.0.0.1:8120/summarize" \
  -H "Content-Type: application/json" \
  -d '{
    "filenames": [
      "book1.pdf",
      "book2.pdf"
    ]
  }'
```

Example:

```bash
curl -X POST "http://127.0.0.1:8120/summarize" \
  -H "Content-Type: application/json" \
  -d '{
    "filenames": [
      "Unit 4 AI Notes.pdf"
    ]
  }'
```

---

# Current Status

Current architecture:

```text
PDF
→ chunk
→ summarize
→ extract topics
→ generate Obsidian notes
→ save into vault
```

Next planned upgrade:

- semantic retrieval (RAG)
- embeddings
- vector search
- topic-specific context retrieval
