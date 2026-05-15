"""Faça um programa que recebe um usuário e senha e enquanto eles não forem iguais ao par usuário = "aluno" e senha = "12345", o programa imprime "Tente novamente". Caso seja atingido o limite de três tentativas, encerre o programa imprimindo "Você tentou 3 vezes". Quando o usuário e senha estiverem corretos, o programa encerra imprimindo "Acesso liberado".
"""
contador = 3
usuario = str(input("Digite o nome do usuário: "))
senha = str(input("Digite a senha do usuário: "))
while (usuario != "aluno" or senha != "12345") and contador > 1:
    contador -= 1
    print(f"Aceso negado, tente novamente você tem {contador} tentativas restantes")
    usuario = str(input("Digite o nome do usuário: "))
    senha = str(input("Digite a senha do usuário: "))
if usuario == "aluno" and senha == "12345":
    print ("Acesso liberado!")
else:
    print("Conta bloqueada")
    