print("Hello, Word!")

altura = 5
largura_tronco = 1
altura_tronco = 3


for i in range(altura):
    espacos = altura - i - 1
    galhos = 2 * i + 1
    print(' ' * espacos + '*' * galhos)


espacos_tronco = altura_tronco // 2
espacos_a_direita = altura - 2
for i in range(altura_tronco):
    print(' ' * espacos_a_direita + ' ' * espacos_tronco + '*' * largura_tronco)
