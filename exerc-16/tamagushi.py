class Tamagushi:
    def __init__(self, nome, fome, saude, idade, tedio):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = tedio

    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome

    def getFome(self):
        return self.fome
    def setFome(self, fome):
        self.fome = fome
    def comer(self):
        self.fome += 20

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

    def getTedio(self):
        return self.tedio
    def setTedio(self, tedio):
        self.tedio = tedio
    def brincar(self, tempo):
        self.fome -= tempo * 1.5
        self.tedio += tempo * 6.6
        if(self.tedio > 100):
            self.tedio = 100
        elif (self.tedio < 0):
            self.tedio = 0
        elif(self.fome > 100):
            self.fome = 100
        elif (self.fome < 0):
            self.fome = 0