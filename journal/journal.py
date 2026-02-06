import csv
from datetime import datetime

def log_trade(symbol, side, qty, price, pnl):
    with open('journal/trades.csv','a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(),symbol,side,qty,price,pnl])
