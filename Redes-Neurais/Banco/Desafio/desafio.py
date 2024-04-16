class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.deposito_realizado = False

    
    def depositar(self, valor):
        if not self.deposito_realizado:
            if valor > 0:
                self.saldo += valor
                print("Deposito realizado com sucesso!")
                print("Saldo atual: R$", "{:.2f}".format(self.saldo))
                self.deposito_realizado = True
            elif valor < 0:
                print("Valor invalido! Digite um valor maior que zero.")
            else:
                print("Encerrando o programa...")
                return True
        else:
            print("Você já fez um deposito. Encerrando o programa...")
            return True
        

def  main():
    conta = ContaBancaria()
    try:
        valor_deposito = float(input())
        encerrar_programa = conta.depositar(valor_deposito)
        if encerrar_programa:
            return
    except ValueError:
        print("Valor invalido! Digite um valor numérico.")

if __name__== "__main__":
    main()









# class ContaBancaria:
#     def __init__(self):
#         self.saldo = 0
    
#     def depositar(self, valor):
#         if valor > 0:
#             self.saldo += valor
#             print("Depósito realizado com sucesso!")
#             print("Saldo atual: R$", "{:.2f}".format(self.saldo))
#             return True  # Retorna True para indicar que o saldo foi atualizado
#         elif valor < 0:
#             print("Valor inválido! Digite um valor maior que zero.")
#         else:
#             print("Encerrando o programa...")
#         return False  # Retorna False para indicar que o saldo não foi atualizado

# def main():
#     conta = ContaBancaria()
#     while True:
#         try:
#             valor_deposito = float(input("Digite o valor do depósito (ou 0 para encerrar): R$ "))
#             saldo_atualizado = conta.depositar(valor_deposito)
#             if not saldo_atualizado:  # Se o saldo não foi atualizado
#                 if valor_deposito <= 0:
#                     break
#         except ValueError:
#             print("Valor inválido! Digite um valor maior que zero.")

# if __name__ == "__main__":
#     main()
