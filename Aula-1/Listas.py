lista = "Python"

print(lista[2])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[:])
print(lista[::-1])


print()

carros = ["Audi", "Porshe", "Ferrari"]

for indice, carros in enumerate(carros):
    print(f"{indice}: {carros}")


print()


numeros = [104, 4, 44, 3, 8, 5, 15]
pares = []


for numero in  numeros:
    if numero % 2 == 0:
        pares.append(numeros)
        print(numero)

print()


numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado,)




