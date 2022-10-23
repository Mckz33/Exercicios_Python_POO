from tamagushi import Tamagushi
import random

nome = str(input("Nome: "))
fome = random.randrange(1, 100)
print(f"Fome: {fome}/100")
saude = random.randrange(1, 100)
print(f"Saude: {saude}/100")
idade = random.randrange(1, 3)
print(f"Idade: {idade}")
tedio = random.randrange(1, 100)
tam = Tamagushi(nome, fome, saude, idade, tedio)

tempo = int(input("Tempo de brincar: "))
tam.brincar(tempo)
print(f"Nome: {tam.getNome()}",
      f"\nFome: {tam.getFome()}/100 ",
      f"\nSaude: {tam.getSaude()}/100",
      f"\nIdade: {tam.getIdade()}/100")

comida = str(input("Alimente, digite uma comida: "))
tam.comer()
print(f"Nome: {tam.getNome()}",
      f"\nFome: {tam.getFome()}/100 ",
      f"\nSaude: {tam.getSaude()}/100",
      f"\nIdade: {tam.getIdade()}/100")

"""CHEAT ON"""
cheat = str(input("Deseja ligar o Cheat s/n: "))
if cheat == "s":
    c1 = str(input("Mudar nome s/n: "))
    if c1 == "s":
        mudarNome = str(input("Nome: "))
        tam.setNome(mudarNome)
    c2 = str(input("Mudar fome s/n: "))
    if c2 == "s":
        mudarFome = int(input("Fome: "))
        tam.setFome(mudarFome)
    c3 = str(input("Mudar saude s/n: "))
    if c3 == "s":
        mudarSaude = int(input("Saude: "))
        tam.setSaude(mudarSaude)
    c4 = str(input("Mudar idade s/n: "))
    if c4 == "s":
        mudarIdade = int(input("Idade: "))
        tam.setIdade(mudarIdade)

print()
print("Nome: ", tam.getNome(),
      "\nFome: ",  tam.getFome(),
      "\nSaude: ", tam.getSaude(),
      "\nIdade: ", tam.getIdade())
