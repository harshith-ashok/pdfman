from tools.cleaner import clean_markdown_output
from tools.llm_utils import invoke_with_retry
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gpt-oss:120b-cloud",
    temperature=0
)


def generate_note(
    topic: str,
    text: str,
    related_topics: list[str],
    source_pdf: str
) -> str:

    backlinks = [
        f"[[{t}]]"
        for t in related_topics
        if t != topic
    ]

    backlink_section = "\n".join(backlinks)

    prompt = f"""
You are a markdown generation engine.

Your task is to output ONLY raw Obsidian markdown.

STRICT RULES:
- Do NOT speak to the user
- Do NOT add ``` unless it is a code block
- Do NOT explain what you are doing
- Do NOT say "Here is your note"
- Do NOT add introductions
- Do NOT add conclusions
- Do NOT use conversational text
- Output ONLY the markdown note
- Begin immediately with YAML frontmatter

TOPIC:
{topic}

SOURCE PDF:
{source_pdf}

RELATED TOPICS:
{backlink_section}

TEXT:
{text[:5000]}
"""

    cleaned = clean_markdown_output(
        invoke_with_retry(llm, prompt)
    )

    return cleaned
