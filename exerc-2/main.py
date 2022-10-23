from quadrado import Quadrado
qdd = Quadrado(33)
print(qdd.getArea())

lado = input("Novo Lado: ")
qdd.setArea(lado)

print(qdd.getArea())