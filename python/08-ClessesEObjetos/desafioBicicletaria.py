class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        # self.aro = aro
        # self.marcha = 1

    def buzinar(self):
        print("Plim Plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummm...")

    # def __str__(self):
    #     return f"Bicicleta: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Valor: {self.valor}"

    # def trocar_marcha(self, nro_marcha):
    #     print("Trocando marcha")
    #     _self = self

    #     def _trocar_marcha():
    #         if nro_marcha > _self.marcha:
    #             print("Marcha trocada...")
    #         else:
    #             print("Não foi possivel trocar de marcha!")

    def __str__(self):
        return f"{self.__class__.__name__} {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("Vermelha", "Caloi", 2005, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "Monark", 2000, 189)
# b2.buzinar()  # Bicicleta.buzinar(b2)

print(b2)
b2.correr()  # Bicicleta.
#b2.trocar_marcha()
