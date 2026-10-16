"""Utilitários dos testes: rodar scripts de console e importar módulos por caminho."""
import importlib.util
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def rodar_script(caminho, entrada="", timeout=10):
    """Executa um script do repositório em outro processo, a partir da pasta dele."""
    arquivo = RAIZ / caminho
    return subprocess.run(
        [sys.executable, arquivo.name],
        cwd=arquivo.parent,
        input=entrada,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def importar_por_caminho(caminho, nome, pasta_no_path=None):
    """Importa um arquivo .py (mesmo com hífen no nome) sem executar o bloco __main__."""
    arquivo = RAIZ / caminho
    if pasta_no_path:
        sys.path.insert(0, str(RAIZ / pasta_no_path))
    try:
        spec = importlib.util.spec_from_file_location(nome, arquivo)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
    finally:
        if pasta_no_path:
            sys.path.remove(str(RAIZ / pasta_no_path))
    return modulo
