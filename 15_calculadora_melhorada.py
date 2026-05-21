"""1. Altere o programa de calculadora feito em aulas anteriores (imagem e códigos em anexo) e acrescente a opção 0 (zero). O programa deve parar de imprimir o menu apenas quando o zero for informado.
"""
while True:
    print("-" * 30)
    print("""[0] Para encerrar o progama
[1] Para somar
[2] Pra Subtrair
[3] Para multiplicar
[4] Para dividir""")
    print("-" * 30)
    opcao = int(input("Digite a operação que deseja realizar: "))
    if opcao == 0:
        print("Progama encerrado!")
        break
    elif opcao >= 1 and opcao <= 4:
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
        if opcao > 1 or opcao < 4:
            print ("selecione uma opção que existe no menu")
        decisao = str(input("Deseja continuar? (precione ENTER): "))
        """ if decisao == "sim":
            opcao = int(input("Digite a operação que deseja realizar: "))
            num1 = float(input("Digite seu primeiro número aqui: "))
            num2 = float(input("Digite seu segundo número aqui: "))
        elif opcao == 1:
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
        if decisao == "não":
            print("Progama encerrado!")
            break
                     """
                

