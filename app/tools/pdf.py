import os
import subprocess
import tempfile
import logging
import time

import fitz

logger = logging.getLogger(__name__)

OCR_LANGUAGE = "eng"
MIN_TEXT_LENGTH = 20
OCR_DPI = 220
MIN_PAGE_DIMENSION = 40
OCR_TIMEOUT_SECONDS = int(
    os.getenv("PDFMAN_OCR_TIMEOUT_SECONDS", "60")
)
OCR_MAX_RETRIES = int(
    os.getenv("PDFMAN_OCR_MAX_RETRIES", "2")
)
TESSERACT_BINARY = os.getenv(
    "PDFMAN_TESSERACT_BIN",
    "tesseract"
)


def parse_document(file_path: str) -> str:
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".md":
        return _parse_markdown(file_path)

    return parse_pdf(file_path)


def parse_pdf(file_path: str) -> str:
    started_at = time.perf_counter()
    doc = fitz.open(file_path)
    text = []

    for page in doc:
        page_text = page.get_text().strip()

        if len(page_text) >= MIN_TEXT_LENGTH:
            text.append(page_text)
            continue

        ocr_text = _extract_page_text_with_ocr(page)

        if ocr_text:
            text.append(ocr_text)
        else:
            text.append(page_text)

    doc.close()
    logger.info(
        "Parsed PDF %s in %.2fs",
        file_path,
        time.perf_counter() - started_at
    )
    return "\n".join(text)


def _parse_markdown(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def _extract_page_text_with_ocr(page: fitz.Page) -> str:
    pixmap = page.get_pixmap(dpi=OCR_DPI, alpha=False)

    if pixmap.width < MIN_PAGE_DIMENSION or pixmap.height < MIN_PAGE_DIMENSION:
        return ""

    image_bytes = pixmap.tobytes("png")

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_image:
        temp_image.write(image_bytes)
        image_path = temp_image.name

    try:
        for attempt in range(1, OCR_MAX_RETRIES + 1):
            try:
                result = subprocess.run(
                    [
                        TESSERACT_BINARY,
                        image_path,
                        "stdout",
                        "-l",
                        OCR_LANGUAGE
                    ],
                    capture_output=True,
                    text=True,
                    check=False,
                    timeout=OCR_TIMEOUT_SECONDS
                )

                if result.returncode != 0:
                    stderr = result.stderr.strip()
                    if stderr:
                        logger.warning(
                            "OCR failed on page %s attempt %s: %s",
                            page.number + 1,
                            attempt,
                            stderr
                        )
                    continue

                return result.stdout.strip()

            except subprocess.TimeoutExpired:
                logger.warning(
                    "OCR timed out on page %s attempt %s after %ss",
                    page.number + 1,
                    attempt,
                    OCR_TIMEOUT_SECONDS
                )

        return ""

    except FileNotFoundError:
        logger.warning(
            "OCR skipped because the tesseract binary was not found."
        )
        return ""

    finally:
        try:
            os.remove(image_path)
        except FileNotFoundError:
            pass
