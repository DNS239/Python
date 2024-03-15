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














itens1 = []
itens2 = []
itens3 = []

itens1.extend(["Espada", "Escudo", "Poção"])
itens2.extend(["Gema", "Flecha", "Capa"])
itens3.extend(["Masterball", "Potion", "Elixir"])

def imprimir_itens(player, itens):
    print(f"Lista de itens:")
    for item in itens:
        print(f"- {item}")

imprimir_itens("player1", itens1)
imprimir_itens("player2", itens2)
imprimir_itens("player3", itens3)
