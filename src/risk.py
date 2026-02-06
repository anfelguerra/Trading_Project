"""
Gestión de riesgo por operación
"""

from config import CAPITAL_INICIAL, RIESGO_POR_TRADE

def calculate_position_size(price: float, stop_loss: float):
    riesgo_total = CAPITAL_INICIAL * RIESGO_POR_TRADE
    riesgo_por_accion = abs(price - stop_loss)

    if riesgo_por_accion == 0:
        return 0

    return int(riesgo_total / riesgo_por_accion)
