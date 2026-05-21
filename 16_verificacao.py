"""2. Crie um programa que recebe números inteiros positivos. Quando o usuário informar um número negativo, o programa deve parar de receber números e imprimir:    
    a) a soma de todos os números positivos informados.
    b) a média aritmética de todos os números positivos informados.
    c) o maior dos números positivos informados."""

soma = 0
quantidade = 0
maior = 0
while True:
    num = int(input("Digite um número inteiro positivo: "))
    if num < 0:
        print("Progama encerrado pois você digitou um número negativo!")
        break
    soma = soma + num
    quantidade = quantidade + 1
    if num > maior:
        maior = num
        if quantidade > 0:
            media = soma / quantidade
    print("-"*30)
    print(f"""RESULTADOS
    a soma dos números é igual à: {soma}
    o maior número é: {maior}
    a média dos números digitados é: {media}
    """)
    print("-"*30)