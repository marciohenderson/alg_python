"""6. Um professor de Matemática deseja construir um programa para imprimir uma Progressão Aritmética (PA). Para isso, devem ser informados 3 argumentos: a) primeiro termo, b) quantidade de termos e c) razão."""

primeiro_termo = int(input("Digite o primeiro termo: "))
quantidade = int(input("Digite a quantidade de termos: "))
razao = int(input("Digite a razão: "))
termo = primeiro_termo

for i in range(quantidade):
    print(f'Os termos da P.A são: {termo}')
    termo += razao
