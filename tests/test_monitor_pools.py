from pathlib import Path
from scripts.monitor_pools import write_alert


def test_write_alert(tmp_path):
    alert = {
        "token": "TEST",
        "chain": "Ethereum",
        "dex": "Uniswap",
        "price_change": 0.25,
        "volume_change": 2.5,
        "fee_change": 2.8,
        "reason": "price-volume-fee spike",
        "source": "https://example.com",
    }
    out = tmp_path / "monitor_alerts.md"
    write_alert(out, alert)
    assert out.exists() and "TEST" in out.read_text()
