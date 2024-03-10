pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa ["telefone"] = "3333-1234"
print(pessoa)



print(pessoa["nome"])
print(pessoa["idade"])

pessoa["nome"] = "Dns"
pessoa["idade"] = 27

print(pessoa["nome"])
print(pessoa["idade"])


contatos = {
    "Dns@.com": {"nome": "Dns", "telefone": "4444-5467"},
    "ght@.com": {"nome": "ght", "telefone": "2234-3421"},
    "ade@.com": {"nome": "ade", "telefone": "5678-8764"},
    "rgt@.com": {"nome": "rgt", "telefone": "5790-3453", "extra": {"a": 1}},

}



print(contatos["Dns@.com"]["telefone"])
print(contatos["rgt@.com"]["extra"]["a"])




for chave in contatos:
    print(chave, contatos[chave])


print()


for chave, valor in contatos.items():
    print(chave, valor)


pessoa = {"a": 1234}
print(pessoa)

pessoa = dict()
print(pessoa)
