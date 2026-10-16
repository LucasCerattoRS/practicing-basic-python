# Revisão e organização da trilha básica

- Data: 2026-10-16
- Branch: `claude/trilha-basica-readmes` (a partir de `main`, 179209b)
- Merge: não feito. PR em rascunho.

## O que mudou

- README reescrito (índice, estado real, ordem de estudo, pendências).
- 3 bugs corrigidos, cada um com teste que falhava antes (6 falhas) e passa depois:
  nome só com espaços (2 arquivos), IMC com altura 0, `cls` fora do Windows (3 arquivos).
- 5 exercícios novos em `exerc_trilha/` com gabaritos em `exerc_trilha/gabaritos/`.
- Testes `pytest` (`tests/`, `pytest.ini`) e CI em `.github/workflows/testes.yml`.

## Testes executados

- Antes das correções: 12 testes de correção, 6 falharam.
- Depois: `python -m pytest` → 64 passaram, 0 falharam (Python 3.13.16).
- Scripts sem entrada rodados individualmente (stdin vazio, timeout de 10 s): todos saem com código 0.

## Pendências

- Escala de notas do Project1-POO (sem decisão do autor; um registro da análise existe
  na branch `claude/task-p0oy1s`, fora da `main`).
- Scripts interativos sem teste (ver README, "Estado real").
- CI ainda não confirmado no GitHub (depende da execução após o push).
