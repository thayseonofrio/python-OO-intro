from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, peso):
        Animal.__init__(self,nome, idade, peso)

    def latir(self, sound = "au au"):
        return "{} faz {}".format(self.nome, sound)

    def fazBarulho(self):
        return "{} faz au au".format(self.nome)

