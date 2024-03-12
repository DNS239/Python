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


"""print(contatos["ade@.com"])
print(contatos.get("ade@.com"))

contatos.pop("ade@.com")

print(contatos.get("ade@.com"))

print(contatos.get("ade@.com", {}))"""




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



#print(contatos.get("chave", {}))

print(contatos.get("Dns@.com", {}))


print()


copia = contatos.copy()
copia["ght@.com"] = {"nome": "tgf"}


print()

contatos.clear()
print(contatos)

print()



contatos = dict.fromkeys(["bairo", "cidade"])
print(contatos)

contatos = dict.fromkeys(["bairo", "cidade"], "vazio")
print(contatos)

print()


for chave, valor in contatos.items():
    print(chave, valor)



contato = {"nome": "Dns", "telefone": "3333-3333"}
contato.setdefault("nome", "maria")
print(contato)

contato.setdefault("idade", 27)
print(contato)





