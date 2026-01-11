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


 
