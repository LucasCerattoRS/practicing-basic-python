"""Smoke test: todo script que não pede entrada deve rodar até o fim, sem erro."""
import pytest

from helpers import rodar_script

SEM_ENTRADA = [
    "basic-python/except.py",
    *[f"exerc-class/classes{i}.py" for i in range(1, 8)],
    "exerc-lists/list1.py",
    "exerc-sistem-bank/mini-sistema-bancario1.py",
    "exerc-sistem-bank/mini-sistema-bancario2.py",
    "exerc_lacos/lacos.py",
    *[f"exerc_lacos/lacos{i}.py" for i in range(1, 10)],
    "Project1-POO/app.py",
    "Project2-POO/main.py",
    "Project2-POO/biblioteca.py",
    *[f"exerc_trilha/gabaritos/{n}_gabarito.py" for n in (
        "ex01_temperatura", "ex02_triangulo", "ex03_fizzbuzz",
        "ex04_contar_palavras", "ex05_estoque")],
]


@pytest.mark.parametrize("script", SEM_ENTRADA)
def test_script_sem_entrada_roda(script):
    resultado = rodar_script(script)
    assert resultado.returncode == 0, resultado.stderr
