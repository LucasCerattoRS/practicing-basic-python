distancia = int(input("Digite a distância percorrida (em km): "))

if distancia < 0:
    print("Erro: distância inválida")
elif distancia < 100:
    print("R$ 10,00")
elif distancia < 200:
    print("R$ 20,00")
else:
    print("R$ 30,00")

# lembre-se, funciona por que a anterior é descartada quando se mostra false #