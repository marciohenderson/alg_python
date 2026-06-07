"""5. Crie um programa no qual o usuário informe 2 números inteiros: a e b. Para que o programa continue sua execução, verifique se a < b. Se sim, calcule a soma dos números inteiros no intervalo [a, b]. Caso contrário, informe uma mensagem de erro. """

num1 = int(input("Digite o primeiro número inteiro (a): "))
num2 = int(input("Digite o segundo número inteiro (b): "))
soma = 0
if num1 < num2:
    for quantidade in range(num1, num2):
        soma = (num1 + num2) * quantidade / 2
    print(f"A soma dos números inteiros no intervalo de {num1} e {num2} é: {soma}")
else:
    print("Erro: o segundo número tem que ser maior que o primeiro!")
