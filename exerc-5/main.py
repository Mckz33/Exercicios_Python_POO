from contacorrente import ContaCorrente

numero = input("Numero: ")
nome = input("Nome: ")
cont = input("Deseja depositar saldo? digite s/n: ")
if cont == "s":
    saldo = input("Saldo: ")
else:
    saldo = 0

cc = ContaCorrente(numero, nome, saldo)

print(cc.getNumero())
print(cc.getNome())
print(cc.getSaldo())
