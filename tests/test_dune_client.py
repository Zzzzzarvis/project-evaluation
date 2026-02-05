from scripts.data_sources.dune_client import build_auth_headers


def test_dune_header():
    headers = build_auth_headers("test")
    assert headers["X-DUNE-API-KEY"] == "test"
