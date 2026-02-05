from scripts.data_sources.cmc_client import build_headers


def test_cmc_header():
    headers = build_headers("key")
    assert headers["X-CMC_PRO_API_KEY"] == "key"
