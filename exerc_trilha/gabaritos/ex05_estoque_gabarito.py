"""Gabarito do exercício 5."""


class Estoque:
    def __init__(self):
        self._itens = {}

    def adicionar(self, item, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero")
        self._itens[item] = self._itens.get(item, 0) + quantidade

    def remover(self, item, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero")
        if self.quantidade(item) < quantidade:
            raise ValueError("Estoque insuficiente")
        self._itens[item] -= quantidade

    def quantidade(self, item):
        return self._itens.get(item, 0)

    def __str__(self):
        return "\n".join(f"{item}: {qtd}" for item, qtd in sorted(self._itens.items()))


if __name__ == "__main__":
    e = Estoque()
    e.adicionar("caneta", 10)
    print(e)
