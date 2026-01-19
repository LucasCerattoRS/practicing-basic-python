def nome_valido(nome):
    # Verifica se o nome não está vazio
    if nome == "":
        return False

    # Verifica se todos os caracteres são letras ou espaços
    for caractere in nome:
        if not (caractere.isalpha() or caractere.isspace()):
            return False

    return True

# Substituí all() por um for, que é mais fácil de visualizar #

def idade_valida(idade):
    try:
        idade_convertida = int(idade)
    except ValueError:
        return False

    if idade_convertida < 0:
        return False

    if idade_convertida > 120:
        return False

    return True

def senha_valida(senha):
    if len(senha) < 6:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif not caractere.isalnum():
            tem_especial = True

    if not tem_maiuscula:
        return False
    if not tem_minuscula:
        return False
    if not tem_numero:
        return False
    if not tem_especial:
        return False

    return True

# Cada regra é visível, Dá para depurar facilmente, Ideal para aprendizado...

while True:
    nome = input("Digite seu nome: ")

    if nome_valido(nome):
        break
    else:
        print("Nome inválido. Use apenas letras e espaços.")

while True:
    idade = input("Digite sua idade: ")

    if idade_valida(idade):
        break
    else:
        print("Idade inválida. Digite um número entre 0 e 120.")

while True:
    senha = input("Digite sua senha: ")

    if senha_valida(senha):
        break
    else:
        print("Senha inválida.")
        print("A senha deve ter:")
        print("- No mínimo 6 caracteres")
        print("- Letra maiúscula")
        print("- Letra minúscula")
        print("- Número")
        print("- Caractere especial")
    
    print("Cadastro realizado com sucesso!")

# Usuário erra → recebe feedback → tenta de novo

# Nenhum encerramento abrupto