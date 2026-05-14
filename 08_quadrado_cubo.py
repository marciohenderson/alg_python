#Construa um programa que receba um número inteiro positivo informado pelo usuário. Caso ele seja par, o programa deve calcular o seu quadrado. Mas, se ele for ímpar, deve ser calculado o seu cubo. Ao fim, o programa deve imprimir o valor calculado.

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    resultado = num ** 2
    print (f"O quadrado desse número é {resultado}")
elif num % 2 ==1:
    resultado = num ** 3
print(f"O cubo desse número é: {resultado}")