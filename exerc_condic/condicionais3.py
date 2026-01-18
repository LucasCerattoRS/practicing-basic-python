temperatura = int(input("Digite a temperatura da sala de servidores: "))
# criaçao de looping #
while temperatura <= 0:
    print("Digite uma temperatura válida.\n")
# "\n" pula uma linha #
    temperatura = int(input("Digite a temperatura da sala de servidores: "))

if temperatura > 25:
    print("Alerta! Temperatura acima do limite permitido.")
else:
    print("Tudo certo")
