from scripts.data_sources.coingecko_client import build_headers


def test_cg_header():
    headers = build_headers("key")
    assert headers["x-cg-pro-api-key"] == "key"
