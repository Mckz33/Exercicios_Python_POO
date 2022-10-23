class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcentagem):
        self.preco = self.preco * porcentagem / 100 + self.preco


produto = Produto("Camisa", 50)