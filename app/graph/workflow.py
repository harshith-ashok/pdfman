from langgraph.graph import StateGraph
from typing import TypedDict
from tools.pdf import parse_pdf
from tools.obsidian import save_markdown


class WorkflowState(TypedDict):
    file_path: str
    text: str
    output_path: str


def parse_pdf_node(state: WorkflowState) -> WorkflowState:
    text = parse_pdf(state["file_path"])
    return {**state, "text": text}


def save_markdown_node(state: WorkflowState) -> WorkflowState:
    filename = state["file_path"].split("/")[-1]
    content = f"# {filename}\n\n{state['text']}"

    output_path = save_markdown(filename, content)

    return {**state, "output_path": output_path}


def build_workflow():
    builder = StateGraph(WorkflowState)

    builder.add_node("parse_pdf", parse_pdf_node)
    builder.add_node("save_markdown", save_markdown_node)

    builder.set_entry_point("parse_pdf")

    builder.add_edge("parse_pdf", "save_markdown")

    return builder.compile()
