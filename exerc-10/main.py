from bomba import BombaCombustivel

'''TIPO COMBUSTIVEL + VALOR DO LITRO'''

while True:
    comb = str(input("\n=====MENU=====\n"
          "Qual Combustivel:\n"
          "1-Gasolina:\n"
          "2-Etanol\n"
          "3-Diesel\n"
          "4-Gas\n"
          "Digite um Número: "))

    if comb == "1":
        tipoCombustivel = "Gasolina"
        valorLitro = 9
        qtdCombustivel = 1000
        break
    if comb == "2":
        tipoCombustivel = "Etanol"
        valorLitro = 6.20
        qtdCombustivel = 1000
        break
    if comb == "3":
        tipoCombustivel = "Diesel"
        valorLitro = 3.89
        qtdCombustivel = 1000
        break
    if comb == "4":
        tipoCombustivel = "Gas"
        valorLitro = 4.99
        qtdCombustivel = 1000
        break

"""OPÇAO DE ABASTECIMENTO COMBUSTIVEL OU VALOR"""

while True:
    ab = str(input("Digite uma Opção de Abastecimento:\n"
                   "1-combustivel\n"
                   "2-valor:\n"
                   "Opção: "))
    if ab == "1":
        abastecerPorLitro = float(input("Litros: "))
        break

    if ab == "2":
        abastecerPorValor = int(input("Valor R$: "))
        break

bc = BombaCombustivel(tipoCombustivel, valorLitro, qtdCombustivel)

if ab == "1":
    if comb == "1":
        lcomb = "Gasolina"
    if comb == "2":
        lcomb = "Etanol"
    if comb == "3":
        lcomb = "Diesel"
    if comb == "4":
        lcomb = "Gas Natural"

    print("Você abasteceu %d Litros de %s\n"
          "Valor a pagar R$%.2f." %(abastecerPorLitro, lcomb, bc.getValorLitro()))

if ab == "2":
    if comb == "1":
        lcomb = "Gasolina"
    if comb == "2":
        lcomb = "Etanol"
    if comb == "3":
        lcomb = "Diesel"
    if comb == "4":
        lcomb = "Gas Natural"

    print("Você comprou R$%.2f de %s\n"
          "Combustivel recebido: %d" % (abastecerPorValor, lcomb, bc.abastecerPorValor(abastecerPorValor)))
