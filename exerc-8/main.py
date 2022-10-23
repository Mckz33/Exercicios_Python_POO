from macaco import Macaco

nome = str(input("Nome: "))
algo = str(input("Dê algo para o maGula: "))
comer = algo
estomago = algo
mac = Macaco(nome, estomago)
mac.comer(algo)

if algo == "macaco":
    print(f"{nome} está com o estomago vazio, alimente o animal!")
else:
    print(f"{nome} tem {mac.getEstomago()} no estomago!")

mac.diferir(algo)