from fastapi import FastAPI, UploadFile, File
import shutil
import os

from graph.workflow import build_workflow

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

workflow = build_workflow()


@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = workflow.invoke({
        "file_path": file_path,
        "text": "",
        "output_path": ""
    })

    return {
        "message": "Processed via LangGraph",
        "output": result["output_path"]
    }
