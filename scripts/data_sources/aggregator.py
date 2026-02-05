from __future__ import annotations

import os
from typing import Iterable, List

from scripts.data_sources.schema import TokenSnapshot


FIELDS = [
    "symbol",
    "name",
    "price_usd",
    "market_cap",
    "volume_24h",
    "liquidity_usd",
    "holders",
    "holder_distribution_note",
]


def merge_sources(snapshots: Iterable[TokenSnapshot]) -> TokenSnapshot:
    snapshots = list(snapshots)
    if not snapshots:
        raise ValueError("snapshots required")

    base = TokenSnapshot(symbol=snapshots[0].symbol)
    sources: List[str] = []

    for snap in snapshots:
        sources.extend(snap.sources)
        for field in FIELDS:
            value = getattr(snap, field)
            if value is not None:
                setattr(base, field, value)

    base.sources = sorted(set(sources))
    return base


def collect_snapshot(contract: str, chain: str) -> TokenSnapshot:
    sources = []
    if os.getenv("NANSEN_API_KEY"):
        sources.append("nansen")
    if os.getenv("DUNE_API_KEY"):
        sources.append("dune")
    if os.getenv("COINMARKETCAP_API_KEY"):
        sources.append("coinmarketcap")
    if os.getenv("COINGECKO_API_KEY"):
        sources.append("coingecko")

    return TokenSnapshot(symbol=contract, name=chain, sources=sources)
