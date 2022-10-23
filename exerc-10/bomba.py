class BombaCombustivel():
    def __init__(self, tipoCombustivel, valorLitro, qtdCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.qtdCombustivel = qtdCombustivel

    def getTipoCombustivel(self):
        return self.tipoCombustivel
    def getValorLitro(self):
        return self.valorLitro
    def getQtdCombustivel(self):
        return self.qtdCombustivel

    def abastecerPorValor(self, abastecerPorValor):
        self.valorLitro /= abastecerPorValor

    def abastecerPorLitro(self, valorLitro):
        self.qtdCombustivel *= valorLitro


    def setValorLitro(self, valorLitro):
        self.valorLitro = valorLitro
    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel
    def setQtdCombustivel(self, qtdCombustivel):
        self.qtdCombustivel = qtdCombustivel

