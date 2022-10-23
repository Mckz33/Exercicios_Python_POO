from containvestimento import ContaInvestimento
cc = ContaInvestimento(3333, "joao", 1000, 10)

print("Numero:", cc.getNumero())
print("Nome:", cc.getNome())
cc.taxaJuros()
cc.taxaJuros()
cc.taxaJuros()
cc.taxaJuros()
print("Saldo R$:", cc.getSaldo())
