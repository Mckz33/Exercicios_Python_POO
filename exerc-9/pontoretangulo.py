class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPonto(self):
        return self.x, self.y

class Retangulo():
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def centro(self):
        return (self.altura + self.largura) / 2

    def getRetangulo(self):
        return print(f"\nAltura: {self.altura} \nLargura: {self.largura}")

    def setRetangulo(self, altura, largura):
        self.altura = altura
        self.largura = largura

