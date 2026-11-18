"""Testes da trilha.

Por padrão testam os gabaritos. Para conferir a SUA solução (os arquivos de
enunciado em exerc_trilha/), rode com a variável TRILHA=enunciado:

    TRILHA=enunciado python -m pytest tests/test_trilha.py
"""
import os

import pytest

from helpers import RAIZ, importar_por_caminho

ALVO = os.environ.get("TRILHA", "gabarito")
if ALVO not in ("gabarito", "enunciado"):
    raise ValueError(f"TRILHA deve ser 'gabarito' ou 'enunciado', não {ALVO!r}")


def _carregar(nome):
    if ALVO == "enunciado":
        caminho = f"exerc_trilha/{nome}.py"
    else:
        caminho = f"exerc_trilha/gabaritos/{nome}_gabarito.py"
    return importar_por_caminho(caminho, f"trilha_{ALVO}_{nome}")


celsius_para_fahrenheit = _carregar("ex01_temperatura").celsius_para_fahrenheit
classificar_triangulo = _carregar("ex02_triangulo").classificar_triangulo
fizzbuzz = _carregar("ex03_fizzbuzz").fizzbuzz
contar_palavras = _carregar("ex04_contar_palavras").contar_palavras
Estoque = _carregar("ex05_estoque").Estoque


@pytest.mark.parametrize("c, f", [(0, 32), (100, 212), (-40, -40), (37, 98.6)])
def test_temperatura(c, f):
    assert celsius_para_fahrenheit(c) == pytest.approx(f)


@pytest.mark.parametrize(
    "lados, esperado",
    [
        ((3, 3, 3), "equilátero"),
        ((3, 3, 5), "isósceles"),
        ((5, 3, 3), "isósceles"),
        ((3, 4, 5), "escaleno"),
        ((1, 2, 3), "inválido"),
        ((0, 1, 1), "inválido"),
        ((-1, 2, 2), "inválido"),
    ],
)
def test_triangulo(lados, esperado):
    assert classificar_triangulo(*lados) == esperado


def test_fizzbuzz():
    assert fizzbuzz(0) == []
    assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert len(fizzbuzz(30)) == 30


def test_contar_palavras():
    assert contar_palavras("Casa, casa! Mesa.") == {"casa": 2, "mesa": 1}
    assert contar_palavras("   ") == {}
    assert contar_palavras("") == {}
    assert contar_palavras("...") == {}


def test_estoque():
    e = Estoque()
    assert e.quantidade("caneta") == 0
    e.adicionar("caneta", 10)
    e.remover("caneta", 3)
    e.adicionar("borracha", 2)
    assert e.quantidade("caneta") == 7
    assert str(e) == "borracha: 2\ncaneta: 7"


@pytest.mark.parametrize("operacao, qtd", [("adicionar", 0), ("adicionar", -1), ("remover", 0)])
def test_estoque_quantidade_invalida(operacao, qtd):
    with pytest.raises(ValueError):
        getattr(Estoque(), operacao)("x", qtd)


def test_estoque_item_zerado_sai_da_listagem():
    e = Estoque()
    e.adicionar("caneta", 2)
    e.adicionar("borracha", 1)
    e.remover("caneta", 2)
    assert e.quantidade("caneta") == 0
    assert str(e) == "borracha: 1"


def test_estoque_insuficiente():
    e = Estoque()
    e.adicionar("x", 1)
    with pytest.raises(ValueError):
        e.remover("x", 2)
    assert e.quantidade("x") == 1


@pytest.mark.skipif(ALVO == "enunciado", reason="checagem do repositório, não da solução")
@pytest.mark.parametrize(
    "arquivo",
    [
        "ex01_temperatura",
        "ex02_triangulo",
        "ex03_fizzbuzz",
        "ex04_contar_palavras",
        "ex05_estoque",
    ],
)
def test_enunciado_e_gabarito_sao_arquivos_separados(arquivo):
    enunciado = RAIZ / "exerc_trilha" / f"{arquivo}.py"
    gabarito = RAIZ / "exerc_trilha" / "gabaritos" / f"{arquivo}_gabarito.py"
    assert enunciado.is_file() and gabarito.is_file()
    # O enunciado não pode trazer a solução pronta.
    assert gabarito.read_text(encoding="utf-8") != enunciado.read_text(encoding="utf-8")
