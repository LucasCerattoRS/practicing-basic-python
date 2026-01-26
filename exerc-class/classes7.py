#adicionar na pasta do github


class ContaBancaria:
    _clientes = []

    def __init__(self, titular: str, saldo: int = 0):
        self.titular = titular.title()
        self.saldo = saldo
        self._ativo = False
        ContaBancaria._clientes.append(self)

    def __str__(self) -> str:
        return f'{self.titular} | Saldo: {self.saldo}'

    # =========================
    # Propriedades
    # =========================

    @property
    def ativo(self) -> bool:
        """Estado lógico da conta."""
        return self._ativo

    @property
    def status(self) -> str:
        """Representação visual do estado."""
        return '⌧' if self._ativo else '☐'

    # =========================
    # Regras de negócio
    # =========================

    def ativar(self) -> None:
        self._ativo = True

    def desativar(self) -> None:
        self._ativo = False

    def alternar_estado(self) -> None:
        self._ativo = not self._ativo

    # =========================
    # Métodos de classe
    # =========================

    @classmethod
    def listar_clientes(cls) -> None:
        for cliente in cls._clientes:
            print(
                f'{cliente.titular.ljust(25)} | '
                f'{str(cliente.saldo).ljust(15)} | '
                f'{cliente.status}'
            )

cliente1 = ContaBancaria('Ana Silva', 28000)
cliente2 = ContaBancaria('Bruno Costa', 35000)
cliente3 = ContaBancaria('Carla Pereira', 22000)

cliente1.ativar()
cliente3.alternar_estado()

ContaBancaria.listar_clientes()
