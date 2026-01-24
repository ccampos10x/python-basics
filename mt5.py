import MetaTrader5 as mt5
import time

# Conectar ao MT5
if not mt5.initialize():
    print("Falha na inicialização")
    mt5.shutdown()

# Obter dados de um ativo
try:
    while True:
        # USDJPY
        symbol = "USDJPY"
        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M2, 0, 1)
        print (symbol , rates)
        time.sleep(1)  # pausa obrigatória
except KeyboardInterrupt:
    print("Encerrado pelo usuário")

# Desconectar
#mt5.shutdown()

