# practicing-basic-python

Exercícios de Python do básico à Programação Orientada a Objetos (POO), feitos
durante os estudos. Não é um app: cada arquivo é um exercício independente.

## Estado real (revisão 08/10/2026)

- Todos os `.py` compilam (checado com `compile()` em todos).
- Scripts sem `input()` (POO, laços, listas) foram executados e rodam.
- Os exercícios interativos (pedem `input()`) **não** foram todos testados à mão;
  só o `fluxo-de-validação-sequencial2.py`, que tinha bug.
- Corrigido em 08/10: imports quebrados do `Project2-POO` (`exerc.livro` → `sub.livro`),
  mensagem de sucesso fora do lugar na validação sequencial 2, nome "exican Food",
  e `.pyc` que estavam versionados.
- Não há testes automatizados (são exercícios de console).

## Como rodar

Python 3.12+ (o `Project1-POO/interface.py` usa aspas aninhadas em f-string, que só valem a partir do 3.12).

```bash
python basic-python/age.py
cd Project1-POO && python app.py        # rodar de dentro da pasta, por causa do import "sub."
cd Project2-POO && python main.py       # idem; também: python biblioteca.py
```

## Estrutura

| Pasta | Assunto |
|---|---|
| `basic-python/` | entrada, condicionais, `try/except`, módulo `%` |
| `exerc_condic/` | 10 exercícios de condicionais |
| `exerc_lacos/` | 11 exercícios de `for`/`while`/`break` |
| `exerc-lists/` | listas e menu em laço |
| `exerc-validation/` | validação de nome/idade/senha (versão com `all/any` e versão com `for`) |
| `exerc-class/` | classes, `__str__`, atributos e métodos de classe, `@property` |
| `exerc-sistem-bank/` | mini-sistema bancário (versão 1: cliente com saldo; versão 2: Cliente/Conta/Banco separados) |
| `Project1-POO/` | Restaurante + Avaliação (`app.py`) e menu procedural (`interface.py`) |
| `Project2-POO/` | Livro + biblioteca (modelo / serviço / aplicação) |
| `yourtime.txt` | roteiro de estudo e desafios para o Project2 |

## Pendências

- `Project1-POO/app.py` dá notas 10 e 8, mas `receber_avaliacao` só aceita `0 < nota <= 5`:
  essas duas são descartadas em silêncio e a média sai 5.0. Decidir a escala (0–5 ou 0–10).
- `os.system('cls')` só limpa a tela no Windows; no Linux aparece `sh: cls: not found`.
- `interface.py` volta ao menu chamando `main()` de novo (recursão a cada opção) e usa `except:` genérico.
- `Project2-POO/sub/livros.py` é uma segunda classe `Livro` que ninguém importa.
- `basic-python/evenorodd.PY` tem extensão em maiúscula.

## Para estudar

- **Tipos e conversão:** `int()`/`float()` em `input()` e o `ValueError` quando falha.
- **Fluxo:** `if/elif/else`, `while True` + `break`, validação em laço até acertar.
- **`all()`/`any()` x laço explícito:** as duas versões de `exerc-validation/` fazem a mesma coisa.
- **POO:** classe x instância, `__init__`, `__str__`, atributo de classe como "banco em memória",
  `@classmethod`, `@staticmethod`, `@property`, encapsulamento com `_atributo`.
- **Responsabilidades:** por que em `mini-sistema-bancario2.py` o saldo é da Conta e não do Cliente.
- **Módulos e pacotes:** `from sub.livro import Livro`, por que o import depende da pasta de onde se roda.
- **Indentação é lógica em Python:** o bug da validação 2 era só uma linha 4 espaços para dentro.

## Anotações originais

Nestes arquivos, explorei os fundamentos cruciais da Programação Orientada a Objetos (POO), uma abordagem poderosa para organizar e estruturar códigos. Mergulhei no conceito de classes, compreendendo sua importância fundamental no desenvolvimento de software. Construíndo a primeira classe, o Restaurante, definindo atributos de instância, como nome, categoria e o estado ativo, que inicia como False.

Ao longo do caminho, aprendi a utilizar métodos especiais da linguagem Python, como o construtor init, e praticar a abstração na escrita de atributos de maneira pythonica. Aprofundando o conhecimento ao explorar a criação de métodos de classe, destacando sua utilidade em operações que envolvem a classe como um todo.

Além disso, dei um passo além na aplicação dos conceitos aprendidos, importando a classe Restaurante no arquivo principal (main.py). Reforçando o entendimento de POO ao criar mais uma classe e, de maneira avançada, integrando a classe Avaliação ao Restaurante. Agora, posso gerenciar uma lista de objetos de avaliação associados a cada restaurante e listar essas avaliações conforme necessário.

"Eu não sou o melhor não, mas sou capaz de fazer coisas que muitas pessoas não acreditam." Guga (tenista brasileiro)
