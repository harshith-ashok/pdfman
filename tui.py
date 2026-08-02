from __future__ import annotations

import curses
import json
import mimetypes
import os
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from collections import deque


DEFAULT_BASE_URL = os.getenv(
    "PDFMAN_API_URL",
    "http://127.0.0.1:8000"
)


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get_session(self, session_id: str) -> dict:
        return self._json_request(
            "GET",
            f"/sessions/{urllib.parse.quote(session_id)}"
        )

    def get_job(self, job_id: str) -> dict:
        return self._json_request(
            "GET",
            f"/jobs/{urllib.parse.quote(job_id)}"
        )

    def summarize(
        self,
        session_id: str,
        filenames: list[str]
    ) -> dict:
        return self._json_request(
            "POST",
            "/summarize",
            {
                "session_id": session_id,
                "filenames": filenames
            }
        )

    def mesh_vault(self, session_id: str) -> dict:
        return self._json_request(
            "POST",
            "/mesh-vault",
            {
                "session_id": session_id
            }
        )

    def upload_files(
        self,
        file_paths: list[str],
        session_id: str | None = None
    ) -> dict:
        boundary = f"----pdfman-{uuid.uuid4().hex}"
        body = bytearray()

        if session_id:
            body.extend(
                _multipart_field(
                    boundary,
                    "session_id",
                    session_id
                )
            )

        for file_path in file_paths:
            filename = os.path.basename(file_path)
            mime_type = (
                mimetypes.guess_type(filename)[0]
                or "application/octet-stream"
            )

            with open(file_path, "rb") as handle:
                content = handle.read()

            body.extend(
                _multipart_file(
                    boundary,
                    "files",
                    filename,
                    mime_type,
                    content
                )
            )

        body.extend(f"--{boundary}--\r\n".encode())

        request = urllib.request.Request(
            url=f"{self.base_url}/upload",
            data=bytes(body),
            headers={
                "Content-Type": (
                    f"multipart/form-data; boundary={boundary}"
                ),
                "Content-Length": str(len(body))
            },
            method="POST"
        )

        try:
            with urllib.request.urlopen(request) as response:
                return json.loads(
                    response.read().decode("utf-8")
                )
        except urllib.error.HTTPError as exc:
            raise RuntimeError(
                _extract_http_error(exc)
            ) from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(
                f"Could not reach API at {self.base_url}: {exc.reason}"
            ) from exc

    def _json_request(
        self,
        method: str,
        path: str,
        payload: dict | None = None
    ) -> dict:
        data = None
        headers = {}

        if payload is not None:
            data = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"

        request = urllib.request.Request(
            url=f"{self.base_url}{path}",
            data=data,
            headers=headers,
            method=method
        )

        try:
            with urllib.request.urlopen(request) as response:
                return json.loads(
                    response.read().decode("utf-8")
                )
        except urllib.error.HTTPError as exc:
            raise RuntimeError(
                _extract_http_error(exc)
            ) from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(
                f"Could not reach API at {self.base_url}: {exc.reason}"
            ) from exc


class PdfmanTUI:
    def __init__(self, stdscr, base_url: str):
        self.stdscr = stdscr
        self.client = ApiClient(base_url)
        self.base_url = base_url
        self.session_id: str | None = None
        self.session_info: dict | None = None
        self.active_job: dict | None = None
        self.messages: deque[str] = deque(maxlen=10)
        self.last_refresh = 0.0

    def run(self) -> None:
        curses.curs_set(0)
        self.stdscr.timeout(200)

        while True:
            self._refresh_if_needed()
            self._draw()

            key = self.stdscr.getch()

            if key == -1:
                continue

            if key in (ord("q"), ord("Q")):
                break
            if key in (ord("u"), ord("U")):
                self._upload_flow()
            elif key in (ord("s"), ord("S")):
                self._summarize_flow()
            elif key in (ord("m"), ord("M")):
                self._mesh_flow()
            elif key in (ord("n"), ord("N")):
                self._reset_session()
            elif key in (ord("i"), ord("I")):
                self._attach_session_flow()
            elif key in (ord("r"), ord("R")):
                self._refresh(force=True)

    def _upload_flow(self) -> None:
        raw = self._prompt(
            "Upload paths (comma separated): "
        )

        if not raw:
            return

        file_paths = [
            os.path.expanduser(path.strip())
            for path in raw.split(",")
            if path.strip()
        ]

        missing = [
            path for path in file_paths
            if not os.path.isfile(path)
        ]

        if missing:
            self._message(
                f"Missing files: {', '.join(missing[:3])}"
            )
            return

        try:
            response = self.client.upload_files(
                file_paths=file_paths,
                session_id=self.session_id
            )
            self.session_id = response["session_id"]
            self._message(
                f"Uploaded {len(response['uploaded_files'])} file(s)"
            )
            if response.get("rejected_files"):
                self._message(
                    f"Rejected: {len(response['rejected_files'])}"
                )
            self._refresh(force=True)
        except Exception as exc:
            self._message(str(exc))

    def _summarize_flow(self) -> None:
        if not self.session_info:
            self._message("No active session")
            return

        uploaded_files = self.session_info.get(
            "uploaded_files",
            []
        )

        if not uploaded_files:
            self._message("No uploaded files to summarize")
            return

        try:
            response = self.client.summarize(
                session_id=self.session_id,
                filenames=uploaded_files
            )
            self.active_job = {
                "job_id": response["job_id"],
                "status": response["status"],
                "stage": response["stage"],
                "progress": 0.0
            }
            self._message(
                f"Started job {response['job_id'][:8]}"
            )
            self._refresh(force=True)
        except Exception as exc:
            self._message(str(exc))

    def _mesh_flow(self) -> None:
        if not self.session_id:
            self._message("No active session")
            return

        try:
            response = self.client.mesh_vault(
                self.session_id
            )
            self._message(
                f"Meshed vault: {response['updated_files']} updated"
            )
            self._refresh(force=True)
        except Exception as exc:
            self._message(str(exc))

    def _attach_session_flow(self) -> None:
        session_id = self._prompt(
            "Attach session id: "
        )

        if not session_id:
            return

        self.session_id = session_id.strip()
        self._refresh(force=True)

    def _reset_session(self) -> None:
        self.session_id = None
        self.session_info = None
        self.active_job = None
        self._message("Detached current session")

    def _refresh_if_needed(self) -> None:
        now = time.time()
        job_running = (
            self.active_job
            and self.active_job.get("status")
            in {"queued", "running"}
        )

        if job_running or now - self.last_refresh > 2:
            self._refresh(force=True)

    def _refresh(self, force: bool = False) -> None:
        if not self.session_id:
            self.last_refresh = time.time()
            return

        try:
            self.session_info = self.client.get_session(
                self.session_id
            )

            if self.active_job:
                self.active_job = self.client.get_job(
                    self.active_job["job_id"]
                )
                if self.active_job.get("status") == "completed":
                    self._message(
                        f"Job {self.active_job['job_id'][:8]} completed"
                    )
                elif self.active_job.get("status") == "failed":
                    self._message(
                        f"Job failed: {self.active_job.get('error')}"
                    )
            else:
                jobs = self.session_info.get("jobs", [])
                if jobs:
                    self.active_job = jobs[0]

            self.last_refresh = time.time()
        except Exception as exc:
            self._message(str(exc))
            self.last_refresh = time.time()

    def _draw(self) -> None:
        self.stdscr.erase()
        height, width = self.stdscr.getmaxyx()

        title = " PDFman TUI "
        self.stdscr.addstr(
            0,
            0,
            title.ljust(width - 1),
            curses.A_REVERSE
        )

        session_label = self.session_id or "none"
        self._safe_addstr(
            2,
            2,
            f"Server : {self.base_url}"
        )
        self._safe_addstr(
            3,
            2,
            f"Session: {session_label}"
        )

        status_line = "No active job"
        if self.active_job:
            status_line = (
                f"Job    : {self.active_job.get('job_id', '')[:8]}  "
                f"{self.active_job.get('status', '-')}"
                f" / {self.active_job.get('stage', '-')}"
                f" / {int(float(self.active_job.get('progress', 0)) * 100)}%"
            )
        self._safe_addstr(4, 2, status_line)

        controls = (
            "[U]pload  [S]ummarize  [M]esh  "
            "[I] Attach session  [N] New  [R]efresh  [Q]uit"
        )
        self._safe_addstr(6, 2, controls)

        mid = width // 2
        list_top = 8
        list_height = max(8, height - 18)

        self._draw_box(
            list_top,
            1,
            list_height,
            mid - 2,
            "Uploads"
        )
        self._draw_box(
            list_top,
            mid,
            list_height,
            width - mid - 1,
            "Vault Notes"
        )

        uploads = (
            self.session_info.get("uploaded_files", [])
            if self.session_info else []
        )
        vault_files = (
            self.session_info.get("vault_files", [])
            if self.session_info else []
        )

        self._draw_list(
            list_top + 1,
            3,
            mid - 6,
            list_height - 2,
            uploads
        )
        self._draw_list(
            list_top + 1,
            mid + 2,
            width - mid - 4,
            list_height - 2,
            vault_files
        )

        job_top = list_top + list_height + 1
        job_height = height - job_top - 1
        if job_height >= 6:
            self._draw_box(
                job_top,
                1,
                job_height,
                width - 2,
                "Activity"
            )
            lines = list(self.messages)
            if self.active_job and self.active_job.get("timings"):
                timing_summary = ", ".join(
                    f"{key}={value}s"
                    for key, value in self.active_job["timings"].items()
                )
                lines = lines + [f"Timings: {timing_summary}"]

            self._draw_list(
                job_top + 1,
                3,
                width - 6,
                job_height - 2,
                lines[-(job_height - 2):]
            )

        self.stdscr.refresh()

    def _draw_box(
        self,
        top: int,
        left: int,
        height: int,
        width: int,
        title: str
    ) -> None:
        if height < 3 or width < 4:
            return

        self.stdscr.addstr(top, left, "+" + "-" * (width - 2) + "+")
        for row in range(top + 1, top + height - 1):
            self.stdscr.addstr(row, left, "|")
            self.stdscr.addstr(row, left + width - 1, "|")
        self.stdscr.addstr(
            top + height - 1,
            left,
            "+" + "-" * (width - 2) + "+"
        )

        label = f" {title} "
        self._safe_addstr(top, left + 2, label)

    def _draw_list(
        self,
        top: int,
        left: int,
        width: int,
        height: int,
        items: list[str]
    ) -> None:
        for index in range(height):
            row = top + index
            if index >= len(items):
                self._safe_addstr(row, left, " " * max(0, width))
                continue

            item = textwrap.shorten(
                str(items[index]),
                width=max(10, width),
                placeholder="..."
            )
            self._safe_addstr(
                row,
                left,
                item.ljust(width)
            )

    def _prompt(self, label: str) -> str:
        height, width = self.stdscr.getmaxyx()
        row = height - 1
        self.stdscr.move(row, 0)
        self.stdscr.clrtoeol()
        self._safe_addstr(row, 0, label)
        curses.echo()
        curses.curs_set(1)
        self.stdscr.refresh()
        try:
            value = self.stdscr.getstr(
                row,
                len(label),
                max(1, width - len(label) - 1)
            )
            return value.decode("utf-8").strip()
        finally:
            curses.noecho()
            curses.curs_set(0)

    def _message(self, text: str) -> None:
        timestamp = time.strftime("%H:%M:%S")
        self.messages.append(
            f"[{timestamp}] {text}"
        )

    def _safe_addstr(
        self,
        row: int,
        col: int,
        text: str,
        attr: int = 0
    ) -> None:
        height, width = self.stdscr.getmaxyx()
        if row < 0 or row >= height or col >= width:
            return

        clipped = text[: max(0, width - col - 1)]
        try:
            self.stdscr.addstr(row, col, clipped, attr)
        except curses.error:
            pass


def _multipart_field(
    boundary: str,
    name: str,
    value: str
) -> bytes:
    return (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="{name}"\r\n\r\n'
        f"{value}\r\n"
    ).encode("utf-8")


def _multipart_file(
    boundary: str,
    field_name: str,
    filename: str,
    mime_type: str,
    content: bytes
) -> bytes:
    header = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="{field_name}"; '
        f'filename="{filename}"\r\n'
        f"Content-Type: {mime_type}\r\n\r\n"
    ).encode("utf-8")
    return header + content + b"\r\n"


def _extract_http_error(exc: urllib.error.HTTPError) -> str:
    try:
        payload = json.loads(
            exc.read().decode("utf-8")
        )
        if "detail" in payload:
            return str(payload["detail"])
        return json.dumps(payload)
    except Exception:
        return f"HTTP {exc.code}"


def main() -> None:
    curses.wrapper(
        lambda stdscr: PdfmanTUI(
            stdscr,
            DEFAULT_BASE_URL
        ).run()
    )


if __name__ == "__main__":
    main()
