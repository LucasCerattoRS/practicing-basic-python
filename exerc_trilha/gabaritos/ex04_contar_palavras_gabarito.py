"""Gabarito do exercício 4."""


def contar_palavras(texto):
    contagem = {}
    for palavra in texto.lower().split():
        palavra = palavra.strip(".,!?;:")
        if palavra:
            contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem


if __name__ == "__main__":
    print(contar_palavras("Casa, casa! Mesa."))
