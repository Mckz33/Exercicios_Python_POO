class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome
    def getFome(self):
        return self.fome
    def setFome(self, fome):
        self.fome = fome
    def getSaude(self):
        return self.saude
    def setSaude(self, saude):
        self.saude = saude
    def getIdade(self):
        return self.idade
    def setIdade(self, idade):
        self.idade = idade
    def humor(self):
        return self.fome + self.saude