import os
import re

VAULT_PATH = "vault"


def sanitize_filename(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "", name)


def save_markdown(
    pdf_name: str,
    note_title: str,
    content: str
) -> str:

    pdf_folder = sanitize_filename(
        pdf_name.replace(".pdf", "")
    )

    note_title = sanitize_filename(note_title)

    folder_path = os.path.join(
        VAULT_PATH,
        pdf_folder
    )

    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(
        folder_path,
        f"{note_title}.md"
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path
