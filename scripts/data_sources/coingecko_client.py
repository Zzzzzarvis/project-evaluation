from __future__ import annotations

from typing import Any, Dict, List

from scripts.data_sources.http_client import request_json


BASE_URL = "https://api.coingecko.com"


def build_headers(api_key: str) -> Dict[str, str]:
    return {"x-cg-pro-api-key": api_key}


def simple_price(ids: List[str], vs_currencies: List[str], api_key: str | None = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/api/v3/simple/price"
    params = {"ids": ",".join(ids), "vs_currencies": ",".join(vs_currencies)}
    headers = build_headers(api_key) if api_key else None
    return request_json(url, headers=headers, params=params)


def token_price(network: str, addresses: List[str], api_key: str | None = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/api/v3/simple/token_price/{network}"
    params = {"contract_addresses": ",".join(addresses), "vs_currencies": "usd"}
    headers = build_headers(api_key) if api_key else None
    return request_json(url, headers=headers, params=params)


def onchain_pool(network: str, address: str, api_key: str | None = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/api/v3/onchain/networks/{network}/pools/{address}"
    headers = build_headers(api_key) if api_key else None
    return request_json(url, headers=headers)
