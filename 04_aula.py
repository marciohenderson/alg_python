massa = float(input("Digite sua massa aqui: "))
altura = float(input("Digite sua altura aqui: "))
imc = massa / altura ** 2
if imc <18.5:
    print (f"Você precisa comer mais... seu IMC é: {imc:.2f}")
elif imc >= 18.5 and imc <25:
    print (f"Você está normal, parabéns! Seu IMC é: {imc:.2f}")
elif imc >= 25 and imc <30:
    print (f"Você está com sobrepeso, cuidado! Seu IMC é: {imc:.2f}")
elif imc >= 30 and imc <35:
    print (f"Você está com obesidade grau 1, cuidado! Seu IMC é: {imc:.2f}")
elif imc >= 35 and imc <40:
    print (f"Você está com obesidade grau 2, cuidado! Seu IMC é: {imc:.2f}")
else:    print (f"Você está com obesidade grau 3, cuidado! Seu IMC é: {imc:.2f}")