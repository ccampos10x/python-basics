numeros = [3, 7, 2, 9, 10, 4, 6]

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print ("Impares:",impares)
print ("Pares:",pares)
