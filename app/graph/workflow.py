from typing import TypedDict

from langgraph.graph import StateGraph

from tools.pdf import parse_pdf
from tools.obsidian import save_markdown
from tools.summarizer import summarize_text


class WorkflowState(TypedDict):
    file_path: str
    text: str
    summary: str
    output_path: str


def parse_pdf_node(state: WorkflowState) -> WorkflowState:
    print("Running parse_pdf_node")

    text = parse_pdf(state["file_path"])

    print("Parse State:", state)

    return {
        **state,
        "text": text
    }


def summarize_node(state: WorkflowState) -> WorkflowState:
    print("Running summarize_node")

    summary = summarize_text(state["text"])

    return {
        **state,
        "summary": summary
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
    builder.add_node("summarize", summarize_node)
    builder.add_node("save_markdown", save_markdown_node)

    builder.set_entry_point("parse_pdf")

    builder.add_edge("parse_pdf", "summarize")
    builder.add_edge("summarize", "save_markdown")

    return builder.compile()
