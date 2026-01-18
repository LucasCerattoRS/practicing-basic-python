while True:
    try:
        nota1 = float(input("Informe a nota para a atividade 1: "))
        nota2 = float(input("Informe a nota para a atividade 2: "))
        nota3 = float(input("Informe a nota para a atividade 3: "))

        if nota1 < 0 or nota2 < 0 or nota3 <0:
            print("Erro: Algum valor invalido. Tente novamente.\n")
        else:
            break
    except ValueError:
        print("Erro: digite apenas números.\n")

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
    # Por que isso funciona corretamente:
    # porque o if media >= 7 já foi descartado antes.
else:
    print("Reprovado")