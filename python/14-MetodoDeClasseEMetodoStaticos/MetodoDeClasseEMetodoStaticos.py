class Pessoa:

    def __init__(self, nome=None, idade=None, endereco=None, telefone=None):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone

    @classmethod
    def criar_de_data_nacimento(cls, ano, mes, dia, nome):
        # print(cls)
        idade = 2024 - ano

        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


# p = Pessoa("Dns", 28, "Rua:Tombador", 67998008084)


# print(p.nome, p.idade, p.endereco, p.telefone)


p = Pessoa.criar_de_data_nacimento(1996, 12, 1996, "Dns")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))