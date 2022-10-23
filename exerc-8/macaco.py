class Macaco:
    def __init__(self, nome, estomago):
        self.nome = nome
        self.estomago = estomago

    def comer(self, coisa):
        if coisa == "macaco":
            print("Essa diabrura de macaco canibal não exite!")
        else:
            print(f"{self.nome} está comendo {coisa}!")

    def getEstomago(self):
        return self.estomago

    def diferir(self, coisa):
        if coisa == "macaco":
            print(f"{self.nome} está com fome! ")
        else:
            print(f"{self.nome} digeriu a/o: {coisa}")
