import os
import time
import logging
from concurrent.futures import ThreadPoolExecutor
from tools.note_generator import generate_note
from tools.topic_extractor import extract_topics
from tools.summarizer import combine_summaries
from tools.summarizer import summarize_chunk
from tools.chunker import chunk_text
from typing import TypedDict

from langgraph.graph import StateGraph

from tools.pdf import parse_document
from tools.obsidian import save_markdown
from tools.jobs import record_job_timing
from tools.jobs import update_job

logger = logging.getLogger(__name__)

MAX_SUMMARY_WORKERS = max(
    1,
    int(os.getenv("PDFMAN_SUMMARY_WORKERS", "4"))
)


class WorkflowState(TypedDict):
    job_id: str
    file_path: str
    vault_path: str
    text: str
    chunks: list[str]
    chunk_summaries: list[str]
    topics: list[str]
    notes: dict[str, str]
    output_paths: list[str]
    summary: str


def extract_topics_node(state: WorkflowState):
    print("Running extract_topics_node")
    started_at = time.perf_counter()

    combined = "\n\n".join(
        state["chunk_summaries"]
    )

    topics = extract_topics(combined)

    print("TOPICS:")
    print(topics)

    _record_stage_timing(
        state["job_id"],
        "extract_topics",
        started_at
    )

    return {
        **state,
        "topics": topics
    }


def generate_notes_node(state: WorkflowState):
    print("Running generate_notes_node")
    started_at = time.perf_counter()

    update_job(
        state["job_id"],
        stage="link",
        progress=0.85
    )

    notes = {}

    combined_text = "\n\n".join(
        state["chunk_summaries"]
    )

    pdf_name = state["file_path"].split("/")[-1]

    for topic in state["topics"]:

        note = generate_note(
            topic=topic,
            text=combined_text,
            related_topics=state["topics"],
            source_pdf=pdf_name
        )

        notes[topic] = note

    _record_stage_timing(
        state["job_id"],
        "generate_notes",
        started_at
    )

    return {
        **state,
        "notes": notes
    }


def save_notes_node(state: WorkflowState):
    print("Running save_notes_node")
    started_at = time.perf_counter()

    output_paths = []

    pdf_name = state["file_path"].split("/")[-1]

    for topic, content in state["notes"].items():

        path = save_markdown(
            pdf_name=pdf_name,
            note_title=topic,
            content=content,
            vault_path=state["vault_path"]
        )

        output_paths.append(path)

    _record_stage_timing(
        state["job_id"],
        "save_notes",
        started_at
    )
    update_job(
        state["job_id"],
        progress=0.98
    )

    return {
        **state,
        "output_paths": output_paths
    }


def parse_pdf_node(state: WorkflowState) -> WorkflowState:
    print("Running parse_pdf_node")
    started_at = time.perf_counter()

    update_job(
        state["job_id"],
        status="running",
        stage="parse",
        progress=0.2,
        current_file=os.path.basename(
            state["file_path"]
        )
    )

    text = parse_document(state["file_path"])

    _record_stage_timing(
        state["job_id"],
        "parse_document",
        started_at
    )

    return {
        **state,
        "text": text
    }


def chunk_node(state: WorkflowState) -> WorkflowState:
    print("Running chunk_node")
    started_at = time.perf_counter()

    chunks = chunk_text(state["text"])

    _record_stage_timing(
        state["job_id"],
        "chunk_text",
        started_at
    )

    return {
        **state,
        "chunks": chunks
    }


def summarize_chunks_node(state: WorkflowState) -> WorkflowState:
    print("Running summarize_chunks_node")
    started_at = time.perf_counter()

    update_job(
        state["job_id"],
        stage="summarize",
        progress=0.5
    )

    chunks = state["chunks"]

    with ThreadPoolExecutor(
        max_workers=min(
            MAX_SUMMARY_WORKERS,
            len(chunks) or 1
        )
    ) as executor:
        summaries = list(
            executor.map(
                summarize_chunk,
                chunks
            )
        )

    _record_stage_timing(
        state["job_id"],
        "summarize_chunks",
        started_at
    )

    return {
        **state,
        "chunk_summaries": summaries
    }


def combine_summaries_node(state: WorkflowState) -> WorkflowState:
    print("Running combine_summaries_node")
    started_at = time.perf_counter()

    final_summary = combine_summaries(
        state["chunk_summaries"]
    )

    _record_stage_timing(
        state["job_id"],
        "combine_summaries",
        started_at
    )

    return {
        **state,
        "summary": final_summary
    }


def save_markdown_node(state: WorkflowState) -> WorkflowState:
    print("Running save_markdown_node")

    filename = state["file_path"].split("/")[-1].replace(".pdf", "")

    content = f"""# {filename}

{state['summary']}
"""

    output_path = save_markdown(
        filename,
        filename,
        content,
        vault_path=state["vault_path"]
    )

    return {
        **state,
        "output_path": output_path
    }


def build_workflow():
    builder = StateGraph(WorkflowState)

    builder.add_node("parse_pdf", parse_pdf_node)
    builder.add_node("chunk", chunk_node)
    builder.add_node("summarize_chunks", summarize_chunks_node)

    builder.add_node("extract_topics", extract_topics_node)
    builder.add_node("generate_notes", generate_notes_node)

    builder.add_node("save_notes", save_notes_node)

    builder.set_entry_point("parse_pdf")

    builder.add_edge("parse_pdf", "chunk")

    builder.add_edge("chunk", "summarize_chunks")

    builder.add_edge(
        "summarize_chunks",
        "extract_topics"
    )

    builder.add_edge(
        "extract_topics",
        "generate_notes"
    )

    builder.add_edge(
        "generate_notes",
        "save_notes"
    )

    return builder.compile()


def _record_stage_timing(
    job_id: str,
    stage_name: str,
    started_at: float
) -> None:
    elapsed = time.perf_counter() - started_at
    logger.info(
        "%s completed in %.2fs",
        stage_name,
        elapsed
    )
    record_job_timing(
        job_id,
        stage_name,
        elapsed
    )
