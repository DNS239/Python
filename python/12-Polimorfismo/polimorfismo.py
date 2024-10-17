class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode Voar")


class Avestrus(Passaro):
    def voar(self):
        print("Avestrus Não pode Voar")


# FIXME: exemplo ruim do uso de herança para "ganhar" o metodo voar
class Aviao(Passaro):
    def voar(self):
        print("Aviao esta decolando...")


def plano_voo(obj):
    obj.voar()


# p1 = Pardal()
# p2 = Avestrus()


plano_voo(Pardal())
plano_voo(Avestrus())
plano_voo(Aviao())
