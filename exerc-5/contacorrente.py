class ContaCorrente:

    def __init__(self, numero, nome, saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo


    def ContaCorrente(self, numero, nome):
        self.numero = numero
        self.nome = nome

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

