from __future__ import annotations

import json
import os
import uuid
from datetime import datetime, timezone


APP_DIR = os.path.dirname(
    os.path.dirname(__file__)
)
DATA_DIR = os.path.join(APP_DIR, "data")
SESSIONS_DIR = os.path.join(DATA_DIR, "sessions")
JOBS_DIR = os.path.join(DATA_DIR, "jobs")


def ensure_runtime_dirs() -> None:
    os.makedirs(SESSIONS_DIR, exist_ok=True)
    os.makedirs(JOBS_DIR, exist_ok=True)


def create_session() -> dict[str, str]:
    ensure_runtime_dirs()

    session_id = uuid.uuid4().hex
    session_root = os.path.join(
        SESSIONS_DIR,
        session_id
    )
    uploads_dir = os.path.join(session_root, "uploads")
    vault_dir = os.path.join(session_root, "vault")

    os.makedirs(uploads_dir, exist_ok=True)
    os.makedirs(vault_dir, exist_ok=True)

    return {
        "session_id": session_id,
        "session_root": session_root,
        "uploads_dir": uploads_dir,
        "vault_dir": vault_dir
    }


def get_session_paths(session_id: str) -> dict[str, str]:
    session_root = os.path.join(
        SESSIONS_DIR,
        session_id
    )

    if not os.path.isdir(session_root):
        raise FileNotFoundError(
            f"Session {session_id} not found"
        )

    return {
        "session_id": session_id,
        "session_root": session_root,
        "uploads_dir": os.path.join(session_root, "uploads"),
        "vault_dir": os.path.join(session_root, "vault")
    }


def create_job(
    session_id: str,
    filenames: list[str]
) -> dict[str, object]:
    ensure_runtime_dirs()

    job_id = uuid.uuid4().hex
    now = _utc_now()
    payload = {
        "job_id": job_id,
        "session_id": session_id,
        "status": "queued",
        "stage": "uploaded",
        "progress": 0.0,
        "current_file": None,
        "completed_files": 0,
        "total_files": len(filenames),
        "filenames": filenames,
        "results": [],
        "error": None,
        "timings": {},
        "created_at": now,
        "updated_at": now
    }

    _write_job(payload)
    return payload


def read_job(job_id: str) -> dict[str, object]:
    path = _job_path(job_id)

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Job {job_id} not found"
        )

    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def update_job(
    job_id: str,
    **updates: object
) -> dict[str, object]:
    payload = read_job(job_id)
    payload.update(updates)
    payload["updated_at"] = _utc_now()
    _write_job(payload)
    return payload


def append_job_result(
    job_id: str,
    result: dict[str, object]
) -> dict[str, object]:
    payload = read_job(job_id)
    payload["results"].append(result)
    payload["completed_files"] = len(
        payload["results"]
    )
    payload["updated_at"] = _utc_now()
    _write_job(payload)
    return payload


def record_job_timing(
    job_id: str,
    key: str,
    seconds: float
) -> dict[str, object]:
    payload = read_job(job_id)
    payload["timings"][key] = round(seconds, 3)
    payload["updated_at"] = _utc_now()
    _write_job(payload)
    return payload


def fail_job(
    job_id: str,
    error: str
) -> dict[str, object]:
    return update_job(
        job_id,
        status="failed",
        error=error
    )


def complete_job(job_id: str) -> dict[str, object]:
    return update_job(
        job_id,
        status="completed",
        stage="completed",
        progress=1.0
    )


def _job_path(job_id: str) -> str:
    return os.path.join(
        JOBS_DIR,
        f"{job_id}.json"
    )


def _write_job(payload: dict[str, object]) -> None:
    path = _job_path(payload["job_id"])
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(
            payload,
            handle,
            indent=2
        )


def _utc_now() -> str:
    return datetime.now(
        timezone.utc
    ).isoformat()
