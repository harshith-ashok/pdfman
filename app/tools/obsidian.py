import os
import re

APP_DIR = os.path.dirname(
    os.path.dirname(__file__)
)
VAULT_PATH = os.path.join(APP_DIR, "vault")


def sanitize_filename(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "", name)


def save_markdown(
    pdf_name: str,
    note_title: str,
    content: str,
    vault_path: str = VAULT_PATH
) -> str:

    pdf_folder = sanitize_filename(
        pdf_name.replace(".pdf", "")
    )

    note_title = sanitize_filename(note_title)

    folder_path = os.path.join(
        vault_path,
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
