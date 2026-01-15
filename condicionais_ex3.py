notas = []

while True:
    nota = float(input("Digite uma nota e aperte enter:"))

    if nota == -1:
        break

    if nota < 0 or nota > 10:
        print("Nota invalida")
        continue

    notas.append(nota)

print (notas)