
secreto = "banana"
digitadas = []

while True:
    letra = str(input("Digite uma letra: "))

    if len(letra) > 1:
        print("Digite apenas uma letra: ")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f"Você acertou, a letra '{letra}' existe na palavra secreta!")

    else:
        print(f"A letra '{letra}' não existe na palavra secreta!")
        digitadas.pop()

    for letraSecreta in secreto:
        secretoTemporario = ""
        if letraSecreta in digitadas:
            secretoTemporario == letraSecreta
        else:
            secretoTemporario += "*"

        print(secretoTemporario)

