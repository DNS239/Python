numros = set ([1, 2, 3, 1, 3, 4,])
fruta = set ("abacaxi")
caros = set (("Audi", "Ferrari", "Porsh", "Audi"))


numero = {1, 2, 3, 2}

numero = list(numero)
print(numero[0])




print(numros)
print(fruta)
print(caros)


conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_c = {1, 0}

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))



