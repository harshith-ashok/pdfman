# app/tools/summarizer.py

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)


def summarize_text(text: str) -> str:
    prompt = f"""
You are an expert summarization assistant that writes in the style of a detailed, well-structured book.
Summarize the following text into rich, thorough Obsidian-compatible notes.

Requirements:

- Use markdown with clear #, ##, and ### headings to organize content hierarchically
- Write full, detailed bullet points — each point should be a complete thought, not a fragment
- Expand on key concepts with sub-bullets that provide context, nuance, and explanation
- Preserve important arguments, examples, evidence, and reasoning from the original text
- Include a ## Overview section at the top with a 3-5 sentence summary of the entire text
- Include a ## Key Takeaways section at the bottom with the most important conclusions
- Use bold for key terms and inline code for technical terms where appropriate
- Aim for depth over brevity — the goal is a thorough reference, not a quick recap

Text:
{text}
"""

    response = llm.invoke(prompt)

    return response.content
