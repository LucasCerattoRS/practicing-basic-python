"""Gabarito do exercício 3."""


def fizzbuzz(n):
    resultado = []
    for numero in range(1, n + 1):
        if numero % 15 == 0:
            resultado.append("FizzBuzz")
        elif numero % 3 == 0:
            resultado.append("Fizz")
        elif numero % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(numero)
    return resultado


if __name__ == "__main__":
    print(fizzbuzz(15))
