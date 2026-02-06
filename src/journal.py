"""
Journal automático de operaciones
"""

import csv
from datetime import datetime

def log_trade(symbol, signal, price, quantity):
    with open("journal.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            symbol,
            signal,
            price,
            quantity
        ])
