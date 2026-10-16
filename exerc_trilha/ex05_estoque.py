"""Exercício 5 — Classes (nível 5)

Crie a classe `Estoque` para controlar a quantidade de itens de uma loja.

    Estoque()                     começa vazio
    adicionar(item, quantidade)   soma ao item; quantidade deve ser > 0,
                                  senão levanta ValueError
    remover(item, quantidade)     subtrai; quantidade deve ser > 0 (ValueError);
                                  se não houver o suficiente, levanta ValueError
    quantidade(item)              devolve a quantidade (0 se o item não existe)
    __str__                       uma linha por item, em ordem alfabética: "item: qtd"

Exemplo:
    e = Estoque()
    e.adicionar("caneta", 10)
    e.remover("caneta", 3)
    e.quantidade("caneta") -> 7

Gabarito: gabaritos/ex05_estoque_gabarito.py
"""


class Estoque:
    # Escreva sua solução aqui.
    pass


if __name__ == "__main__":
    e = Estoque()
    e.adicionar("caneta", 10)
    print(e)
