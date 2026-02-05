from typing import Mapping


def is_anomalous(data: Mapping[str, float], baseline_multiplier: float) -> bool:
    price_change = float(data.get("price_change", 0.0))
    volume_change = float(data.get("volume_change", 0.0))
    fee_change = float(data.get("fee_change", 0.0))

    return (
        price_change >= 0.0
        and volume_change >= baseline_multiplier
        and fee_change >= baseline_multiplier
        and price_change >= 0.2
    )
