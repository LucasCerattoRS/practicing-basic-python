"""Testes dos gabaritos da trilha e verificação de que os enunciados continuam sem solução."""
import pytest

from ex01_temperatura_gabarito import celsius_para_fahrenheit
from ex02_triangulo_gabarito import classificar_triangulo
from ex03_fizzbuzz_gabarito import fizzbuzz
from ex04_contar_palavras_gabarito import contar_palavras
from ex05_estoque_gabarito import Estoque
from helpers import RAIZ


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


def test_estoque_insuficiente():
    e = Estoque()
    e.adicionar("x", 1)
    with pytest.raises(ValueError):
        e.remover("x", 2)
    assert e.quantidade("x") == 1


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
