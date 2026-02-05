# DEX Project Evaluator Runbook

## Purpose
Run the DEX listing evaluation system inside Codex app with professional external reports and internal decision notes.

## Prerequisites
- Codex app installed and opened at the project root.
- Skills installed to `~/.codex/skills/`.
- API keys set in `~/.codex/skills/.env` (do NOT commit keys to git).

## Required Environment Variables
Create `~/.codex/skills/.env` and set:
```
NANSEN_API_KEY=...
DUNE_API_KEY=...
COINMARKETCAP_API_KEY=...
COINGECKO_API_KEY=...
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
```

## Data Sources (必须使用)
- Nansen: 资金流与持币分布
- Dune: 自建查询 + 手动面板（见 `docs/dune_dashboard_steps.md`）
- CoinMarketCap: 市值/报价/DEX 数据
- CoinGecko: 价格/池子/链上接口

## Input Options
1. Project folder with `contract.txt`, `website_url.txt`, `twitter_url.txt` plus any PDFs/images.
2. Paste content directly into Codex app.
3. Provide contract address + official website + X link.

## How to Run
1. Open Codex app in this repo.
2. Place project materials in a folder.
3. Run the master skill:
   - Command: `/dex_project_evaluator`
4. Wait for expert outputs, coordinator debate, and draft report.
5. Human-in-the-loop pause: confirm to proceed.

## Outputs
- `report.md` (external research report)
- `report.pdf` (external report PDF)
- `decision_notes.md` (internal decision notes)
- Optional: `monitor_alerts.md` (pool anomaly alerts log)

## Monitoring (Optional)
- Run monitor script periodically (6 hours):
```
python scripts/monitor_pools.py
```
- Alerts are appended to `monitor_alerts.md` and sent to Telegram if env vars are set.

## Evaluation Summary Notification (Optional)
- After evaluation completes, run:
```
python scripts/notify_report.py
```
- This sends a brief summary plus internal decision highlights to Telegram.

## Security Notes
- Never paste API keys into chat.
- Never commit `.env` files to git.
- Rotate keys if ever exposed.
