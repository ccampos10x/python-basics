numeros = []

while True:
    numero = float(input("Digite um numero:"))

    if  numero == 0:
        break

    if numero > 0:
        numeros.append(numero)
    else:
        continue

    

print (numeros)
print (len(numeros))
print (sum(numeros))