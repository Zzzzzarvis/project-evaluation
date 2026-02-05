from scripts.data_sources.schema import TokenSnapshot


def test_token_snapshot_defaults():
    s = TokenSnapshot(symbol="TEST")
    assert s.symbol == "TEST"
