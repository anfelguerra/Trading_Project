"""
Bot principal (paper trading)
"""

from strategy import generate_signal
from risk import calculate_position_size
from journal import log_trade
from config import SYMBOL

def run_bot(data):
    signal = generate_signal(data)
    if not signal:
        return

    price = data.iloc[-1]["close"]
    stop_loss = price * 0.98
    qty = calculate_position_size(price, stop_loss)

    if qty <= 0:
        return

    log_trade(SYMBOL, signal, price, qty)
    print(f"{signal} {qty} {SYMBOL} @ {price}")
