from __future__ import annotations

import time
from typing import Any, Dict, Optional

import requests


RETRY_STATUS = {429, 500, 502, 503, 504}


def request_json(
    url: str,
    method: str = "GET",
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    timeout: int = 10,
) -> Dict[str, Any]:
    if not url:
        raise ValueError("url is required")

    attempts = 2
    for attempt in range(attempts):
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json_body,
            timeout=timeout,
        )
        if response.status_code in RETRY_STATUS and attempt < attempts - 1:
            time.sleep(0.5)
            continue
        response.raise_for_status()
        return response.json()

    raise RuntimeError("request failed after retries")
