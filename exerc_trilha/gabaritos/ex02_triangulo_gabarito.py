"""Gabarito do exercício 2."""


def classificar_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "inválido"
    if a >= b + c or b >= a + c or c >= a + b:
        return "inválido"
    if a == b == c:
        return "equilátero"
    if a == b or b == c or a == c:
        return "isósceles"
    return "escaleno"


if __name__ == "__main__":
    print(classificar_triangulo(3, 4, 5))
