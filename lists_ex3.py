# Dados Iniciais
corridas = [
    ("uber", 25.40),
    ("99", 18.00),
    ("uber", 30.00),
    ("indrive", 22.50),
    ("uber", 18.10),
    ("99", 15.00)
]

# P1 -Exibe Aplicativos usado
aplicativos = set()

for app, valor in corridas:
    aplicativos.add(app)
print (aplicativos)

# P2 - Exibe Total por Aplicativo
# Precisa percorrer cada lista de "corridas" e se for igual ao "aplicativos" deve somar e depois fora de um laço deve exibir o total
# Como fazer isso sem usar variavel fixa ? A ideia seria usar a lista unica gerada na primeira parte do exercicio

# Guardar os valores no dict
total = {}

for app, valor in corridas:
    if app not in total:
        total[app] = 0
    total[app] = total[app] +valor

print (total)


 
# P3 Você vai simular um controle diário de ganhos como motorista.
# Objetivo: Registrar corridas (valor e km)
# Calcular: Total ganho, Total de km, Média por km, Média por corrida

corridas = [
    {"valor": 22.0, "km": 7},
    {"valor": 18.5, "km": 5},
    {"valor": 35.0, "km": 12},
]

total_valor = 0
total_km = 0

for corrida in corridas:
    total_valor += corrida["valor"]
    total_km += corrida["km"]

media_por_km = total_valor / total_km
media_por_corrida = total_valor / len(corridas)

print(f"Total ganho: R$ {total_valor:.2f}")
print(f"Total km: {total_km}")
print(f"Média por km: R$ {media_por_km:.2f}")
print(f"Média por corrida: R$ {media_por_corrida:.2f}")