"""
Estrategia conservadora basada en medias móviles
"""

import pandas as pd

def generate_signal(data: pd.DataFrame):
    if len(data) < 50:
        return None

    data["ma20"] = data["close"].rolling(20).mean()
    data["ma50"] = data["close"].rolling(50).mean()

    last = data.iloc[-1]
    prev = data.iloc[-2]

    if prev["ma20"] < prev["ma50"] and last["ma20"] > last["ma50"]:
        return "BUY"

    if prev["ma20"] > prev["ma50"] and last["ma20"] < last["ma50"]:
        return "SELL"

    return None
