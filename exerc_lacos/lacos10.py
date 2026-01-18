# Usuário → mínimo 5 caracteres
# Senha → mínimo 8 caracteres

# continuar pedindo os dados enquanto estiverem inválidos
# só finalizar quando as duas regras forem atendidas

while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if len(usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.\n")
    elif len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.\n")
    else:
        print("Cadastro realizado com sucesso!")
        break
