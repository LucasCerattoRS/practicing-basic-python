"""Um teste (ou mais) para cada bug corrigido na revisão. Todos falhavam antes da correção."""
import os

import pytest

from helpers import importar_por_caminho, rodar_script

VALIDACOES = [
    "exerc-validation/fluxo-de-validação-sequencial.py",
    "exerc-validation/fluxo-de-validação-sequencial2.py",
]


# Bug 1: nome formado só por espaços era aceito como válido.
@pytest.mark.parametrize("script", VALIDACOES)
def test_nome_so_com_espacos_e_recusado(script):
    # Entrada: nome em branco; depois dados válidos (para a versão com laço terminar).
    resultado = rodar_script(script, "   \nAna Souza\n30\nAbc12!\n")
    assert "Nome inválido" in resultado.stdout


@pytest.mark.parametrize("script", VALIDACOES)
def test_nome_valido_continua_aceito(script):
    resultado = rodar_script(script, "Ana Souza\n30\nAbc12!\n")
    assert "Cadastro realizado com sucesso!" in resultado.stdout


# Bug 2: altura 0 gerava ZeroDivisionError no cálculo do IMC.
def test_imc_com_altura_zero_nao_quebra():
    resultado = rodar_script("exerc_condic/condicionais4.py", "70\n0\n1.75\n")
    assert "ZeroDivisionError" not in resultado.stderr
    assert resultado.returncode == 0
    assert "Peso normal" in resultado.stdout  # depois de pedir a altura de novo


def test_imc_normal():
    resultado = rodar_script("exerc_condic/condicionais4.py", "70\n1.75\n")
    assert "Peso normal" in resultado.stdout
    assert "22.86" in resultado.stdout


# Bug 3: os.system('cls') não limpa a tela fora do Windows (aparece "cls: not found").
@pytest.fixture
def comandos(monkeypatch):
    registrados = []
    monkeypatch.setattr(os, "system", lambda cmd: registrados.append(cmd) or 0)
    return registrados


@pytest.mark.parametrize("sistema, esperado", [("posix", "clear"), ("nt", "cls")])
@pytest.mark.parametrize(
    "caminho, funcao, args",
    [
        ("exerc-lists/list2.py", "exibir_main", ("t",)),
        ("exerc-lists/list3.py", "exibir_main", ("t",)),
        ("Project1-POO/interface.py", "exibir_subtitulo", ("t",)),
    ],
)
def test_limpar_tela_depende_do_sistema(monkeypatch, comandos, caminho, funcao, args, sistema, esperado):
    modulo = importar_por_caminho(caminho, "mod_" + caminho.replace("/", "_").replace(".", "_"))
    monkeypatch.setattr(os, "name", sistema)
    getattr(modulo, funcao)(*args)
    assert comandos == [esperado]
