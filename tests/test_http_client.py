from scripts.data_sources.http_client import request_json


def test_request_json_requires_url():
    try:
        request_json("")
        assert False, "expected ValueError"
    except ValueError:
        assert True

import responses
from scripts.data_sources.http_client import request_json


@responses.activate
def test_request_json_success():
    responses.add(
        responses.GET,
        "https://example.com",
        json={"ok": True},
        status=200,
    )
    data = request_json("https://example.com")
    assert data["ok"] is True
