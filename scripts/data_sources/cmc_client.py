from __future__ import annotations

from typing import Any, Dict, Optional

from scripts.data_sources.http_client import request_json


BASE_URL = "https://pro-api.coinmarketcap.com"


def build_headers(api_key: str) -> Dict[str, str]:
    return {"X-CMC_PRO_API_KEY": api_key}


def quotes_latest(api_key: str, symbols: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/v1/cryptocurrency/quotes/latest"
    params = {"symbol": symbols}
    return request_json(url, headers=build_headers(api_key), params=params)


def dex_spot_pairs_latest(api_key: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/v4/dex/spot-pairs/latest"
    return request_json(url, headers=build_headers(api_key), params=params)


def dex_pairs_quotes_latest(api_key: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/v4/dex/pairs/quotes/latest"
    return request_json(url, headers=build_headers(api_key), params=params)
