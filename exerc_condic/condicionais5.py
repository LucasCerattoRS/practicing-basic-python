despesas = float(input("Informe o total de despesas do mês (R$): "))

while despesas < 0:
    print("Digite um valor válida.\n")
    despesas = float(input("Informe o total de despesas do mês (R$): "))


if despesas >= 3000:
    print("Atenção Você ultrapassou o limite do orçamento")
else:
    print("VocÊ está dentro do orçamento")