"""Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria (considere que o usuário informou cinco medicamentos distintos). O programa deve informar o nome e o preço do medicamento mais barato, bem como a média aritmética dos preços informados."""

soma = 0
nome_mais_barato = ""
mais_barato = 0

for num in range (0, 5):
    nome = input("Digite o nome do medicamento: ")
    valor = float(input("Digite o valor do medicamento: "))
    soma += valor
    if num == 0:
        mais_barato = valor
        nome_mais_barato = nome
    else:
        if valor < mais_barato:
            mais_barato = valor
            nome_mais_barato = nome


media = soma / 5
print("-" * 50)
print(f"A média dos valores é: {media:.2f}")
print(f"o medicamento mais barato é: {nome_mais_barato} com um valor de: R${mais_barato}")
print("-" * 50)