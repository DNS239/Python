altura = 6
largura_tronco = 3
altura_tronco = 3


for i in range(altura):
    espacos = altura - i - 1
    galhos = 2 * i + 1
    
    print(' ' * espacos + '*' * galhos)


for i in range(altura_tronco):
    print('    '  + '*' * largura_tronco)



carros = ["Audi", "Porshe", "Ferrari"]

for indice, carros in enumerate(carros):
    print(f"{indice}: {carros}")




#                        Desafio  1                         #

"""# Solicita a entrada do usuário
quantidade_passos = int(input(""))

# Verifica se a quantidade de passos é positiva
if quantidade_passos <= 0:
    print("Nenhum passo dado na floresta.")
else:
    # Utiliza um loop for para simular os passos do explorador
    for passo in range(1, quantidade_passos + 1):
        if passo == 1:
            print(f"Explorador: {passo} passo")
        else:
            print(f"Explorador: {passo} passos")"""














#                               Desafio 2                         #



"""itens = []
repeticao = 1

def lista(itens):
    print("Lista de itens:")
    for item in itens:
        print(f"- {item}")
        
while repeticao <= 3:
    itens.append(input(" "))
    repeticao += 1


lista(itens)"""




#                                Desafio 3                          #



"""capacidade_atual, aumento_percentual = map(int, input().split())

aumento_teraflops = (capacidade_atual * aumento_percentual) // 100

nova_capacidade_total = capacidade_atual + aumento_teraflops

print(int(nova_capacidade_total))
"""