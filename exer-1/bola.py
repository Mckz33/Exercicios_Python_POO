class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def setCor(self, cor):
        self.cor = cor
    def getCor(self):
        return self.cor
    def setCircunferencia(self, circunferencia):
        self.circunferencia = circunferencia
    def getCircunferencia(self):
        return self.circunferencia
    def setMaterial(self, materal):
        self.material = materal
    def getMaterial(self):
        return self.material