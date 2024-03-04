altura = 6
largura_tronco = 3
altura_tronco = 3


for i in range(altura):
    espacos = altura - i - 1
    galhos = 2 * i + 1
    
    print(' ' * espacos + '*' * galhos)


for i in range(altura_tronco):
    print('    '  + '*' * largura_tronco)
