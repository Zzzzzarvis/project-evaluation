import os
from typing import Mapping, Tuple

import requests


def get_telegram_config() -> Tuple[str | None, str | None]:
    return os.getenv("TELEGRAM_BOT_TOKEN"), os.getenv("TELEGRAM_CHAT_ID")


def build_alert_message(alert: Mapping[str, object]) -> str:
    return (
        "[监控异动]\n"
        f"Token: {alert.get('token')}\n"
        f"Chain: {alert.get('chain')}\n"
        f"DEX: {alert.get('dex')}\n"
        f"Price Δ: {alert.get('price_change')}\n"
        f"Volume Δ: {alert.get('volume_change')}\n"
        f"Fee Δ: {alert.get('fee_change')}\n"
        f"Reason: {alert.get('reason')}\n"
        f"Source: {alert.get('source')}"
    )


def send_message(text: str, token: str | None = None, chat_id: str | None = None) -> bool:
    token = token or os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": True,
    }
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    return True
