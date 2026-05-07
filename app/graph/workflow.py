from tools.note_generator import generate_note
from tools.topic_extractor import extract_topics
from tools.summarizer import combine_summaries
from tools.summarizer import summarize_chunk
from tools.chunker import chunk_text
from typing import TypedDict

from langgraph.graph import StateGraph

from tools.pdf import parse_pdf
from tools.obsidian import save_markdown


class WorkflowState(TypedDict):
    file_path: str
    text: str
    chunks: list[str]
    chunk_summaries: list[str]
    topics: list[str]
    notes: dict[str, str]
    output_paths: list[str]


def extract_topics_node(state: WorkflowState):
    print("Running extract_topics_node")

    combined = "\n\n".join(
        state["chunk_summaries"]
    )

    topics = extract_topics(combined)

    print("TOPICS:")
    print(topics)

    return {
        **state,
        "topics": topics
    }


def generate_notes_node(state: WorkflowState):
    print("Running generate_notes_node")

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

    return {
        **state,
        "notes": notes
    }


def save_notes_node(state: WorkflowState):
    print("Running save_notes_node")

    output_paths = []

    pdf_name = state["file_path"].split("/")[-1]

    for topic, content in state["notes"].items():

        path = save_markdown(
            pdf_name=pdf_name,
            note_title=topic,
            content=content
        )

        output_paths.append(path)

    return {
        **state,
        "output_paths": output_paths
    }


def parse_pdf_node(state: WorkflowState) -> WorkflowState:
    print("Running parse_pdf_node")

    text = parse_pdf(state["file_path"])

    print("Parse State:", state)

    return {
        **state,
        "text": text
    }


def chunk_node(state: WorkflowState) -> WorkflowState:
    print("Running chunk_node")

    chunks = chunk_text(state["text"])

    return {
        **state,
        "chunks": chunks
    }


def summarize_chunks_node(state: WorkflowState) -> WorkflowState:
    print("Running summarize_chunks_node")

    summaries = []

    for chunk in state["chunks"]:
        summary = summarize_chunk(chunk)
        summaries.append(summary)

    return {
        **state,
        "chunk_summaries": summaries
    }


def combine_summaries_node(state: WorkflowState) -> WorkflowState:
    print("Running combine_summaries_node")

    final_summary = combine_summaries(
        state["chunk_summaries"]
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

    output_path = save_markdown(filename, content)

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
