from funcionario import Funcionario

nome = str(input("NOME: "))
salario = int(input("Salario: "))

func = Funcionario(nome, salario)

while True:
    op = str(input("Deseja adicionar aumento s/n: "))
    if (op == "s"):
        func.setSalario(10)
        print(f"Salario atual: {func.getSalario()}")
        break
    else: print("Você nao tem opção escolha s/!!!\n")