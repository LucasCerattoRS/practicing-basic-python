macas = int(input("Informe o numero de maçãs vendidas: "))
bananas = int(input("Informe o numero de bananas vendidas: "))

if macas <= 0 and bananas <= 0:
    print("Não houve vendas :(")
elif macas > bananas:
    print("As maçãs tiveram mais vendas!")
elif macas == bananas:
    print("As frutas tiveram o mesmo número de vendas")
else:
    print("As bananas tiveram mais vendas!")

# Atenção a sequencia logica