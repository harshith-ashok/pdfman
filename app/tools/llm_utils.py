from __future__ import annotations

import logging
import os
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError


logger = logging.getLogger(__name__)

LLM_TIMEOUT_SECONDS = int(
    os.getenv("PDFMAN_LLM_TIMEOUT_SECONDS", "180")
)
LLM_MAX_RETRIES = int(
    os.getenv("PDFMAN_LLM_MAX_RETRIES", "2")
)


def invoke_with_retry(llm, prompt: str) -> str:
    last_error = None

    for attempt in range(1, LLM_MAX_RETRIES + 1):
        started_at = time.perf_counter()

        try:
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(
                    llm.invoke,
                    prompt
                )
                response = future.result(
                    timeout=LLM_TIMEOUT_SECONDS
                )

            elapsed = time.perf_counter() - started_at
            logger.info(
                "LLM call succeeded on attempt %s in %.2fs",
                attempt,
                elapsed
            )
            return response.content

        except TimeoutError as exc:
            last_error = TimeoutError(
                f"LLM call timed out after {LLM_TIMEOUT_SECONDS}s"
            )
            logger.warning(
                "LLM call timed out on attempt %s",
                attempt
            )
        except Exception as exc:
            last_error = exc
            logger.warning(
                "LLM call failed on attempt %s: %s",
                attempt,
                exc
            )

    raise RuntimeError(
        f"LLM invocation failed after {LLM_MAX_RETRIES} attempts: {last_error}"
    )
