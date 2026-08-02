from langchain_ollama import ChatOllama
from tools.llm_utils import invoke_with_retry

llm = ChatOllama(
    model="gpt-oss:120b-cloud",
    temperature=0
)


def summarize_chunk(chunk: str) -> str:
    prompt = f"""
You are an expert summarization assistant that writes in the style of a detailed, well-structured book chapter.

Summarize the following chunk of text into rich, thorough Obsidian-compatible notes.

**Requirements:**
- Use markdown with clear `#`, `##`, and `###` headings to organize content hierarchically
- Write **full, detailed bullet points** — each point should be a complete thought, not a fragment
- Expand on key concepts with sub-bullets that provide context, nuance, and explanation
- Preserve important arguments, examples, evidence, and reasoning from the original text
- Use **bold** for key terms and `inline code` for technical terms where appropriate
- Include a `## chunk Overview` section at the top with 2-4 sentences summarizing this section
- Do not include emojis
- Aim for depth over brevity — the goal is a thorough reference, not a quick recap

**Text:**
{chunk}
"""

    return invoke_with_retry(llm, prompt)


def combine_summaries(summaries: list[str]) -> str:
    combined_text = "\n\n".join(summaries)

    prompt = f"""
You are an expert editor and summarization assistant. Your job is to merge multiple detailed section summaries into one unified, book-style reference document in Obsidian-compatible markdown.

**Requirements:**
- Begin with a `## Document Overview` section: a 4-6 sentence synthesis of the entire document's scope, argument, and significance
- Merge and reorganize all sections under clear `#`, `##`, and `###` headings — group related ideas together even if they appeared in separate chunks
- Eliminate redundancy: if the same concept appears multiple times, consolidate it into one rich, expanded entry rather than repeating it
- Preserve and expand on all key arguments, examples, evidence, and reasoning — do not flatten detail in the name of brevity
- Write **full, detailed bullet points** with sub-bullets that add context and explanation
- Use **bold** for key terms and `inline code` for technical terms where appropriate
- End with a `## Key Takeaways` section listing the most important conclusions and insights from the full document
- The final output should read like a thorough book-chapter reference a researcher would rely on

**Summaries:**
{combined_text}
"""

    return invoke_with_retry(llm, prompt)
