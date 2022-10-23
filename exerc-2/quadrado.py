class Quadrado:
    def __init__(self, lado):
        self.lado = lado ** 2

    def getArea(self):
        return self.lado
    def setArea(self, lado):
        self.lado = lado