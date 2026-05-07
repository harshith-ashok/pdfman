from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

import shutil
import os

from graph.workflow import build_workflow

app = FastAPI()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

workflow = build_workflow()


class SummarizeRequest(BaseModel):
    filenames: list[str]


@app.post("/upload")
async def upload_files(files: list[UploadFile] = File(...)):
    uploaded_files = []

    for file in files:
        if not file.filename.endswith(".pdf"):
            continue

        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        uploaded_files.append(file.filename)

    return {
        "uploaded_files": uploaded_files
    }


@app.post("/summarize")
async def summarize_files(request: SummarizeRequest):
    results = []

    for filename in request.filenames:
        file_path = os.path.join(UPLOAD_DIR, filename)

        if not os.path.exists(file_path):
            raise HTTPException(
                status_code=404,
                detail=f"{filename} not found"
            )

        result = workflow.invoke({
            "file_path": file_path,
            "text": "",
            "chunks": [],
            "chunk_summaries": [],
            "summary": "",
            "output_path": ""
        })

        results.append({
            "file": filename,
            "saved_to": result["output_paths"]
        })

    return {
        "processed_files": results
    }
