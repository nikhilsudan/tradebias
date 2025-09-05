# TradeBias 🧠📈

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**TradeBias** is a lightweight behavioral analytics tool for traders.  
It processes CSV trade logs to detect common psychological trading biases (FOMO, revenge trading, overtrading, emotional entries), produces summary statistics, and creates visual reports to help improve trading discipline.

---

## Key Features
- Detects common trading biases from CSV trade logs
- Generates synthetic trade data for testing and demos
- Produces summary statistics: win rate, total PnL, average PnL, bias counts
- Exports a processed CSV report
- Simple visualizations (bias distribution, PnL histograms)
- Modular codebase for easy extension (e.g., connect to trading platforms later)

---

## Quick start (local)
1. Create & activate a Python venv (recommended)
```bash
python3 -m venv venv
source venv/bin/activate      # macOS / Linux
# or: venv\Scripts\activate    # Windows (PowerShell)
