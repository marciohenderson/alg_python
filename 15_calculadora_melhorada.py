"""1. Altere o programa de calculadora feito em aulas anteriores (imagem e códigos em anexo) e acrescente a opção 0 (zero). O programa deve parar de imprimir o menu apenas quando o zero for informado.
"""

print("-" * 30)

print("""[0] Para encerrar o progama
[1] Para somar
[2] Pra Subtrair
[3] Para multiplicar
[4] Para dividir""")
print("-" * 30)
opcao = -1

while opcao != 0:
    opcao = int(input("Digite a operação que deseja realizar: "))
    if opcao == 0:
        print("Progama encerrado!")
        break
    if opcao >= 1 and opcao <= 4:
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
        decisao = input("Deseja continuar? (precione ENTER): ")
    else:
        print ("selecione uma opção que existe no menu")
        
        
