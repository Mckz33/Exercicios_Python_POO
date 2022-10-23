class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def getLadoA(self):
        return self.ladoA

    def setLadoA(self, ladoA):
        self.ladoA = ladoA

    def getLadoB(self):
        return self.ladoB

    def setLadoB(self, ladoB):
        self.ladoB = ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def perimetro(self):
        return (self.ladoA * 2) + (self.ladoB * 2)
