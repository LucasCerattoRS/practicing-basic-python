def nome_valido(nome):
    if not nome or not all(c.isalpha() or c.isspace() for c in nome):
        return False
    return True

# Ela valida se o nome é aceitável com duas regras: Não pode estar vazio e só pode conter letras e espaços. #
# c.isalpha() → verifica se é letra # c.isspace() → verifica se é espaço #
# all() só retorna True se todos os caracteres passarem no teste #

def idade_valida(idade):
    try:
        idade_int = int(idade)
        return 0 <= idade_int <= 120
    except ValueError:
        return False
    
# O try/except evita que o programa quebre e trata o erro de forma controlada. #

def senha_valida(senha):
    if len(senha) < 6:
        return False
    has_upper = any(c.isupper() for c in senha)
    # Tem letra maiúscula?
    has_lower = any(c.islower() for c in senha)
    # Tem letra minúscula?
    has_digit = any(c.isdigit() for c in senha)
    # Tem número?
    has_special = any(not c.isalnum() for c in senha)
    # Tem caractere especial?
    return has_upper and has_lower and has_digit and has_special

# any() funciona assim: Retorna True se pelo menos um caractere atender à condição

# Fluxo principal
nome = input("Digite seu Nome: ")

if not nome_valido(nome):
    print("Nome inválido!")
    exit()

idade = input("Digite sua Idade: ")

if not idade_valida(idade):
    print("Idade inválida!")
    exit()

senha = input("Digite sua Senha: ")

if not senha_valida(senha):
    print("Senha inválida!")
    exit()

print("Cadastro realizado com sucesso!")
