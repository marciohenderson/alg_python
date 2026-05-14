valor = float(input("O valor total da compra é: "))
print("-" * 50)
print("[1] À vista 15% de desconto")
print("[2] Cartão de débito 10% de desconto")
print("[3] Cartão de cŕedito 5% de desconto")
print("-" * 50)
opcao = int(input("Escolha uma opção: "))
if opcao == 1:
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
