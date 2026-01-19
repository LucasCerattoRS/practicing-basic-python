# O principal problema conceitual do código original é este: Cliente não deveria ter saldo: Quem tem saldo é a conta.

# Classe	Responsabilidade
# Cliente	Identidade da pessoa
# Conta	    Dinheiro, operações financeiras
# Banco	    Gerenciar clientes e contas

# Isso evita:

# Mistura de regras

# Acoplamento excessivo

# Problemas de escalabilidade




# Mini-sistema bancário (arquitetura limpa):

# Classe Cliente (entidade pura)

class Cliente:
    def __init__(self, nome: str, cpf: str, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __str__(self):
        return f'{self.nome} | CPF: {self.cpf} | Idade: {self.idade}'

# Cliente não sabe nada sobre dinheiro.

# Ele só representa uma pessoa.



# Classe Conta (regra de negócio)

class Conta:
    def __init__(self, cliente: Cliente, agencia: str, saldo: float = 0.0):
        self.cliente = cliente
        self.agencia = agencia
        self._saldo = saldo

# observe:

# A conta pertence a um cliente

# _saldo é protegido (encapsulamento)




# Operações financeiras

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError('Valor de depósito inválido')
        self._saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('Valor de saque inválido')
        if valor > self._saldo:
            raise ValueError('Saldo insuficiente')
        self._saldo -= valor

    def consultar_saldo(self) -> float:
        return self._saldo

# Aqui temos:

# Validação

# Regras explícitas

# Falha controlada (raise)


# Representação da conta

    def __str__(self):
        return (
            f'{self.cliente.nome} | '
            f'Agência: {self.agencia} | '
            f'Saldo: {self._saldo:.2f}'
        )

# Classe Banco (orquestrador)

class Banco:
    def __init__(self, nome: str):
        self.nome = nome
        self.clientes = []
        self.contas = []

# Aqui não usamos atributo de classe.
# Cada banco tem seu próprio estado.



# Cadastro de cliente

    def cadastrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

# Abertura de conta

    def abrir_conta(self, cliente: Cliente, agencia: str, saldo_inicial=0.0):
        conta = Conta(cliente, agencia, saldo_inicial)
        self.contas.append(conta)
        return conta


# Listagem de contas

    def listar_contas(self):
        for conta in self.contas:
            print(conta)


# Uso do sistema (fluxo realista)

banco = Banco('Banco Python')

cliente1 = Cliente('Ana Silva', '123.456.789-00', 30)
cliente2 = Cliente('Bruno Costa', '987.654.321-00', 42)

banco.cadastrar_cliente(cliente1)
banco.cadastrar_cliente(cliente2)

conta1 = banco.abrir_conta(cliente1, '0001', 2500)
conta2 = banco.abrir_conta(cliente2, '0002', 4800)

conta1.depositar(500)
conta2.sacar(800)

banco.listar_contas()


# Isso já é arquitetura de sistema real, apenas sem persistência.


# Agora o ponto mais importante: isso não é Python — é OOP.