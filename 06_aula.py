usuario = str(input("Digite o nome de usuário: "))
senha = str(input("Digite a senha: "))
if usuario == "aluno" and senha == "aluno@ifpi":
    print (f"Acesso liberado, seja bem vindo!")
else:
    print("Acesso negado!")