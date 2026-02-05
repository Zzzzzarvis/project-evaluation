from scripts.data_sources.nansen_client import build_token_screener_payload


def test_nansen_payload_chains():
    payload = build_token_screener_payload(["ethereum"], "2025-01-01", "2025-01-03")
    assert payload["parameters"]["chains"] == ["ethereum"]
