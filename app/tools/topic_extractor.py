from langchain_ollama import ChatOllama
import json
import re
from tools.llm_utils import invoke_with_retry

llm = ChatOllama(
    model="gpt-oss:120b-cloud",
    temperature=0
)


def extract_topics(text: str) -> list[str]:
    prompt = f"""
You are a JSON API.

Your ONLY task is to extract topic names.

RULES:
- Return ONLY valid JSON
- No explanations
- No markdown
- No comments
- No prose
- Output must be a JSON array of strings

VALID OUTPUT:
[
  "Topic 1",
  "Topic 2",
  "Topic 3"
]

TEXT:
----------------
{text[:4000]}
----------------
"""

    content = invoke_with_retry(
        llm,
        prompt
    ).strip()

    print("RAW TOPIC RESPONSE:")
    print(content)

    content = re.sub(
        r"```json|```",
        "",
        content
    ).strip()

    try:
        parsed = json.loads(content)

    except Exception as e:
        print("JSON PARSE ERROR:")
        print(e)

        return []

    topics = []

    for item in parsed:
        if isinstance(item, str):
            topics.append(item)

    return topics
