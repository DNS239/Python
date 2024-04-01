def classificar_numero(numero):
    if numero > 0:
        return "positivo!"
    elif numero < 0:
        return "negativo!"
    else:
        return "Zero"

def main():
    positivos = 0
    negativos = 0
    
    while True:
        numero = int(input(""))
        
        if numero == 0:
            break  # Encerra o loop se o usuário digitar 0.
        
        # Chama a função classificar_numero para imprimir a classificação do número
        print(classificar_numero(numero))
        
        # Faz a verificação para saber quantos números positivos e negativos foram inseridos
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    
    # Imprime a quantidade de números positivos e negativos inseridos
    print(f"{positivos} números positivos, {negativos} números negativos")

if __name__ == "__main__":
    main()









