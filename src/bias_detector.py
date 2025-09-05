import pandas as pd


def detect_bias(row):
    """Check notes & trade context for psychological trading biases."""
    notes = str(row.get("notes", "")).lower()
    pnl = row.get("pnl", 0)

    biases = []

    # --- simple keyword rules ---
    if "fomo" in notes or "chasing" in notes:
        biases.append("FOMO trade detected")

    if "revenge" in notes or ("loss" in notes and pnl < 0):
        biases.append("Revenge trading detected")

    if "overtrading" in notes or "too many" in notes:
        biases.append("Overtrading detected")

    if "emotional" in notes or "panic" in notes or "fear" in notes:
        biases.append("Emotional trading detected")

    if "forced" in notes or "no signal" in notes:
        biases.append("Forced trade detected")

    return biases


def analyze_biases(df):
    """Apply bias detection across the DataFrame."""
    df = df.copy()

    # detect biases row by row
    df["detected_biases"] = df.apply(lambda row: "|".join(detect_bias(row)), axis=1)

    return df

