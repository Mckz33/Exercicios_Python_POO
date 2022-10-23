class ContaInvestimento:

    def __init__(self, numero, nome, saldo, juros):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.juros = juros


    def ContaCorrente(self, numero, nome):
        self.numero = numero
        self.nome = nome

    def taxaJuros(self):
        juros = self.juros * self.saldo / 100
        self.saldo -= juros

    def getNome(self):
        return self.nome

    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo

    def setNome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo + valor

