print("-" * 30)
print("[1] ADIÇÃO")
print("[2] SUBTRAÇÃO")
print("[3] MULTIPLICAÇÃO")
print("[4] DIVISÃO")
print("-" * 30)
opcao = int(input("Digite a operação que deseja realizar: "))
num1 = float(input("Digite seu primeiro número aqui: "))
num2 = float(input("Digite seu segundo número aqui: "))
if opcao == 1:
    resultado = num1 + num2
    print(f"O resultado é: {resultado}")
elif opcao ==2:
    resultado = num1 - num2
    print(f"O resultado é: {resultado}")
elif opcao == 3:
    resultado = num1 * num2
    print(f"O resultado é: {resultado}")
elif opcao == 4:
    if num2 > num1:
        print("Operação inválida!")
    else:
        resultado = num1 / num2
        print(f"O resultado é: {resultado}")
elif opcao != 1 or 2 or 3 or 4:
    print ("selecione uma opção que existe no menu")
