"""def exibir_mensagem():
    print("Olà Mundo!")



def exibir_mensagem_2(nome):
    print(f"Seja Bem vindo {nome}!")




def exibir_mensagem_3(nome="Anonimo"):
    print(f"Seja Bem vindo {nome}!")"""



#exibir_mensagem()
#exibir_mensagem_2(nome="Dns")
#exibir_mensagem_3()
#exibir_mensagem_3(nome="Dns")
    













def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 20, 33]))
print(retorna_antecessor_e_sucessor(10))



















def salvar_carros(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso!{marca}/{modelo}/{ano}/{placa}")




#print(salvar_carros("Porsh", "911", 2024, "dns-3333"))
#print(salvar_carros(marca="Porsh", modelo="911", ano=2024, placa="dns-3333"))
#print(salvar_carros(**{"marca": "Porsh", "modelo": "911", "ano": 2024, "placa": "dns-3333"}))

salvar_carros("Porsh", "911", 2024, "dns-3333")
salvar_carros(marca="Porsh", modelo="911", ano=2024, placa="dns-3333")
salvar_carros(**{"marca": "Fiat", "modelo": "Palio", "ano": 2024, "placa": "dns-3333"})




def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)





exibir_poema("Domingo, 23 de abril de 2024", "Zen og Python", "Beatiful is better then ugly.", autor="Tim Perters", ano=1999)   










#def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
#    print(modelo, ano, placa, marca, motor, combustivel)

#criar_carro("Astra", 1999, "DNS-3333", marca="????????", motor="2.0", combustivel="Gasolina")




#def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
#    print(modelo, ano, placa, marca, motor, combustivel)

#criar_carro(modelo="Palio", ano=1999, placa="DNS-3333", marca="FIat", motor="2.0", combustivel="Gasolona")




def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "DNS-3333", marca="FIat", motor="2.0", combustivel="Gasolona")



def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b



def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação è = {resultado}")


exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, multiplicar)
exibir_resultado(10, 10, dividir)


op = somar

print(somar(1, 22))




salario = 2000

def  salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux= {lista_aux}")

    salario += bonus
    return salario

lista = [1]
print(salario_bonus(500, lista))
print(lista)

