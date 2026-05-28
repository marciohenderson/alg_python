"""Refaça a questão 9 da Black Friday (imagem em anexo) adicionando estrutura de repetição. O programa deve parar quando a opção zero for informada."""

valor = float(input("O valor total da compra é: "))
print("-" * 50)
print("""[0] para sair do progama
[1] 15% de deconto
[2] 10% de desconto
[3] 5% d desconto
""")
print("-" * 50)
opcao = -1
while opcao != 0:
    opcao = int(input("Escolha uma opção: "))
    if opcao == 0:
        print("Progama encerrado!")
        break
    elif opcao == 1:
        valor_desconto = (15/100) * valor
        final = valor - valor_desconto
        print (f"O desconto é de R${valor_desconto} e o valor final a ser pago é de R${final:.2f}")
    elif opcao == 2:
        valor_desconto = (10/100) * valor
        final = valor - valor_desconto
        print (f"O desconto é de R${valor_desconto} e o valor final a ser pago é de R${final:.2f}")
    elif opcao == 3:
        valor_desconto = (5/100) * valor
        final = valor - valor_desconto
        print (f"O desconto é de R${valor_desconto} e o valor final a ser pago é de R${final:.2f}")
    else:
        print("Selecione uma opção disponível no menu")
