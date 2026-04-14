# Pego os dados de um retãngulo e calcule sua área
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
área = base * altura
if altura <= 0 or base <= 0:
    print("A base e a altura devem ser maiores que zero.")
else:
    print(f"A área do retângulo é: {área:.2f}m²")