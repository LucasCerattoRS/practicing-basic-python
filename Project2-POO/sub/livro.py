# Este arquivo define o MODELO do sistema.
# Ele representa o conceito central: o Livro.

# ARQUIVO: livro.py
#
# Este arquivo contém apenas a definição da classe Livro.
# Ele NÃO executa lógica de aplicação nem testes diretos.
#
# Aqui ficam:
# - atributos
# - regras de negócio
# - comportamentos do objeto Livro
#
# Em arquitetura organizada:
# → este arquivo representa a camada de DOMÍNIO / MODELO

# Conceitos importantes aplicados

# ✔ Programação Orientada a Objetos
# ✔ Encapsulamento (uso de atributos privados _atributo)
# ✔ Método de instância (emprestar)
# ✔ Método estático (verificar_disponibilidade)
# ✔ Método mágico __str__
# ✔ Atributo de classe (lista de livros)

#1️⃣ A classe define o que é um Livro
#2️⃣ O __init__ cria livros com estado inicial
#3️⃣ Cada livro se registra na lista da classe
#4️⃣ Métodos manipulam ou consultam esse estado
#5️⃣ Outros arquivos apenas USAM essa classe


class Livro:
    """
    Classe que representa um livro.

    Cada instância de Livro possui:
    - título
    - autor
    - ano de publicação
    - status de disponibilidade

    A classe também mantém uma lista com TODOS os livros criados,
    simulando um banco de dados em memória.
    """

    # Atributo de classe (compartilhado por todas as instâncias)
    livros = []

    def __init__(self, titulo: str, autor: str, publicacao: int):
        """
        Construtor da classe Livro.

        Executado automaticamente sempre que um novo livro é criado.
        """
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._publicacao = int(publicacao)
        self._disponivel = True  # Livro começa disponível

        # Registra automaticamente o livro na lista da classe
        Livro.livros.append(self)

    def __str__(self):
        """
        Retorna uma representação textual do livro.
        É chamada automaticamente quando usamos print(objeto).
        """
        status = "Disponível" if self._disponivel else "Emprestado"
        return f"{self._titulo} | {self._autor} | {self._publicacao} | {status}"

    def emprestar(self):
        """
        Método de instância.

        Marca o livro como emprestado, se estiver disponível.
        """
        if self._disponivel:
            self._disponivel = False
        else:
            print(f"O livro '{self._titulo}' já está emprestado.")

    @property
    def disponivel(self):
        """
        Propriedade para acessar o status de disponibilidade.
        """
        return self._disponivel

    # MÉTODO ESTÁTICO
#
# Um método estático pertence à CLASSE, não a uma instância específica.
# Ele não recebe o parâmetro `self` (objeto) nem `cls` (classe).
#
# Características principais:
# - Não acessa atributos de instância diretamente
# - Pode acessar atributos da classe, se referenciados explicitamente
# - Funciona como uma função "organizacional" dentro da classe
#
# Quando usar:
# - Quando a lógica faz sentido conceitualmente dentro da classe
# - Quando a operação NÃO depende de um objeto específico
# - Quando queremos evitar criar instâncias desnecessárias
#
# Exemplo neste projeto:
# O método verificar_disponibilidade analisa TODOS os livros cadastrados
# e retorna aqueles que:
# - estão disponíveis
# - foram publicados em um determinado ano
#
# Apesar de não depender de um livro específico, ele pertence à classe Livro
# porque opera sobre o conjunto de livros da biblioteca.
#
# Uso:
# Livro.verificar_disponibilidade(1949)


    @staticmethod
    def verificar_disponibilidade(ano: int):
        """
        Método estático.

        Recebe um ano e retorna uma lista de livros disponíveis
        publicados nesse ano.
        """
        return [
            livro
            for livro in Livro.livros
            if livro._publicacao == ano and livro._disponivel
        ]
