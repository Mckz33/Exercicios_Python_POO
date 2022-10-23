from pontoretangulo import Ponto, Retangulo
print("===== MENU =====")
i = 0
while i != 1:
    mudar = str(input("Mudar os valores do retangulo? s/n: "))
    if mudar == "s":
        largura = int(input("Largura: "))
        altura = int(input("Altura: "))
        i += 1
    else:
        print("Você nao tem opção, escreva s ou sofra as consequencias! ")
    continue

re = Retangulo(altura, largura)
po = Ponto(6, 7)

print(re.getRetangulo())
print(po.getPonto())