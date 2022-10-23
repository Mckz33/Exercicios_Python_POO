from carro import Carro
consumo = int(input("Consumo: "))
carro = Carro(consumo)

while True:
    op = str(input("==== MENU ====\n"
                   "1- Consumo.\n"
                   "2- Add gasolina.\n"
                   "3- Andar.\n"
                   "4- Ver tanque.\n"
                   "5- Sair.\n"
                   "Opção: "))
    if op == "1":
        print(f"{carro.gasto()} quilômetros por litro de combustível.\n")

    if op == "2":
        abastecer = int(input("Litros: "))
        carro.abastecerGasolina(abastecer)
        print(f"abastece com {abastecer} litros de combustível.\n")

    if op == "3":
        km = int(input("KM: "))
        carro.andar(km)
        print(f"anda {km} quilômetros.\n")
    if op == "4":
        print(f"O tanque possui {carro.obterGasolina()} litros\n")

    elif op == "5":
        break

print("Programa encerrado.")