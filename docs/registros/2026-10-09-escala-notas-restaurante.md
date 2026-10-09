# Escala das notas do Project1-POO (Restaurante/Avaliação)

- Data: 2026-10-09
- Branch: claude/task-os7b5n
- Base SHA: 179209bef2ef15e012f9b8db818fdc459fd89e5f

## Inconsistência

`Project1-POO/app.py` registra notas 10 (Gui), 8 (Lais) e 5 (Emy), mas
`Restaurante.receber_avaliacao` só aceita `0 < nota <= 5`. As notas 10 e 8
são descartadas em silêncio e a média do restaurante "Praça" sai 5.0.

## Fontes consultadas

- `Project1-POO/app.py`, `sub/restaurante.py`, `sub/avaliacao.py`: dados de
  exemplo usam 10 e 8; a validação usa 0–5. Sem comentário que explique a escala.
- `README.md`: lista a dúvida como pendência ("decidir a escala").
- `yourtime.txt:153` ("Nota ... entre 0 e 10"): refere-se ao Project2 (Livro),
  não ao restaurante. Não é fonte para o Project1.
- Não existem enunciado do exercício nem testes no repositório
  (o README já diz que não há testes automatizados).
- `git log -S"0 < nota"`: a validação veio no upload b2b2fae, sem mensagem útil.

## Decisão

**Nenhum código foi alterado.** Não há fonte clara da escala pretendida: os dois
lados (dados 0–10, validação 0–5) estão no mesmo código, sem enunciado nem teste
que desempate. Escolher uma seria inventar regra.

## Decisão necessária (do autor)

Escolher uma opção:

1. Escala 0–5: trocar as notas de exemplo em `app.py` (10 e 8 → valores ≤ 5).
2. Escala 0–10: trocar a validação para `0 <= nota <= 10` (ou `0 < nota <= 10`).

Além disso, definir se nota inválida deve levantar erro/avisar em vez de ser
descartada em silêncio, e se 0 é nota válida (hoje não é: `0 < nota`).
Com a decisão, o teste pequeno seria: dar nota 10 (ou 8) a um restaurante e
conferir a média esperada; falha hoje (média 5.0 com as três notas do app).

## Comandos e resultados

- `python3 --version` → Python 3.13.16
- `cd Project1-POO && python3 app.py` → roda; "Praça" aparece com avaliação
  `5.0` (esperado se 10 e 8 contassem: 7.7). Confirma o sintoma.
- Testes automatizados: nenhum existe; nenhum foi rodado.

## Limites

- Execução apenas do `app.py` (sem entrada interativa); `interface.py` não foi testado.
- Sem merge, deploy ou subagentes.

## Pendências

- Decisão da escala (acima). Depois: aplicar a opção escolhida e adicionar o teste.
