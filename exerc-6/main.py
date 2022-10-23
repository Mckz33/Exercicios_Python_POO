from tv import Tv

canal = int(input("Canal: "))
volume = int(input("Volume: "))
if canal < 1 and canal > 99:
    print("Canal invalido!")
if volume < 0 and volume > 100:
    print("Escolha entre 0 a 100")
tv = Tv(canal, volume)

print(tv.getCanal())
print(tv.getVolume())

print()
mudar = str(input("Mudar canal s/n? "))
if mudar == "s":
    canal = int(input("Canal: "))
    tv.setCanal(canal)
print()

mudarVolume = str(input("Mudar volume s/n? "))
if mudarVolume == "s":
    volume = int(input("Volume: "))
    if volume < tv.getVolume():
        print("Volume diminuido! ")
        tv.diminuirVolume(volume)
    else:
        print("Volume aumentado! ")
        tv.aumentarVolume(volume)

print(tv.getCanal())
print(tv.getVolume())