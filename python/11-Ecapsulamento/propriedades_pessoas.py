class Ninja:
    def __init__(self, nome, ano_nacimento):
        self.nome = nome
        self._ano_nacimento = ano_nacimento

    # @property
    # def nome(self):
    #     return self._nome

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nacimento


pessoa = Ninja("Denis", 1996)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
