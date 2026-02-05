# DEX Listing Evaluator (Codex App) — Design v1

## Summary
Build a Codex-app-native, multi-agent evaluation system for DEX listing decisions with professional external research reports and a separate internal decision file. No external AI API usage; public data sources allowed. A decoupled liquidity-pool anomaly monitor runs every 6 hours and produces alerts (TG integration deferred).

## Goals
- Produce a professional Chinese research report suitable for leadership.
- Keep internal scoring/decision discussion in a separate file.
- Support three input modes (project folder, paste text, address+links).
- Operate fully inside Codex app without external AI APIs.
- Allow future upgrade to paid data APIs via adapters.

## Non‑Goals
- Full automation of final decision (human-in-the-loop required).
- Mandatory TG notifications in v1.

## Core Components
- **Master Orchestrator**: `dex_project_evaluator` (reads inputs, dispatches agents, handles pause points, writes outputs).
- **7 Expert Agents**
  - Contract/Security
  - Liquidity & Pool Structure (includes Tokenomics)
  - Market & Competition (includes Compliance/Regulatory)
  - Community & Growth
  - Team Background
  - Product & Tech Maturity
  - On‑chain Behavior & Funds Flow
- **Coordinator**: `dex_coordinator` (conflict detection, 2nd-round responses, report draft).
- **Outputs**
  - `report.md` (external research report, no scores/decision)
  - `report.pdf` (external report PDF)
  - `decision_notes.md` (internal notes: scores, rating, conflicts, decision)
- **Monitor**: liquidity-pool anomaly watcher (6h polling, alert log file; TG placeholder).

## External Research Report (report.md)
Structure and tone (all Chinese):
1. Executive summary (positioning, key strengths, key risks)
2. Project overview (contract, chain, product, user flow)
3. Evidence & verification (all claims with sources)
4. 7‑dimension deep analysis (facts, evidence, risks, trend judgment)
5. Liquidity & profit potential (volume, depth, fee potential, sustainability assumptions)
6. Risk list (tech, compliance, funds, sentiment, competition)
7. Conclusion (no pass/reject, no AI‑style language)

**Rule**: Every key assertion must include source links. Avoid “model says/AI thinks”.

## Internal Decision File (decision_notes.md)
1. Quick decision suggestion (Pass / Conditional / Reject) + confidence
2. 7‑dimension scores + total (reference only)
3. Conflicts/uncertainties and missing evidence
4. Profitability summary (fee potential, liquidity quality, growth)
5. Human notes section (manual override space)

## Input Handling
- **Supported inputs**: project folder, pasted text, or address+website+X link.
- **Gate**: If required materials are missing, pause and request completion before evaluation.

## Data Sources & Adapters
- Use public APIs and scrapers.
- Normalize to a common data schema (token info, liquidity, volume, holders, pools, social signals).
- If a source fails: record missing, continue; if all sources for a dimension fail, disclose evidence gap in report.

## Liquidity‑Pool Monitor
- **Frequency**: every 6 hours.
- **Chains**: Ethereum, BNB Chain, Arbitrum, Optimism, Base, Polygon, Solana, Avalanche, Aptos, Sui.
- **DEX list**: Uniswap, Curve, Balancer, PancakeSwap, BiSwap, GMX, Camelot, Velodrome, Aerodrome, QuickSwap, Orca, Raydium, Phoenix, Trader Joe, Liquidswap, Cetus, Turbos.
- **Trigger**: price‑volume‑fee linkage; relative thresholds based on 7‑day baseline; new tokens use 3‑day baseline.
- **Output**: `monitor_alerts.md` entries with token, chain, DEX, 24h fee/volume/price deltas, trigger reason, source links.
- **Notification**: TG integration deferred (placeholder).

## Error Handling & Downgrade
- Missing required input → pause and request.
- Single source failure → log and continue.
- All sources for a dimension fail → mark “evidence gap” in report + internal notes.
- Monitor API failure → log, no alert.

## Acceptance Criteria
- All three input modes start evaluation.
- Missing required data triggers pause.
- 7 agents output standardized sections.
- `report.md` contains no scores/decision.
- `decision_notes.md` contains scores/decision/conflicts.
- Report includes source links for key assertions.
- PDF renders cleanly.
- Monitor writes alerts for simulated anomalies.

## Human‑in‑the‑Loop Checkpoints
- After coordinator debate, before final report generation.
- User confirms to proceed with final report/PDF.
