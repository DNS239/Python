#             Desafio1                            #

# Recebe a entrada e armazena na variável "entrada"
# entrada = input()


# Função reponsável por extrair os domínios dos emails
def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula
    lista_emails = emails.split(";")

    # TODO: Implemente a lógica necessária para extrair os domínios
    dominios = []

    for email in lista_emails:
        # Divide o email no caractere '@' e pega a parte do domínio (parte após o '@')
        dominio = email.split("@")[1]
        # Adiciona o domínio à lista de domínios
        dominios.append(dominio)
    return dominios


# Imprime a lista de strings com os domínios
# print(extrair_dominios(entrada))

entrada = "ana@example.com;bob@test.com"
saida = extrair_dominios(entrada)
print(saida)  # Saída: ['example.com', 'test.com']
