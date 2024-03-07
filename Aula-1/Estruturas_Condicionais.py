"""
saldo = 2000.0
saque = float(input("Informe o Valor do Saque:"))

if saldo >= saque:
    print("Realizando Saque!")
else:
    print("Saldo Insuficiente!")
"""

"""import sys


opcao = int(input("Informe sua Opçao: \n[1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a Quantia para o Saque: "))

elif opcao == 2:
    print("Exibindo o Extrato...")
else:
    sys.exit("Opçao Inválida!")"""







"""MIOR_IDADE = 18

IDADE_ESPECIAL = 17

idade = int(input("Informe sua Idade!"))"""

"""if idade >= MIOR_IDADE:
    print("Maior de Idade pode tirar a CNH.")

if idade <= MIOR_IDADE:
    print("Menor de Idade nao pode tirar CNH.")"""

"""else:
    print("Menor de Idade nao pode tirar CNH.")"""


"""if idade >= MIOR_IDADE:
    print("Maior de Idade pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Vócê pode fazer aulas teoricas.")
else:
    print("Menor de Idade nao pode tirar CNH.")"""







"""conta_normal = False
conta_univercitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450


if conta_normal:

    if saldo >= saque:
        print("Realizando Saque!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do Cheque especial!")
    else:
        print("Não foi possivel realizar o Saque!. Saldo insuficiente.")

elif conta_univercitaria:
    if saldo >= saque:
        print("Saque ralizado com sucesso!")
    else:
        print("Saldo insuficiente.")
        
elif conta_especial:
    print("Conta Especial selecionada.")

else:
    print("Sistema não reconhe sua conta entre em contato com seu Gerente!")"""    




saldo = 2000
saque = 2500

 
satatus = "Sucesso" if saldo >= saque else "falha"

print(f"{satatus} ao realizar o saque!")
