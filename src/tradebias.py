import argparse
import pandas as pd
from bias_detector import analyze_biases


def load_trades(path):
    """Load CSV trades file."""
    print(f"Loading trades from: {path}")
    df = pd.read_csv(path)
    return df


def clean_trades(df):
    """Clean and standardize trades DataFrame."""
    df = df.copy()

    # ensure timestamp is datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

    # ensure pnl is numeric
    df['pnl'] = pd.to_numeric(df['pnl'], errors='coerce')

    # drop rows with missing essential values
    df = df.dropna(subset=['timestamp', 'pair', 'action', 'price', 'pnl'])
    return df


def analyze_trades(df):
    """Produce overall trade statistics and bias counts."""
    results = {}
    results['total_trades'] = len(df)
    results['winning_trades'] = int((df['pnl'] > 0).sum())
    results['losing_trades'] = int((df['pnl'] <= 0).sum())
    results['win_rate'] = round(
        results['winning_trades'] / results['total_trades'] * 100, 2
    ) if results['total_trades'] else 0.0
    results['avg_pnl'] = round(df['pnl'].mean(), 2) if results['total_trades'] else 0.0
    results['total_pnl'] = float(df['pnl'].sum()) if results['total_trades'] else 0.0

    # Count detected biases (from detected_biases column)
    bias_counts = {}
    if 'detected_biases' in df.columns:
        exploded = (
            df['detected_biases']
            .fillna("")
            .astype(str)
            .str.split('|')
            .explode()
            .str.strip()
        )
        exploded = exploded[exploded != ""]
        bias_counts = exploded.value_counts().to_dict()

    results['bias_counts'] = bias_counts
    return results


def save_report(df, output_path, summary):
    """Save processed DataFrame and print summary."""
    df.to_csv(output_path, index=False)
    print(f"Processed file saved at: {output_path}")

    print("\n--- Analysis Summary ---")
    for k, v in summary.items():
        print(f"{k}: {v}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", required=True, help="Path to raw trades CSV")
    parser.add_argument("--output", "-o", required=True, help="Path to save processed CSV")
    args = parser.parse_args()

    # load & clean
    df = load_trades(args.input)
    df = clean_trades(df)

    # run behavioral detector
    df = analyze_biases(df)

    # create a simple bias flag column for CSV
    df['bias_flag'] = df['detected_biases'].apply(lambda s: "Yes" if str(s).strip() else "No")

    # summary
    summary = analyze_trades(df)

    # save
    save_report(df, args.output, summary)


if __name__ == "__main__":
    main()
