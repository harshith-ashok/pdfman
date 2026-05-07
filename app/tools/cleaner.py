import re


def clean_markdown_output(text: str) -> str:

    unwanted_phrases = [
        r"^Here's your.*?$",
        r"^Here is your.*?$",
        r"^Certainly!.*?$",
        r"^Below is.*?$",
        r"```markdown"
    ]

    lines = text.splitlines()

    cleaned = []

    for line in lines:
        should_skip = False

        for pattern in unwanted_phrases:
            if re.match(pattern, line.strip(), re.IGNORECASE):
                should_skip = True
                break

        if not should_skip:
            cleaned.append(line)

    return "\n".join(cleaned).strip()
