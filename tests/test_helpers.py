"""Testes do próprio helper de importação usado pela trilha."""
from helpers import importar_por_caminho

SOLUCAO_COM_DATACLASS = '''from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Estoque:
    total: int = 0
'''


def test_importar_solucao_com_dataclass(tmp_path):
    # No Python 3.12, @dataclass com anotações adiadas procura o módulo em
    # sys.modules; sem registro, a importação quebrava com AttributeError.
    arquivo = tmp_path / "solucao.py"
    arquivo.write_text(SOLUCAO_COM_DATACLASS, encoding="utf-8")
    modulo = importar_por_caminho(arquivo, "solucao_dataclass_teste")
    assert modulo.Estoque().total == 0
