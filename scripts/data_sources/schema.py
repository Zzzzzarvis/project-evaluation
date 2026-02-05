from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class TokenSnapshot:
    symbol: str
    name: Optional[str] = None
    price_usd: Optional[float] = None
    market_cap: Optional[float] = None
    volume_24h: Optional[float] = None
    liquidity_usd: Optional[float] = None
    holders: Optional[int] = None
    holder_distribution_note: Optional[str] = None
    sources: List[str] = field(default_factory=list)
