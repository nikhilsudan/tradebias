# src/generate_synthetic.py
# Usage:
#   python3 src/generate_synthetic.py --n 1200 --out data/raw/synthetic_trades.csv

import argparse
import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from pathlib import Path

PAIRS = [
    "EUR/USD","GBP/USD","USD/JPY","EUR/GBP","GBP/JPY","AUD/USD","NZD/USD",
    "USD/CAD","EUR/JPY","USD/CHF","EUR/AUD","GBP/AUD","EUR/CAD","USD/SGD",
    "EUR/NZD","GBP/NZD","USD/MXN","AUD/JPY","NZD/JPY"
]

def random_price(base, vol=0.002):
    """Return price around base with a small random move (vol is fraction)."""
    # for JPY pairs base might be large; vol interpreted as absolute scale for USD pairs
    noise = np.random.normal(loc=0.0, scale=vol)
    return round(base * (1 + noise), 5)

def base_price_for(pair):
    """Simple approximate base price for each pair for plausible simulation."""
    if "USD/JPY" in pair or pair.endswith("/JPY"):
        return 145.00
    mapping = {
        "EUR/USD": 1.09, "GBP/USD": 1.27, "AUD/USD": 0.67, "NZD/USD": 0.63,
        "USD/CAD": 1.34, "USD/CHF": 0.88, "EUR/GBP": 0.86, "EUR/JPY": 158.0,
        "GBP/JPY": 183.5, "EUR/AUD": 1.61, "GBP/AUD": 1.91, "EUR/CAD": 1.46,
        "USD/SGD": 1.35, "EUR/NZD": 1.74, "GBP/NZD": 2.03, "USD/MXN": 17.8,
        "AUD/JPY": 95.2, "NZD/JPY": 88.1
    }
    return mapping.get(pair, 1.20)

def generate(n=1200, out_path="data/raw/synthetic_trades.csv", seed=42):
    random.seed(seed)
    np.random.seed(seed)

    rows = []
    start_dt = datetime(2024, 1, 1, 8, 0)  # start date/time
    cur_dt = start_dt
    prev_pnl = 0.0

    for i in range(n):
        # advance time by 0-2 days and random minutes so timestamps are non-uniform
        cur_dt += timedelta(days=random.choices([0,0,1,1,2], weights=[50,30,15,4,1])[0],
                            minutes=random.randint(5, 720))
        pair = random.choice(PAIRS)
        base = base_price_for(pair)
        entry = random_price(base, vol=0.003)
        # Simulate direction and small move
        direction = random.choice(["Buy", "Sell"])
        # make exit move correlated to a bit of noise
        # bigger moves sometimes
        move = np.random.normal(loc=0.0, scale=0.0015)
        # occasionally make larger moves
        if random.random() < 0.05:
            move += np.random.normal(loc=0.0, scale=0.01)
        exit_price = round(entry * (1 + move if "JPY" not in pair else 1 + move), 5)

        # compute pips
        pip_factor = 100 if pair.endswith("/JPY") else 10000
        pips = round((exit_price - entry) * pip_factor)
        # convert pips to USD-like PnL: assume $10 per pip per lot
        size = round(random.choice([0.1,0.2,0.5,1.0,1.5,2.0]), 2)
        pnl = round(pips * size * 10, 2)

        # Notes injection (behavioral patterns)
        note = ""
        # If previous was big win, small chance of FOMO next
        if prev_pnl > 500 and random.random() < 0.15:
            note = random.choice(["FOMO trade", "Chased breakout, FOMO"])
        # If previous was a loss, chance of revenge
        elif prev_pnl < -200 and random.random() < 0.18:
            note = random.choice(["Revenge trade after loss", "Entered to recover loss"])
        # random chance for overtrading/emotional
        elif random.random() < 0.03:
            note = random.choice(["Overtrading mistake", "Emotional trade, panic"])
        # forced/no-signal small chance
        elif random.random() < 0.02:
            note = "Forced trade, no signal"
        # sometimes short descriptive notes
        elif random.random() < 0.15:
            note = random.choice(["Good risk/reward", "Followed trading plan", "News-driven entry", "Technical setup"])

        # store row: timestamp,pair,action,size,price,pnl,notes
        rows.append({
            "timestamp": cur_dt.strftime("%Y-%m-%d %H:%M"),
            "pair": pair,
            "action": direction,
            "size": size,
            "price": entry,
            "pnl": pnl,
            "notes": note
        })

        prev_pnl = pnl

    df = pd.DataFrame(rows, columns=["timestamp","pair","action","size","price","pnl","notes"])
    outp = Path(out_path)
    outp.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(outp, index=False)
    print(f"✅ Generated {len(df)} synthetic trades -> {outp.resolve()}")
    print(df.head().to_string(index=False))
    print("...done.")
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=1200, help="Number of trades to generate")
    parser.add_argument("--out", type=str, default="data/raw/synthetic_trades.csv", help="Output CSV path")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    args = parser.parse_args()
    generate(n=args.n, out_path=args.out, seed=args.seed)
