"""Faça um programa que recebe 10 números inteiros positivos e ao final imprime o resultado do somatório de todos eles."""
print("-"*50)
print("DIGITE 10 NÚMEROS INTEIROS PARA FAZER O SOMATÓRIO!")
print("-"*50)
soma = 0
for contador in range(1, 11):
    num = int(input(f"Digite o {contador}º número: "))
    soma = soma + num
    print(f"A soma de todos os números digitados até agora é: {soma}")