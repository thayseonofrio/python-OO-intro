from animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, peso):
        Animal.__init__(self,nome, idade, peso)

    def miar(self, sound = "miau"):
        return "{} faz {}".format(self.nome, sound)

    def fazBarulho(self):
        return "{} faz miau".format(self.nome)
