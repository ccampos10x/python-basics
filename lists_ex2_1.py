corridas = [
    ("uber", 25.40),
    ("99", 18.00),
    ("uber", 30.00),
    ("indrive", 22.50),
    ("uber", 18.10)
]

# Atribui 'aplicativos' para uma lista com itens unicos, que e o que você precisa ao entrar e buscar todos os itens da lista
aplicativos = set()

# Define app e valor que sao os dois valores da lista e depois busca em corridas atribuindo pra ela
for app, valor in corridas:
    # percorre aplicativos e busca somente app e adiciona por eles na lista sem gerar duplicata
    aplicativos.add(app)
    
#exibe - obs: tem que esta for do laço porque se nao da erro
print (aplicativos)