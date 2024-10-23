class Estudante:
    escola = "DIO"
    Periodo = "Vespertino"

    def __init__(self, nome, idade, endereco, matricula):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.matricula = matricula

    def __str__(self):
        return f"Nome: {self.nome} - Idade: {self.idade} - Endereço: {self.endereco} - Matrícula: {self.matricula} - Escola: {self.escola} - Periodo: {self.Periodo}"


def mostrar_valores(*obj):
    for obj in obj:
        print(obj)


aluno_1 = Estudante("Dns", 28, "Rua:Tombador", 1)
aluno_2 = Estudante("Denis", 30, "Rua:Tombador", 2)

mostrar_valores(aluno_1, aluno_2)

aluno_1.matricula = 3

mostrar_valores(aluno_1, aluno_2)
