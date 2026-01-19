# aqui você já entrou em OOP intermediário

# Este código representa um sistema simples de clientes de banco, onde: 
# Cada cliente é um objeto; 
# Todos os clientes criados ficam registrados em uma lista compartilhada;
# A classe sabe listar todos os clientes;

# Em termos de domínio:

# ClienteBanco = entidade
# clientes = “tabela em memória”

class ClienteBanco:
    clientes = []

# Esse é o ponto mais importante do código.
# clientes não pertence a um cliente específico
# Ele pertence à classe inteira

# Todos os objetos compartilham essa lista.

# Visualmente: ClienteBanco
           #   └── clientes → [cliente1, cliente2, cliente3]

# Isso permite:

# Registrar automaticamente cada cliente criado

# Ter controle global sem usar variáveis externas

# Construtor (__init__) com tipagem
# O que a tipagem faz: Não valida automaticamente.
# Serve para: Documentação; IDEs; Leitura humana; Ferramentas de análise estática.
# Exemplo: Saldo: float (Deixa claro que o saldo deveria ser numérico decimal.)
    def __init__(
        self,
        nome: str,
        cpf: str,
        idade: int,
        agencia: str,
        saldo: float
    ):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.agencia = agencia
        self.saldo = saldo

        ClienteBanco.clientes.append(self)
        # Essa linha é crucial: Toda vez que um cliente nasce ele se adiciona automaticamente à lista da classe
        # “Todo cliente criado passa a existir no banco.” #


    def __str__(self) -> str:
        return f'{self.nome} | CPF: {self.cpf} | Saldo: {self.saldo}'
    
    # É uma representação resumida, não a listagem completa.

    @classmethod
    # Não opera sobre um cliente: Opera sobre a classe inteira.
    # “Listar clientes é responsabilidade de um cliente ou do banco?” 
    # Por isso o método é de classe.
    def listar_clientes(cls) -> None:
        for cliente in cls.clientes:
            print(
                f'{cliente.nome.ljust(20)} | '
                f'{cliente.cpf.ljust(14)} | '
                f'{str(cliente.idade).ljust(5)} | '
                f'{cliente.agencia.ljust(6)} | '
                f'{str(cliente.saldo).ljust(10)}'
            )

# Formatação com ljust: alinha o texto à esquerda

# Criação dos objetos:

cliente1 = ClienteBanco(
    nome='Ana Silva',
    cpf='123.456.789-00',
    idade=30,
    agencia='0001',
    saldo=2500.00
)

cliente2 = ClienteBanco(
    nome='Bruno Costa',
    cpf='987.654.321-00',
    idade=42,
    agencia='0002',
    saldo=4800.50
)

cliente3 = ClienteBanco(
    nome='Carla Pereira',
    cpf='456.789.123-00',
    idade=25,
    agencia='0001',
    saldo=1200.75
)

ClienteBanco.listar_clientes()
