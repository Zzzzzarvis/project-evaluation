from __future__ import annotations

from typing import Any, Dict, List

from scripts.data_sources.http_client import request_json


BASE_URL = "https://api.nansen.ai"


def build_token_screener_payload(chains: List[str], date_from: str, date_to: str) -> Dict[str, Any]:
    return {
        "parameters": {
            "chains": chains,
            "date_range": {
                "from": date_from,
                "to": date_to,
            },
        }
    }


def token_screener(api_key: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    headers = {"api-key": api_key}
    url = f"{BASE_URL}/token-screener"
    return request_json(url, method="POST", headers=headers, json_body=payload)
