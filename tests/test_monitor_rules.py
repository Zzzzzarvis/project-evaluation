from scripts.monitor_rules import is_anomalous


def test_anomaly_rule_detects_spike():
    sample = {
        "price_change": 0.35,
        "volume_change": 3.0,
        "fee_change": 3.5,
    }
    assert is_anomalous(sample, baseline_multiplier=2.0)
