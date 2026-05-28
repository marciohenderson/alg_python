"""2. Crie um programa que recebe números inteiros positivos. Quando o usuário informar um número negativo, o programa deve parar de receber números e imprimir:    
    a) a soma de todos os números positivos informados.
    b) a média aritmética de todos os números positivos informados.
    c) o maior dos números positivos informados."""
num = 1
soma = 0
quantidade = 0
maior = 0
while num > 0:
    num = int(input("Digite um número inteiro positivo: "))
    if num > 0:
        soma += num
        quantidade += 1
        media = soma / quantidade
    if num > maior:
        maior = num
    else:
        print("Nenhum número digitado...")

print("-"*40)
print(f"""RESULTADOS
a quantidade de números digitados é {quantidade}
a soma dos números é igual à: {soma}
o maior número é: {maior}
a média dos números digitados é: {media:.2f}
""")
print("-"*40)