from scripts.telegram_notify import build_alert_message


def test_build_alert_message():
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
    text = build_alert_message(alert)
    assert "TEST" in text
    assert "Ethereum" in text
    assert "Uniswap" in text
    assert "price-volume-fee" in text
