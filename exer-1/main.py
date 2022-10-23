from bola import Bola

p = Bola("Verde", 33, "Couro")
print(p.getCor())
print(p.getCircunferencia())
print(p.getMaterial())
print()

cor = input("Nova Cor: ")
p.setCor(cor)
circunferencia = input("Nova Circunferencia: ")
p.setCircunferencia(circunferencia)
material = input("Novo Material: ")
p.setMaterial(material)

print()
print(p.getCor())
print(p.getCircunferencia())
print(p.getMaterial())