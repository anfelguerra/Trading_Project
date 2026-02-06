# Interactive Brokers (Paper Trading) connector skeleton
from ib_insync import *

def connect_ib(host='127.0.0.1', port=7497, client_id=1):
    ib = IB()
    ib.connect(host, port, clientId=client_id)
    return ib
