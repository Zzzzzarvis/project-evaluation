from pathlib import Path
from datetime import datetime
from typing import Mapping

from scripts.telegram_notify import build_alert_message, send_message


def write_alert(path: Path, alert: Mapping[str, object]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
    entry = [
        f"## {alert.get('token')} ({alert.get('chain')} / {alert.get('dex')})",
        f"- time: {timestamp}",
        f"- price_change: {alert.get('price_change')}",
        f"- volume_change: {alert.get('volume_change')}",
        f"- fee_change: {alert.get('fee_change')}",
        f"- reason: {alert.get('reason')}",
        f"- source: {alert.get('source')}",
        "",
    ]

    with path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(entry))


def notify_alert(alert: Mapping[str, object]) -> bool:
    text = build_alert_message(alert)
    return send_message(text)
