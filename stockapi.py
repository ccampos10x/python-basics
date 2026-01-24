import MetaTrader5 as mt5
import time

# Conectar ao MT5
if not mt5.initialize():
    print("Falha na inicialização")
    mt5.shutdown()

# Obter dados de um ativo

# USDJPY
symbol = "USDJPY"
rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H1, 0, 99999)
print (symbol , rates)

if rates is None:
    print("Erro:", mt5.last_error())
else:
    print(symbol, len(rates))

# Desconectar
#mt5.shutdown()