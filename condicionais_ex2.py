lista = [7,6,5,9,6]

soma_notas =0
nota_maior7=0
nota_menor7=0

for listas in lista:
    soma_notas += listas
    if listas >= 7:
        nota_maior7 += 1
    else:
        nota_menor7 +=1

media_notas = soma_notas / len(lista)

print ("Media =",media_notas)

if media_notas >= 5.0: 
    print ("Aprovados")
else: 
    print ("Reprovados")

print("Notas MAIORES que 7 são:", nota_maior7)
print("Notas MENORES que 7 são:", nota_menor7)
