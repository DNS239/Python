from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("TV ligada")

    def desligar(self):
        print("TV desligada")

    @property
    def marca(self):
        return "Sansung"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Arcondicionado Ligado")

    def desligar(self):
        print("Arcondicionado Desligado")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)