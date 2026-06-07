numero_escolhido = 7
tentativas = 3

while tentativas > 0:
    numero = int(input("Digite um número: "))
    tentativas -= 1
    if numero == numero_escolhido:
        print("Você acertou! parabéns")
        break
    else:
        print(f"Você errou! tente novamente")
        print(f"aproveita que ainda ainda tem {tentativas} tentativas restantes restates!")
        if numero > numero_escolhido:
            print("Tente um número um pouco menor!")
        else:
            print("Escolha um número maior")
    if tentativas == 0:
        print("Você esgotou suas tentivas, tente novamente mais tarde!")