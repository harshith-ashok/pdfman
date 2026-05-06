from fastapi import FastAPI, UploadFile, File
import shutil
import os

from tools.pdf import parse_pdf
from tools.obsidian import save_markdown

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = parse_pdf(file_path)

    md_content = f"# {file.filename}\n\n{text}"

    saved_path = save_markdown(file.filename, md_content)

    return {
        "message": "File processed",
        "saved_to": saved_path
    }
