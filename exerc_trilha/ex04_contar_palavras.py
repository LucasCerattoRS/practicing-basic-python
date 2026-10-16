"""Exercício 4 — Listas e dicionários (nível 4)

Escreva `contar_palavras(texto)` que devolve um dicionário {palavra: quantidade}.

Regras:
    - ignore maiúsculas/minúsculas ("Casa" e "casa" são a mesma palavra)
    - ignore pontuação nas pontas das palavras (. , ! ? ; :)
    - texto vazio (ou só com espaços) devolve {}

Exemplo:
    contar_palavras("Casa, casa! Mesa.") -> {"casa": 2, "mesa": 1}

Gabarito: gabaritos/ex04_contar_palavras_gabarito.py
"""


def contar_palavras(texto):
    # Escreva sua solução aqui.
    raise NotImplementedError


if __name__ == "__main__":
    print(contar_palavras("Casa, casa! Mesa."))
