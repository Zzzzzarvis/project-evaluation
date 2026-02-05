from __future__ import annotations

from typing import Any, Dict, Optional

from scripts.data_sources.http_client import request_json


BASE_URL = "https://api.dune.com"


def build_auth_headers(api_key: str) -> Dict[str, str]:
    return {"X-DUNE-API-KEY": api_key}


def create_query(api_key: str, name: str, query_sql: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/api/v1/query"
    body = {"name": name, "query_sql": query_sql}
    return request_json(url, method="POST", headers=build_auth_headers(api_key), json_body=body)


def update_query(api_key: str, query_id: int, query_sql: str, name: Optional[str] = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/api/v1/query/{query_id}"
    body: Dict[str, Any] = {"query_sql": query_sql}
    if name:
        body["name"] = name
    return request_json(url, method="PATCH", headers=build_auth_headers(api_key), json_body=body)


def execute_query(api_key: str, query_id: int, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/api/v1/query/{query_id}/execute"
    body: Dict[str, Any] = {}
    if parameters:
        body["parameters"] = parameters
    return request_json(url, method="POST", headers=build_auth_headers(api_key), json_body=body)
