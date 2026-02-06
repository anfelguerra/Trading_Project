# Simple backtester framework
import pandas as pd

def run_backtest(data: pd.DataFrame, strategy_fn):
    results = []
    for i in range(len(data)):
        signal = strategy_fn(data.iloc[:i+1])
        results.append(signal)
    return results
