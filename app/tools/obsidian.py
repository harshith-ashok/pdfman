import os

VAULT_PATH = "vault"


def save_markdown(filename: str, content: str) -> str:
    os.makedirs(VAULT_PATH, exist_ok=True)

    if not filename.endswith(".md"):
        filename += ".md"

    file_path = os.path.join(VAULT_PATH, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path
