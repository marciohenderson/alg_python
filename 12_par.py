qpar = 0
for contador in range(1, 11):
    num = int(input(f"Digite o {contador}º número: "))
    if num % 2 == 0:
        qpar += 1      
print(f"A quantidade de números par é de: {qpar}")
