#2. Construa um programa que solicite ao usuário dois números positivos. Em seguida, o programa deve apresentar o seguintemenu:1. Média ponderada, com pesos 2 e 3, respectivamente 2. Quadrado da soma dos 2 números3. Cubo do menor número scolha uma opção:De acordo com a opção informada, o programa deve calcular a operação apresentada no menu. Se a opção escolhida for inválida, o programa deve mostrar a mensagem “Opção inválida” e ser encerrado.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print("-" * 60)
print("""[1] média ponderada com pesos 2 e 3, respectivamente
[2] Quadrado da soma dos 2 números
[3] Cubo do menor número""")
print("-" * 60)
#print("[2] Quadrado da soma dos 2 números")
#print("[3] Cubo do menor número")
opcao = int(input("Escolha uma opção: "))
if opcao == 1:
    resultado = ((num1 * 2) + (num2 * 3)) / (2+3)
    print (f"O resultado é: {resultado}")
elif opcao == 2:
    resultado = (num1 + num2) ** 2
    print (f"O resultado é: {resultado}")
elif opcao == 3:
    if num1 < num2:
        resultado = num1 ** 3
        print (f"O resultado é: {resultado}")
    else:
        resultado = num2 ** 3
        print (f"O resultado é: {resultado}")
else:
    print("Selecione uma opção que está no menu")
    