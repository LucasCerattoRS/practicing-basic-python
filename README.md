# practicing-basic-python

Exercícios de Python do básico à Programação Orientada a Objetos (POO), feitos
durante os estudos. Não é um app: cada arquivo é um exercício independente.

## Índice

- [Estado real](#estado-real)
- [Como rodar](#como-rodar)
- [Ordem de estudo](#ordem-de-estudo)
- [Trilha nova com gabarito](#trilha-nova-com-gabarito)
- [Testes e CI](#testes-e-ci)
- [Correções feitas na revisão](#correções-feitas-na-revisão)
- [Pendências](#pendências)

## Estado real

Revisão de 16/10/2026, em Python 3.13, feita sem abrir janela nem navegador.

- Todos os scripts que **não** pedem `input()` rodam até o fim (24 scripts originais, mais os 5 gabaritos, verificados
  pelos testes automatizados, incluindo `Project1-POO/app.py` e `Project2-POO`).
- Os scripts interativos (pedem `input()`) **não** são rodados inteiros pelos
  testes. Só são exercitados, com entrada simulada, os que têm teste próprio:
  as duas validações sequenciais e `condicionais4.py`. Os demais foram apenas lidos
  e rodados até o primeiro `input()` (param com `EOFError`, esperado sem entrada).
- `Project1-POO/interface.py` (menu com recursão) foi lido e só testado na parte de
  limpar a tela; o fluxo do menu não foi exercitado.
- Há uma inconsistência de escala de notas no `Project1-POO` ainda **sem decisão**
  (ver [Pendências](#pendências)).

## Como rodar

Python 3.12+ (o `Project1-POO/interface.py` usa aspas aninhadas em f-string, que só
valem a partir do 3.12).

```bash
python basic-python/age.py
cd Project1-POO && python app.py        # rodar de dentro da pasta, por causa do import "sub."
cd Project2-POO && python main.py       # idem; também: python biblioteca.py
```

## Ordem de estudo

Do mais simples ao mais complexo. Dentro de cada pasta, siga a numeração dos arquivos.

| # | Pasta | Assunto | Pede entrada? |
|---|---|---|---|
| 1 | `basic-python/` | entrada, condicionais, `try/except`, módulo `%`, quadrantes | quase todos |
| 2 | `exerc_condic/` | 10 exercícios de condicionais (`if/elif/else`) | sim |
| 3 | `exerc_lacos/` | 11 exercícios de `for`, `while`, `break`, `range` | só o `lacos10.py` |
| 4 | `exerc-lists/` | listas e menu em laço (`list1` básico; `list2` e `list3` com menu) | `list2`, `list3` |
| 5 | `exerc-validation/` | validação de nome/idade/senha (versão com `all/any` e versão com `for`) | sim |
| 6 | `exerc_trilha/` | **5 exercícios novos graduais**, com gabarito separado | não |
| 7 | `exerc-class/` | classes, `__str__`, atributos e métodos de classe, `@property` | não |
| 8 | `exerc-sistem-bank/` | mini-sistema bancário (v1: cliente com saldo; v2: Cliente/Conta/Banco) | não |
| 9 | `Project1-POO/` | Restaurante + Avaliação (`app.py`) e menu procedural (`interface.py`) | só `interface.py` |
| 10 | `Project2-POO/` | Livro + biblioteca (modelo / serviço / aplicação) | não |

Extras:

- `yourtime.txt`: roteiro de estudo e desafios de reescrita para o Project2.
- `docs/registros/`: registros de cada etapa de trabalho (o que mudou, testes, pendências).

## Trilha nova com gabarito

Em `exerc_trilha/`, do mais fácil ao mais difícil. Cada enunciado é um arquivo com
função (ou classe) a completar; a solução fica em `exerc_trilha/gabaritos/`, em arquivo
separado, para você tentar antes de olhar.

| Nível | Enunciado | Conceito | Gabarito |
|---|---|---|---|
| 1 | `ex01_temperatura.py` | variáveis e operações | `gabaritos/ex01_temperatura_gabarito.py` |
| 2 | `ex02_triangulo.py` | condicionais encadeadas | `gabaritos/ex02_triangulo_gabarito.py` |
| 3 | `ex03_fizzbuzz.py` | laço e ordem das condições | `gabaritos/ex03_fizzbuzz_gabarito.py` |
| 4 | `ex04_contar_palavras.py` | strings, listas e dicionários | `gabaritos/ex04_contar_palavras_gabarito.py` |
| 5 | `ex05_estoque.py` | classe, validação e exceções | `gabaritos/ex05_estoque_gabarito.py` |

Os testes cobrem **apenas os gabaritos**, então os enunciados incompletos não
quebram o CI. Para conferir a sua solução, aponte os testes de
`tests/test_trilha.py` para o seu arquivo (troque os imports) ou rode o enunciado
com seus próprios exemplos.

## Testes e CI

```bash
python -m pip install pytest
python -m pytest
```

- `tests/test_execucao.py`: roda todo script sem `input()` e exige sair com código 0.
- `tests/test_correcoes.py`: um teste para cada bug corrigido (falhavam antes da correção).
- `tests/test_trilha.py`: testa os 5 gabaritos.
- CI: `.github/workflows/testes.yml` roda `pytest` em Python 3.12 e 3.13 a cada
  PR e a cada push na `main`. Só testa; não publica nem faz deploy.

## Correções feitas na revisão

1. **Nome só com espaços era aceito** nas duas validações sequenciais
   (`"   "` passava). Agora é recusado (`nome.strip()`).
2. **`condicionais4.py` (IMC) quebrava com altura 0** (`ZeroDivisionError`).
   Agora pede a altura de novo enquanto for `<= 0`.
3. **`os.system('cls')` não limpava a tela fora do Windows** (`list2.py`, `list3.py`,
   `Project1-POO/interface.py`). Agora usa `cls` no Windows e `clear` nos demais.

Correções anteriores (08/10): imports do `Project2-POO`, mensagem de sucesso fora do
lugar na validação sequencial 2, nome "Mexican Food" e `.pyc` versionados.

## Pendências

- **Escala de notas do `Project1-POO`**: `app.py` dá notas 10 e 8, mas
  `receber_avaliacao` só aceita `0 < nota <= 5`; as duas são descartadas em silêncio e a
  média sai 5.0. Não há enunciado que desempate, então **não foi alterado**. Decidir:
  escala 0–5 (trocar as notas de exemplo) ou 0–10 (trocar a validação) e se a nota 0 vale.
- `interface.py` volta ao menu chamando `main()` de novo (recursão a cada opção) e usa
  `except:` genérico, que engole qualquer erro.
- `Project2-POO/sub/livros.py` é uma segunda classe `Livro` que ninguém importa.
- `basic-python/evenorodd.PY` tem extensão em maiúscula.
- Entradas não numéricas em vários exercícios de `exerc_condic/` fazem o script parar
  com `ValueError` (só alguns tratam isso).
- `basic-python/age.py` aceita idade negativa e a classifica como criança.
