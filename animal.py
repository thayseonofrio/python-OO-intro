class Animal:

    # Initializer / Instance Attributes
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso


    # instance method
    def dormir(self):
        return "{} dorme".format(self.nome)

    def fazBarulho(self):
        return "{} fazendo algum barulho".format(self.nome)
