#                      Desafio2                 #


# Recebe a entrada do usuário como uma string e divide essa string nos caracteres ',' (vírgula),
# temperaturas_celsius = input().split(',')


# função chamada converter_celsius_para_fahrenheit que recebe uma lista de strings
def converter_celsius_para_fahrenheit(temperaturas_celsius):
    temperaturas_celsius = [float(temp) for temp in temperaturas_celsius]

    # TODO: Calcule as temperaturas em Fahrenheit para cada temperatura em Celsius convertida para float
    temperaturas_fahrenheit = []

    # Converte cada temperatura de Celsius para Fahrenheit
    for temp in temperaturas_celsius:
        fahrenheit = (temp * 9 / 5) + 32
        temperaturas_fahrenheit.append(fahrenheit)

    return temperaturas_fahrenheit


# Imprime o resultado das temperaturas convertidas para Fahrenheit.
# print(converter_celsius_para_fahrenheit(temperaturas_celsius))


temperaturas_celsius = ["0", "25", "100"]  # Temperaturas em Celsius como strings
temperaturas_fahrenheit = converter_celsius_para_fahrenheit(temperaturas_celsius)
print(temperaturas_fahrenheit)  # Saída: [32.0, 77.0, 212.0]
