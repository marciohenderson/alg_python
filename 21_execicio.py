"""6. Um professor de Matemática deseja construir um programa para imprimir uma Progressão Aritmética (PA). Para isso, devem ser informados 3 argumentos: a) primeiro termo, b) quantidade de termos e c) razão."""

primeiro_termo = int(input("Digite o primeiro termo: "))
quantidade = int(input("Digite a quantidade de termos: "))
razao = int(input("Digite a razão: "))


for i in range(quantidade):
    primeiro_termo += razao
    print(f"Os termos num intervalo de {razao} números são: {primeiro_termo}")

print("OU")

for i in range(quantidade):
    primeiro_termo += razao
print(f"Os termos num intervalo de {razao} números são: {primeiro_termo}")