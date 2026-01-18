# Entrada de dados
renda = float(input("Digite o valor da sua renda mensal (R$): "))
parcela = float(input("Digite o valor da parcela desejada (R$): "))

# Verificação das condições
if renda > 2000 and parcela / renda <= 0.3:
# Verifica se a parcela compromete no máximo 30% da renda. #
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")
