while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if senha != nome_usuario:
        break
    else:
        print("Senha igual ao nome de usuário. Tente novamente.")

print("Senha aceita.")