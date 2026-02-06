# Risk management & kill switch
MAX_DAILY_LOSS = -50

def check_risk(daily_pnl):
    if daily_pnl <= MAX_DAILY_LOSS:
        raise Exception("Daily loss limit reached. Trading halted.")
