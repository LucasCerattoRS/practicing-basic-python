while True:
    try:
        hora = int(input("Informe a hora atual (0 a 23): "))
        minuto = int(input("Informe os minutos (0 a 59): "))

        if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
            print("Erro: horário inválido. Tente novamente.\n")
        else:
            break
    except ValueError:
        print("Erro: digite apenas números.\n")

horario = hora * 60 + minuto
inicio = 8 * 60
fim = 18 * 60

# Aqui está convertendo tudo para minutos desde 00:00, o que é uma excelente prática #

if inicio <= horario <= fim:
# if horario >= inicio and horario <= fim: #
    print("Acesso permitido")
else:
    print("Acesso negado")
