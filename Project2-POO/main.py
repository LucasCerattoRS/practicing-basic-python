# Este é o arquivo principal da aplicação.
# Ele coordena a execução do sistema.

# ARQUIVO: main.py
#
# Este arquivo é o PONTO DE ENTRADA do programa.
# Ele é responsável por:
#
# - criar objetos
# - exibir informações
# - controlar o fluxo principal
#
# Aqui NÃO ficam regras de negócio complexas.

# ✔ Importação de classes
# ✔ Instanciação de objetos
# ✔ Uso do método __str__
# ✔ Organização do fluxo principal

# O método __str__ define como o objeto será exibido
# quando usamos print(objeto).
#
# Isso permite:
# - saída limpa
# - código mais legível
# - padronização da exibição

# 1️⃣ O Python começa aqui
# 2️⃣ Objetos são criados
# 3️⃣ Informações são exibidas
# 4️⃣ O programa termina

# livro.py       → define o QUE é o objeto
# biblioteca.py → mostra COMO ele é usado
# main.py       → executa o sistema

# Modelo → Serviço → Aplicação


from exerc.livro import Livro

"""
Arquivo principal da aplicação.
Responsável por instanciar objetos e exibi-los.
"""

def main():
    livro1 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien", 1954)
    livro2 = Livro("Harry Potter", "J. K. Rowling", 1997)

    print(livro1)
    print(livro2)


if __name__ == "__main__":
    main()
