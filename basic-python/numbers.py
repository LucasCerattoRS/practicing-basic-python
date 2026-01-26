while True:
    try:
        numero = float(input("Digite um número positivo: "))

        if numero > 0:
            print("Número válido.")
            break
        else:
            print("Número inválido. Digite um número maior que zero.\n")

    except ValueError:
        print("Entrada inválida. Digite apenas números.\n")

# float é um tipo de dado para representar números decimais em Python. #
