class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getPeso(self):
        return self.peso
    def getAltura(self):
        return self.altura
    def envelhecer(self):
        self.idade = self.idade + 969
        print(f"{self.nome} ganhou 969 anos, {self.nome} virou pó assim que recebeu esse beneficio de idade")
    def engordar(self):
        self.peso = self.peso + 150
        print(f"{self.nome} ganhou 150kg Peso atual: {self.peso} e está gordo!")
    def emagrecer(self):
        self.peso = self.peso -150
        print(f"{self.nome} perdeu 150kg, já, não existe mais.")
    def crescer(self):
        print(f"{self.nome} está maior de idade\n")
        if self.idade < 21:
            ainda = (21 - self.idade) * 0.5
            print(f"{self.nome} ainda vai crescer {ainda} até os 21 anos.")
