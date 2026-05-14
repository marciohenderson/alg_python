from math import sqrt
x1 = int(input("Digite a primeira coordenada no eixo X: "))
y1 = int(input("Digite a primeira coordenada no eixo Y: "))
x2 = int(input("Digite a segunda coordenada no eixo X: "))
y2 = int(input("Digite a segunda coordenada no eixo Y: "))
d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print (f"A distância entre os pontos escohidos é: {d:.2f}")