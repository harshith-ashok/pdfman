import logging
import os
import time

import fitz
from fastapi import BackgroundTasks
from fastapi import FastAPI
from fastapi import File
from fastapi import Form
from fastapi import HTTPException
from fastapi import UploadFile
from pydantic import BaseModel

from graph.workflow import build_workflow
from tools.jobs import append_job_result
from tools.jobs import complete_job
from tools.jobs import create_job
from tools.jobs import create_session
from tools.jobs import ensure_runtime_dirs
from tools.jobs import fail_job
from tools.jobs import get_session_paths
from tools.jobs import read_job
from tools.jobs import record_job_timing
from tools.jobs import update_job
from tools.vault_mesh import mesh_vault_notes


logging.basicConfig(
    level=os.getenv("PDFMAN_LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

MAX_UPLOAD_BYTES = int(
    os.getenv("PDFMAN_MAX_UPLOAD_BYTES", "26214400")
)
SUPPORTED_UPLOAD_EXTENSIONS = {
    ".pdf",
    ".md"
}

ensure_runtime_dirs()
workflow = build_workflow()


class SummarizeRequest(BaseModel):
    session_id: str
    filenames: list[str]


class MeshVaultRequest(BaseModel):
    session_id: str


@app.post("/upload")
async def upload_files(
    files: list[UploadFile] = File(...),
    session_id: str | None = Form(None)
):
    session = (
        get_session_paths(session_id)
        if session_id
        else create_session()
    )

    uploaded_files = []
    rejected_files = []

    for file in files:
        try:
            upload_result = await _store_upload(
                file=file,
                uploads_dir=session["uploads_dir"]
            )
            uploaded_files.append(upload_result)
        except HTTPException as exc:
            rejected_files.append({
                "filename": file.filename,
                "reason": exc.detail
            })

    return {
        "session_id": session["session_id"],
        "uploads_dir": session["uploads_dir"],
        "vault_dir": session["vault_dir"],
        "uploaded_files": uploaded_files,
        "rejected_files": rejected_files
    }


@app.post("/summarize")
async def summarize_files(
    request: SummarizeRequest,
    background_tasks: BackgroundTasks
):
    session = _require_session(
        request.session_id
    )
    filenames = [
        _normalize_filename(filename)
        for filename in request.filenames
    ]

    if not filenames:
        raise HTTPException(
            status_code=400,
            detail="No filenames provided"
        )

    missing_files = [
        filename
        for filename in filenames
        if not os.path.exists(
            os.path.join(
                session["uploads_dir"],
                filename
            )
        )
    ]

    if missing_files:
        raise HTTPException(
            status_code=404,
            detail=f"Files not found in session: {missing_files}"
        )

    job = create_job(
        session_id=request.session_id,
        filenames=filenames
    )

    background_tasks.add_task(
        _run_summarize_job,
        session["session_id"],
        filenames,
        job["job_id"]
    )

    return {
        "message": "Summarization job started",
        "job_id": job["job_id"],
        "session_id": session["session_id"],
        "status": job["status"],
        "stage": job["stage"]
    }


@app.get("/jobs/{job_id}")
async def get_job(job_id: str):
    try:
        return read_job(job_id)
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc)
        ) from exc


@app.post("/mesh-vault")
async def mesh_vault(request: MeshVaultRequest):
    session = _require_session(
        request.session_id
    )

    started_at = time.perf_counter()
    stats = mesh_vault_notes(
        session["vault_dir"]
    )
    elapsed = time.perf_counter() - started_at

    logger.info(
        "Vault mesh completed for session %s in %.2fs",
        request.session_id,
        elapsed
    )

    return {
        "message": "Vault mesh linking complete",
        "session_id": request.session_id,
        "timing_seconds": round(elapsed, 3),
        **stats
    }


async def _store_upload(
    file: UploadFile,
    uploads_dir: str
) -> dict[str, object]:
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Missing filename"
        )

    safe_filename = _normalize_filename(
        file.filename
    )
    extension = os.path.splitext(
        safe_filename
    )[1].lower()

    if extension not in SUPPORTED_UPLOAD_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Unsupported file type {extension}. "
                "Supported types: .pdf, .md"
            )
        )

    content = await file.read()

    if len(content) > MAX_UPLOAD_BYTES:
        raise HTTPException(
            status_code=400,
            detail=(
                f"{safe_filename} exceeds max upload size of "
                f"{MAX_UPLOAD_BYTES} bytes"
            )
        )

    _validate_upload_content(
        filename=safe_filename,
        extension=extension,
        content=content
    )

    os.makedirs(uploads_dir, exist_ok=True)
    file_path = os.path.join(
        uploads_dir,
        safe_filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(content)

    logger.info(
        "Stored upload %s (%s bytes) at %s",
        safe_filename,
        len(content),
        file_path
    )

    return {
        "filename": safe_filename,
        "size_bytes": len(content),
        "saved_to": file_path
    }


def _validate_upload_content(
    filename: str,
    extension: str,
    content: bytes
) -> None:
    if extension == ".md":
        try:
            content.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise HTTPException(
                status_code=400,
                detail=f"{filename} is not valid UTF-8 markdown"
            ) from exc
        return

    try:
        document = fitz.open(
            stream=content,
            filetype="pdf"
        )
        document.close()
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} is not a readable PDF"
        ) from exc


def _run_summarize_job(
    session_id: str,
    filenames: list[str],
    job_id: str
) -> None:
    session = _require_session(session_id)
    uploads_dir = session["uploads_dir"]
    vault_dir = session["vault_dir"]

    job_started_at = time.perf_counter()

    update_job(
        job_id,
        status="running",
        stage="uploaded",
        progress=0.05
    )

    try:
        total_files = len(filenames)

        for index, filename in enumerate(
            filenames,
            start=1
        ):
            file_path = os.path.join(
                uploads_dir,
                filename
            )

            logger.info(
                "Starting file %s/%s for job %s: %s",
                index,
                total_files,
                job_id,
                filename
            )

            update_job(
                job_id,
                current_file=filename,
                progress=min(
                    0.1 + ((index - 1) / total_files) * 0.8,
                    0.9
                )
            )

            result = workflow.invoke({
                "job_id": job_id,
                "file_path": file_path,
                "vault_path": vault_dir,
                "text": "",
                "chunks": [],
                "chunk_summaries": [],
                "topics": [],
                "notes": {},
                "output_paths": [],
                "summary": ""
            })

            append_job_result(
                job_id,
                {
                    "file": filename,
                    "saved_to": result["output_paths"],
                    "topics": result["topics"]
                }
            )

        record_job_timing(
            job_id,
            "total_job",
            time.perf_counter() - job_started_at
        )
        complete_job(job_id)
        logger.info(
            "Job %s completed successfully",
            job_id
        )

    except Exception as exc:
        logger.exception(
            "Job %s failed",
            job_id
        )
        fail_job(job_id, str(exc))


def _require_session(session_id: str) -> dict[str, str]:
    try:
        return get_session_paths(session_id)
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc)
        ) from exc


def _normalize_filename(filename: str) -> str:
    normalized = os.path.basename(
        filename.strip()
    )

    if not normalized:
        raise HTTPException(
            status_code=400,
            detail="Invalid filename"
        )

    return normalized
