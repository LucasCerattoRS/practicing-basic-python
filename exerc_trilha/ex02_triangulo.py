"""Exercício 2 — Condicionais (nível 2)

Escreva `classificar_triangulo(a, b, c)` que recebe os três lados e devolve:

    "inválido"    se algum lado for <= 0 ou se não formar triângulo
                  (cada lado precisa ser menor que a soma dos outros dois)
    "equilátero"  três lados iguais
    "isósceles"   exatamente dois lados iguais
    "escaleno"    três lados diferentes

Exemplos:
    classificar_triangulo(3, 3, 3) -> "equilátero"
    classificar_triangulo(3, 3, 5) -> "isósceles"
    classificar_triangulo(3, 4, 5) -> "escaleno"
    classificar_triangulo(1, 2, 3) -> "inválido"

Gabarito: gabaritos/ex02_triangulo_gabarito.py
"""


def classificar_triangulo(a, b, c):
    # Escreva sua solução aqui.
    raise NotImplementedError


if __name__ == "__main__":
    print(classificar_triangulo(3, 4, 5))
