# Este arquivo simula o uso da classe Livro em um contexto de biblioteca.

# ARQUIVO: biblioteca.py
#
# Este arquivo NÃO define classes principais.
# Ele utiliza a classe Livro para executar ações:
#
# - emprestar livros
# - verificar disponibilidade
# - testar regras de negócio
#
# Pode ser visto como:
# → uma camada de SERVIÇO ou SIMULAÇÃO


# ✔ Importação de módulos próprios
# ✔ Uso de métodos de instância
# ✔ Uso de método estático
# ✔ Separação entre definição e uso

#1️⃣ Importamos o modelo Livro
#2️⃣ Criamos instâncias
#3️⃣ Chamamos métodos
#4️⃣ Observamos o comportamento
#5️⃣ Validamos se as regras funcionam


# Nunca misture:
# - definição da classe
# - com execução da aplicação

# Isso facilita manutenção e testes.


from exerc.livro import Livro

"""
Arquivo responsável por simular operações da biblioteca:
- empréstimo
- verificação de disponibilidade
"""

# Criando livros
livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
livro2 = Livro("1984", "George Orwell", 1949)
livro3 = Livro("Revolução dos Bichos", "George Orwell", 1945)

# Emprestando um livro
livro1.emprestar()

# Verificando se o livro está disponível
print(f"Livro '{livro1._titulo}' disponível? {livro1.disponivel}")

# Usando o método estático
ano = 1949
livros_disponiveis = Livro.verificar_disponibilidade(ano)

print(f"\nLivros disponíveis publicados em {ano}:")
for livro in livros_disponiveis:
    print(livro)
