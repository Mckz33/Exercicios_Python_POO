from retangulo import Retangulo

ladoA = int(input("LadoA: "))
ladoB = int(input("LadoB: "))
ret = Retangulo(ladoA, ladoB)

print(ret.perimetro())
print(ret.calcularArea())