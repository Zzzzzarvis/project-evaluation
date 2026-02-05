from scripts.data_sources.aggregator import merge_sources
from scripts.data_sources.schema import TokenSnapshot


def test_merge_sources_prefers_non_null():
    a = TokenSnapshot(symbol="T", price_usd=1.0)
    b = TokenSnapshot(symbol="T", price_usd=None, volume_24h=10.0)
    c = merge_sources([a, b])
    assert c.price_usd == 1.0
    assert c.volume_24h == 10.0
